#!/bin/bash

code_dir=$AMD_CODE_DIR
model_dir=
output_dir=$PWD
calib_dataset=${CM_DATASET_OPENORCA_CALIBRATION_PATH}

cd $code_dir/llama2-70b-99.9/tools/quark-0.1.0+a9827f5-mlperf/examples/torch/language_modeling/
python3 quantize_quark.py --model_dir $model_dir \
    --output_dir $output_dir \
    --quant_scheme w_fp8_a_fp8_o_fp8 \
    --dataset $calib_dataset \
    --num_calib_data 1000 \
    --model_export vllm_adopted_safetensors \
    --no_weight_matrix_merge

test $? -eq 0 || exit $?
