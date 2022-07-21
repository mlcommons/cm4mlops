from cmind import utils
import os

def preprocess(i):

    env = i['env']
    state = i['state']

    os_info = i['os_info']

    # Update env variables
    env['CM_HOST_OS_TYPE'] = os_info['platform']
    env['CM_HOST_OS_BITS'] = os_info['bits']
    env['CM_HOST_PYTHON_BITS'] = os_info['python_bits']

    # Update state (demo)
    state['os_info'] = os_info

    return {'return':0}


def postprocess(i):

    env = i['env']
    state = i['state']

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        print ('Windows: TBD')

    else:
        r = utils.load_txt(file_name='tmp-run.out',
                           check_if_exists = True,
                           split = True)
        if r['return']>0: return r

        s = r['list']

        state['os_uname_machine'] = s[0]
        state['os_uname_all'] = s[1]

        env['CM_HOST_OS_MACHINE'] = state['os_uname_machine']

    return {'return':0}
