#!/bin/bash

CUR=${PWD}
mkdir -p install
INSTALL_DIR=${CUR}/install

cd ${CM_MLPERF_INFERENCE_CLASSIFICATION_AND_DETECTION_PATH}
cd tools

if [[ ${CM_DATASET_CALIBRATION} == "no" ]]; then
  if [ ! -z {CM_DATASET_SIZE} ]; then
    max_images=" -m ${CM_DATASET_SIZE}"
  else
    max_images=""
  fi
  cmd="./openimages_mlperf.sh -d ${INSTALL_DIR} ${max_images}"
  echo $cmd
  eval $cmd
  test $? -eq 0 || exit 1
else
  cmd="./openimages_calibration_mlperf.sh -d ${INSTALL_DIR}"
  echo $cmd
  eval $cmd
  test $? -eq 0 || exit 1
  cd $INSTALL_DR
  wget ${CM_CALIBRATION_DATASET_WGET_URL}
  test $? -eq 0 || exit 1
fi
cd ${INSTALL_DIR}
if [[ ! -f "open-images-v6-mlperf" ]]; then
  ln -s ../ open-images-v6-mlperf
fi

test $? -eq 0 || exit 1
