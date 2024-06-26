#!/bin/bash

export CM_HOST_OS_DEFAULT_LIBRARY_PATH="/usr/local/lib/x86_64-linux-gnu:/lib/x86_64-linux-gnu:/usr/lib/x86_64-linux-gnu:/usr/lib/x86_64-linux-gnu64:/usr/local/lib64:/lib64:/usr/lib64:/usr/local/lib:/lib:/usr/lib:/usr/x86_64-linux-gnu/lib64:/usr/x86_64-linux-gnu/lib:${CM_HOST_OS_DEFAULT_LIBRARY_PATH}"
export CPLUS_INCLUDE_PATH="/home/anandhu/CM/repos/local/cache/9053e99e1d64476c/install/include:${CPLUS_INCLUDE_PATH}"
export C_INCLUDE_PATH="/home/anandhu/CM/repos/local/cache/9053e99e1d64476c/install/include:${C_INCLUDE_PATH}"
export DYLD_FALLBACK_LIBRARY_PATH="/home/anandhu/CM/repos/local/cache/9053e99e1d64476c/install/lib:${DYLD_FALLBACK_LIBRARY_PATH}"
export LD_LIBRARY_PATH="/home/anandhu/CM/repos/local/cache/9053e99e1d64476c/install/lib:${LD_LIBRARY_PATH}"
export PYTHONPATH="/home/anandhu/CM/repos/local/cache/83d1da9dade244bc/inference/vision/classification_and_detection/python:/home/anandhu/CM/repos/local/cache/83d1da9dade244bc/inference/tools/submission:/home/anandhu/CM/repos/anandhu-eng@cm4mlops/script/get-mlperf-inference-utils:/home/anandhu/CM/repos/local/cache/9053e99e1d64476c/install/python:${PYTHONPATH}"
export CK_PROGRAM_TMP_DIR="None"
export CM_ABTF_ML_MODEL_CONFIG="baseline_8MP_ss_scales_fm1_5x5_all"
export CM_ABTF_ML_MODEL_SKIP_WARMUP="yes"
export CM_ABTF_ML_MODEL_TRAINING_FORCE_COGNATA_LABELS="yes"
export CM_ABTF_NUM_CLASSES="15"
export CM_ABTF_POC_DEMO="True"
export CM_COGNATA_ACCURACY_DUMP_FILE="/home/anandhu/CM/repos/local/cache/030bfa7b77044ef3/test_results/anandhu_VivoBook_ASUSLaptop_X515UA_M515UA-reference-cpu-pytorch-v2.3.0-default_config/retinanet/singlestream/performance/run_1/accuracy.txt"
export CM_DATASET_MLCOMMONS_COGNATA_DOWNLOAD_TOOL="rclone"
export CM_DATASET_MLCOMMONS_COGNATA_FILE_NAMES=""
export CM_DATASET_MLCOMMONS_COGNATA_GROUP_NAMES="Cognata_Camera_01_8M"
export CM_DATASET_MLCOMMONS_COGNATA_KEY1="Dataset 1.0"
export CM_DATASET_MLCOMMONS_COGNATA_PATH="/home/anandhu/CM/repos/local/cache/5f9ed03332b34a31"
export CM_DATASET_MLCOMMONS_COGNATA_SERIAL_NUMBERS="10002_Urban_Clear_Morning"
export CM_ENABLE_NUMACTL="0"
export CM_ENABLE_PROFILING="0"
export CM_HOST_CPU_ARCHITECTURE="x86_64"
export CM_HOST_CPU_FAMILY="23"
export CM_HOST_CPU_L1D_CACHE_SIZE="192 KiB (6 instances)"
export CM_HOST_CPU_L1I_CACHE_SIZE="192 KiB (6 instances)"
export CM_HOST_CPU_L2_CACHE_SIZE="3 MiB (6 instances)"
export CM_HOST_CPU_L3_CACHE_SIZE="8 MiB (2 instances)"
export CM_HOST_CPU_MAX_MHZ="2100.0000"
export CM_HOST_CPU_MODEL_NAME="AMD Ryzen 5 5500U with Radeon Graphics"
export CM_HOST_CPU_NUMA_NODES="1"
export CM_HOST_CPU_ON_LINE_CPUS_LIST="0-11"
export CM_HOST_CPU_PHYSICAL_CORES_PER_SOCKET="6"
export CM_HOST_CPU_SOCKETS="1"
export CM_HOST_CPU_THREADS_PER_CORE="2"
export CM_HOST_CPU_TOTAL_CORES="12"
export CM_HOST_CPU_TOTAL_LOGICAL_CORES="12"
export CM_HOST_CPU_VENDOR_ID="AuthenticAMD"
export CM_HOST_DISK_CAPACITY="205G"
export CM_HOST_MEMORY_CAPACITY="19G"
export CM_HOST_OS_BITS="64"
export CM_HOST_OS_FLAVOR="ubuntu"
export CM_HOST_OS_FLAVOR_LIKE="debian"
export CM_HOST_OS_GLIBC_VERSION="2.35"
export CM_HOST_OS_KERNEL_VERSION="5.15.0-107-generic"
export CM_HOST_OS_MACHINE="x86_64"
export CM_HOST_OS_PACKAGE_MANAGER="apt"
export CM_HOST_OS_PACKAGE_MANAGER_INSTALL_CMD="DEBIAN_FRONTEND=noninteractive apt-get install -y"
export CM_HOST_OS_PACKAGE_MANAGER_UPDATE_CMD="apt-get update -y"
export CM_HOST_OS_TYPE="linux"
export CM_HOST_OS_VERSION="22.04"
export CM_HOST_PLATFORM_FLAVOR="x86_64"
export CM_HOST_PYTHON_BITS="64"
export CM_HOST_SYSTEM_NAME="anandhu-VivoBook-ASUSLaptop-X515UA-M515UA"
export CM_HW_NAME="anandhu_VivoBook_ASUSLaptop_X515UA_M515UA"
export CM_LOGS_DIR="/home/anandhu/CM/repos/local/cache/030bfa7b77044ef3/test_results/anandhu_VivoBook_ASUSLaptop_X515UA_M515UA-reference-cpu-pytorch-v2.3.0-default_config/retinanet/singlestream/performance/run_1"
export CM_MAX_EXAMPLES="20"
export CM_MLPERF_ACCURACY_RESULTS_DIR=""
export CM_MLPERF_BACKEND="pytorch"
export CM_MLPERF_BACKEND_VERSION="2.3.0"
export CM_MLPERF_CONF="/home/anandhu/CM/repos/local/cache/83d1da9dade244bc/inference/mlperf.conf"
export CM_MLPERF_DEVICE="cpu"
export CM_MLPERF_IMPLEMENTATION="reference"
export CM_MLPERF_INFERENCE_3DUNET_PATH="/home/anandhu/CM/repos/local/cache/83d1da9dade244bc/inference/vision/medical_imaging/3d-unet-kits19"
export CM_MLPERF_INFERENCE_BERT_PATH="/home/anandhu/CM/repos/local/cache/83d1da9dade244bc/inference/language/bert"
export CM_MLPERF_INFERENCE_CLASSIFICATION_AND_DETECTION_PATH="/home/anandhu/CM/repos/local/cache/83d1da9dade244bc/inference/vision/classification_and_detection"
export CM_MLPERF_INFERENCE_CONF_PATH="/home/anandhu/CM/repos/local/cache/83d1da9dade244bc/inference/mlperf.conf"
export CM_MLPERF_INFERENCE_DLRM_PATH="/home/anandhu/CM/repos/local/cache/83d1da9dade244bc/inference/recommendation/dlrm"
export CM_MLPERF_INFERENCE_DLRM_V2_PATH="/home/anandhu/CM/repos/local/cache/83d1da9dade244bc/inference/recommendation/dlrm_v2"
export CM_MLPERF_INFERENCE_FINAL_RESULTS_DIR="/home/anandhu/CM/repos/local/cache/030bfa7b77044ef3/test_results"
export CM_MLPERF_INFERENCE_GPTJ_PATH="/home/anandhu/CM/repos/local/cache/83d1da9dade244bc/inference/language/gpt-j"
export CM_MLPERF_INFERENCE_LOADGEN_BUILD_CLEAN="yes"
export CM_MLPERF_INFERENCE_LOADGEN_INCLUDE_PATH="/home/anandhu/CM/repos/local/cache/9053e99e1d64476c/install/include"
export CM_MLPERF_INFERENCE_LOADGEN_INSTALL_PATH="/home/anandhu/CM/repos/local/cache/9053e99e1d64476c/install"
export CM_MLPERF_INFERENCE_LOADGEN_LIBRARY_PATH="/home/anandhu/CM/repos/local/cache/9053e99e1d64476c/install/lib"
export CM_MLPERF_INFERENCE_LOADGEN_PYTHON_PATH="/home/anandhu/CM/repos/local/cache/9053e99e1d64476c/install/python"
export CM_MLPERF_INFERENCE_RESULTS_DIR="/home/anandhu/CM/repos/local/cache/030bfa7b77044ef3"
export CM_MLPERF_INFERENCE_RESULTS_VERSION="4_0"
export CM_MLPERF_INFERENCE_RNNT_PATH="/home/anandhu/CM/repos/local/cache/83d1da9dade244bc/inference/speech_recognition/rnnt"
export CM_MLPERF_INFERENCE_SOURCE="/home/anandhu/CM/repos/local/cache/83d1da9dade244bc/inference"
export CM_MLPERF_INFERENCE_VERSION="poc-demo"
export CM_MLPERF_INFERENCE_VISION_PATH="/home/anandhu/CM/repos/local/cache/83d1da9dade244bc/inference/inference/vision"
export CM_MLPERF_LAST_RELEASE="v4.0"
export CM_MLPERF_LOADGEN_ALL_MODES="yes"
export CM_MLPERF_LOADGEN_BUILD_FROM_SRC="on"
export CM_MLPERF_LOADGEN_COMPLIANCE="no"
export CM_MLPERF_LOADGEN_EXTRA_OPTIONS="   --max-batchsize 1 --count 20 --mlperf_conf '/home/anandhu/CM/repos/local/cache/83d1da9dade244bc/inference/mlperf.conf'"
export CM_MLPERF_LOADGEN_LOGS_DIR="/home/anandhu/CM/repos/local/cache/030bfa7b77044ef3/test_results/anandhu_VivoBook_ASUSLaptop_X515UA_M515UA-reference-cpu-pytorch-v2.3.0-default_config/retinanet/singlestream/performance/run_1"
export CM_MLPERF_LOADGEN_MAX_BATCHSIZE="1"
export CM_MLPERF_LOADGEN_MODE="performance"
export CM_MLPERF_LOADGEN_MODES="['performance', 'accuracy']"
export CM_MLPERF_LOADGEN_QPS_OPT=""
export CM_MLPERF_LOADGEN_QUERY_COUNT="20"
export CM_MLPERF_LOADGEN_SCENARIO="SingleStream"
export CM_MLPERF_LOADGEN_SCENARIOS="['SingleStream']"
export CM_MLPERF_MAX_QUERY_COUNT="20"
export CM_MLPERF_MODEL="abtf-poc-model"
export CM_MLPERF_OUTPUT_DIR="/home/anandhu/CM/repos/local/cache/030bfa7b77044ef3/test_results/anandhu_VivoBook_ASUSLaptop_X515UA_M515UA-reference-cpu-pytorch-v2.3.0-default_config/retinanet/singlestream/performance/run_1"
export CM_MLPERF_PYTHON="yes"
export CM_MLPERF_QUANTIZATION="False"
export CM_MLPERF_RANGING_USER_CONF="/home/anandhu/CM/repos/anandhu-eng@cm4mlops/script/generate-mlperf-inference-user-conf/tmp/ranging_47b6b843ed404540955d8d06dd1a9909.conf"
export CM_MLPERF_RUN_CMD="/usr/bin/python3 /home/anandhu/CM/repos/mlcommons@cm4abtf/script/demo-ml-model-abtf-cognata-pytorch-loadgen/ref/python/main.py --profile retinanet-pytorch --model='/home/anandhu/CM/repos/local/cache/25b2614e96944b33/baseline_8MP_ss_scales_fm1_5x5_all_ep60.pth' --dataset=cognata-8mp-pt --dataset-path='/home/anandhu/CM/repos/local/cache/5f9ed03332b34a31' --cache_dir='/home/anandhu/CM/repos/mlcommons@cm4abtf/script/demo-ml-model-abtf-cognata-pytorch-loadgen/tmp-preprocessed-dataset' --scenario SingleStream  --output '/home/anandhu/CM/repos/local/cache/030bfa7b77044ef3/test_results/anandhu_VivoBook_ASUSLaptop_X515UA_M515UA-reference-cpu-pytorch-v2.3.0-default_config/retinanet/singlestream/performance/run_1'    --max-batchsize 1 --count 20 --mlperf_conf '/home/anandhu/CM/repos/local/cache/83d1da9dade244bc/inference/mlperf.conf' --threads 12 --user_conf '/home/anandhu/CM/repos/anandhu-eng@cm4mlops/script/generate-mlperf-inference-user-conf/tmp/47b6b843ed404540955d8d06dd1a9909.conf'"
export CM_MLPERF_RUN_STYLE="test"
export CM_MLPERF_SKIP_RUN="no"
export CM_MLPERF_SKIP_SUBMISSION_GENERATION="yes"
export CM_MLPERF_SUBMISSION_GENERATION_STYLE="full"
export CM_MLPERF_SUT_NAME_IMPLEMENTATION_PREFIX="reference"
export CM_MLPERF_SUT_NAME_RUN_CONFIG_SUFFIX=""
export CM_MLPERF_TESTING_USER_CONF="/home/anandhu/CM/repos/anandhu-eng@cm4mlops/script/generate-mlperf-inference-user-conf/tmp/47b6b843ed404540955d8d06dd1a9909.conf"
export CM_MLPERF_USER_CONF="/home/anandhu/CM/repos/anandhu-eng@cm4mlops/script/generate-mlperf-inference-user-conf/tmp/47b6b843ed404540955d8d06dd1a9909.conf"
export CM_MLPERF_VISION_DATASET_OPTION="cognata-8mp-pt"
export CM_ML_MODEL_CHECKSUM="26845c3b9573ce115ef29dca4ae5be14"
export CM_ML_MODEL_CODE_WITH_PATH="/home/anandhu/CM/repos/local/cache/2e674002c62a41bc/repo"
export CM_ML_MODEL_DATASET="cognata"
export CM_ML_MODEL_FILE="baseline_8MP_ss_scales_fm1_5x5_all_ep60.pth"
export CM_ML_MODEL_FILENAME="baseline_8MP_ss_scales_fm1_5x5_all_ep60.pth"
export CM_ML_MODEL_FILE_WITH_PATH="/home/anandhu/CM/repos/local/cache/25b2614e96944b33/baseline_8MP_ss_scales_fm1_5x5_all_ep60.pth"
export CM_ML_MODEL_IMAGE_SIZE="8M"
export CM_ML_MODEL_URL="https://automotive.mlcommons-storage.org/SSD_ResNet50%2Fbaseline_8MP_ss_scales_fm1_5x5_all_ep60.pth"
export CM_MODEL="retinanet"
export CM_NUMPY_VERSION="1.26.4"
export CM_NUM_THREADS="12"
export CM_OPENCV_PYTHON_VERSION="4.10.0.84"
export CM_OUTPUT_FOLDER_NAME="test_results"
export CM_PYCOCOTOOLS_VERSION="2.0.8"
export CM_PYTHONLIB_CMIND_CACHE_TAGS="version-2.3.1"
export CM_PYTHONLIB_FASTER_COCO_EVAL_CACHE_TAGS="version-1.5.7"
export CM_PYTHONLIB_NUMPY_CACHE_TAGS="version-1.26.4"
export CM_PYTHONLIB_OPENCV_PYTHON_CACHE_TAGS="version-4.10.0.84"
export CM_PYTHONLIB_PIP_CACHE_TAGS="version-22.0.2"
export CM_PYTHONLIB_PSUTIL_CACHE_TAGS="version-5.9.8"
export CM_PYTHONLIB_PYCOCOTOOLS_CACHE_TAGS="version-2.0.8"
export CM_PYTHONLIB_TORCHMETRICS_CACHE_TAGS="version-1.4.0.post0"
export CM_PYTHONLIB_TORCHVISION_CACHE_TAGS="version-0.18.0"
export CM_PYTHONLIB_TORCH_CACHE_TAGS="version-2.3.0"
export CM_PYTHON_BIN="python3"
export CM_PYTHON_BIN_PATH="/usr/bin"
export CM_PYTHON_BIN_WITH_PATH="/usr/bin/python3"
export CM_PYTHON_CACHE_TAGS="version-3.10.12,non-virtual"
export CM_PYTHON_MAJOR_VERSION="3"
export CM_PYTHON_MINOR_VERSION="10"
export CM_PYTHON_PATCH_VERSION="12"
export CM_PYTHON_VERSION="3.10.12"
export CM_QUIET="yes"
export CM_RUN_CMD="/usr/bin/python3 /home/anandhu/CM/repos/mlcommons@cm4abtf/script/demo-ml-model-abtf-cognata-pytorch-loadgen/ref/python/main.py --profile retinanet-pytorch --model='/home/anandhu/CM/repos/local/cache/25b2614e96944b33/baseline_8MP_ss_scales_fm1_5x5_all_ep60.pth' --dataset=cognata-8mp-pt --dataset-path='/home/anandhu/CM/repos/local/cache/5f9ed03332b34a31' --cache_dir='/home/anandhu/CM/repos/mlcommons@cm4abtf/script/demo-ml-model-abtf-cognata-pytorch-loadgen/tmp-preprocessed-dataset' --scenario SingleStream  --output '/home/anandhu/CM/repos/local/cache/030bfa7b77044ef3/test_results/anandhu_VivoBook_ASUSLaptop_X515UA_M515UA-reference-cpu-pytorch-v2.3.0-default_config/retinanet/singlestream/performance/run_1'    --max-batchsize 1 --count 20 --mlperf_conf '/home/anandhu/CM/repos/local/cache/83d1da9dade244bc/inference/mlperf.conf' --threads 12 --user_conf '/home/anandhu/CM/repos/anandhu-eng@cm4mlops/script/generate-mlperf-inference-user-conf/tmp/47b6b843ed404540955d8d06dd1a9909.conf' 2>&1 ; echo \$? > exitstatus | tee '/home/anandhu/CM/repos/local/cache/030bfa7b77044ef3/test_results/anandhu_VivoBook_ASUSLaptop_X515UA_M515UA-reference-cpu-pytorch-v2.3.0-default_config/retinanet/singlestream/performance/run_1/console.out'"
export CM_RUN_DIR="/home/anandhu/CM/repos/mlcommons@cm4abtf/script/demo-ml-model-abtf-cognata-pytorch-loadgen/ref"
export CM_RUN_MLPERF_INFERENCE_APP_DEFAULTS="poc-demo"
export CM_SUT_CONFIGS_PATH="/home/anandhu/CM/repos/local/cache/0a0ca8118bc54941"
export CM_SUT_DESC_CACHE="no"
export CM_SUT_META_EXISTS="yes"
export CM_SUT_NAME="anandhu_VivoBook_ASUSLaptop_X515UA_M515UA-reference-cpu-pytorch-v2.3.0-default_config"
export CM_TEST_QUERY_COUNT="20"
export CM_TMP_CURRENT_PATH="/home/anandhu/CM/repos/anandhu-eng@cm4mlops"
export CM_TMP_CURRENT_SCRIPT_PATH="/home/anandhu/CM/repos/anandhu-eng@cm4mlops/script/benchmark-program"
export CM_TMP_CURRENT_SCRIPT_REPO_PATH="/home/anandhu/CM/repos/anandhu-eng@cm4mlops"
export CM_TMP_CURRENT_SCRIPT_REPO_PATH_WITH_PREFIX="/home/anandhu/CM/repos/anandhu-eng@cm4mlops"
export CM_TMP_CURRENT_SCRIPT_WORK_PATH="/home/anandhu/CM/repos/anandhu-eng@cm4mlops"
export CM_TMP_PIP_VERSION_STRING=""
export CM_TORCHVISION_VERSION="0.18.0"
export CM_TORCH_VERSION="2.3.0"
export CM_VERBOSE="yes"
export CUDA_VISIBLE_DEVICES=""
export HOST_CPU_ARCHITECTURE="x86_64"
export HOST_CPU_FAMILY="23"
export HOST_CPU_L1D_CACHE_SIZE="192 KiB (6 instances)"
export HOST_CPU_L1I_CACHE_SIZE="192 KiB (6 instances)"
export HOST_CPU_L2_CACHE_SIZE="3 MiB (6 instances)"
export HOST_CPU_L3_CACHE_SIZE="8 MiB (2 instances)"
export HOST_CPU_MAX_MHZ="2100.0000"
export HOST_CPU_MODEL_NAME="AMD Ryzen 5 5500U with Radeon Graphics"
export HOST_CPU_NUMA_NODES="1"
export HOST_CPU_ON_LINE_CPUS_LIST="0-11"
export HOST_CPU_PHYSICAL_CORES_PER_SOCKET="6"
export HOST_CPU_SOCKETS="1"
export HOST_CPU_THREADS_PER_CORE="2"
export HOST_CPU_TOTAL_CORES="12"
export HOST_CPU_TOTAL_LOGICAL_CORES="12"
export HOST_CPU_VENDOR_ID="AuthenticAMD"
export HOST_DISK_CAPACITY="205G"
export HOST_MEMORY_CAPACITY="19G"
export HOST_OS_BITS="64"
export HOST_OS_FLAVOR="ubuntu"
export HOST_OS_FLAVOR_LIKE="debian"
export HOST_OS_GLIBC_VERSION="2.35"
export HOST_OS_KERNEL_VERSION="5.15.0-107-generic"
export HOST_OS_MACHINE="x86_64"
export HOST_OS_PACKAGE_MANAGER="apt"
export HOST_OS_PACKAGE_MANAGER_INSTALL_CMD="DEBIAN_FRONTEND=noninteractive apt-get install -y"
export HOST_OS_PACKAGE_MANAGER_UPDATE_CMD="apt-get update -y"
export HOST_OS_TYPE="linux"
export HOST_OS_VERSION="22.04"
export HOST_PLATFORM_FLAVOR="x86_64"
export HOST_PYTHON_BITS="64"
export HOST_SYSTEM_NAME="anandhu-VivoBook-ASUSLaptop-X515UA-M515UA"
export ML_MODEL_CHECKSUM="26845c3b9573ce115ef29dca4ae5be14"
export ML_MODEL_CODE_WITH_PATH="/home/anandhu/CM/repos/local/cache/2e674002c62a41bc/repo"
export ML_MODEL_DATASET="cognata"
export ML_MODEL_FILE="baseline_8MP_ss_scales_fm1_5x5_all_ep60.pth"
export ML_MODEL_FILENAME="baseline_8MP_ss_scales_fm1_5x5_all_ep60.pth"
export ML_MODEL_FILE_WITH_PATH="/home/anandhu/CM/repos/local/cache/25b2614e96944b33/baseline_8MP_ss_scales_fm1_5x5_all_ep60.pth"
export ML_MODEL_IMAGE_SIZE="8M"
export ML_MODEL_URL="https://automotive.mlcommons-storage.org/SSD_ResNet50%2Fbaseline_8MP_ss_scales_fm1_5x5_all_ep60.pth"
export MODEL_DIR="/home/anandhu/CM/repos/local/cache/25b2614e96944b33"
export MODEL_FILE="/home/anandhu/CM/repos/local/cache/25b2614e96944b33/baseline_8MP_ss_scales_fm1_5x5_all_ep60.pth"
export OUTPUT_BASE_DIR="/home/anandhu/CM/repos/local/cache/030bfa7b77044ef3"
export OUTPUT_DIR="/home/anandhu/CM/repos/local/cache/030bfa7b77044ef3/test_results/anandhu_VivoBook_ASUSLaptop_X515UA_M515UA-reference-cpu-pytorch-v2.3.0-default_config/retinanet/singlestream/performance/run_1"
export RUN_DIR="/home/anandhu/CM/repos/mlcommons@cm4abtf/script/demo-ml-model-abtf-cognata-pytorch-loadgen/ref"
export USE_CUDA="False"
export USE_GPU="False"


. "/home/anandhu/CM/repos/anandhu-eng@cm4mlops/script/benchmark-program/run-ubuntu.sh"
