from cmind import utils
import os
import json
import shutil
import cmind
import sys
from tabulate import tabulate
import mlperf_utils

def preprocess(i):
    return {'return': 0}

# Helper function to fill dictionary from JSON file
def fill_from_json(file_path, keys, sut_info):
    with open(file_path, 'r') as f:
        data = json.load(f)
        for key in keys:
            if key in data and sut_info[key] is None:
                sut_info[key] = data[key]
            elif key in data and sut_info[key] != data[key]:
                return -1 # error saying there is a mismatch in the value of a key
        return sut_info
    
# Helper function to check whether all the keys(sut information) are assigned
def check_dict_filled(keys, sut_info):
    for key in keys:
        if key in sut_info and sut_info[key] is None:
            return False
    return True

def generate_submission(i):

    # Save current user directory
    cur_dir=os.getcwd()
    env = i['env']
    state = i['state']
    inp=i['input']

    if env.get('CM_MLPERF_INFERENCE_RESULTS_DIR_', '') == '':
        results_dir = os.path.join(env['CM_MLPERF_INFERENCE_RESULTS_DIR'], f"{env['CM_MLPERF_RUN_STYLE']}_results")
    else:
        results_dir = env['CM_MLPERF_INFERENCE_RESULTS_DIR_']

    mlperf_path = env['CM_MLPERF_INFERENCE_SOURCE']
    submission_checker_dir = os.path.join(mlperf_path, "tools", "submission")
    sys.path.append(submission_checker_dir)

    if env.get('CM_MLPERF_INFERENCE_SUBMISSION_DIR', '') == '':
        from pathlib import Path
        user_home = str(Path.home())
        env['CM_MLPERF_INFERENCE_SUBMISSION_DIR'] = os.path.join(user_home, "mlperf_submission")

    submission_dir = env.get('CM_MLPERF_INFERENCE_SUBMISSION_DIR', '')

    if env.get('CM_MLPERF_CLEAN_SUBMISSION_DIR','')!='':
        print ('=================================================')
        print ('Cleaning {} ...'.format(env['CM_MLPERF_INFERENCE_SUBMISSION_DIR']))
        if os.path.exists(env['CM_MLPERF_INFERENCE_SUBMISSION_DIR']):
            shutil.rmtree(env['CM_MLPERF_INFERENCE_SUBMISSION_DIR'])
        print ('=================================================')

    if not os.path.isdir(submission_dir):
        os.makedirs(submission_dir)

    print('* MLPerf inference submission dir: {}'.format(submission_dir))
    print('* MLPerf inference results dir: {}'.format(results_dir))
    results = [f for f in os.listdir(results_dir) if not os.path.isfile(os.path.join(results_dir, f))]

    system_meta_default = state['CM_SUT_META']
    system_meta = {}
    if 'CM_MLPERF_SUBMISSION_SYSTEM_TYPE' in env:
        system_meta['system_type'] = env['CM_MLPERF_SUBMISSION_SYSTEM_TYPE']

    if 'CM_MLPERF_SUBMISSION_DIVISION' in env:
        system_meta['division'] = env['CM_MLPERF_SUBMISSION_DIVISION']

    if 'CM_MLPERF_SUBMISSION_CATEGORY' in env:
        system_meta['system_type'] = env['CM_MLPERF_SUBMISSION_CATEGORY'].replace("-", ",")

    duplicate= (env.get('CM_MLPERF_DUPLICATE_SCENARIO_RESULTS', 'no') in ["yes", "True"])

    if env.get('CM_MLPERF_SUBMISSION_DIVISION', '') != '':
        division = env['CM_MLPERF_SUBMISSION_DIVISION']
        system_meta['division'] = division
    else:
        division = system_meta_default['division']

    if division not in ['open','closed']:
        return {'return':1, 'error':'"division" must be "open" or "closed"'}

    print('* MLPerf inference division: {}'.format(division))

    path_submission_root = submission_dir
    path_submission_division=os.path.join(path_submission_root, division)
    if not os.path.isdir(path_submission_division):
        os.makedirs(path_submission_division)

    # Check submitter
    if env.get('CM_MLPERF_SUBMITTER'):
        submitter = env['CM_MLPERF_SUBMITTER']
        system_meta['submitter'] = submitter
    else:
        submitter = system_meta_default['submitter']
        env['CM_MLPERF_SUBMITTER'] = submitter

    print('* MLPerf inference submitter: {}'.format(submitter))

    if 'Collective' not in system_meta_default.get('sw_notes'):
        system_meta['sw_notes'] =  "Automated by MLCommons CM v{}. ".format(cmind.__version__) + system_meta_default['sw_notes']

    if env.get('CM_MLPERF_SUT_SW_NOTES_EXTRA','') != '':
        sw_notes = f"{system_meta['sw_notes']} {env['CM_MLPERF_SUT_SW_NOTES_EXTRA']}"
        system_meta['sw_notes'] = sw_notes

    if env.get('CM_MLPERF_SUT_HW_NOTES_EXTRA','') != '':
        hw_notes = f"{system_meta['hw_notes']} {env['CM_MLPERF_SUT_HW_NOTES_EXTRA']}"
        system_meta['hw_notes'] = hw_notes

    path_submission=os.path.join(path_submission_division, submitter)
    if not os.path.isdir(path_submission):
        os.makedirs(path_submission)

    # SUT base
    system=env.get('CM_HW_NAME','default').replace(' ','_')

    code_path = os.path.join(path_submission, "code")

    for res in results:
        result_path = os.path.join(results_dir, res)
        # variable to check whether the sut_meta.json is present in the root folder
        saved_system_meta_file_path = os.path.join(result_path, 'system_meta.json')
        # checks for json file containing system meta
        sut_info = {
            "hardware_name": None,
            "implementation": None,
            "device": None,
            "framework": None,
            "run_config": None
        } # variable to store the system meta 

        model_mapping_combined = {} # to store all the model mapping related to an SUT

        # check whether the root folder contains the sut infos
        # if yes then there is no need to check for meta files inside individual model folders
        if "cm-sut-info.json" in os.listdir(result_path):
            sut_info = fill_from_json(os.path.join(result_path, "cm-sut-info.json"), sut_info.keys(), sut_info)
            if sut_info == -1:
                return {'return':1, 'error':f"key value mismatch. Refer the populating dictionary:\n{sut_info}\n and file {os.path.join(result_path, 'cm-sut-info.json')}"}
            if check_dict_filled(sut_info.keys(), sut_info):
                print(f"sut info completely filled from {os.path.join(result_path, 'cm-sut-info.json')}!")

        # Check whether the root folder contains the model mapping file
        # expects json file in the format:
        # {
        #   custom_model1:official_model(could be any official model),
        #   custom_model2:official_model(could be any official model)
        # }
        if "model_mapping.json" in os.listdir(result_path):
            with open(os.path.join(result_path, "model_mapping.json"), 'r') as f:
                model_mapping_combined = json.load(f)

        # Preprocessing part.
        # Even the model mapping json file is present in root directory, the folders are traversed
        # and the data is updated provided not duplicated. 
        models = [f for f in os.listdir(result_path) if not os.path.isfile(os.path.join(result_path, f))]
        if division == "open":
            for model in models:
                result_model_path = os.path.join(result_path, model)
                scenarios = [f for f in os.listdir(result_model_path) if not os.path.isfile(os.path.join(result_model_path, f))]
                for scenario in scenarios:
                    result_scenario_path = os.path.join(result_model_path, scenario)
                    modes = [f for f in os.listdir(result_scenario_path) if not os.path.isfile(os.path.join(result_scenario_path, f))]
                    for mode in modes:
                        result_mode_path = os.path.join(result_scenario_path,mode)
                        if mode == "performance":
                            compliance_performance_run_path = os.path.join(result_mode_path, "run_1")
                            # model mapping part 
                            tmp_model_mapping_file_path = os.path.join(compliance_performance_run_path, "model_mapping.json")
                            if os.path.exists(tmp_model_mapping_file_path):
                                with open(tmp_model_mapping_file_path, 'r') as f:
                                    new_model_mapping = json.load(f)
                                    for new_custom_model in new_model_mapping:
                                        if new_custom_model not in model_mapping_combined:
                                            model_mapping_combined.update({new_custom_model:new_model_mapping[new_custom_model]})
                            else:
                                return {"return":1, "error":f"model_mapping.json not found in {compliance_performance_run_path}"}

        if check_dict_filled(sut_info.keys(), sut_info):              
            system = sut_info["hardware_name"]
            implementation = sut_info["implementation"]
            device = sut_info["device"]
            framework = sut_info["framework"].replace(" ","_")
            run_config = sut_info["run_config"]
            new_res = f"{system}-{implementation}-{device}-{framework}-{run_config}"
        else:
            parts = res.split("-")
            if len(parts) > 5: #result folder structure used by CM script
                system = parts[0] if system == 'default' else system
                implementation = parts[1]
                device = parts[2]
                framework = parts[3]
                framework_version = parts[4]
                run_config = parts[5]

                print('* System: {}'.format(system))
                print('* Implementation: {}'.format(implementation))
                print('* Device: {}'.format(device))
                print('* Framework: {}'.format(framework))
                print('* Framework Version: {}'.format(framework_version))
                print('* Run Config: {}'.format(run_config))

                new_res = system + "-" + "-".join(parts[1:])

                # Override framework and framework versions from the folder name
                system_meta_default['framework'] = framework + " " + framework_version
            else:
                print(parts)
                return {'return': 1, 'error': f"The required details for generating the inference submission:\n1.system_name\n2.implementation\n3.framework\n4.run_config\nInclude a cm-sut-info.json file with the above content in {result_path}"}
            
        platform_prefix = inp.get('platform_prefix', '')
        if platform_prefix:
            sub_res = platform_prefix + "-" + new_res
        else:
            sub_res = new_res

        submission_path = os.path.join(path_submission, "results", sub_res)
        measurement_path = os.path.join(path_submission, "measurements", sub_res)
        compliance_path = os.path.join(path_submission, "compliance", sub_res)
        system_path = os.path.join(path_submission, "systems")
        submission_system_path = system_path
        if not os.path.isdir(submission_system_path):
            os.makedirs(submission_system_path)
        system_file = os.path.join(submission_system_path, sub_res+".json")

        # Save the model mapping json file
        with open(os.path.join(path_submission,"model_mapping.json"), "w") as fp:
            json.dump(model_mapping_combined, fp, indent=2)

        models = [f for f in os.listdir(result_path) if not os.path.isfile(os.path.join(result_path, f))]

        results = {}

        model_platform_info_file = None

        for model in models:
            results[model] = {}
            platform_info_file = None
            result_model_path = os.path.join(result_path, model)
            submission_model_path = os.path.join(submission_path, model)
            measurement_model_path = os.path.join(measurement_path, model)
            compliance_model_path = os.path.join(compliance_path, model)
            code_model_path = os.path.join(code_path, model)
            scenarios = [f for f in os.listdir(result_model_path) if not os.path.isfile(os.path.join(result_model_path, f))]
            submission_code_path = code_model_path
            if not os.path.isdir(submission_code_path):
                os.makedirs(submission_code_path)
            if not os.path.exists(os.path.join(submission_code_path, "README.md")):
                with open(os.path.join(submission_code_path, "README.md"), mode='w') as f:
                    f.write("TBD") #create an empty README

            print('* MLPerf inference model: {}'.format(model))
            for scenario in scenarios:
                results[model][scenario] = {}
                result_scenario_path = os.path.join(result_model_path, scenario)
                submission_scenario_path = os.path.join(submission_model_path, scenario)
                measurement_scenario_path = os.path.join(measurement_model_path, scenario)
                compliance_scenario_path = os.path.join(compliance_model_path, scenario)

                if duplicate and scenario=='singlestream':
                    if not os.path.exists(os.path.join(result_model_path, "offline")):
                        print('Duplicating results from {} to offline:'.format(scenario))
                        shutil.copytree(result_scenario_path, os.path.join(result_model_path, "offline"))
                        scenarios.append("offline")
                    if not os.path.exists(os.path.join(result_model_path, "multistream")):
                        print('Duplicating results from {} to multistream:'.format(scenario))
                        shutil.copytree(result_scenario_path, os.path.join(result_model_path, "multistream"))
                        scenarios.append("multistream")

                modes = [f for f in os.listdir(result_scenario_path) if not os.path.isfile(os.path.join(result_scenario_path, f))]
                power_run = False

                #we check for the existance of mlperf_log_summary.txt mlperf_log_detail.txt to consider a result folder as valid. Rest of the checks are done later by the submission checker
                files_to_check = [ "mlperf_log_summary.txt", "mlperf_log_detail.txt" ]
                if not all([os.path.exists(os.path.join(result_scenario_path, "performance", "run_1", f)) for f in files_to_check]):
                    continue

                for mode in modes:
                    result_mode_path = os.path.join(result_scenario_path, mode)
                    submission_mode_path = os.path.join(submission_scenario_path, mode)
                    submission_measurement_path = measurement_scenario_path
                    submission_compliance_path = os.path.join(compliance_scenario_path, mode)
                    if mode.startswith("TEST"):
                        submission_results_path = submission_compliance_path
                    else:
                        submission_results_path = submission_mode_path
                    if os.path.exists(submission_results_path):
                        shutil.rmtree(submission_results_path)

                    if not os.path.isdir(submission_measurement_path):
                        os.makedirs(submission_measurement_path)

                    if mode=='performance':

                        if os.path.exists(os.path.join(result_mode_path, "power")):
                            power_run = True
                            result_power_path=os.path.join(result_mode_path, 'power')
                            submission_power_path=os.path.join(submission_mode_path, 'power')
                            os.makedirs(submission_power_path)
                            power_files = []
                            for f in os.listdir(result_power_path):
                                power_files.append(f) #Todo add required check from submission_checker
                            for f in power_files:
                                shutil.copy(os.path.join(result_power_path, f), os.path.join(submission_power_path, f))

                            analyzer_settings_file = env.get('CM_MLPERF_POWER_ANALYZER_SETTINGS_FILE_PATH', os.path.join(env['CM_TMP_CURRENT_SCRIPT_PATH'], "default_files", "analyzer_table.md"))
                            power_settings_file = env.get('CM_MLPERF_POWER_SETTINGS_FILE_PATH', os.path.join(env['CM_TMP_CURRENT_SCRIPT_PATH'], "default_files", "power_settings.md"))

                            shutil.copy(analyzer_settings_file, os.path.join(submission_measurement_path, "analyzer_table.md"))
                            shutil.copy(power_settings_file, os.path.join(submission_measurement_path, "power_settings.md"))

                            result_ranging_path=os.path.join(result_mode_path, 'ranging')
                            submission_ranging_path=os.path.join(submission_mode_path, 'ranging')
                            os.makedirs(submission_ranging_path)
                            ranging_files = []
                            for f in os.listdir(result_ranging_path):
                                ranging_files.append(f) #Todo add required check from submission_checker
                            for f in ranging_files:
                                shutil.copy(os.path.join(result_ranging_path, f), os.path.join(submission_ranging_path, f))

                        result_mode_path=os.path.join(result_mode_path, 'run_1')
                        submission_results_path=os.path.join(submission_mode_path, 'run_1')

                        if not os.path.exists(saved_system_meta_file_path):
                            saved_system_meta_file_path = os.path.join(result_mode_path, "system_meta.json")
                            if os.path.exists(saved_system_meta_file_path):
                                with open(saved_system_meta_file_path, "r") as f:
                                    saved_system_meta = json.load(f)
                                    for key in list(saved_system_meta):
                                        if saved_system_meta[key]==None or str(saved_system_meta[key]).strip() == '':
                                            del(saved_system_meta[key])
                                    system_meta = {**saved_system_meta, **system_meta} #override the saved meta with the user inputs
                                system_meta = {**system_meta_default, **system_meta} #add any missing fields from the defaults

                    if not os.path.isdir(submission_results_path):
                        os.makedirs(submission_results_path)

                    #if division == "closed" and not os.path.isdir(submission_compliance_path):
                    #    os.makedirs(submission_compliance_path)

                    mlperf_inference_conf_path = os.path.join(result_mode_path, "mlperf.conf")
                    if os.path.exists(mlperf_inference_conf_path):
                        shutil.copy(mlperf_inference_conf_path, os.path.join(submission_measurement_path, 'mlperf.conf'))
                    user_conf_path = os.path.join(result_mode_path, "user.conf")
                    if os.path.exists(user_conf_path):
                        shutil.copy(user_conf_path, os.path.join(submission_measurement_path, 'user.conf'))
                    measurements_json_path = os.path.join(result_mode_path, "measurements.json")
                    # get model precision
                    model_precision = "fp32"
                    if os.path.exists(measurements_json_path):
                        with open(measurements_json_path, "r") as f:
                            measurements_json = json.load(f)
                            model_precision = measurements_json.get("weight_data_types", "fp32")
                    if os.path.exists(measurements_json_path):
                        # This line can be removed once the PR in the inference repo is merged.
                        shutil.copy(measurements_json_path, os.path.join(submission_measurement_path, sub_res+'.json'))
                        shutil.copy(measurements_json_path, os.path.join(submission_measurement_path, 'model-info.json'))
                    files = []
                    readme = False

                    for f in os.listdir(result_mode_path):
                        if mode.startswith("TEST"):
                            if f.startswith('verify_'):
                                files.append(f)
                            elif f == "performance":
                                compliance_performance_run_path = os.path.join(result_mode_path, f, "run_1")
                                if os.path.exists(compliance_performance_run_path):
                                    target = os.path.join(submission_results_path, "performance", "run_1")
                                    os.makedirs(target)
                                    for log_file in os.listdir(compliance_performance_run_path):
                                        if log_file.startswith("mlperf_"):
                                            shutil.copy(os.path.join(compliance_performance_run_path, log_file), os.path.join(target, log_file))
                            elif f == "accuracy":
                                compliance_accuracy_run_path = os.path.join(result_mode_path, f)
                                if os.path.exists(compliance_accuracy_run_path):
                                    target = os.path.join(submission_results_path, "accuracy")
                                    os.makedirs(target)
                                    for log_file in os.listdir(compliance_accuracy_run_path):
                                        if log_file.startswith("mlperf_log_accuracy.json") or log_file.endswith("accuracy.txt"):
                                            shutil.copy(os.path.join(compliance_accuracy_run_path, log_file), os.path.join(target, log_file))
                        else:
                            if f.startswith('mlperf_') and not f.endswith('trace.json'):
                                files.append(f)
                            elif f == "spl.txt":
                                files.append(f)
                            elif f in [ "README.md", "README-extra.md", "cm-version-info.json", "os_info.json", "cpu_info.json", "pip_freeze.json", "system_info.txt" ] and mode == "performance":
                                shutil.copy(os.path.join(result_mode_path, f), os.path.join(submission_measurement_path, f))
                                if f == "system_info.txt" and not platform_info_file:
                                    platform_info_file = os.path.join(result_mode_path, f)
                            elif f in [ "console.out" ]:
                                shutil.copy(os.path.join(result_mode_path, f), os.path.join(submission_measurement_path, mode+"_"+f))


                    if mode == "accuracy":
                        if os.path.exists(os.path.join(result_mode_path, "accuracy.txt")):
                            files.append("accuracy.txt")
                        if model == "stable-diffusion-xl" and os.path.exists(os.path.join(result_mode_path, "images")):
                            shutil.copytree(os.path.join(result_mode_path, "images"), os.path.join(submission_results_path, "images"))

                    for f in files:
                        print(' * ' + f)
                        p_target = os.path.join(submission_results_path, f)
                        shutil.copy(os.path.join(result_mode_path, f), p_target)


                readme_file = os.path.join(submission_measurement_path, "README.md")
                if not os.path.exists(readme_file):
                    with open(readme_file, mode='w') as f:
                        f.write("TBD") #create an empty README
                else:
                    readme_suffix = ""
                    result_string, result = mlperf_utils.get_result_string(env['CM_MLPERF_LAST_RELEASE'], model, scenario, result_scenario_path, power_run, sub_res, division, system_file, model_precision, env.get('CM_MLPERF_INFERENCE_SOURCE_VERSION'))

                    for key in result:
                        results[model][scenario][key] = result[key]
                    with open(readme_file, mode='a') as f:
                        f.write(result_string)

            #Copy system_info.txt to the submission measurements model folder if any scenario performance run has it
            sys_info_file = None
            if os.path.exists(os.path.join(result_model_path, "system_info.txt")):
                sys_info_file = os.path.join(result_model_path, "system_info.txt")
            elif platform_info_file:
                sys_info_file = platform_info_file
            if sys_info_file:
                model_platform_info_file = sys_info_file
                shutil.copy(sys_info_file, os.path.join(measurement_model_path, "system_info.txt"))

        #Copy system_info.txt to the submission measurements folder if any model performance run has it
        sys_info_file = None
        if os.path.exists(os.path.join(result_path, "system_info.txt")):
            sys_info_file = os.path.join(result_path, "system_info.txt")
        elif model_platform_info_file:
            sys_info_file = model_platform_info_file
        if sys_info_file:
            shutil.copy(sys_info_file, os.path.join(measurement_path, "system_info.txt"))
 

        with open(system_file, "w") as fp:
            json.dump(system_meta, fp, indent=2)

        result_table, headers = mlperf_utils.get_result_table(results)

        print(tabulate(result_table, headers = headers, tablefmt="pretty"))
        sut_readme_file = os.path.join(measurement_path, "README.md")
        with open(sut_readme_file, mode='w') as f:
            f.write(tabulate(result_table, headers = headers, tablefmt="github"))


    return {'return':0}

def postprocess(i):

    r = generate_submission(i)
    if r['return'] > 0:
        return r

    return {'return':0}
