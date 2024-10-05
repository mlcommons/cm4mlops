from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    cmd = "gh auth login"
    if env.get('CM_GH_AUTH_TOKEN', '') != '':
        if os_info['platform'] == 'windows':
            cmd = f"{cmd} --with-token %CM_GH_AUTH_TOKEN%"
        else:
            cmd = f" echo {env['CM_GH_AUTH_TOKEN']} | {cmd} --with-token"

    env['CM_RUN_CMD'] = cmd
    quiet = (env.get('CM_QUIET', False) == 'yes')

    return {'return':0}

def postprocess(i):

    env = i['env']

    return {'return':0}
