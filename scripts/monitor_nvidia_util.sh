#!/usr/bin/env bash
# Monitor the GPU utilization.
# Output:
# A time-series of GPU utilization percentage over time.
# Default sampling rate: 1 sample/second.
# Default monitoring time: 24 hrs

set -eou pipefail

nvidia-smi --query-gpu=gpu_name,timestamp,utilization.gpu,memory.used --format=csv -lms 1000 &> monitor-util-out.csv &

NVIDIA_PID=$!
echo "Running nvidia-smi, pid ${NVIDIA_PID}, saving to ${PWD}/monitor-util-out.csv ..."

sleep 86400

kill ${NVIDIA_PID}
