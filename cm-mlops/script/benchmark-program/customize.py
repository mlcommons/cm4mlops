from cmind import utils
import os

def preprocess(i):
    os_info = i['os_info']
    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    env = i['env']

    env['CM_BIN_NAME'] = env['CM_BIN_NAME'] if 'CM_BIN_NAME' in env else "run.out"
    
    if env['CM_ENABLE_NUMACTL'].lower() in ["on", "1", "true", "yes"]:
        env['CM_ENABLE_NUMACTL'] = "1"
        CM_RUN_PREFIX = "numactl " + env['CM_NUMACTL_MEMBIND'] + ' '
    else:
        CM_RUN_PREFIX = ''
    CM_RUN_PREFIX += env['CM_RUN_PREFIX'] if 'CM_RUN_PREFIX' in env else ''
    env['CM_RUN_PREFIX'] = CM_RUN_PREFIX

    CM_RUN_SUFFIX = (env['CM_REDIRECT_OUT'] + ' ') if 'CM_REDIRECT_OUT' in env else ''
    CM_RUN_SUFFIX += (env['CM_REDIRECT_ERR'] + ' ') if 'CM_REDIRECT_ERR' in env else ''
    env['CM_RUN_SUFFIX'] = env['CM_RUN_SUFFIX'] + CM_RUN_SUFFIX if 'CM_RUN_SUFFIX' in env else CM_RUN_SUFFIX

    env['CM_RUN_CMD'] = CM_RUN_PREFIX + ' ./' + env['CM_BIN_NAME'] + ' ' + env['CM_RUN_SUFFIX']

    return {'return':0}

def postprocess(i):

    env = i['env']

    return {'return':0}
