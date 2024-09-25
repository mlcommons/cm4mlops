from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    if str(env.get('CUDA_SKIP_SUDO','')).lower() == 'true':
        env['CM_SUDO'] = ''

    meta = i['meta']
    automation = i['automation']
    version = env.get('CM_VERSION')

    if version not in env.get('CM_CUDA_LINUX_FILENAME', ''):
        supported_versions = list(meta['versions'].keys())
        return {'return': 1, 'error': "Only CUDA versions {} are supported now".format(', '.join(supported_versions))}

    install_prefix = env.get('CM_CUDA_INSTALL_PREFIX', os.getcwd())

    env['CM_CUDA_INSTALL_PREFIX'] = install_prefix

    recursion_spaces = i['recursion_spaces']
    nvcc_bin = "nvcc"

    env['WGET_URL']="https://developer.download.nvidia.com/compute/cuda/"+env['CM_VERSION']+"/local_installers/"+env['CM_CUDA_LINUX_FILENAME']

    extra_options = env.get('CUDA_ADDITIONAL_INSTALL_OPTIONS', '')
    if env.get('CM_CUDA_INSTALL_DRIVER','') == "yes":
        extra_options += " --driver"
    env['CUDA_ADDITIONAL_INSTALL_OPTIONS'] = extra_options

    env['CM_CUDA_INSTALLED_PATH'] = os.path.join(install_prefix, 'install')
    env['CM_NVCC_BIN_WITH_PATH'] = os.path.join(install_prefix, 'install', 'bin', nvcc_bin)
    env['CM_GET_DEPENDENT_CACHED_PATH'] =  env['CM_NVCC_BIN_WITH_PATH']

    # Set CUDA_RUN_FILE_LOCAL_PATH to empty if not set for backwards compatibility in download file
    env['CUDA_RUN_FILE_LOCAL_PATH'] = env.get('CUDA_RUN_FILE_LOCAL_PATH','')

    return {'return':0}
