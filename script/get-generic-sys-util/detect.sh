#!/bin/bash

if [[ -n "${CM_SYS_UTIL_VERSION_CMD}" ]]; then
  ${CM_SYS_UTIL_VERSION_CMD}  > tmp-ver.out
fi

test $? -eq 0 || exit $?
