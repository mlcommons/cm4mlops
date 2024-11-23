from cmind import utils
import os


def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    return {'return': 0}


def postprocess(i):

    env = i['env']

    cache_dir = os.getcwd()
    if env.get('CM_CACHE_DIR_ENV_NAME', '') != '':
        env[env['CM_CACHE_DIR_ENV_NAME']] = cache_dir

    env['CM_CACHE_DIR'] = cache_dir
    env['CM_GET_DEPENDENT_CACHED_PATH'] = cache_dir

    return {'return': 0}
