from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    env['CM_RUN_CMD'] = f"""{env['CM_PYTHON_BIN_WITH_PATH']} {os.path.join(env['CM_TMP_CURRENT_SCRIPT_PATH'],"process-cm-deps.py")}  {env['CM_JSON_INPUT_FILE']}""" 

    return {'return':0}

def postprocess(i):

    env = i['env']

    return {'return':0}
