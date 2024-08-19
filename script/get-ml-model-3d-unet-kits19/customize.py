from cmind import utils
import os
import hashlib

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    automation = i['automation']

    cm = automation.cmind

    path = os.path.dirname(env['CM_ML_MODEL_FILE_WITH_PATH'])

    print(env['CM_ML_MODEL_ACCURACY'])
    
    if env.get('CM_UNZIP') == "yes":
            zip_filename = env['CM_ML_MODEL_FILE_WITH_PATH']
            os.system("unzip -o "+zip_filename)
            model_filename = env['CM_ML_MODEL_FILE']
            env['CM_ML_MODEL_FILE_WITH_PATH']=os.path.join(path, model_filename)

    env['CM_ML_MODEL_PATH']=path

    return {'return':0}
