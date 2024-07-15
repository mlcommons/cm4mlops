from cmind import utils
import os
import shutil

def preprocess(i):

    env = i['env']

    if env.get("CM_MLPERF_IMPLEMENTATION", "") == "redhat":
        auth_s3_bucket = "rclone config create mlc-inference s3 provider=Cloudflare access_key_id=f65ba5eef400db161ea49967de89f47b secret_access_key=fbea333914c292b854f14d3fe232bad6c5407bf0ab1bebf78833c2b359bdfd2b endpoint=https://c2686074cb2caf5cbaf6d134bdba8b47.r2.cloudflarestorage.com"
        download_cmd = "rclone copy mlc-inference:mlcommons-inference-wg-public/open_orca . -P"
        run_cmd = f"{auth_s3_bucket} && {download_cmd}"

        print(run_cmd)
        env['CM_RUN_CMD'] = run_cmd

    return {'return': 0}

def postprocess(i):
    env = i['env']
    if env.get('CM_DATASET_CALIBRATION','') == "no":
        if env.get("CM_MLPERF_IMPLEMENTATION", "") != "redhat":
            env['CM_DATASET_PATH_ROOT'] = env['CM_DATASET_OPENORCA_PATH']
            env['CM_DATASET_PATH'] = env['CM_DATASET_OPENORCA_PATH']
            env['CM_DATASET_OPENORCA_PARQUET'] = os.path.join(env['CM_DATASET_OPENORCA_PATH'], '1M-GPT4-Augmented.parquet')
    else:
        env['CM_CALIBRATION_DATASET_PATH'] = os.path.join(os.getcwd(), 'install', 'calibration', 'data')

    return {'return': 0}
