#!/bin/bash

if [[ -n "${CM_SYS_UTIL_VERSION_CMD}" ]]; then
  if [[ "${CM_SYS_UTIL_VERSION_CMD}" == *"pstree --version"* ]]; then
    # Redirect both stdout and stderr to tmp-ver.out
    ${CM_SYS_UTIL_VERSION_CMD}  > tmp-ver.out 2>&1
  else		
    ${CM_SYS_UTIL_VERSION_CMD}  > tmp-ver.out
  fi
  echo ${CM_SYS_UTIL_VERSION_CMD}
  echo $PWD
fi

test $? -eq 0 || exit $?
