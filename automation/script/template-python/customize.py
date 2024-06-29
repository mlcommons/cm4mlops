from cmind import utils
import os
import logging
def preprocess(i):

    logging.info ('')
    logging.info ('Preprocessing ...')

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    logging.info ('  ENV CM_VAR1: {}'.format(env.get('CM_VAR1','')))
    
    return {'return':0}

def postprocess(i):

    logging.info ('')
    logging.info ('Postprocessing ...')

    env = i['env']

    return {'return':0}
