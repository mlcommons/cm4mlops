#!/bin/bash


if [[ -n ${CM_DOWNLOAD_CONFIG_CMD} ]]; then
  echo ""
  echo "${CM_DOWNLOAD_CONFIG_CMD}"
  eval "${CM_DOWNLOAD_CONFIG_CMD}"
  test $? -eq 0 || exit $?
fi

require_download=1

if [[ "${CM_DOWNLOAD_LOCAL_FILE_PATH}" != "" ]]; then
  require_download=0
fi

if [[ ${CM_DOWNLOAD_TOOL} == "cmutil" ]]; then
  require_download=0

elif [ -e "${CM_DOWNLOAD_DOWNLOADED_PATH}" ]; then
  if [[ "${CM_DOWNLOAD_CHECKSUM_CMD}" != "" ]]; then
    echo ""
    echo "${CM_DOWNLOAD_CHECKSUM_CMD}"
    eval "${CM_DOWNLOAD_CHECKSUM_CMD}"
    if [ $? -ne 0 ]; then
       # checksum not supposed to fail for locally given file
       if [[ "${CM_DOWNLOAD_LOCAL_FILE_PATH}" != "" ]]; then
          exit 1
       fi
    else
       require_download="0"
    fi
  fi
fi

if [[ ${require_download} == "1" ]]; then
  echo ""
  echo ${CM_PRE_DOWNLOAD_CLEAN_CMD}
  ${CM_PRE_DOWNLOAD_CLEAN_CMD}

  echo ""
  echo "${CM_DOWNLOAD_CMD}"
  eval "${CM_DOWNLOAD_CMD}"
  test $? -eq 0 || exit $?

  if [[ "${CM_DOWNLOAD_CHECKSUM_CMD}" != "" ]]; then
     echo ""
     echo "${CM_DOWNLOAD_CHECKSUM_CMD}"
     eval "${CM_DOWNLOAD_CHECKSUM_CMD}"
     test $? -eq 0 || exit $?
  fi
fi
test $? -eq 0 || exit $?
