#
# Copyright: https://github.com/mlcommons/ck/blob/master/cm-mlops/COPYRIGHT.md
# License: https://github.com/mlcommons/ck/blob/master/cm-mlops/LICENSE.md
#
# White paper: https://arxiv.org/abs/2406.16791
# History: https://github.com/mlcommons/ck/blob/master/HISTORY.CM.md
# Original repository: https://github.com/mlcommons/ck/tree/master/cm-mlops
#
# CK and CM project contributors: https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md
#

from cmind import utils
import os
import shutil


def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return': 1, 'error': 'Windows is not supported in this script yet'}
    env = i['env']

    if '+LIBRARY_PATH' not in env:
        env['+LIBRARY_PATH'] = []

    if 'CM_TENSORRT_INSTALL_PATH' in env:
        env['+LIBRARY_PATH'].append(os.path.join(
            env['CM_TENSORRT_INSTALL_PATH'], "lib"))

    cxxflags = [
        "-Wno-error=switch",
        "-DDALI_1_15=1",
        "-Wno-error=maybe-uninitialized"]

    if env.get('CM_GCC_VERSION', '') != '':
        gcc_major_version = env['CM_GCC_VERSION'].split(".")[0]
        if int(gcc_major_version) > 10:
            if env.get('CM_MLPERF_INFERENCE_VERSION', '') != "4.1":
                cxxflags.append("-Wno-error=range-loop-construct")

    if env.get('CM_MLPERF_DEVICE', '') == "inferentia":
        env['USE_INFERENTIA'] = "1"
        env['USE_NIGHTLY'] = "0"
        env['CM_MAKE_BUILD_COMMAND'] = "build"

    if '+ CXXFLAGS' not in env:
        env['+ CXXFLAGS'] = []

    env['+ CXXFLAGS'] += cxxflags
    return {'return': 0}


def postprocess(i):

    env = i['env']

    return {'return': 0}
