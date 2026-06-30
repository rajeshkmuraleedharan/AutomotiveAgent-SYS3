# HTP Orchestration — Hexagon Architecture

## SA8620P Hexagon HTP

- Architecture: Hexagon V73 (TBD — confirm from QC-SA8620P-TRM)
- Runtime: SNPE (Snapdragon Neural Processing Engine) / QNN (Qualcomm Neural Networks)
- Interface: FastRPC (QNX ↔ Hexagon DSP)
- Memory: separate DDR region, SMMU-isolated

## FastRPC

FastRPC is the inter-processor communication mechanism between QNX (host) and the Hexagon DSP:
- Synchronous RPC call from QNX → Hexagon
- SMMU ensures Hexagon DMA cannot access SAIL TCM or other protected regions
- Error: FastRPC timeout → DTC_HTP_DEADLINE_MISS

## DLC Model Format

- Models compiled to .dlc format by SNPE SDK
- Loaded into Hexagon VTCM (Vector TCM) at initialization
- Supports INT8/FP16 quantization

## TODO: Add SNPE/QNN API usage examples
