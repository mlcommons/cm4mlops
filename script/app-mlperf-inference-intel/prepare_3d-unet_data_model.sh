#!/bin/bash


export DOWNLOAD_DATA_DIR=${CM_DATASET_PATH}
cd ${CM_HARNESS_CODE_ROOT}
pwd

mkdir -p build
ln -s ${CM_DATASET_PREPROCESSED_PATH} build/preprocessed_data

#make setup
#make duplicate_kits19_case_00185

#make preprocess_data
make preprocess_calibration_data
make preprocess_gaussian_patches

export LD_PRELOAD=${CONDA_PREFIX}/lib/libiomp5.so:$LD_PRELOAD
python trace_model.py
exit 1
