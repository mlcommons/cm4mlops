from cmind import utils
import os
import json
import shutil
import subprocess
import cmind as cm
import copy
from tabulate import tabulate
import mlperf_utils

summary_ext = ['.csv', '.json', '.xlsx']

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    inp = i['input']
    state = i['state']
    script_path = i['run_script_input']['path']

    if env.get('CM_RUN_DOCKER_CONTAINER', '') == "yes": 
        return {'return':0}

    dump_version_info = env.get('CM_DUMP_VERSION_INFO', True)
    system_meta = state['CM_SUT_META']
    env['CM_SUT_META_EXISTS'] = "yes"

    env['CM_MODEL'] = env['CM_MLPERF_MODEL']

    # Clean MLPerf inference output tar file if non-standard
    x=env.get('MLPERF_INFERENCE_SUBMISSION_TAR_FILE','')
    if x!='' and os.path.isfile(x):
        os.remove(x)

    # Clean MLPerf inference submission summary files
    x=env.get('MLPERF_INFERENCE_SUBMISSION_SUMMARY','')
    if x!='':
        for y in summary_ext:
            z = x+y
            if os.path.isfile(z):
                os.remove(z)

    if env.get('CM_MLPERF_SUBMISSION_SYSTEM_TYPE', '') != '':
        system_type = env['CM_MLPERF_SUBMISSION_SYSTEM_TYPE']
        system_meta['system_type'] = system_type

    if env.get('CM_MLPERF_SUBMISSION_DIVISION', '') != '':
        division = env['CM_MLPERF_SUBMISSION_DIVISION']
        system_meta['division'] = division

    if system_meta.get('division', '') != "closed":
        env["CM_MLPERF_LOADGEN_COMPLIANCE"] = "no" #no compliance runs needed for open division

    clean = False

    if 'CM_MLPERF_CLEAN_ALL' in env:
        clean = True
        if 'CM_MLPERF_CLEAN_SUBMISSION_DIR' not in env:
            env['CM_MLPERF_CLEAN_SUBMISSION_DIR'] = "yes"
        if 'CM_RERUN' not in env:
            env['CM_RERUN'] = "yes"

    if str(env.get('CM_SYSTEM_POWER','no')).lower() != "no" or env.get('CM_MLPERF_POWER', '') == "yes":
        power_variation = ",_power"
        env['CM_MLPERF_POWER'] = "yes"
    else:
        power_variation = ""

    if env.get('CM_RUN_STYLE', '') == "valid" and 'CM_RUN_MLPERF_ACCURACY' not in env:
        env['CM_RUN_MLPERF_ACCURACY'] = "on"

    print("Using MLCommons Inference source from " + env['CM_MLPERF_INFERENCE_SOURCE'])


    if 'CM_MLPERF_LOADGEN_EXTRA_OPTIONS' not in env:
        env['CM_MLPERF_LOADGEN_EXTRA_OPTIONS'] = ""

    if 'CM_MLPERF_LOADGEN_MODES' not in env:
        if 'CM_MLPERF_LOADGEN_MODE' not in env:
            env['CM_MLPERF_LOADGEN_MODE'] = "performance"

    if 'CM_MLPERF_LOADGEN_SCENARIOS' not in env:
        if 'CM_MLPERF_LOADGEN_SCENARIO' not in env:
            env['CM_MLPERF_LOADGEN_SCENARIO'] = "Offline"

    if env.get('CM_MLPERF_LOADGEN_ALL_SCENARIOS', '') == "yes":
        env['CM_MLPERF_LOADGEN_SCENARIOS'] = get_valid_scenarios(env['CM_MODEL'], system_meta['system_type'], env['CM_MLPERF_LAST_RELEASE'], env['CM_MLPERF_INFERENCE_SOURCE'])
    else:
        system_meta = {}
        env['CM_MLPERF_LOADGEN_SCENARIOS'] = [ env['CM_MLPERF_LOADGEN_SCENARIO'] ]

    if env.get('CM_MLPERF_LOADGEN_ALL_MODES', '') == "yes":
        env['CM_MLPERF_LOADGEN_MODES'] = [ "performance", "accuracy" ]
    else:
        env['CM_MLPERF_LOADGEN_MODES'] = [ env['CM_MLPERF_LOADGEN_MODE'] ]

    if env.get('OUTPUT_BASE_DIR', '') == '':
        env['OUTPUT_BASE_DIR'] = env.get('CM_MLPERF_INFERENCE_RESULTS_DIR', os.getcwd())

    test_list = ["TEST01",  "TEST05"]
    if env['CM_MODEL']  in ["resnet50"]:
        test_list.append("TEST04")
    if "gpt" in env['CM_MODEL'] or "sdxl" in env['CM_MODEL'] or "llama2-70b" in env['CM_MODEL']:
        test_list.remove("TEST01")
        test_list.remove("TEST05")

    variation_implementation= "_" + env.get("CM_MLPERF_IMPLEMENTATION", "reference")
    variation_model= ",_" + env["CM_MLPERF_MODEL"]
    variation_backend= ",_" + env["CM_MLPERF_BACKEND"] if env.get("CM_MLPERF_BACKEND","") != "" else ""
    variation_device= ",_" + env["CM_MLPERF_DEVICE"] if env.get("CM_MLPERF_DEVICE","") != "" else ""
    variation_run_style= ",_" + env.get("CM_MLPERF_EXECUTION_MODE", "test")
    variation_reproducibility= ",_" + env["CM_RUN_MLPERF_INFERENCE_APP_DEFAULTS"]

    if env.get("CM_MLPERF_MODEL_PRECISION", '') != '':
        variation_quantization_string= ",_" + env["CM_MLPERF_MODEL_PRECISION"]
    else:
        variation_quantization_string = ""

    tags =  "app,mlperf,inference,generic,"+variation_implementation+variation_model+variation_backend+variation_device+variation_run_style+variation_reproducibility+variation_quantization_string+power_variation
    verbose = inp.get('v', False)
    print_env = inp.get('print_env', False)
    print_deps = inp.get('print_deps', False)
    add_deps_recursive = inp.get('add_deps_recursive', {})
    add_deps = inp.get('add_deps', {})
    ad = inp.get('ad', {})
    adr = inp.get('adr', {})
    adr_from_meta = i['run_script_input'].get('add_deps_recursive')

    for key in adr_from_meta:
        add_deps_recursive[key] = adr_from_meta[key]

    if clean and 'OUTPUT_BASE_DIR' in env:
        path_to_clean = os.path.join(env['OUTPUT_BASE_DIR'], env['CM_OUTPUT_FOLDER_NAME'])

        print ('=========================================================')
        print ('Cleaning results in {}'.format(path_to_clean))
        if os.path.exists(path_to_clean):
            shutil.rmtree(path_to_clean)

        print ('=========================================================')

    local_keys = [ 'CM_MLPERF_SKIP_RUN', 'CM_MLPERF_LOADGEN_QUERY_COUNT' ]

    for scenario in env['CM_MLPERF_LOADGEN_SCENARIOS']:
        scenario_tags = tags + ",_"+scenario.lower()
        env['CM_MLPERF_LOADGEN_SCENARIO'] = scenario

        if scenario == "Offline":
            if env.get('CM_MLPERF_LOADGEN_OFFLINE_TARGET_QPS'):
                env['CM_MLPERF_LOADGEN_TARGET_QPS'] = env['CM_MLPERF_LOADGEN_OFFLINE_TARGET_QPS']
        elif scenario == "Server":
            if env.get('CM_MLPERF_LOADGEN_SERVER_TARGET_QPS'):
                env['CM_MLPERF_LOADGEN_TARGET_QPS'] = env['CM_MLPERF_LOADGEN_SERVER_TARGET_QPS']
        elif scenario == "SingleStream":
            if env.get('CM_MLPERF_LOADGEN_SINGLESTREAM_TARGET_LATENCY'):
                env['CM_MLPERF_LOADGEN_TARGET_LATENCY'] = env['CM_MLPERF_LOADGEN_SINGLESTREAM_TARGET_LATENCY']
        elif scenario == "MultiStream":
            if env.get('CM_MLPERF_LOADGEN_MULTISTREAM_TARGET_LATENCY'):
                env['CM_MLPERF_LOADGEN_TARGET_LATENCY'] = env['CM_MLPERF_LOADGEN_MULTISTREAM_TARGET_LATENCY']

        for mode in env['CM_MLPERF_LOADGEN_MODES']:
            env['CM_MLPERF_LOADGEN_MODE'] = mode

            print(f"\nRunning loadgen scenario: {scenario} and mode: {mode}")
            ii = {'action':'run', 'automation':'script', 'tags': scenario_tags, 'quiet': 'true',
                'env': env, 'input': inp, 'state': state, 'add_deps': add_deps, 'add_deps_recursive':
                copy.deepcopy(add_deps_recursive), 'ad': ad, 'adr': copy.deepcopy(adr), 'v': verbose, 'print_env': print_env, 'print_deps': print_deps, 'dump_version_info': dump_version_info}
            r = cm.access(ii)
            if r['return'] > 0:
                return r
            if env.get('CM_MLPERF_SKIP_RUN', '') != '':
                del(env['CM_MLPERF_SKIP_RUN'])

            for key in local_keys:
                if env.get(key, '') != '':
                    del(env[key])

        if env.get("CM_MLPERF_LOADGEN_COMPLIANCE", "") == "yes":
            for test in test_list:
                env['CM_MLPERF_LOADGEN_COMPLIANCE_TEST'] = test
                env['CM_MLPERF_LOADGEN_MODE'] = "compliance"
                r = cm.access({'action':'run', 'automation':'script', 'tags': scenario_tags, 'quiet': 'true',
                    'env': env, 'input': inp, 'state': state, 'add_deps': add_deps, 'add_deps_recursive':
                    copy.deepcopy(add_deps_recursive), 'adr': copy.deepcopy(adr), 'ad': ad, 'v': verbose, 'print_env': print_env, 'print_deps': print_deps, 'dump_version_info': dump_version_info})
                if r['return'] > 0:
                    return r

                for key in local_keys:
                    if env.get(key, '') != '':
                        del(env[key])

    if state.get("CM_MLPERF_RESULTS"):
        #print(state["CM_MLPERF_RESULTS"])
        for sut in state["CM_MLPERF_RESULTS"]:#only one sut will be there
            result_table, headers = mlperf_utils.get_result_table(state["CM_MLPERF_RESULTS"][sut])
            print(tabulate(result_table, headers = headers, tablefmt="pretty"))

    return {'return':0}


def get_valid_scenarios(model, category, mlperf_version, mlperf_path):

    import sys
    
    submission_checker_dir = os.path.join(mlperf_path, "tools", "submission")

    sys.path.append(submission_checker_dir)
    if not os.path.exists(os.path.join(submission_checker_dir, "submission_checker.py")):
        shutil.copy(os.path.join(submission_checker_dir,"submission-checker.py"), os.path.join(submission_checker_dir,
        "submission_checker.py"))

    import submission_checker as checker

    if "dlrm-99" in model:
      model = model.replace("dlrm-99", "dlrm-v2-99")
    if "sdxl" in model:
      model = "stable-diffusion-xl"

    config = checker.MODEL_CONFIG

    internal_model_name = config[mlperf_version]["model_mapping"].get(model, model)

    valid_scenarios = config[mlperf_version]["required-scenarios-"+category][internal_model_name]

    print("Valid Scenarios for " + model + " in " + category + " category are :" +  str(valid_scenarios))

    return valid_scenarios

def postprocess(i):

    return {'return':0}
