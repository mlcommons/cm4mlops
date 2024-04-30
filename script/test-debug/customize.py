# Developer(s): Grigori Fursin

import os

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    meta = i['meta']

    print ("********************************************************")
    print ('- Importing CM library ...')
    import cmind
    print ('  SUCCESS!')

    cmind.utils.debug_here(__file__, port=5678, text='Debugging customize.py!', env=env, env_debug_uid='8d96cd9fa4734204').breakpoint()

    print ('')
    print ('- List CM repos ...')
    print ('')
    r = cmind.access({'action':'show', 'automation':'repo', 'out':'con'})
    print ('')
    print ('  SUCCESS!')
    print ("********************************************************")


    return {'return':0}


def postprocess(i):

    env = i['env']
    state = i['state']

    return {'return':0}
