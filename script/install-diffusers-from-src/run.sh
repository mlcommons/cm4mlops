#!/bin/bash

CUR_DIR=$PWD
rm -rf diffusers
cp -r ${CM_DIFFUSERS_SRC_REPO_PATH} diffusers
cd diffusers
test "${?}" -eq "0" || exit $?
rm -rf build

${CM_PYTHON_BIN_WITH_PATH} -m pip install .
test "${?}" -eq "0" || exit $?
