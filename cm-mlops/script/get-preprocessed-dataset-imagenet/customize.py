from cmind import utils
import os
from os.path import exists
import shutil
import glob

def preprocess(i):

    env = i['env']
    if 'CM_IMAGENET_PREPROCESSED_PATH' in env:
        files = glob.glob(env['CM_IMAGENET_PREPROCESSED_PATH']+"/**/"+env['CM_IMAGENET_PREPROCESSED_FILENAME'], recursive = True)
        if files:
            env['CM_DATASET_PREPROCESSED_PATH'] = env['CM_IMAGENET_PREPROCESSED_PATH']
        else:
            return {'return': 1, 'error': 'No preprocessed images found in '+env['CM_IMAGENET_PREPROCESSED_PATH']}
    else:
        if env.get('CM_DATASET_REFERENCE_PREPROCESSOR',"0") == "1":
            print("Using MLCommons Inference source from '" + env['CM_MLPERF_INFERENCE_SOURCE'] +"'")

        env['CM_DATASET_PREPROCESSED_PATH'] = os.getcwd()
        if not exists(os.path.join(env['CM_DATASET_PATH'], "val_map.txt")):
            shutil.copy(os.path.join(env['CM_DATASET_AUX_PATH'], "val.txt"), os.path.join(env['CM_DATASET_PATH'],
            "val_map.txt"))

    preprocessed_path = env['CM_DATASET_PREPROCESSED_PATH']
    
    if env.get('CM_DATASET_TYPE', '') == "validation" and not exists(os.path.join(preprocessed_path, "val_map.txt")):
        shutil.copy(os.path.join(env['CM_DATASET_AUX_PATH'], "val.txt"), 
                    os.path.join(preprocessed_path, "val_map.txt"))

    if env.get('CM_DATASET_TYPE', '') == "calibration":
        env['CM_DATASET_IMAGES_LIST'] = env['CM_MLPERF_IMAGENET_CALIBRATION_LIST_FILE_WITH_PATH']
        env['CM_DATASET_SIZE'] = 500

    return {'return': 0}

def postprocess(i):

    env = i['env']

    # finalize path
    preprocessed_path = env['CM_DATASET_PREPROCESSED_PATH']
    preprocessed_images_list = []

    match_text = "/*."+env.get("CM_DATASET_PREPROCESSED_EXTENSION","*")
    for filename in sorted(glob.glob(preprocessed_path + match_text)):
        preprocessed_images_list.append(filename)
    with open("preprocessed_files.txt", "w") as f:
        f.write("\n".join(preprocessed_images_list))

    env['CM_DATASET_PREPROCESSED_IMAGES_LIST'] = os.path.join(os.getcwd(), "preprocessed_files.txt")

    return {'return':0}
