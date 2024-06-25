#!/bin/bash

export PATH=${CM_CONDA_BIN_PATH}:${PATH}

rm -rf ipex_src
cp -r ${IPEX_DIR} ipex_src
cd ipex_src

git submodule update --init --recursive

if [[ ${aCM_INTEL_IPEX_RESNET50_PATCH} == "yes" ]]; then
  bash ${CM_TMP_CURRENT_SCRIPT_PATH}/apply_intel_resnet50_patch.sh
  test "$?" -eq 0 || exit "$?"
fi

rm -rf build
echo ${CM_RUN_CMD}
eval ${CM_RUN_CMD}

test "$?" -eq 0 || exit "$?"

echo "******************************************************"

