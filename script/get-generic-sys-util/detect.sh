#!/bin/bash

if [[ -n "${CM_SYS_UTIL_VERSION_CMD}" ]]; then
  if [[ "${CM_SYS_UTIL_VERSION_CMD_USE_ERROR_STREAM}" == "yes" ]]; then
    # Redirect both stdout and stderr to tmp-ver.out
    ${CM_SYS_UTIL_VERSION_CMD}  > tmp-ver.out 2>&1
  else		
    ${CM_SYS_UTIL_VERSION_CMD}  > tmp-ver.out
  fi
  echo ${CM_SYS_UTIL_VERSION_CMD}
  echo $PWD
fi

test $? -eq 0 || exit $?
