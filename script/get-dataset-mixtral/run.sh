#!/bin/bash

echo ""

rclone copyurl ${CM_RCLONE_LINUX_URL} ./ -a -P
test $? -eq 0 || exit 1

echo "CM_DATASET_PREPROCESSED_PATH=$PWD/${CM_DATASET_FILE_NAME}" > tmp-run-env.out
