#!/bin/bash

${CM_PYTHON_BIN_WITH_PATH} ${CM_TMP_CURRENT_SCRIPT_PATH}/src/main.py ${CM_RUN_OPTS} ${CM_ML_MODEL_FILE_WITH_PATH}
test $? -eq 0 || exit 1
