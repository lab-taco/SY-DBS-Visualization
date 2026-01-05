#!/bin/bash

docker run --rm \
  -v ~/data:/data \
  -v ~/fastsurfer_output:/output \
  deepmi/fastsurfer:latest \
  --t1 /data/sub-001_T1w.nii.gz \
  --sid sub-001 \
  --sd /output \
  --seg_only \
  --parallel
