# gPTP — SA8620P + Marvell TSN Integration

## Hardware Timestamping

Marvell 88Q5050 TSN switch performs hardware timestamping on ingress/egress of Sync messages. Accuracy: TBD (see MRVL-88Q5050-DS §4.2).

## ara::tsync Configuration

- End-station mode: `kSlave`
- syncInterval: –3 (125 ms)
- Time domain: 0 (default automotive)
- Status interface: `ara::tsync::SynchronizationStatus` → kSynchronized | kUncertain

## SA8620P MAC Integration

TODO: Add MAC register configuration for hardware timestamping

## ara::tsync API (Vector MICROSAR Adaptive)

```cpp
// Read current synchronized time
auto time = ara::tsync::TimeSync::GetInstance().GetCurrentTime();
auto status = ara::tsync::TimeSync::GetInstance().GetSyncStatus();
if (status == ara::tsync::SynchronizationStatus::kUncertain) {
    // Trigger EKF degraded mode
}
```

## TODO: Add Marvell PHY (88Q22xx) configuration details
