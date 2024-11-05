from cmind import utils
import cmind as cm
import os
from os.path import exists
import shutil

def clean_dir(dir_name):
    for item in os.listdir(dir_name):
        item_path = os.path.join(dir_name, item)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)
        else:
            os.remove(item_path)

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    submission_dir = env.get("CM_MLPERF_INFERENCE_SUBMISSION_DIR", "")

    if submission_dir == "":
        print("Please set CM_MLPERF_INFERENCE_SUBMISSION_DIR")
        return {'return': 1, 'error':'CM_MLPERF_INFERENCE_SUBMISSION_DIR is not specified'}

    submitter = env.get("CM_MLPERF_SUBMITTER", "cTuning")
    submission_processed = submission_dir + "_processed"

    if os.path.exists(submission_processed):
        clean_dir(submission_processed)

    os.system("rm -rf " + submission_dir + "_processed")

    CMD = env['CM_PYTHON_BIN'] + " '" + os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], "tools", "submission",
            "preprocess_submission.py") + "' --input '" + submission_dir + "' --submitter '" + submitter + "' --output '" + submission_processed + "'"
    env['CM_RUN_CMD'] = CMD

    return {'return':0}

def postprocess(i):

    env = i['env']
    submission_dir = env["CM_MLPERF_INFERENCE_SUBMISSION_DIR"]
    import datetime
    submission_backup = submission_dir+"_backup_"+'{date:%Y-%m-%d_%H:%M:%S}'.format( date=datetime.datetime.now() )

    submission_processed = submission_dir + "_processed"
    shutil.copytree(submission_dir, submission_backup)

    clean_dir(submission_dir)
            
    # copy the files from submission processed directory to submission directory
    for item in os.listdir(submission_processed):
        source = os.path.join(submission_processed, item)
        destination = os.path.join(submission_dir, item)
        if os.path.isdir(source):
            shutil.copytree(source, destination)  # Copy entire directory
        else:
            shutil.copy(source, destination)     # Copy individual files
            
    return {'return':0}
