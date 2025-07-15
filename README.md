# Metaflow-Gov-Gate-Risk-Scoring
Governance Gate to use with Metaflow, Risk Scoring with Adaptive Oversight
# Metaflow Governance Gate

This package provides a plug-and-play governance gate for Metaflow pipelines, enabling risk scoring with adaptive oversight using minimal code changes.

## Features
- Risk scoring (customizable)
- Adaptive HITL approval
- Audit logging
- Easy integration

## Usage

1. Import `GovernanceGate` into your Metaflow step.
2. Instantiate with your prompt/context/intent.
3. Call `.run()` to apply risk scoring and adaptive oversight.
4. Set the `HUMAN_APPROVED` environment variable to approve high-risk steps.

## Example

See `example_flow.py` for a full workflow.
