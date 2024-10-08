#!/bin/bash

# function to safely exit the background process
safe_exit() {
  if [[ "${CM_POST_RUN_CMD}" != "" ]]; then
    eval ${CM_POST_RUN_CMD}
    if [ $? -eq 0 ]; then
      exit 0
    else
      exit $?
    fi
  fi
}

# trap signals to redirect the execution flow to safe_exit
trap safe_exit SIGINT SIGTERM

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

echo $CM_PRE_RUN_CMD
eval ${CM_PRE_RUN_CMD}

# Check CM_RUN_CMD0
if [[ "${CM_RUN_CMD0}" != "" ]]; then
  eval ${CM_RUN_CMD0}
  exitstatus=$?
else
  echo "${CM_RUN_CMD}"
  eval ${CM_RUN_CMD}
  exitstatus=$?
fi

eval ${CM_POST_RUN_CMD}
test $? -eq 0 || exit $? 

test $exitstatus -eq 0 || $exitstatus


