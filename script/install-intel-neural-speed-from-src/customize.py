from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    env = i['env']

    env['CM_PYTHON_BIN_WITH_PATH'] = os.path.join(env['CM_CONDA_BIN_PATH'], "python")

    automation = i['automation']

    recursion_spaces = i['recursion_spaces']

    env['+PATH'] = []

    return {'return':0}
