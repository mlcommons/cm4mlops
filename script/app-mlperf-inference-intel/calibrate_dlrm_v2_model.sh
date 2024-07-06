#!/bin/bash

export MODEL_DIR=${CM_ML_MODEL_FILE_WITH_PATH}
echo ${CM_HARNESS_CODE_ROOT}
cd ${CM_HARNESS_CODE_ROOT}
numactl -m 1 python python/dump_torch_model.py --model-path=$MODEL_DIR --dataset-path=$DATA_DIR
exit 1
