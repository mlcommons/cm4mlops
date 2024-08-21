from cmind import utils
import os
import hashlib

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    automation = i['automation']

    cm = automation.cmind

    path = os.path.dirname(env['CM_ML_MODEL_FILE_WITH_PATH'])

    # unzipping .pth file is not handled in download-and-extract
    if env.get('CM_UNZIP') == "yes":
        os.system("unzip -o "+env['CM_ML_MODEL_FILE_WITH_PATH'])
         
    if env.get("CM_DAE_EXTRACT_DOWNLOADED", " ") != " ":
        env['CM_ML_MODEL_PATH'] = os.path.join(path, env['CM_ML_MODEL_FILE'])
        env['CM_ML_MODEL_FILE_WITH_PATH'] = env['CM_ML_MODEL_PATH']
    else:
        env['CM_ML_MODEL_PATH'] = path

    return {'return':0}
