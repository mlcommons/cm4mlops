<details>
<summary>Click here to see the table of contents.</summary>

* [About](#about)
* [Summary](#summary)
* [Reuse this script in your project](#reuse-this-script-in-your-project)
  * [ Install CM automation language](#install-cm-automation-language)
  * [ Check CM script flags](#check-cm-script-flags)
  * [ Run this script from command line](#run-this-script-from-command-line)
  * [ Run this script from Python](#run-this-script-from-python)
  * [ Run this script via GUI](#run-this-script-via-gui)
  * [ Run this script via Docker (beta)](#run-this-script-via-docker-(beta))
* [Customization](#customization)
  * [ Variations](#variations)
  * [ Script flags mapped to environment](#script-flags-mapped-to-environment)
  * [ Default environment](#default-environment)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit!*

### About

This script is a CM wrapper to the official [Nvidia submission code](https://github.com/mlcommons/inference_results_v3.0/tree/master/closed/NVIDIA) used for MLPerf inference submissions. 



## Download the needed files

* Please ask privately in [this discord channel](https://discord.gg/y7hupJsUNb) if you would like to get access to an Amazon S3 bucket containing all the needed files for easiness. Otherwise, you can download them from the below links.
  
For x86 machines, please download the latest install tar files from the below sites
1. [cuDNN](https://developer.nvidia.com/cudnn) (for cuda 11)
2. [TensorRT](https://developer.nvidia.com/tensorrt)
3. Imagenet validation set (unfortunately not available via public URL) following the instructions given [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/get-dataset-imagenet-val/README-extra.md)

<details>

<summary>
    
## Using Docker (Recommended on x86 systems)

</summary>
Assuming all the downloaded files are to the user home directory please do the following steps:

1. Download CUDA 11.8
    ```
    wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda_11.8.0_520.61.05_linux.run
    ```
2. [Install docker](https://docs.docker.com/engine/install/) and [Nvidia container toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)
     
3. Give docker permission to the current user
     ```
     sudo usermod -aG docker $USER
     ```
     Logout and login
     Restart docker if required and confirm that Nvidia container toolkit is working by
     ```
     nvidia-ctk --version
     ```
4. Check if Nvidia driver is working properly on the host. 
     ```
     nvidia-smi
     ```
     If the above command produces any error you'll need to install Nvidia drivers on the host. You can do this via CM if you have sudo access
     ```
     cmr "install cuda prebuilt _driver" --version=11.8.0
     ```
5. Build the docker container and mount the paths from the host machine.
    ** You may want to change the `scratch_path` location as it can take 100s of GBs.**
    ```bash
    cm docker script --tags=build,nvidia,inference,server \
    --cuda_run_file_path=$HOME/cuda_11.8.0_520.61.05_linux.run \
    --tensorrt_tar_file_path=$HOME/TensorRT-8.6.1.6.Linux.x86_64-gnu.cuda-11.8.tar.gz \
    --cudnn_tar_file_path=$HOME/cudnn-linux-x86_64-8.9.2.26_cuda11-archive.tar.xz \
    --imagenet_path=$HOME/imagenet-2012-val \
    --scratch_path=$HOME/mlperf_scratch \
    --docker_cm_repo=mlcommons@ck  \
    --results_dir=$HOME/results_dir \
    --submission_dir=$HOME/submission_dir \
    --adr.compiler.tags=gcc
    ```
      * Use `--docker_cache=no` to turn off docker caching
      * Use `--docker_run_cmd_prefix="cm pull repo mlcommons@ck"` to update the CK repository when docker caching is used
      * Use `--custom_system=no` if you are using a similar system to the [Nvidia submission systems for MLPerf inference 3.0](https://github.com/mlcommons/inference_results_v3.0/tree/main/closed/NVIDIA/systems).

6. At the end of the build you'll get the following prompt unless you have chosen `--custom_system=no`. Please give a system name and say yes to generating the configuration files
    ### Example output
    ```
    ============================================
    => A system ID is a string containing only letters, numbers, and underscores
    => that is used as the human-readable name of the system. It is also used as
    => the system name when creating the measurements/ and results/ entries.
    => This string should also start with a letter to be a valid Python enum member name.
    => Specify the system ID to use for the current system: phoenix
      => Reloaded system list. MATCHED_SYSTEM: KnownSystem.phoenix
    => This script will generate Benchmark Configuration stubs for the detected system.
    Continue? [y/n]: y
    ```
    Now you'll be inside the CM Nvidia docker container and can run further scripts. 

7. Once the build is complete, you can proceed with any further CM scripts like for MLPerf inference. You can also save the container at this stage using [docker commit](https://docs.docker.com/engine/reference/commandline/commit/) so that it can be launched later without having to go through the previous steps.

</details>

<details>

<summary>

## Without Docker
</summary>

1. Install CUDA
    If CUDA is not detected, CM should download and install it automatically when you run the workflow. 
    ** Nvidia drivers are expected to be installed on the system **

2. Install cuDNN
    ```bash
      cmr "get cudnn" --tar_file=<PATH_TO_CUDNN_TAR_FILE>
    ```
3. Install TensorRT
    ```bash
      cmr "get tensorrt _dev" --tar_file=<PATH_TO_TENSORRT_TAR_FILE>
    ```
    On non x86 systems like Nvidia Orin, you can do a package manager install and then CM should pick up the installation automatically during the workflow run.

4. Build the Nvidia inference server 
    ```
      cmr "build nvidia inference server" \
      --adr.install-cuda-prebuilt.local_run_file_path=/data/cuda_11.8.0_520.61.05_linux.run \
      --adr.tensorrt.tar_file=/data/TensorRT-8.6.1.6.Linux.x86_64-gnu.cuda-11.8.tar.gz \
      --adr.cudnn.tar_file=/data/cudnn-linux-x86_64-8.9.2.26_cuda11-archive.tar.xz \
      --adr.compiler.tags=gcc \
      [--custom_system=no]
      ```
    Use `--custom_system=no` if you are using a similar system to the [Nvidia submission systems for MLPerf inference 3.0](https://github.com/mlcommons/inference_results_v3.0/tree/main/closed/NVIDIA/systems).

5. At the end of the build you'll get the following prompt unless you have chosen `--custom_system=no`. Please give a system name and say yes to generating the configuration files

    ### Example output
    ```
    ============================================
    => A system ID is a string containing only letters, numbers, and underscores
    => that is used as the human-readable name of the system. It is also used as
    => the system name when creating the measurements/ and results/ entries.
    => This string should also start with a letter to be a valid Python enum member name.
    => Specify the system ID to use for the current system: phoenix
      => Reloaded system list. MATCHED_SYSTEM: KnownSystem.phoenix
    => This script will generate Benchmark Configuration stubs for the detected system.
    Continue? [y/n]: y
    ```
</details>


## Acknowledgments

* A common CM interface and automation for MLPerf inference benchmarks was developed by Arjun Suresh and Grigori Fursin 
  sponsored by the [cTuning foundation](https://cTuning.org) and [cKnowledge.org](https://cKnowledge.org).
* Nvidia's MLPerf inference implementation was developed by Zhihan Jiang, Ethan Cheng, Yiheng Zhang and Jinho Suh.


#### Summary

* Category: *Reproduce MLPerf benchmarks.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-nvidia)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* CM "database" tags to find this script: *reproduce,mlcommons,mlperf,inference,harness,nvidia-harness,nvidia*
* Output cached? *False*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=reproduce,mlcommons,mlperf,inference,harness,nvidia-harness,nvidia[,variations] [--input_flags]`

2. `cmr "reproduce mlcommons mlperf inference harness nvidia-harness nvidia[ variations]" [--input_flags]`

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'reproduce,mlcommons,mlperf,inference,harness,nvidia-harness,nvidia'
                  'out':'con',
                  ...
                  (other input keys for this script)
                  ...
                 })

if r['return']>0:
    print (r['error'])

```

</details>


#### Run this script via GUI

```cmr "cm gui" --script="reproduce,mlcommons,mlperf,inference,harness,nvidia-harness,nvidia"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=reproduce,mlcommons,mlperf,inference,harness,nvidia-harness,nvidia) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "reproduce mlcommons mlperf inference harness nvidia-harness nvidia[ variations]" [--input_flags]`

___
### Customization


#### Variations

  * *Internal group (variations should not be selected manually)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_3d-unet_`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_transformers
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.nibabel
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_pandas
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * `_bert_`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_transformers
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_safetensors
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_onnx
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * `_dlrm_`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_torch
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.torchsnapshot
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.fbgemm-gpu
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)

    </details>


  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_a100,sxm,3d-unet_,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `8`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_a100,sxm,bert_,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `256`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_a100,sxm,dlrm_,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `1400`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_a100,sxm,resnet50,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `2048`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
        - *CM_MLPERF_PERFORMANCE_SAMPLE_COUNT*: `2048`
      - Workflow:
    * `_a100,sxm,retinanet,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `32`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_COPY_STREAMS*: `2`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_INFERENCE_STREAMS*: `2`
        - *CM_MLPERF_NVIDIA_HARNESS_WORKSPACE_SIZE*: `300000000000`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_a100,sxm,rnnt,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `2048`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_dla_batch_size.#`
      - Environment variables:
        - *CM_MLPERF_NVIDIA_HARNESS_DLA_BATCH_SIZE*: `#`
        - *CM_MLPERF_SUT_NAME_RUN_CONFIG_SUFFIX2*: `dla_batch_size.#`
      - Workflow:
    * `_gpu_memory.16,3d-unet_,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `4`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_gpu_memory.16,bert_,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `256`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_gpu_memory.16,dlrm_,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `1400`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_gpu_memory.16,resnet50,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `1024`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_COPY_STREAMS*: `4`
      - Workflow:
    * `_gpu_memory.16,retinanet,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `2`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_gpu_memory.16,rnnt,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `1024`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_gpu_memory.24,3d-unet_,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `8`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_gpu_memory.24,bert_,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `256`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_gpu_memory.24,dlrm_,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `1400`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_gpu_memory.24,resnet50,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `64`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_gpu_memory.24,retinanet,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `2`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_gpu_memory.24,rnnt,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `2048`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_gpu_memory.32,3d-unet_,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `8`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_gpu_memory.32,bert_,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `256`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_gpu_memory.32,dlrm_,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `1400`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_gpu_memory.32,resnet50,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `2048`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_gpu_memory.32,retinanet,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `4`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_gpu_memory.32,rnnt,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `2048`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_gpu_memory.40,3d-unet_,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `8`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_gpu_memory.40,bert_,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `256`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_gpu_memory.40,dlrm_,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `1400`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_gpu_memory.40,resnet50,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `2048`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_gpu_memory.40,retinanet,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `4`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_gpu_memory.40,rnnt,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `2048`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_gpu_memory.48,3d-unet_,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `8`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_gpu_memory.48,bert_,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `1024`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_gpu_memory.48,dlrm_,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `1400`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_gpu_memory.48,resnet50,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `2048`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_gpu_memory.48,retinanet,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `4`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_gpu_memory.48,rnnt,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `2048`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_gpu_memory.80,3d-unet_,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `8`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_gpu_memory.80,bert_,server,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `64`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_gpu_memory.80,dlrm_,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `1400`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_gpu_memory.80,resnet50,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `2048`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_gpu_memory.80,retinanet,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `8`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_gpu_memory.80,rnnt,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `2048`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_l4,3d-unet_,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `1`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_l4,bert_,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `16`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_l4,bert_,server,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `16`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
        - *CM_MLPERF_NVIDIA_HARNESS_GRAPHS_MAX_SEQLEN*: `200`
        - *CM_MLPERF_NVIDIA_HARNESS_SERVER_NUM_ISSUE_QUERY_THREADS*: `1`
        - *CM_MLPERF_NVIDIA_HARNESS_SOFT_DROP*: `1.0`
        - *CM_MLPERF_NVIDIA_HARNESS_USE_SMALL_TILE_GEMM_PLUGIN*: `True`
      - Workflow:
    * `_l4,dlrm_,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `1400`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_l4,resnet50`
      - Workflow:
    * `_l4,resnet50,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `32`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_COPY_STREAMS*: `2`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_INFERENCE_STREAMS*: `1`
        - *CM_MLPERF_NVIDIA_HARNESS_USE_GRAPHS*: `True`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_l4,resnet50,server,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `16`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_COPY_STREAMS*: `9`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_INFERENCE_STREAMS*: `2`
        - *CM_MLPERF_NVIDIA_HARNESS_USE_GRAPHS*: `True`
        - *CM_MLPERF_NVIDIA_HARNESS_USE_DEQUE_LIMIT*: `True`
        - *CM_MLPERF_NVIDIA_HARNESS_DEQUE_TIMEOUT_USEC*: `2000`
        - *CM_MLPERF_NVIDIA_HARNESS_USE_CUDA_THREAD_PER_DEVICE*: `True`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_l4,retinanet,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `2`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_l4,retinanet,server,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `2`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_INFERENCE_STREAMS*: `2`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_COPY_STREAMS*: `2`
        - *CM_MLPERF_NVIDIA_HARNESS_USE_DEQUE_LIMIT*: `True`
        - *CM_MLPERF_NVIDIA_HARNESS_DEQUE_TIMEOUT_USEC*: `30000`
        - *CM_MLPERF_NVIDIA_HARNESS_WORKSPACE_SIZE*: `20000000000`
      - Workflow:
    * `_l4,rnnt,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `512`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_l4,rnnt,server,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `512`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
        - *CM_MLPERF_NVIDIA_HARNESS_AUDIO_BATCH_SIZE*: `64`
        - *CM_MLPERF_NVIDIA_HARNESS_AUDIO_BUFFER_NUM_LINES*: `1024`
        - *CM_MLPERF_NVIDIA_HARNESS_NUM_WARMUPS*: `1024`
      - Workflow:
    * `_multistream,resnet50`
      - Environment variables:
        - *SKIP_POLICIES*: `1`
      - Workflow:
    * `_orin,rnnt,singlestream,run_harness`
      - Environment variables:
        - *CM_MLPERF_NVIDIA_HARNESS_NUM_WARMUPS*: `1`
      - Workflow:
    * `_resnet50,multistream,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `8`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_resnet50,server,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `64`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_retinanet,multistream,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `2`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_retinanet,server,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `8`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_rtx_4090,3d-unet_,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `8`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_rtx_4090,3d-unet_,server,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `8`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_rtx_4090,bert_,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `256`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_rtx_4090,bert_,server,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `256`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_rtx_4090,dlrm_,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `1400`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_rtx_4090,resnet50,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `64`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_rtx_4090,resnet50,server,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `32`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_rtx_4090,retinanet,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `2`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_rtx_4090,retinanet,server,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `2`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_rtx_4090,rnnt,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `2048`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_rtx_4090,rnnt,server,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `2048`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_rtx_6000_ada,3d-unet_,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `8`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_rtx_6000_ada,3d-unet_,server,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `8`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_rtx_6000_ada,bert_,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `256`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_rtx_6000_ada,bert_,server,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `256`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_rtx_6000_ada,dlrm_,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `1400`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_rtx_6000_ada,resnet50,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `64`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_rtx_6000_ada,resnet50,server,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `32`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_rtx_6000_ada,retinanet,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `2`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_rtx_6000_ada,retinanet,server,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `2`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_rtx_6000_ada,rnnt,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `512`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_rtx_6000_ada,rnnt,server,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `512`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_rtx_a6000,3d-unet_,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `8`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_rtx_a6000,3d-unet_,server,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `8`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_rtx_a6000,bert_,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `256`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_rtx_a6000,bert_,server,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `256`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_rtx_a6000,dlrm_,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `1400`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_rtx_a6000,resnet50,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `64`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_rtx_a6000,resnet50,server,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `32`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_rtx_a6000,retinanet,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `2`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_rtx_a6000,retinanet,server,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `2`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_rtx_a6000,rnnt,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `2048`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_rtx_a6000,rnnt,server,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `512`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_singlestream,resnet50`
      - Environment variables:
        - *SKIP_POLICIES*: `1`
      - Workflow:
    * `_singlestream,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `1`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_t4,3d-unet_,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `8`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_t4,bert_,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `256`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_t4,bert_,server,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `4`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
        - *CM_MLPERF_NVIDIA_HARNESS_GRAPHS_MAX_SEQLEN*: `240`
        - *CM_MLPERF_NVIDIA_HARNESS_SERVER_NUM_ISSUE_QUERY_THREADS*: `0`
        - *CM_MLPERF_NVIDIA_HARNESS_USE_SMALL_TILE_GEMM_PLUGIN*: `no`
      - Workflow:
    * `_t4,dlrm_,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `1400`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_t4,resnet50`
      - Workflow:
    * `_t4,resnet50,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `256`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_COPY_STREAMS*: `4`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_t4,resnet50,server,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `26`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_INFERENCE_STREAMS*: `2`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_COPY_STREAMS*: `4`
        - *CM_MLPERF_NVIDIA_HARNESS_USE_DEQUE_LIMIT*: `True`
        - *CM_MLPERF_NVIDIA_HARNESS_DEQUE_TIMEOUT_USEC*: `2000`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
        - *CM_MLPERF_NVIDIA_HARNESS_SOFT_DROP*: `0.993`
      - Workflow:
    * `_t4,retinanet,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `4`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_t4,retinanet,server,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `2`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_INFERENCE_STREAMS*: `2`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_COPY_STREAMS*: `2`
        - *CM_MLPERF_NVIDIA_HARNESS_USE_DEQUE_LIMIT*: `True`
        - *CM_MLPERF_NVIDIA_HARNESS_DEQUE_TIMEOUT_USEC*: `20000`
        - *CM_MLPERF_NVIDIA_HARNESS_WORKSPACE_SIZE*: `20000000000`
      - Workflow:
    * `_t4,rnnt,offline,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `2048`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_COPY_STREAMS*: `4`
        - *CM_MLPERF_NVIDIA_HARNESS_USE_GRAPHS*: `True`
        - *CM_MLPERF_NVIDIA_HARNESS_AUDIO_BATCH_SIZE*: `128`
        - *CM_MLPERF_NVIDIA_HARNESS_DISABLE_ENCODER_PLUGIN*: `True`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_t4,rnnt,server,run_harness`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `2048`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_COPY_STREAMS*: `4`
        - *CM_MLPERF_NVIDIA_HARNESS_USE_GRAPHS*: `True`
        - *CM_MLPERF_NVIDIA_HARNESS_AUDIO_BATCH_SIZE*: `128`
        - *CM_MLPERF_NVIDIA_HARNESS_DISABLE_ENCODER_PLUGIN*: `True`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:

    </details>


  * Group "**backend**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_tensorrt`** (default)
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `tensorrt`
        - *CM_MLPERF_BACKEND_NAME*: `TensorRT`
      - Workflow:

    </details>


  * Group "**batch-size**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_batch_size.#`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `#`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `#`
      - Workflow:

    </details>


  * Group "**build-engine-options**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_build_engine_options.#`
      - Environment variables:
        - *CM_MLPERF_NVIDIA_HARNESS_EXTRA_BUILD_ENGINE_OPTIONS*: `#`
      - Workflow:

    </details>


  * Group "**device**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_cpu`
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `cpu`
      - Workflow:
    * **`_cuda`** (default)
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `gpu`
        - *CM_MLPERF_DEVICE_LIB_NAMESPEC*: `cudart`
      - Workflow:

    </details>


  * Group "**device-memory**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_gpu_memory.16`
      - Environment variables:
        - *CM_NVIDIA_GPU_MEMORY*: `16`
      - Workflow:
    * `_gpu_memory.24`
      - Environment variables:
        - *CM_NVIDIA_GPU_MEMORY*: `24`
      - Workflow:
    * `_gpu_memory.32`
      - Environment variables:
        - *CM_NVIDIA_GPU_MEMORY*: `32`
      - Workflow:
    * `_gpu_memory.40`
      - Environment variables:
        - *CM_NVIDIA_GPU_MEMORY*: `40`
      - Workflow:
    * `_gpu_memory.48`
      - Environment variables:
        - *CM_NVIDIA_GPU_MEMORY*: `48`
      - Workflow:
    * `_gpu_memory.8`
      - Environment variables:
        - *CM_NVIDIA_GPU_MEMORY*: `8`
      - Workflow:
    * `_gpu_memory.80`
      - Environment variables:
        - *CM_NVIDIA_GPU_MEMORY*: `80`
      - Workflow:

    </details>


  * Group "**gpu-connection**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_pcie`
      - Workflow:
    * `_sxm`
      - Workflow:

    </details>


  * Group "**gpu-name**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_a100`
      - Environment variables:
        - *CM_NVIDIA_CUSTOM_GPU*: `yes`
      - Workflow:
    * `_a6000`
      - Environment variables:
        - *CM_NVIDIA_CUSTOM_GPU*: `yes`
      - Workflow:
    * `_custom`
      - Environment variables:
        - *CM_NVIDIA_CUSTOM_GPU*: `yes`
        - *CM_MODEL_BATCH_SIZE*: ``
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_l4`
      - Environment variables:
        - *CM_NVIDIA_CUSTOM_GPU*: `yes`
      - Workflow:
    * `_orin`
      - Environment variables:
        - *CM_NVIDIA_CUSTOM_GPU*: `yes`
        - *CM_MODEL_BATCH_SIZE*: ``
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `<<<CM_MODEL_BATCH_SIZE>>>`
      - Workflow:
    * `_rtx_4090`
      - Environment variables:
        - *CM_NVIDIA_CUSTOM_GPU*: `yes`
      - Workflow:
    * `_rtx_6000_ada`
      - Environment variables:
        - *CM_NVIDIA_CUSTOM_GPU*: `yes`
      - Workflow:
    * `_t4`
      - Environment variables:
        - *CM_NVIDIA_CUSTOM_GPU*: `yes`
      - Workflow:

    </details>


  * Group "**loadgen-scenario**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_multistream`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_SCENARIO*: `MultiStream`
      - Workflow:
    * `_offline`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_SCENARIO*: `Offline`
      - Workflow:
    * `_server`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_SCENARIO*: `Server`
      - Workflow:
    * `_singlestream`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_SCENARIO*: `SingleStream`
      - Workflow:

    </details>


  * Group "**model**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_3d-unet-99`
      - Environment variables:
        - *CM_MODEL*: `3d-unet-99`
        - *CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://zenodo.org/record/5597155/files/3dunet_kits19_128x128x128.onnx`
      - Workflow:
    * `_3d-unet-99.9`
      - Environment variables:
        - *CM_MODEL*: `3d-unet-99.9`
        - *CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://zenodo.org/record/5597155/files/3dunet_kits19_128x128x128.onnx`
      - Workflow:
    * `_bert-99`
      - Environment variables:
        - *CM_MODEL*: `bert-99`
        - *CM_NOT_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://zenodo.org/record/3750364/files/bert_large_v1_1_fake_quant.onnx`
      - Workflow:
    * `_bert-99.9`
      - Environment variables:
        - *CM_MODEL*: `bert-99.9`
        - *CM_NOT_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://zenodo.org/record/3733910/files/model.onnx`
      - Workflow:
    * `_dlrm-v2-99`
      - Environment variables:
        - *CM_MODEL*: `dlrm-v2-99`
      - Workflow:
    * `_dlrm-v2-99.9`
      - Environment variables:
        - *CM_MODEL*: `dlrm-v2-99.9`
      - Workflow:
    * **`_resnet50`** (default)
      - Environment variables:
        - *CM_MODEL*: `resnet50`
      - Workflow:
    * `_retinanet`
      - Environment variables:
        - *CM_MODEL*: `retinanet`
        - *CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://zenodo.org/record/6617981/files/resnext50_32x4d_fpn.pth`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_Pillow
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_torch
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_torchvision
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_opencv-python
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_numpy
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_pycocotools
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * `_rnnt`
      - Environment variables:
        - *CM_MODEL*: `rnnt`
        - *CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://zenodo.org/record/3662521/files/DistributedDataParallel_1576581068.9962234-epoch-100.pt`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_toml
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_torchvision
             * CM names: `--adr.['torchvision']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_torch
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_nvidia-apex
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_unidecode
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_inflect
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_librosa
             * CM names: `--adr.['librosa']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_sox
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-sys-util,_sox
             - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)

    </details>


  * Group "**power-mode**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_maxn`
      - Environment variables:
        - *CM_MLPERF_NVIDIA_HARNESS_MAXN*: `True`
      - Workflow:
    * `_maxq`
      - Environment variables:
        - *CM_MLPERF_NVIDIA_HARNESS_MAXQ*: `True`
      - Workflow:

    </details>


  * Group "**run-mode**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_build`
      - Environment variables:
        - *MLPERF_NVIDIA_RUN_COMMAND*: `build`
        - *CM_MLPERF_NVIDIA_HARNESS_RUN_MODE*: `build`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,cmake
             - CM script: [get-cmake](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cmake)
           * get,generic,sys-util,_glog-dev
             - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
           * get,generic,sys-util,_gflags-dev
             - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
           * get,generic,sys-util,_libgmock-dev
             - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
           * get,generic,sys-util,_libre2-dev
             - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
           * get,generic,sys-util,_libnuma-dev
             - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
           * get,generic,sys-util,_libboost-all-dev
             - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
           * get,generic,sys-util,_rapidjson-dev
             - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
    * `_build_engine`
      - Environment variables:
        - *MLPERF_NVIDIA_RUN_COMMAND*: `generate_engines`
        - *CM_MLPERF_NVIDIA_HARNESS_RUN_MODE*: `generate_engines`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * reproduce,mlperf,inference,nvidia,harness,_preprocess_data
             * `if (CM_MODEL not in dlrm-v2-99)`
             - CM script: [reproduce-mlperf-inference-nvidia](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-nvidia)
           * reproduce,mlperf,inference,nvidia,harness,_download_model
             * `if (CM_MODEL not in ['retinanet_old', 'resnet50', 'bert-99', 'bert-99.9', 'dlrm-v2-99', 'dlrm-v2-99.9'])`
             - CM script: [reproduce-mlperf-inference-nvidia](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-nvidia)
           * reproduce,mlperf,inference,nvidia,harness,_calibrate
             * `if (CM_MODEL  == retinanet)`
             - CM script: [reproduce-mlperf-inference-nvidia](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-nvidia)
    * `_calibrate`
      - Environment variables:
        - *MLPERF_NVIDIA_RUN_COMMAND*: `calibrate`
        - *CM_MLPERF_NVIDIA_HARNESS_RUN_MODE*: `calibrate`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * reproduce,mlperf,inference,nvidia,harness,_download_model
             * `if (CM_MODEL not in ['retinanet_old', 'resnet50', 'bert-99', 'bert-99.9', 'dlrm-v2-99', 'dlrm-v2-99.9'])`
             - CM script: [reproduce-mlperf-inference-nvidia](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-nvidia)
    * `_download_model`
      - Environment variables:
        - *MLPERF_NVIDIA_RUN_COMMAND*: `download_model`
        - *CM_MLPERF_NVIDIA_HARNESS_RUN_MODE*: `download_model`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_torch_cuda
             * `if (CM_MODEL  == retinanet)`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * `_prebuild`
      - Environment variables:
        - *MLPERF_NVIDIA_RUN_COMMAND*: `prebuild`
        - *CM_MLPERF_NVIDIA_HARNESS_RUN_MODE*: `prebuild`
      - Workflow:
    * `_preprocess_data`
      - Environment variables:
        - *MLPERF_NVIDIA_RUN_COMMAND*: `preprocess_data`
        - *CM_MLPERF_NVIDIA_HARNESS_RUN_MODE*: `preprocess_data`
      - Workflow:
    * **`_run_harness`** (default)
      - Environment variables:
        - *CM_MLPERF_NVIDIA_HARNESS_RUN_MODE*: `run_harness`
        - *MLPERF_NVIDIA_RUN_COMMAND*: `run_harness`
        - *CM_CALL_MLPERF_RUNNER*: `yes`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * reproduce,mlperf,inference,nvidia,harness,_build_engine
             * CM names: `--adr.['build-engine']...`
             - CM script: [reproduce-mlperf-inference-nvidia](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-nvidia)
           * reproduce,mlperf,inference,nvidia,harness,_preprocess_data
             * `if (CM_MODEL not in dlrm-v2-99)`
             - CM script: [reproduce-mlperf-inference-nvidia](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-nvidia)
           * reproduce,mlperf,inference,nvidia,harness,_download_model
             * `if (CM_MODEL not in ['retinanet', 'resnet50', 'bert-99', 'bert-99.9', 'dlrm-v2-99', 'dlrm-v2-99.9'])`
             - CM script: [reproduce-mlperf-inference-nvidia](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-nvidia)

    </details>


  * Group "**triton**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_use_triton`
      - Environment variables:
        - *CM_MLPERF_NVIDIA_HARNESS_USE_TRITON*: `yes`
        - *CM_MLPERF_SUT_NAME_RUN_CONFIG_SUFFIX3*: `using_triton`
      - Workflow:

    </details>


#### Default variations

`_cuda,_resnet50,_run_harness,_tensorrt`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--audio_buffer_num_lines=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_AUDIO_BUFFER_NUM_LINES=value`
* `--count=value`  &rarr;  `CM_MLPERF_LOADGEN_QUERY_COUNT=value`
* `--deque_timeout_usec=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_DEQUE_TIMEOUT_USEC=value`
* `--devices=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_DEVICES=value`
* `--dla_batch_size=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_DLA_BATCH_SIZE=value`
* `--dla_copy_streams=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_DLA_COPY_STREAMS=value`
* `--dla_inference_streams=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_DLA_INFERENCE_STREAMS=value`
* `--end_on_device=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_END_ON_DEVICE=value`
* `--extra_run_options=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_EXTRA_RUN_OPTIONS=value`
* `--gpu_batch_size=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE=value`
* `--gpu_copy_streams=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_GPU_COPY_STREAMS=value`
* `--gpu_inference_streams=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_GPU_INFERENCE_STREAMS=value`
* `--graphs_max_seqlen=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_GRAPHS_MAX_SEQLEN=value`
* `--input_format=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_INPUT_FORMAT=value`
* `--log_dir=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_LOG_DIR=value`
* `--make_cmd=value`  &rarr;  `MLPERF_NVIDIA_RUN_COMMAND=value`
* `--max_batchsize=value`  &rarr;  `CM_MLPERF_LOADGEN_MAX_BATCHSIZE=value`
* `--max_dlas=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_MAX_DLAS=value`
* `--mlperf_conf=value`  &rarr;  `CM_MLPERF_CONF=value`
* `--mode=value`  &rarr;  `CM_MLPERF_LOADGEN_MODE=value`
* `--multistream_target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_MULTISTREAM_TARGET_LATENCY=value`
* `--num_issue_query_threads=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_NUM_ISSUE_QUERY_THREADS=value`
* `--num_warmups=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_NUM_WARMUPS=value`
* `--offline_target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_OFFLINE_TARGET_QPS=value`
* `--output_dir=value`  &rarr;  `CM_MLPERF_OUTPUT_DIR=value`
* `--performance_sample_count=value`  &rarr;  `CM_MLPERF_LOADGEN_PERFORMANCE_SAMPLE_COUNT=value`
* `--power_setting=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_POWER_SETTING=value`
* `--rerun=value`  &rarr;  `CM_RERUN=value`
* `--run_infer_on_copy_streams=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_RUN_INFER_ON_COPY_STREAMS=value`
* `--scenario=value`  &rarr;  `CM_MLPERF_LOADGEN_SCENARIO=value`
* `--server_target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_SERVER_TARGET_QPS=value`
* `--singlestream_target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_SINGLESTREAM_TARGET_LATENCY=value`
* `--skip_preprocess=value`  &rarr;  `CM_SKIP_PREPROCESS_DATASET=value`
* `--skip_preprocessing=value`  &rarr;  `CM_SKIP_PREPROCESS_DATASET=value`
* `--soft_drop=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_SOFT_DROP=value`
* `--start_from_device=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_START_FROM_DEVICE=value`
* `--target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_TARGET_LATENCY=value`
* `--target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_TARGET_QPS=value`
* `--use_cuda_thread_per_device=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_USE_CUDA_THREAD_PER_DEVICE=value`
* `--use_deque_limit=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_USE_DEQUE_LIMIT=value`
* `--use_graphs=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_USE_GRAPHS=value`
* `--use_small_tile_gemm_plugin=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_USE_SMALL_TILE_GEMM_PLUGIN=value`
* `--use_triton=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_USE_TRITON=value`
* `--user_conf=value`  &rarr;  `CM_MLPERF_USER_CONF=value`
* `--workspace_size=value`  &rarr;  `CM_MLPERF_NVIDIA_HARNESS_WORKSPACE_SIZE=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "audio_buffer_num_lines":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_BATCH_COUNT: `1`
* CM_BATCH_SIZE: `1`
* CM_FAST_COMPILATION: `yes`
* CM_MLPERF_LOADGEN_SCENARIO: `Offline`
* CM_MLPERF_LOADGEN_MODE: `performance`
* CM_SKIP_PREPROCESS_DATASET: `no`
* CM_SKIP_MODEL_DOWNLOAD: `no`
* CM_MLPERF_SUT_NAME_IMPLEMENTATION_PREFIX: `nvidia_original`
* CM_MLPERF_SKIP_RUN: `no`

</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-nvidia/_cm.yaml)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,sys-utils-cm
       - CM script: [get-sys-utils-cm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
     * get,cuda,_cudnn
       * CM names: `--adr.['cuda']...`
       - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
     * get,tensorrt
       * CM names: `--adr.['tensorrt']...`
       - CM script: [get-tensorrt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tensorrt)
     * build,nvidia,inference,server
       * CM names: `--adr.['nvidia-inference-server']...`
       - CM script: [build-mlperf-inference-server-nvidia](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-mlperf-inference-server-nvidia)
     * get,mlperf,inference,nvidia,scratch,space
       * CM names: `--adr.['nvidia-scratch-space']...`
       - CM script: [get-mlperf-inference-nvidia-scratch-space](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-nvidia-scratch-space)
     * get,generic-python-lib,_mlperf_logging
       * CM names: `--adr.['mlperf-logging']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,dataset,original,imagenet,_full
       * `if (CM_MODEL  == resnet50)`
       * CM names: `--adr.['imagenet-original']...`
       - CM script: [get-dataset-imagenet-val](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val)
     * get,ml-model,resnet50,_fp32,_onnx,_opset-8
       * `if (CM_MODEL  == resnet50)`
       * CM names: `--adr.['resnet50-model', 'ml-model']...`
       - CM script: [get-ml-model-resnet50](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50)
     * get,dataset,original,kits19
       * `if (CM_MODEL in ['3d-unet-99-disabled', '3d-unet-99.9-disabled'])`
       * CM names: `--adr.['kits19-original']...`
       - CM script: [get-dataset-kits19](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-kits19)
     * get,dataset,original,librispeech
       * `if (CM_MODEL  == rnnt)`
       * CM names: `--adr.['librispeech-original']...`
       - CM script: [get-dataset-librispeech](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-librispeech)
     * get,dataset,preprocessed,criteo
       * `if (CM_MODEL in ['dlrm-v2-99', 'dlrm-v2-99.9'])`
       * CM names: `--adr.['criteo-preprocessed']...`
       - CM script: [get-preprocessed-dataset-criteo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-criteo)
     * get,ml-model,dlrm,_pytorch
       * `if (CM_MODEL in ['dlrm-v2-99', 'dlrm-v2-99.9'])`
       * CM names: `--adr.['dlrm-model']...`
       - CM script: [get-ml-model-dlrm-terabyte](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-dlrm-terabyte)
     * get,ml-model,bert,_onnx,_fp32
       * `if (CM_MODEL in ['bert-99', 'bert-99.9'])`
       * CM names: `--adr.['bert-model', 'bert-model-fp32']...`
       - CM script: [get-ml-model-bert-large-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-large-squad)
     * get,ml-model,bert,_onnx,_int8
       * `if (CM_MODEL in ['bert-99', 'bert-99.9'])`
       * CM names: `--adr.['bert-model', 'bert-model-int8']...`
       - CM script: [get-ml-model-bert-large-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-large-squad)
     * get,squad-vocab
       * `if (CM_MODEL in ['bert-99', 'bert-99.9'])`
       * CM names: `--adr.['bert-vocab']...`
       - CM script: [get-dataset-squad-vocab](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-squad-vocab)
     * get,dataset,original,openimages,_validation,_full,_custom-annotations
       * `if (CM_MODEL  == retinanet)`
       * CM names: `--adr.['openimages-original']...`
       - CM script: [get-dataset-openimages](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages)
     * get,dataset,original,openimages,_calibration
       * `if (CM_MODEL  == retinanet)`
       * CM names: `--adr.['openimages-calibration']...`
       - CM script: [get-dataset-openimages](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages)
     * get,mlcommons,inference,src
       * CM names: `--adr.['inference-src']...`
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
     * get,nvidia,mlperf,inference,common-code
       * CM names: `--adr.['nvidia-inference-common-code']...`
       - CM script: [get-mlperf-inference-nvidia-common-code](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-nvidia-common-code)
     * generate,user-conf,mlperf,inference
       * `if (CM_MLPERF_NVIDIA_HARNESS_RUN_MODE  == run_harness)`
       * CM names: `--adr.['user-conf-generator']...`
       - CM script: [generate-mlperf-inference-user-conf](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-user-conf)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-nvidia/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-nvidia/_cm.yaml)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-nvidia/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-nvidia/_cm.yaml)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-nvidia/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-nvidia/_cm.yaml)***
     * benchmark-mlperf
       * `if (CM_CALL_MLPERF_RUNNER  == True) AND (CM_MLPERF_SKIP_RUN not in ['yes', True])`
       * CM names: `--adr.['runner', 'mlperf-runner']...`
       - CM script: [benchmark-program-mlperf](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/benchmark-program-mlperf)
</details>

___
### Script output
`cmr "reproduce mlcommons mlperf inference harness nvidia-harness nvidia[,variations]" [--input_flags] -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)