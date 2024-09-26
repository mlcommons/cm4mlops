from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    if env.get('CM_RCLONE_CONFIG_CMD', '') != '':
      env['CM_RUN_CMD'] = env['CM_RCLONE_CONFIG_CMD']

    return {'return':0}

def postprocess(i):

    env = i['env']

    return {'return':0}
