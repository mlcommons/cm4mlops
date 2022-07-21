#!/bin/bash

uname -m > tmp-run.out
uname -a >> tmp-run.out

if test -f "/etc/os-release"; then
   echo "CM_HOST_OS_FLAVOR=`cat /etc/os-release | grep '^ID=' | cut -d'=' -f2 | cut -d'"' -f2 | tr '[:upper:]' '[:lower:]'`" >> tmp-run-env.out
   echo "CM_HOST_OS_FLAVOR_LIKE=`cat /etc/os-release | grep '^ID_LIKE=' | cut -d'=' -f2 | cut -d'"' -f2 | tr '[:upper:]' '[:lower:]'`" >> tmp-run-env.out
   echo "CM_HOST_OS_VERSION=`cat /etc/os-release | grep '^VERSION_ID=' | cut -d'=' -f2 | cut -d'"' -f2 | cut -d'"' -f2 | tr '[:upper:]' '[:lower:]'`" >> tmp-run-env.out
   echo "CM_HOST_OS_KERNEL_VERSION=`uname -r`" >> tmp-run-env.out
   echo "CM_HOST_PLATFORM_FLAVOR=`uname -m`" >> tmp-run-env.out
else
   echo "CM_HOST_OS_FLAVOR=`sw_vers | grep '^ProductName:' | cut -f2 | tr '[:upper:]' '[:lower:]' `" >> tmp-run-env.out
   echo "CM_HOST_OS_VERSION=`sw_vers | grep '^ProductVersion:' | cut -f2 | tr '[:upper:]' '[:lower:]' `" >> tmp-run-env.out
   echo "CM_HOST_OS_KERNEL_VERSION=`uname -r`" >> tmp-run-env.out
   echo "CM_HOST_PLATFORM_FLAVOR=`uname -m `" >> tmp-run-env.out
fi
