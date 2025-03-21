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


def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    return {'return': 0}


def postprocess(i):

    env = i['env']

    env['CM_AOCL_SRC_PATH'] = env['CM_GIT_REPO_CHECKOUT_PATH']
    env['CM_AOCL_BUILD_PATH'] = os.path.join(
        env['CM_GIT_REPO_CHECKOUT_PATH'], "build")
    aocl_lib_path = os.path.join(
        env['CM_GIT_REPO_CHECKOUT_PATH'],
        "build",
        "aocl-release",
        "src")
    env['CM_AOCL_LIB_PATH'] = aocl_lib_path
    env['+LIBRARY_PATH'] = [aocl_lib_path] if '+LIBRARY_PATH' not in env else env['+LIBRARY_PATH'] + [aocl_lib_path]
    env['+LD_LIBRARY_PATH'] = [aocl_lib_path] if '+LD_LIBRARY_PATH' not in env else env['+LD_LIBRARY_PATH'] + [aocl_lib_path]

    return {'return': 0}
