#!/bin/bash

if [[ ${CM_HOST_OS_FLAVOR} == "macos" ]]; then
    sysctl -a | grep hw > tmp-lscpu.out
else
    lscpu > tmp-lscpu.out
    memory_capacity=`free -h --si | grep Mem: | tr -s ' ' | cut -d' ' -f2`
    echo "CM_HOST_MEMORY_CAPACITY=$memory_capacity">>tmp-run-env.out
    disk_capacity=`df -h --total -l |grep total |tr -s ' '|cut -d' ' -f2`
    echo "CM_HOST_DISK_CAPACITY=$disk_capacity">>tmp-run-env.out
    # extract cpu information which are not there in lscpu
    cpuinfo=$(cat /proc/cpuinfo)
    echo "CM_HOST_CPU_WRITE_PROTECT_SUPPORT=$(echo "$cpuinfo" | grep -m 1 "wp" | cut -d ':' -f 2 | xargs)">>tmp-run-env.out
    echo "CM_HOST_CPU_MICROCODE=$(echo "$cpuinfo" | grep -m 1 "microcode" | cut -d ':' -f 2 | xargs)">>tmp-run-env.out
    echo "CM_HOST_CPU_FPU_SUPPORT=$(echo "$cpuinfo" | grep -m 1 "fpu" | cut -d ':' -f 2 | xargs)">>tmp-run-env.out
    echo "CM_HOST_CPU_FPU_EXCEPTION_SUPPORT=$(echo "$cpuinfo" | grep -m 1 "fpu_exception" | cut -d ':' -f 2 | xargs)">>tmp-run-env.out
    echo "CM_HOST_CPU_BUGS=$(echo "$cpuinfo" | grep -m 1 "bugs" | cut -d ':' -f 2 | xargs)">>tmp-run-env.out
    echo "CM_HOST_CPU_TLB_SIZE=$(echo "$cpuinfo" | grep -m 1 "TLB size" | cut -d ':' -f 2 | xargs)">>tmp-run-env.out
    echo "CM_HOST_CPU_CFLUSH_SIZE=$(echo "$cpuinfo" | grep -m 1 "clush size" | cut -d ':' -f 2 | xargs)">>tmp-run-env.out
    echo "CM_HOST_CACHE_ALLIGNMENT_SIZE=$(echo "$cpuinfo" | grep -m 1 "cache_alignment" | cut -d ':' -f 2 | xargs)">>tmp-run-env.out
    echo "CM_HOST_POWER_MANAGEMENT=$(echo "$cpuinfo" | grep -m 1 "power management" | cut -d ':' -f 2 | xargs)">>tmp-run-env.out    
fi
