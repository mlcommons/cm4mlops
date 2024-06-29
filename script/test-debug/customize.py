# Developer(s): Grigori Fursin

import os
import logging
def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    meta = i['meta']

    logging.info ("********************************************************")
    logging.info ('- Importing CM library ...')
    import cmind
    logging.info ('  SUCCESS!')

    cmind.utils.debug_here(__file__, port=5678, text='Debugging customize.py!', env=env, env_debug_uid='8d96cd9fa4734204').breakpoint()

    logging.info ('')
    logging.info ('- List CM repos ...')
    logging.info ('')
    r = cmind.access({'action':'show', 'automation':'repo', 'out':'con'})
    logging.info ('')
    logging.info ('  SUCCESS!')
    logging.info ("********************************************************")


    return {'return':0}


def postprocess(i):

    env = i['env']
    state = i['state']

    return {'return':0}
