from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    automation = i['automation']
    version = env.get('CM_VERSION')
    if version not in env.get('CM_CUDA_LINUX_FILENAME', ''):
        return {'return': 1, 'error': "Only CUDA versions 11.7.0, 11.8.0, 12.0.0 and 12.2.0 are supported now!"}

    recursion_spaces = i['recursion_spaces']
    nvcc_bin = "nvcc"

    env['WGET_URL']="https://developer.download.nvidia.com/compute/cuda/"+env['CM_VERSION']+"/local_installers/"+env['CM_CUDA_LINUX_FILENAME']

    if env.get('CM_CUDA_INSTALL_DRIVER','') == "yes":
        env['CUDA_ADDITIONAL_INSTALL_OPTIONS'] = " --driver"
    else:
        env['CUDA_ADDITIONAL_INSTALL_OPTIONS'] = ""

    env['CM_CUDA_INSTALLED_PATH'] = os.path.join(os.getcwd(), 'install')
    env['CM_NVCC_BIN_WITH_PATH'] = os.path.join(os.getcwd(), 'install', 'bin', nvcc_bin)
    env['CM_GET_DEPENDENT_CACHED_PATH'] =  env['CM_NVCC_BIN_WITH_PATH']

    return {'return':0}
