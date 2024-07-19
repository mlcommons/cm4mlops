#!/bin/bash

#CM Script location: ${CM_TMP_CURRENT_SCRIPT_PATH}

#To export any variable
#echo "VARIABLE_NAME=VARIABLE_VALUE" >>tmp-run-env.out

#${CM_PYTHON_BIN_WITH_PATH} contains the path to python binary if "get,python" is added as a dependency



function exit_if_error() {
  test $? -eq 0 || exit $?
}

function run() {
  echo "Running: "
  echo "$1"
  echo ""
  if [[ ${CM_FAKE_RUN} != 'yes' ]]; then
    eval "$1"
    exit_if_error
  fi
}

if [ "$CM_DLRM_DATASET_DOWNLOAD" = true ]; then
    if [ -n "$CM_DLRM_DATA_PATH" ]; then
        cp -r "$CM_CRITEO_PREPROCESSED_PATH" "$CM_DLRM_DATA_PATH/criteo/day23/fp32"
    else
        cp -r "$CM_CRITEO_PREPROCESSED_PATH" "$(pwd)/criteo/day23/fp32"
    fi
    exit_if_error
fi

if [ "$CM_DLRM_MODEL_DOWNLOAD" = true ]; then
    if [ -n "$CM_DLRM_DATA_PATH" ]; then
        cp -r "$CM_ML_MODEL_FILE_WITH_PATH" "$CM_DLRM_DATA_PATH/model"
    else
        cp -r "$CM_ML_MODEL_FILE_WITH_PATH" "$(pwd)/model"
    fi
    exit_if_error
fi


#Add your run commands here...
run "$CM_RUN_CMD"
