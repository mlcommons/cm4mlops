#!/bin/bash
if [[ ${CM_MLPERF_POWER} == "yes" && ${CM_MLPERF_LOADGEN_MODE} == "performance" ]]; then
    exit 0
fi

# Run
if [ -z ${CM_RUN_DIR} ]; then
  echo "CM_RUN_DIR is not set"
  exit 1
fi

cd ${CM_RUN_DIR}

if [[ "${CM_DEBUG_SCRIPT_BENCHMARK_PROGRAM}" == "True" ]]; then
  echo "*****************************************************"
  echo "You are now in Debug shell with pre-set CM env and can run the following command line manually:"

  echo ""
  if [[ "${CM_RUN_CMD0}" != "" ]]; then
    echo "${CM_RUN_CMD0}"
  else
    echo "${CM_RUN_CMD}"
  fi

  echo ""
  echo "Type exit to return to CM script."
  echo ""
#  echo "You can also run . ./debug-script-benchmark-program.sh to reproduce and customize run."
#  echo ""
#
#  cp -f tmp-run.sh debug-script-benchmark-program.sh
#
#  sed -e 's/CM_DEBUG_SCRIPT_BENCHMARK_PROGRAM="True"/CM_DEBUG_SCRIPT_BENCHMARK_PROGRAM="False"/g' -i debug-script-benchmark-program.sh

  bash

  # do not re-run command below to pick up manual run!
  exit 0
fi

if [[ "${CM_PROFILE_NVIDIA_POWER}" == "on" ]]; then
  echo "Starting monitoring system utilisation!!!"
  echo "cm run script --tags=record,system,utilisation${CM_SYS_UTILISATION_SCRIPT_TAGS}"
  cm run script --tags=record,system,utilisation${CM_SYS_UTILISATION_SCRIPT_TAGS} &
  cmd1_pid=$!
  echo $cmd1_pid
  test $? -eq 0 || exit 1
fi

# Check CM_RUN_CMD0
if [[ "${CM_RUN_CMD0}" != "" ]]; then
  eval ${CM_RUN_CMD0}
  exitstatus=$?
  if [ -e exitstatus ]; then
    exitstatus=$( cat exitstatus )
  fi
  test $exitstatus -eq 0 || $exitstatus
else
  echo "${CM_RUN_CMD}"
  eval ${CM_RUN_CMD}
  exitstatus=$?
  if [ -e exitstatus ]; then
    exitstatus=$( cat exitstatus )
  fi
  test $exitstatus -eq 0 || $exitstatus
fi

test $? -eq 0 || exit $? 


if [[ "${CM_PROFILE_NVIDIA_POWER}" == "on" ]]; then
  echo "killing process ${cmd1_pid}"
  kill ${cmd1_pid}
  test $? -eq 0 || exit $? 
fi