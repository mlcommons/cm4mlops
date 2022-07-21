from cmind import utils
import os

def preprocess(i):
    os_info = i['os_info']
    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    env = i['env']
    
    CPPFLAGS = env.get('+ CPPFLAGS', [])
    env['CM_C_COMPILER_FLAGS'] = " ".join(env.get('+ CFLAGS', []) + CPPFLAGS)
    env['CM_CXX_COMPILER_FLAGS'] = " ".join(env.get('+ CXXFLAGS', []) + CPPFLAGS)
    env['CM_F_COMPILER_FLAGS'] = " ".join(env.get('+ FFLAGS', []))

    CPATH = env.get('+CPATH', [])
    env['CM_C_INCLUDE_FLAGS'] = " -I".join(env.get('+C_INCLUDE_DIR', []) + CPATH)
    env['CM_CXX_INCLUDE_FLAGS'] = " -I".join(env.get('+CXX_INCLUDE_DIR', []) + CPATH)
    env['CM_F_INCLUDE_FLAGS'] = " -I".join(env.get('+F_INCLUDE_DIR', []) + CPATH)
    
    LDFLAGS = env.get('+ LDFLAGS', [])
    env['CM_C_LINKER_FLAGS'] = " ".join(env.get('+ LDCFLAGS', []) + LDFLAGS)
    env['CM_CXX_LINKER_FLAGS'] = " ".join(env.get('+ LDCXXFLAGS', []) + LDFLAGS)
    env['CM_F_LINKER_FLAGS'] = " ".join(env.get('+ LDFFLAGS', []) + LDFLAGS)
    env['CM_LD_LIBRARY_PATHS'] = " -L".join(env.get('+LD_LIBRARY_PATH', []))
    env['CM_SOURCE_FOLDER_PATH'] = env['CM_SOURCE_FOLDER_PATH'] if 'CM_SOURCE_FOLDER_PATH' in env else env['CM_TMP_CURRENT_SCRIPT_PATH'] if 'CM_TMP_CURRENT_SCRIPT_PATH' in env else ''

    return {'return':0}

def postprocess(i):

    return {'return':0}
