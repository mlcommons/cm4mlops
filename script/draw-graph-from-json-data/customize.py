from cmind import utils
import os


def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    env['CM_RUN_CMD'] = f"""{env['CM_PYTHON_BIN_WITH_PATH']} {os.path.join(env['CM_TMP_CURRENT_SCRIPT_PATH'],"process-cm-deps.py")}  {env['CM_JSON_INPUT_FILE']}"""

    if env.get('CM_OUTPUT_IMAGE_PATH', '') != '':
        env['CM_RUN_CMD'] += f""" --output_image {env['CM_OUTPUT_IMAGE_PATH']}"""

    if env.get('CM_OUTPUT_MERMAID_PATH', '') != '':
        env['CM_RUN_CMD'] += f""" --output_mermaid {env['CM_OUTPUT_MERMAID_PATH']}"""

    return {'return': 0}


def postprocess(i):

    env = i['env']

    return {'return': 0}
