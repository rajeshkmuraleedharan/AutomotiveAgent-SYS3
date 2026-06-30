# HTP Orchestration — Overview

## What is the Hexagon HTP?

The Hexagon Tensor Processor (HTP) is a dedicated AI accelerator on the SA8620P SoC. It executes Deep Learning Container (DLC) models for ADAS perception workloads (object detection, segmentation, depth estimation).

## Why "Orchestration"?

The HTP requires software orchestration on QNX to:
- Manage DLC model lifecycle (load, warm-up, run, unload)
- Schedule inference requests across the HTP
- Supervise deadline compliance (ara::phm)
- Detect out-of-distribution (OOD) inputs
- Maintain SMMU isolation from SAIL memory

## Safety Model

- Hexagon HTP: **QM** — not safety certified
- HTP Orchestrator (QNX:KryoP0): **ASIL-B** — supervises QM accelerator
- Supervision via ara::phm DeadlineSupervision (100 ms timeout)

## TODO: Add inference pipeline diagram
