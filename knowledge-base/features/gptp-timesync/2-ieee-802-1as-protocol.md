# gPTP — IEEE 802.1AS-2020 Protocol

## Key Protocol Elements

| Element | Description |
|---------|-------------|
| Grandmaster (GM) | Reference clock; selected by BMCA |
| Bridge | Forwards sync messages with residence time correction |
| End-station | Consumer; synchronizes to GM |
| syncInterval | Time between Sync messages (default: 125 ms = log2 -3) |
| pdelayInterval | Peer delay measurement interval |

## BMCA (Best Master Clock Algorithm)

Priority1 → clockClass → clockAccuracy → offsetScaledLogVariance → Priority2 → clockIdentity

## Holdover

When sync messages are missed, the end-station enters holdover mode:
- Uses local oscillator to maintain time estimate
- After threshold (3 × syncInterval): status → kUncertain

## TODO: Add message sequence diagram, parameter table for SA8620P configuration
