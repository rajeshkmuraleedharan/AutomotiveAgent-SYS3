# gPTP TimeSync — Overview

## What is gPTP?

IEEE 802.1AS-2020 (generalized Precision Time Protocol) provides sub-microsecond time synchronization across automotive Ethernet networks. It is the time protocol for IEEE 802.1Q TSN (Time-Sensitive Networking).

## Why it matters for ADAS

Sensor fusion (camera + radar + LiDAR + IMU) requires all sensor data to be timestamped in a common time domain. The SA8620P uses gPTP to align all sensor timestamps to the network grandmaster with ≤ 1 µs (3σ) accuracy.

## SA8620P Role

The SA8620P acts as a **gPTP end-station** (time consumer). The grandmaster is external (TODO: confirm placement — dedicated GM unit or another ECU).

## Key References

- IEEE 802.1AS-2020 — gPTP standard
- MRVL-88Q5050-DS — Marvell switch hardware timestamping
- VEC-MSR-ADAPT-TSYNC — ara::tsync implementation

## TODO: Expand with network topology diagram
