from cmind import utils
import os
import re

def preprocess(i):

    os_info = i['os_info']

    env = i['env']
    state = i['state']
    pm = env.get('CM_HOST_OS_PACKAGE_MANAGER')

    if os_info['platform'] == 'windows':
        print ('')
        print ('WARNING: for now skipping get-generic-sys-util on Windows ...')
        print ('')

        return {'return':0}
    
    if not pm:
        return {'return': 1, 'error': 'Package manager not detected for the given OS'}

    util = env.get('CM_SYS_UTIL_NAME', '')
    if util == '':
        return {'return': 1, 'error': 'Please select a variation specifying the sys util name'}



    if not package:
        return {'return': 1, 'error': 'No package name specified for {} and util name {}'.format(pm, util)}

    package_name = package.get(pm)
    if not package_name:
        return {'return': 1, 'error': 'No package name specified for {} and util name {}'.format(pm, util)}
    
    if util == "libffi":
        if env.get("CM_HOST_OS_FLAVOR", "") == "ubuntu":
            if env.get("CM_HOST_OS_VERSION", "") in [ "20.04", "20.10", "21.04", "21.10" ]:
                package_name = "libffi7"
            else:
                package_name = "libffi8"

    package = state.get(util)
    # Temporary handling of dynamic state variables
    tmp_values = re.findall(r'<<<(.*?)>>>', str(package_name))
    for tmp_value in tmp_values:
            if tmp_value not in env:
                return {'return':1, 'error':'variable {} is not in env'.format(tmp_value)}
            if tmp_value in env:
                if type(package_name) == str:
                    package_name = package_name.replace("<<<"+tmp_value+">>>", str(env[tmp_value]))

    install_cmd = env.get('CM_HOST_OS_PACKAGE_MANAGER_INSTALL_CMD')
    if not install_cmd:
        return {'return': 1, 'error': 'Package manager installation command not detected for the given OS'}

    if pm == "brew":
        sudo = ''
    else:
        sudo = env.get('CM_SUDO', '')
    env['CM_SYS_UTIL_INSTALL_CMD'] = sudo + ' ' +install_cmd + ' ' + package_name

    env['+PATH'] = []

    if env.get('CM_HOST_OS_FLAVOR', '') == 'rhel':
        if env['CM_SYS_UTIL_NAME'] == "g++12":
            env['+PATH'] = [ "/opt/rh/gcc-toolset-12/root/usr/bin" ]

        if env['CM_SYS_UTIL_NAME'] == "numactl" and env['CM_HOST_OS_VERSION'] in [ "9.1", "9.2", "9.3" ]:
            env['CM_SYS_UTIL_INSTALL_CMD'] = ''

    return {'return':0}
