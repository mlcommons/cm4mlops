from cmind import utils
import os

lscpu_out = 'tmp-lscpu.out'

def preprocess(i):

    if os.path.isfile(lscpu_out):
        os.remove(lscpu_out)

    return {'return':0}


def postprocess(i):

    state = i['state']

    env = i['env']

    if not os.path.isfile(lscpu_out):
        print ('WARNING TBD: Add Windows support in the "detect-cpu" script ...')

        return {'return':0}
#        return {'return':1, 'error':'{} was not generated'.format(lscpu_out)}

    r = utils.load_txt(file_name=lscpu_out)

    if r['return']>0: return r

    ss = r['string']

    #state['cpu_info_raw'] = ss

    # Unifying some CPU info across different platforms
    unified_env = {
            'CM_CPUINFO_CPUs':'CM_HOST_CPU_TOTAL_CORES',
            'CM_CPUINFO_L1d_cache': 'CM_HOST_CPU_L1D_CACHE_SIZE',
            'CM_CPUINFO_L1i_cache': 'CM_HOST_CPU_L1I_CACHE_SIZE',
            'CM_CPUINFO_L2_cache': 'CM_HOST_CPU_L2_CACHE_SIZE',
            'CM_CPUINFO_L3_cache': 'CM_HOST_CPU_L3_CACHE_SIZE',
            'CM_CPUINFO_Sockets': 'CM_HOST_CPU_SOCKETS',
            'CM_CPUINFO_NUMA_nodes': 'CM_HOST_CPU_NUMA_NODES',
            'CM_CPUINFO_Cores_per_socket': 'CM_HOST_CPU_PHYSICAL_CORES_PER_SOCKET',
            'CM_CPUINFO_Cores_per_cluster': 'CM_HOST_CPU_PHYSICAL_CORES_PER_SOCKET',
            'CM_CPUINFO_Threads_per_core': 'CM_HOST_CPU_THREADS_PER_CORE',
            'CM_CPUINFO_Architecture': 'CM_HOST_CPU_ARCHITECTURE',
            'CM_CPUINFO_CPU_family': 'CM_HOST_CPU_FAMILY',
            'CM_CPUINFO_CPU_max_MHz': 'CM_HOST_CPU_MAX_MHZ',
            'CM_CPUINFO_Model_name': 'CM_HOST_CPU_MODEL_NAME',
            'CM_CPUINFO_On_line_CPUs_list': 'CM_HOST_CPU_ON_LINE_CPUS_LIST',
            'CM_CPUINFO_Vendor_ID': 'CM_HOST_CPU_VENDOR_ID',
            'CM_CPUINFO_hw_physicalcpu': 'CM_HOST_CPU_TOTAL_PHYSICAL_CORES',
            'CM_CPUINFO_hw_logicalcpu': 'CM_HOST_CPU_TOTAL_CORES',
            'CM_CPUINFO_hw_packages': 'CM_HOST_CPU_SOCKETS',
            'CM_CPUINFO_hw_memsize': 'CM_HOST_CPU_MEMSIZE',
            'CM_CPUINFO_hw_l1icachesize': 'CM_HOST_CPU_L1I_CACHE_SIZE',
            'CM_CPUINFO_hw_l1dcachesize': 'CM_HOST_CPU_L1D_CACHE_SIZE',
            'CM_CPUINFO_hw_l2cachesize': 'CM_HOST_CPU_L2_CACHE_SIZE'
            }

    if env['CM_HOST_OS_TYPE'] == 'linux':
        vkeys = [ 'Architecture', 'Model name', 'Vendor ID', 'CPU family', 'NUMA node(s)', 'CPU(s)', \
                'On-line CPU(s) list', 'Socket(s)', 'Core(s) per socket', 'Core(s) per cluster', 'Thread(s) per core', 'L1d cache', 'L1i cache', 'L2 cache', \
                'L3 cache', 'CPU max MHz' ]
    elif env['CM_HOST_OS_FLAVOR'] == 'macos':
        vkeys = [ 'hw.physicalcpu', 'hw.logicalcpu', 'hw.packages', 'hw.ncpu', 'hw.memsize', 'hw.l1icachesize', \
                'hw.l2cachesize' ]
    if vkeys:
        for s in ss.split('\n'):
            v = s.split(':')
            key = v[0]
            if key in vkeys:
                env_key = 'CM_CPUINFO_'+key.replace(" ","_").replace('(','').replace(')','').replace('-','_').replace('.','_')
                if env_key in unified_env:
                    env[unified_env[env_key]]=v[1].strip()
                else:
                    env[env_key] = v[1].strip()

    if env.get('CM_HOST_CPU_SOCKETS','') == '-':#assume as 1
        env['CM_HOST_CPU_SOCKETS'] = '1'

    if env.get('CM_HOST_CPU_TOTAL_CORES', '') != '' and env.get('CM_HOST_CPU_TOTAL_LOGICAL_CORES', '') == '':
        env['CM_HOST_CPU_TOTAL_LOGICAL_CORES'] = env['CM_HOST_CPU_TOTAL_CORES']

    if env.get('CM_HOST_CPU_TOTAL_LOGICAL_CORES','') != '' and env.get('CM_HOST_CPU_TOTAL_PHYSICAL_CORES','') != '' and env.get('CM_HOST_CPU_THREADS_PER_CORE','') == '':
        env['CM_HOST_CPU_THREADS_PER_CORE'] = str(int(int(env['CM_HOST_CPU_TOTAL_LOGICAL_CORES']) //
            int(env['CM_HOST_CPU_TOTAL_PHYSICAL_CORES'])))

    if env.get('CM_HOST_CPU_SOCKETS','') != '' and env.get('CM_HOST_CPU_TOTAL_PHYSICAL_CORES','') != '' and env.get('CM_HOST_CPU_PHYSICAL_CORES_PER_SOCKET','') == '':
        env['CM_HOST_CPU_PHYSICAL_CORES_PER_SOCKET'] = str(int(env['CM_HOST_CPU_TOTAL_PHYSICAL_CORES']) // int(env['CM_HOST_CPU_SOCKETS']))

    return {'return':0}
