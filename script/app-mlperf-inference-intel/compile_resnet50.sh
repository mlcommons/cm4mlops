export DATA_CAL_DIR=calibration_dataset
export CHECKPOINT=resnet50-fp32-model.pth

cd ${CM_HARNESS_CODE_ROOT}
bash generate_torch_model.sh

bash build_binaries.sh
