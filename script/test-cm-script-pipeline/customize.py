# Developers: Grigori Fursin

from cmind import utils
import os
import logging
def preprocess(i):

    logging.info ('')
    logging.info ('customize.py: preprocess')
    logging.info ('')

    return {'return':0}

def postprocess(i):

    automation = i['automation']
    run_script_input = i['run_script_input']
    env = i['env']

    logging.info ('')
    logging.info ('customize.py: postprocess')
    logging.info ('')

    r = automation.run_native_script({'run_script_input':run_script_input, 'env':env, 'script_name':'run2'})
    if r['return']>0:
        return r

    return {'return':0}

def detect_version(i):


    logging.info ('')
    logging.info ('customize.py: detect_version')
    logging.info ('')


    return {'return':0}
