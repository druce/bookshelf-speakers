"""Compute CTA-2034 curves and wiki summary metrics from Klippel-format H/V SPL exports.

Input: a directory holding "SPL Horizontal.txt" and "SPL Vertical.txt" (Klippel NFS export, as stored in
the spinorama.org repository for ASR and Erin's Audio Corner measurements; levels are dB SPL @ 2.83 V / 1 m).

Method (documented in wiki/concepts/spinorama.md and wiki/concepts/listening-window.md):
- Spatial averages are energy (pressure-squared) averages, per CTA-2034-A.
- LW = 0°, ±10° V, ±10/20/30° H. ER = mean of floor/ceiling/front/side/rear groups. SP = CTA weighted average.
- Curves are smoothed to 1/6 octave on a log grid (48 points/octave) before metrics are taken.
- ref level = mean LW 300 Hz-10 kHz. lw/on-axis deviation = half the peak-to-peak range over 300 Hz-10 kHz (±dB).
- sensitivity = mean LW 300 Hz-3 kHz, dB SPL @ 2.83 V / 1 m.
- f3/f6 = sustained roll-off: scanning UP from 20 Hz, where LW first reaches ref-3/ref-6 dB (below 300 Hz).
  Any deeper-than-3 dB dip between 1.15*f3 and 300 Hz is reported separately (lw_dip_above_f3_*).
- beamwidth = -6 dB full angle relative to on-axis, median over 1-10 kHz (1/3-octave points).
- di_smoothness from max |residual| of ERDI vs a straight line in log f, 500 Hz-10 kHz: <1 smooth, <2 minor, else major.
- on_minus_lw_4_10k_db = mean(on-axis - LW) over 4-10 kHz; > +1 means on-axis is brighter than the window
  (less toe-in sounds more neutral), < -1 means treble falls fast off-axis (aim at the listener).
- er_dip_db = deepest negative residual of ER vs a straight line in log f (300 Hz-10 kHz), searched 1-5 kHz.

Usage: python3 -I scripts/cta2034.py <measurement_dir> [--json]
"""
import json
import re
import sys
from pathlib import Path

import numpy as np

SP_WEIGHTS = [0.000604486, 0.004730189, 0.008955027, 0.012387354, 0.014989611,
              0.016868154, 0.018165962, 0.019006744, 0.019477787, 0.019629373]


def sp_weight(angle):
    a = abs(angle)
    if a > 90:
        a = 180 - a
    return SP_WEIGHTS[a // 10]


def read_klippel(path):
    lines = Path(path).read_text(encoding="utf-8", errors="replace").splitlines()
    labels = [x for x in lines[1].split("\t") if x.strip()]
    angles = []
    for lab in labels:
        lab = lab.strip().strip('"')
        if lab.lower().startswith("on"):
            angles.append(0)
        else:
            angles.append(int(re.sub(r"[^0-9\-]", "", lab)))
    freq = None
    rows = []
    for line in lines[3:]:
        parts = [p for p in line.split("\t") if p.strip()]
        if len(parts) < 2 * len(angles):
            continue
        try:
            rows.append([float(p.replace(",", "")) for p in parts[: 2 * len(angles)]])
        except ValueError:
            continue
    arr = np.array(rows)
    freq = arr[:, 0]
    data = {a: arr[:, 2 * i + 1] for i, a in enumerate(angles)}
    if 180 not in data and -180 in data:
        data[180] = data[-180]
    return freq, data


def energy_mean(curves, weights=None):
    curves = np.array(curves)
    p2 = 10 ** (curves / 10)
    w = np.ones(len(curves)) if weights is None else np.array(weights)
    return 10 * np.log10((p2 * w[:, None]).sum(axis=0) / w.sum())


def log_grid(fmin=20, fmax=20000, ppo=48):
    n = int(np.log2(fmax / fmin) * ppo) + 1
    return fmin * 2 ** (np.arange(n) / ppo)


def resample(freq, curve, grid):
    return np.interp(np.log(grid), np.log(freq), curve)


def smooth(grid, curve, frac=6):
    """Fractional-octave smoothing in the energy domain on a log grid."""
    lg = np.log2(grid)
    p2 = 10 ** (curve / 10)
    out = np.empty_like(curve)
    half = 1 / (2 * frac)
    for i, x in enumerate(lg):
        m = (lg >= x - half) & (lg <= x + half)
        out[i] = 10 * np.log10(p2[m].mean())
    return out


def band(grid, lo, hi):
    return (grid >= lo) & (grid <= hi)


def line_residual(grid, curve, lo, hi):
    m = band(grid, lo, hi)
    x = np.log10(grid[m])
    coef = np.polyfit(x, curve[m], 1)
    res = np.full_like(curve, np.nan)
    res[m] = curve[m] - np.polyval(coef, x)
    return res


def crossing_below(grid, curve, level, start=300.0):
    """Sustained roll-off: scan up from the lowest frequency to the first point at or above `level`
    (below `start`); return the interpolated crossing. None if the curve is never below `level`."""
    idx = np.where(grid <= start)[0]
    if curve[idx[0]] >= level:
        return None
    for i in idx[1:]:
        if curve[i] >= level:
            f0, f1 = np.log(grid[i - 1]), np.log(grid[i])
            c0, c1 = curve[i - 1], curve[i]
            t = (level - c0) / (c1 - c0) if c1 != c0 else 0
            return float(np.exp(f0 + t * (f1 - f0)))
    return None


def deepest_dip(grid, curve, ref, lo, hi=300.0):
    m = (grid > lo) & (grid <= hi) if lo else (grid <= hi)
    if not m.any():
        return None, None
    i = np.argmin(np.where(m, curve, np.inf))
    return float(curve[i] - ref), float(grid[i])


def beamwidth(data, freq, f, max_angle=180):
    pos = sorted(a for a in data if 0 <= a <= max_angle)
    neg = sorted((a for a in data if -max_angle <= a <= 0), reverse=True)
    on = np.interp(np.log(f), np.log(freq), data[0])

    def edge(seq):
        prev_a, prev_v = 0, 0.0
        for a in seq[1:]:
            v = np.interp(np.log(f), np.log(freq), data[a]) - on
            if v <= -6:
                t = (-6 - prev_v) / (v - prev_v) if v != prev_v else 0
                return abs(prev_a) + t * (abs(a) - abs(prev_a))
            prev_a, prev_v = a, v
        return None

    e1, e2 = edge(pos), edge(neg)
    if e1 is None or e2 is None:
        return None
    return e1 + e2


def compute(meas_dir):
    meas_dir = Path(meas_dir)
    fh, h = read_klippel(meas_dir / "SPL Horizontal.txt")
    fv, v = read_klippel(meas_dir / "SPL Vertical.txt")
    vv = {a: np.interp(np.log(fh), np.log(fv), c) for a, c in v.items()}

    on = h[0]
    lw = energy_mean([h[0], vv[10], vv[-10], h[10], h[-10], h[20], h[-20], h[30], h[-30]])
    floor = energy_mean([vv[-20], vv[-30], vv[-40]])
    ceiling = energy_mean([vv[40], vv[50], vv[60]])
    front = energy_mean([h[0], h[10], h[-10], h[20], h[-20], h[30], h[-30]])
    side = energy_mean([h[a] for a in (40, -40, 50, -50, 60, -60, 70, -70, 80, -80)])
    rear = energy_mean([h[90], h[-90], h[180]])
    er = energy_mean([floor, ceiling, front, side, rear])
    sp_curves, sp_w = [], []
    for a, c in h.items():
        if a == -180:
            continue
        sp_curves.append(c)
        sp_w.append(sp_weight(a))
    for a, c in vv.items():
        if a in (0, 180, -180):
            continue
        sp_curves.append(c)
        sp_w.append(sp_weight(a))
    sp = energy_mean(sp_curves, sp_w)
    pir = energy_mean([lw, er, sp], [0.12, 0.44, 0.44])

    g = log_grid(max(20, fh.min()), min(20000, fh.max()))
    S = {k: smooth(g, resample(fh, c, g)) for k, c in
         dict(on=on, lw=lw, er=er, sp=sp, pir=pir).items()}

    m = band(g, 300, 10000)
    ref = float(S["lw"][m].mean())
    sens = float(S["lw"][band(g, 300, 3000)].mean())
    lw_dev = float((S["lw"][m].max() - S["lw"][m].min()) / 2)
    on_dev = float((S["on"][m].max() - S["on"][m].min()) / 2)
    f3 = crossing_below(g, S["lw"], ref - 3)
    f6 = crossing_below(g, S["lw"], ref - 6)
    dip_db, dip_hz = deepest_dip(g, S["lw"], ref, f3 * 1.15 if f3 else None)

    erdi = S["lw"] - S["er"]
    spdi = S["lw"] - S["sp"]
    r = line_residual(g, erdi, 500, 10000)
    di_res = float(np.nanmax(np.abs(r)))
    di_smooth = "smooth" if di_res < 1.0 else ("minor-discontinuity" if di_res < 2.0 else "major-discontinuity")
    er_res = line_residual(g, S["er"], 300, 10000)
    er_dip = float(-np.nanmin(er_res[band(g, 1000, 5000)]))

    thirds = 1000 * 2 ** (np.arange(0, 10.1) / 3)
    thirds = thirds[thirds <= 10000]
    hb = [beamwidth(h, fh, f) for f in thirds]
    vb = [beamwidth(vv, fh, f) for f in thirds]
    hb = [x for x in hb if x is not None]
    vb = [x for x in vb if x is not None]

    return {
        "method": "scripts/cta2034.py v2 (1/6-oct smoothing; LW ref 300 Hz-10 kHz)",
        "ref_level_db": round(ref, 1),
        "sensitivity_db_2v83": round(sens, 1),
        "lw_deviation_db": round(lw_dev, 1),
        "on_axis_deviation_db": round(on_dev, 1),
        "f3_hz": round(f3) if f3 else None,
        "f6_hz": round(f6) if f6 else None,
        "lw_dip_above_f3_db": round(dip_db, 1) if dip_db is not None and dip_db < -3 else None,
        "lw_dip_above_f3_hz": round(dip_hz) if dip_db is not None and dip_db < -3 else None,
        "hor_beamwidth_deg": round(float(np.median(hb))) if hb else None,
        "ver_beamwidth_deg": round(float(np.median(vb))) if vb else None,
        "erdi_max_residual_db": round(di_res, 1),
        "di_smoothness": di_smooth,
        "er_dip_1_5khz_db": round(er_dip, 1),
        "on_minus_lw_4_10k_db": round(float((S["on"] - S["lw"])[band(g, 4000, 10000)].mean()), 1),
        "spdi_1k_db": round(float(np.interp(1000, g, spdi)), 1),
        "spdi_10k_db": round(float(np.interp(10000, g, spdi)), 1),
    }


if __name__ == "__main__":
    res = compute(sys.argv[1])
    print(json.dumps(res, indent=1))
