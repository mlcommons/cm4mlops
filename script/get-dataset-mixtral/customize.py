from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    return {'return':0}


def postprocess(i):
    env = i['env']
    
    env['CM_DATASET_MIXTRAL_PREPROCESSED_PATH'] = env['CM_DATASET_PREPROCESSED_PATH']

    return {'return':0}
