#!/bin/bash

export PATH=${CM_CONDA_BIN_PATH}:${PATH}

if [[ ${CM_INTEL_IPEX_RESNET50_PATCH} == "yes" ]]; then
  bash ${CM_TMP_CURRENT_SCRIPT_PATH}/apply_intel_resnet50_patch.sh
fi

cd ${CM_RUN_DIR}
echo ${CM_RUN_CMD}
eval ${CM_RUN_CMD}

if [ "${?}" != "0" ]; then exit 1; fi

echo "******************************************************"

