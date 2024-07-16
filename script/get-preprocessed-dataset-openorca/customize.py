from cmind import utils
import os
import shutil

def preprocess(i):

    env = i['env']

    if str(env.get('CM_DATASET_PREPROCESSED_BY_MLC','')).lower() in [ "yes", "1", "true" ]:
        run_dir = os.getcwd()
        env['CM_DATASET_PREPROCESSED_PATH'] = os.path.join(env['CM_OPENORCA_PREPROCESSED_ROOT'], "open_orca_gpt4_tokenized_llama.sampled_24576.pkl.gz")
        #run_cmd = f"gunzip -k {env['CM_DATASET_PREPROCESSED_PATH']}"
        run_cmd = ''
    else:
        inference_src = env['CM_MLPERF_INFERENCE_SOURCE']
        run_dir = os.path.join(inference_src, 'language', 'llama2-70b')
        model_dir = env['CM_ML_MODEL_PATH']
        run_cmd = env['CM_PYTHON_BIN_WITH_PATH'] + ' processorca.py --dataset_pq_path=' + env['CM_DATASET_OPENORCA_PARQUET'] + ' --model_dir=' + model_dir +' --seqlen_limit=2048 --export_dir=' + os.path.join(os.getcwd(), "processed-openorca") + ' --num_total_samples=' + env['CM_DATASET_SIZE']

    env['CM_RUN_DIR'] = run_dir
    env['CM_RUN_CMD'] = run_cmd

    return {'return': 0}

def postprocess(i):
    env = i['env']
    if str(env.get('CM_DATASET_PREPROCESSED_BY_MLC','')).lower() in [ "yes", "1", "true", "on" ]:
        pass #set in preprocess
    else:
        env['CM_DATASET_PREPROCESSED_PATH'] = os.path.join(os.path.join(os.getcwd(), "processed-openorca", 'open_orca_gpt4_tokenized_llama.sampled_'+env['CM_DATASET_SIZE']+'.pkl'))

    env['CM_GET_DEPENDENT_CACHED_PATH'] = env['CM_DATASET_PREPROCESSED_PATH']

    return {'return': 0}
