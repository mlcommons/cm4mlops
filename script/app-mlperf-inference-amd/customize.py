from cmind import utils
import os
import shutil

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}
    env = i['env']

    if env.get('CM_MLPERF_SKIP_RUN', '') == "yes":
        return {'return':0}

    if 'CM_MODEL' not in env:
        return {'return': 1, 'error': 'Please select a variation specifying the model to run'}
    if 'CM_MLPERF_BACKEND' not in env:
        return {'return': 1, 'error': 'Please select a variation specifying the backend'}
    if 'CM_MLPERF_DEVICE' not in env:
        return {'return': 1, 'error': 'Please select a variation specifying the device to run on'}

    r = get_run_cmd(env['CM_MODEL'], i)
    if r['return'] > 0:
        return r
    run_cmd = r['run_cmd']
    run_dir = r ['run_dir']
    print(run_cmd)
    print(run_dir)
    env['CM_MLPERF_RUN_CMD'] = run_cmd
    env['CM_RUN_DIR'] = run_dir
    env['CM_RUN_CMD'] = run_cmd

    return {'return':0}
    #return {'return':1, 'error': 'Run command needs to be tested'}

def get_run_cmd(model, i):
    env = i['env']
    
    if "llama2" in model:
        scenario = env['CM_MLPERF_LOADGEN_SCENARIO']
        device = env['CM_MLPERF_DEVICE']
        mode = env['CM_MLPERF_LOADGEN_MODE']
        outdir = env['CM_MLPERF_OUTPUT_DIR']
        mlperf_conf_path = env['CM_MLPERF_CONF']
        user_conf_path = env['CM_MLPERF_USER_CONF']
        api_server = env.get('CM_MLPERF_INFERENCE_API_SERVER', 'localhost:8000/v1')
        api_model_name = env['CM_VLLM_SERVER_MODEL_NAME']
        dataset_path = env['CM_DATASET_OPENORCA_PATH']
        precision = env['CM_MLPERF_MODEL_PRECISION']
        if mode == "accuracy":
            accuracy_string = " --accuracy "
        else:
            accuracy_string = ""

        run_cmd = f"python3 -u  'main.py' --scenario {scenario} --model-path {api_model_name} --api-model-name {api_model_name} --api-server {api_server} --mlperf-conf {mlperf_conf_path} {accuracy_string} --vllm --user-conf {user_conf_path} --dataset-path {dataset_path} --output-log-dir {outdir} --dtype float32 --device {device} "
        submitter = "RedHat-Supermicro"
        run_dir = os.path.join(env['CM_MLPERF_INFERENCE_IMPLEMENTATION_REPO'], "open", submitter, "code", model)

        return {'return': 0, 'run_cmd': run_cmd, 'run_dir': run_dir}

def postprocess(i):

    env = i['env']

    return {'return':0}