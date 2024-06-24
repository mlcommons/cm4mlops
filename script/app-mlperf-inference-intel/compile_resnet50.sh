export PATH=${CM_CONDA_BIN_PATH}:$PATH
echo $PWD


export DATA_CAL_DIR=calibration_dataset
export CHECKPOINT=${CM_ML_MODEL_FILE_WITH_PATH}

cd ${CM_HARNESS_CODE_ROOT}
#mkdir -p 
#cp src/ckernels/scripts/resnet50-int8-scales.json 
bash generate_torch_model.sh
test "$?" -eq 0 || exit "$?"
