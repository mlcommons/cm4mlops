from cmind import utils
import os, subprocess

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    cmd_args = ""

    model_name = env.get("CM_VLLM_SERVER_MODEL_NAME", False)
    if not model_name:
        return {'return': 1, 'error': 'Model name not specified'}
    else:
        cmd_args += f" --model {env['CM_ML_MODEL_PATH']} --served-model-name {model_name}"

    tp_size = env.get("CM_VLLM_SERVER_TP_SIZE", False)
    if tp_size:
        cmd_args += f" --tensor-parallel-size {tp_size}"

    pp_size = env.get("CM_VLLM_SERVER_PP_SIZE", False)
    if pp_size:
        cmd_args += f" --pipeline-parallel-size {pp_size}"

    api_key = env.get("CM_VLLM_SERVER_API_KEY", "root")
    if pp_size:
        cmd_args += f" --api-key {api_key}"

    distributed_executor_backend = env.get("CM_VLLM_SERVER_DIST_EXEC_BACKEND", False)
    if distributed_executor_backend:
        cmd_args += f" --distributed-executor-backend {distributed_executor_backend}"

    cmd = f"{env['CM_PYTHON_BIN_WITH_PATH']} -m vllm.entrypoints.openai.api_server {cmd_args}"
    print(cmd)
    
    env['CM_VLLM_RUN_CMD'] = cmd

    return {'return':0}

def postprocess(i):

    env = i['env']

    return {'return':0}
