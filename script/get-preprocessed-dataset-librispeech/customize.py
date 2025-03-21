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

    env = i['env']

    print("Using MLCommons Inference source from '" +
          env['CM_MLPERF_INFERENCE_SOURCE'] + "'")
    preprocess_src = os.path.join(
        env['CM_MLPERF_INFERENCE_RNNT_PATH'],
        'pytorch',
        'utils',
        'convert_librispeech.py')
    cmd = 'cd ' + env['CM_MLPERF_INFERENCE_3DUNET_PATH'] + ' && ${CM_PYTHON_BIN_WITH_PATH} ' + preprocess_src + ' --input_dir ' + env['CM_DATASET_LIBRISPEECH_PATH'] + \
        ' --dest_dir ' + os.path.join(os.getcwd(), 'dev-clean-wav') + \
        ' --output_json ' + os.path.join(os.getcwd(), 'dev-clean-wav.json')
    env['CM_TMP_CMD'] = cmd

    return {'return': 0}


def postprocess(i):
    env = i['env']
    env['CM_DATASET_PREPROCESSED_PATH'] = os.path.join(
        os.getcwd(), 'dev-clean-wav')
    env['CM_DATASET_PREPROCESSED_JSON'] = os.path.join(
        os.getcwd(), 'dev-clean-wav.json')

    return {'return': 0}
