from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']
    env = i['env']

    if env.get('CM_TMP_ML_MODEL_PROVIDER', '') == 'nvidia':
        i['run_script_input']['script_name'] = 'run-nvidia'
        gpu_arch = int(float(env['CM_CUDA_DEVICE_PROP_GPU_COMPUTE_CAPABILITY']) * 10)
        env['CM_GPU_ARCH'] = gpu_arch
        env['CM_TMP_REQUIRE_DOWNLOAD'] = 'no'
    else:
        path = env.get('LLAMA2_CHECKPOINT_PATH', '').strip()

        if path == '' or not os.path.exists(path):
            env['CM_TMP_REQUIRE_DOWNLOAD'] = 'yes'

        return {'return':0}

def postprocess(i):

    env = i['env']
    if env.get('LLAMA2_CHECKPOINT_PATH', '' ) ==  '':
        env['LLAMA2_CHECKPOINT_PATH'] = env['CM_ML_MODEL_PATH']

    env['CM_ML_MODEL_PATH'] = env['LLAMA2_CHECKPOINT_PATH']
    env['CM_ML_MODEL_LLAMA2_FILE_WITH_PATH'] = env['LLAMA2_CHECKPOINT_PATH']
    env['CM_GET_DEPENDENT_CACHED_PATH'] = env['CM_ML_MODEL_PATH']

    return {'return':0}
