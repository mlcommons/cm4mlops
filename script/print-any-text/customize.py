# Developer(s): Grigori Fursin

from cmind import utils
import os
import logging
def postprocess(i):

    env = i['env']

    cm_env_keys = env.get('CM_PRINT_ANY_CM_ENV_KEYS', '').strip()
    os_env_keys = env.get('CM_PRINT_ANY_OS_ENV_KEYS', '').strip()

    printed = False
    for k,e,t in [(cm_env_keys, env, 'CM_ENV'), 
                  (os_env_keys, os.environ, 'OS_ENV')]:

        if k!='':
            for kk in k.split(','):
                kk = kk.strip()
                if kk!='':
                    vv = e.get(kk)

                    logging.info ('{}[{}]: {}'.format(t, kk, vv))
                    printed = True

    if printed:
        logging.info ('')

    return {'return':0}

