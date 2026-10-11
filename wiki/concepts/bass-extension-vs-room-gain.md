---
type: concept
slug: bass-extension-vs-room-gain
last_updated: 2026-10-11
---
# Bass extension vs room gain

## Anechoic f3/f6
`f3_hz` and `f6_hz` are the frequencies at which the anechoic LW falls 3 and 6 dB below its 300 Hz–10 kHz mean. `scripts/cta2034.py` scans downward from 300 Hz and records the first crossing. A narrow dip, such as a baffle-step or port-interaction notch, can therefore set f3 higher than the overall roll-off suggests. Where f3 and f6 are far apart, the speaker page checks for this.

Reviewers often quote f3/f6 against a different reference (e.g. 300 Hz–3 kHz, or −6 dB relative to the 1 kHz level). Those values are recorded separately.

## Interpretation (Claude.md §7)
< 45 Hz excellent for a bookshelf · 45–60 Hz good · 60–75 Hz modest · > 75 Hz needs a sub.

## Room gain
In a real room, boundaries reinforce bass:
- **Boundary gain:** near a wall, up to +6 dB below the frequency where the wall distance is about λ/4. Corners add more.
- **Pressure-zone gain:** in small sealed rooms, below the lowest mode.

Room gain does not belong to the speaker. Pages credit only anechoic figures. Placement advice from users (Tier E), such as "needs to be near a wall", is recorded as an attributed pattern.

## Ported vs sealed
Ported designs reach lower for a given box size but roll off at 24 dB/octave and unload below tuning. Sealed designs roll off at 12 dB/octave and integrate more predictably with room gain and subwoofers.

## Related
[[preference-score]] · [[compression-and-max-spl]] · [[spinorama]]
