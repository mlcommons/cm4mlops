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
  * [ Default environment](#default-environment)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit!*

### About


See extra [notes](README-extra.md) from the authors and contributors.

#### Summary

* Category: *MLPerf benchmark support.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-tiny-submission)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *generate,submission,mlperf,mlperf-tiny,tiny,mlcommons,tiny-submission,mlperf-tiny-submission,mlcommons-tiny-submission*
* Output cached? *False*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=generate,submission,mlperf,mlperf-tiny,tiny,mlcommons,tiny-submission,mlperf-tiny-submission,mlcommons-tiny-submission `

2. `cmr "generate submission mlperf mlperf-tiny tiny mlcommons tiny-submission mlperf-tiny-submission mlcommons-tiny-submission" `

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'generate,submission,mlperf,mlperf-tiny,tiny,mlcommons,tiny-submission,mlperf-tiny-submission,mlcommons-tiny-submission'
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

```cmr "cm gui" --script="generate,submission,mlperf,mlperf-tiny,tiny,mlcommons,tiny-submission,mlperf-tiny-submission,mlcommons-tiny-submission"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=generate,submission,mlperf,mlperf-tiny,tiny,mlcommons,tiny-submission,mlperf-tiny-submission,mlcommons-tiny-submission) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "generate submission mlperf mlperf-tiny tiny mlcommons tiny-submission mlperf-tiny-submission mlcommons-tiny-submission" `

___
### Customization

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-tiny-submission/_cm.json)***
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,sut,system-description
       - CM script: [get-mlperf-inference-sut-description](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-description)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-tiny-submission/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-tiny-submission/_cm.json)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-tiny-submission/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-tiny-submission/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-tiny-submission/_cm.json)***
     * 
       * `if (CM_MLPERF_RUN_STYLE  == valid)`
       - CM script: [app-image-corner-detection](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-corner-detection)
       - CM script: [get-mlperf-logging](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-logging)
       - CM script: [reproduce-mlperf-inference-qualcomm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-qualcomm)
       - CM script: [get-mlperf-tiny-eembc-energy-runner-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-tiny-eembc-energy-runner-src)
       - CM script: [generate-mlperf-tiny-report](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-tiny-report)
       - CM script: [reproduce-micro-2023-paper-victima](reproduce-micro-2023-paper-victima)
       - CM script: [get-dataset-coco](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-coco)
       - CM script: [get-preprocessed-dataset-librispeech](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-librispeech)
       - CM script: [import-mlperf-training-to-experiment](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/import-mlperf-training-to-experiment)
       - CM script: [get-lib-qaic-api](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-lib-qaic-api)
       - CM script: [get-ml-model-huggingface-zoo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-huggingface-zoo)
       - CM script: [prune-bert-models](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/prune-bert-models)
       - CM script: [reproduce-ieee-acm-micro2023-paper-85](https://github.com/ctuning/cm-reproduce-research-projects/tree/master/script/reproduce-ieee-acm-micro2023-paper-85)
       - CM script: [test-script3](https://github.com/gfursin/cm-tests/tree/master/script/test-script3)
       - CM script: [get-llvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-llvm)
       - CM script: [reproduce-ieee-acm-micro2023-paper-38](https://github.com/ctuning/cm-reproduce-research-projects/tree/master/script/reproduce-ieee-acm-micro2023-paper-38)
       - CM script: [get-ml-model-rnnt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-rnnt)
       - CM script: [install-python-venv](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-python-venv)
       - CM script: [get-mlperf-tiny-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-tiny-src)
       - CM script: [set-performance-mode](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/set-performance-mode)
       - CM script: [test-abtf-ssd-pytorch](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-abtf-ssd-pytorch)
       - CM script: [get-dataset-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-squad)
       - CM script: [prepare-training-data-bert](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/prepare-training-data-bert)
       - CM script: [run-how-to-run-server](https://github.com/how-to-run/server/tree/master/script/run-how-to-run-server)
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
       - CM script: [set-echo-off-win](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/set-echo-off-win)
       - CM script: [reproduce-ipol-paper-2022-439](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-ipol-paper-2022-439)
       - CM script: [get-mlperf-inference-nvidia-common-code](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-nvidia-common-code)
       - CM script: [install-qaic-compute-sdk-from.src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-qaic-compute-sdk-from.src)
       - CM script: [destroy-terraform](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/destroy-terraform)
       - CM script: [get-dataset-cnndm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-cnndm)
       - CM script: [build-dockerfile](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-dockerfile)
       - CM script: [get-kilt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-kilt)
       - CM script: [download-torrent](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-torrent)
       - CM script: [install-tensorflow-for-c](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-tensorflow-for-c)
       - CM script: [create-fpgaconvnet-config-tinyml](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/create-fpgaconvnet-config-tinyml)
       - CM script: [get-ml-model-bert-large-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-large-squad)
       - CM script: [install-openssl](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-openssl)
       - CM script: [run-mlperf-inference-submission-checker](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-submission-checker)
       - CM script: [print-hello-world-javac](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world-javac)
       - CM script: [install-github-cli](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-github-cli)
       - CM script: [get-rocm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-rocm)
       - CM script: [build-mlperf-inference-server-nvidia](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-mlperf-inference-server-nvidia)
       - CM script: [get-dataset-imagenet-val](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val)
       - CM script: [app-mlperf-inference-tflite-cpp](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-tflite-cpp)
       - CM script: [get-preprocessed-dataset-imagenet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet)
       - CM script: [get-dataset-imagenet-aux](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-aux)
       - CM script: [not-needed--get-android-cmdline-tools](https://github.com/cknowledge/tests/tree/master/cm/script/not-needed--get-android-cmdline-tools)
       - CM script: [app-image-classification-tf-onnx-cpp](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-tf-onnx-cpp)
       - CM script: [get-zendnn](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-zendnn)
       - CM script: [pull-git-repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/pull-git-repo)
       - CM script: [print-python-version](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-python-version)
       - CM script: [get-docker](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-docker)
       - CM script: [get-openssl](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-openssl)
       - CM script: [create-fpgaconvnet-app-tinyml](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/create-fpgaconvnet-app-tinyml)
       - CM script: [upgrade-python-pip](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/upgrade-python-pip)
       - CM script: [get-ml-model-retinanet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-retinanet)
       - CM script: [reproduce-mlperf-inference-nvidia](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-nvidia)
       - CM script: [get-ml-model-3d-unet-kits19](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-3d-unet-kits19)
       - CM script: [run-experiments](run-experiments)
       - CM script: [install-tflite-from-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-tflite-from-src)
       - CM script: [get-google-test](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-google-test)
       - CM script: [get-dataset-criteo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-criteo)
       - CM script: [truncate-mlperf-inference-accuracy-log](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/truncate-mlperf-inference-accuracy-log)
       - CM script: [install-pytorch-from.src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-pytorch-from.src)
       - CM script: [get-ml-model-retinanet-nvidia](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-retinanet-nvidia)
       - CM script: [reproduce-micro-paper-2023-victima](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-micro-paper-2023-victima)
       - CM script: [process-ae-users](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/process-ae-users)
       - CM script: [app-mlperf-inference-reference](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-reference)
       - CM script: [get-ml-model-resnet50](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50)
       - CM script: [get-brew](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-brew)
       - CM script: [reproduce-mlperf-inference-intel](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-intel)
       - CM script: [produce-plots](produce-plots)
       - CM script: [get-mlperf-inference-nvidia-scratch-space](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-nvidia-scratch-space)
       - CM script: [app-image-classification-onnx-py-ck](https://github.com/cknowledge/tests/tree/master/cm/script/app-image-classification-onnx-py-ck)
       - CM script: [install-llvm-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-llvm-src)
       - CM script: [run-all-mlperf-models](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-all-mlperf-models)
       - CM script: [test-download-and-extract-artifacts](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-download-and-extract-artifacts)
       - CM script: [get-go](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-go)
       - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
       - CM script: [import-mlperf-inference-to-experiment](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/import-mlperf-inference-to-experiment)
       - CM script: [remote-run-commands](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/remote-run-commands)
       - CM script: [process-mlperf-inference-results](https://github.com/mlcommons/ck_mlperf_results/tree/master/script/process-mlperf-inference-results)
       - CM script: [reproduce-ieee-acm-micro2023-paper-33](https://github.com/ctuning/cm-reproduce-research-projects/tree/master/script/reproduce-ieee-acm-micro2023-paper-33)
       - CM script: [run-mlperf-power-client](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-power-client)
       - CM script: [run-mlperf-inference-mobilenet-models](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-mobilenet-models)
       - CM script: [get-java](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-java)
       - CM script: [reproduce-mlperf-training-nvidia](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-training-nvidia)
       - CM script: [get-mlperf-training-nvidia-code](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-training-nvidia-code)
       - CM script: [get-ml-model-gptj](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-gptj)
       - CM script: [get-xilinx-sdk](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-xilinx-sdk)
       - CM script: [get-cl](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cl)
       - CM script: [push-mlperf-inference-results-to-github](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/push-mlperf-inference-results-to-github)
       - CM script: [get-rclone](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-rclone)
       - CM script: [run-docker-container](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-docker-container)
       - CM script: [get-dataset-imagenet-helper](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-helper)
       - CM script: [get-preprocesser-script-generic](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocesser-script-generic)
       - CM script: [reproduce-ieee-acm-micro2023-paper-5](https://github.com/ctuning/cm-reproduce-research-projects/tree/master/script/reproduce-ieee-acm-micro2023-paper-5)
       - CM script: [generate-mlperf-tiny-submission](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-tiny-submission)
       - CM script: [activate-python-venv](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/activate-python-venv)
       - CM script: [get-ml-model-tiny-resnet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-tiny-resnet)
       - CM script: [convert-ml-model-huggingface-to-onnx](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/convert-ml-model-huggingface-to-onnx)
       - CM script: [generate-nvidia-engine](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-nvidia-engine)
       - CM script: [get-ml-model-stable-diffusion](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-stable-diffusion)
       - CM script: [get-mlperf-inference-results](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-results)
       - CM script: [test-set-sys-user-cm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-set-sys-user-cm)
       - CM script: [get-sys-utils-min](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-min)
       - CM script: [run-refiners-hello-world](https://github.com/cknowledge/cm-reproduce/tree/master/script/run-refiners-hello-world)
       - CM script: [print-hello-world](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world)
       - CM script: [get-terraform](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-terraform)
       - CM script: [get-zephyr](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-zephyr)
       - CM script: [set-sqlite-dir](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/set-sqlite-dir)
       - CM script: [get-ml-model-neuralmagic-zoo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-neuralmagic-zoo)
       - CM script: [get-cudnn](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cudnn)
       - CM script: [download-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-file)
       - CM script: [test-script1](https://github.com/gfursin/cm-tests/tree/master/script/test-script1)
       - CM script: [get-github-cli](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-github-cli)
       - CM script: [get-compiler-rust](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-compiler-rust)
       - CM script: [get-android-sdk](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-android-sdk)
       - CM script: [install_dep](install_dep)
       - CM script: [import-mlperf-tiny-to-experiment](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/import-mlperf-tiny-to-experiment)
       - CM script: [download-and-extract](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-and-extract)
       - CM script: [tar-my-folder](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/tar-my-folder)
       - CM script: [calibrate-model-for.qaic](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/calibrate-model-for.qaic)
       - CM script: [get-aocl](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-aocl)
       - CM script: [app-image-classification-torch-py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-torch-py)
       - CM script: [wrapper-reproduce-octoml-tinyml-submission](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/wrapper-reproduce-octoml-tinyml-submission)
       - CM script: [get-lib-protobuf](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-lib-protobuf)
       - CM script: [install-cuda-prebuilt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-cuda-prebuilt)
       - CM script: [not-needed--install-android-cmdline-tools](https://github.com/cknowledge/tests/tree/master/cm/script/not-needed--install-android-cmdline-tools)
       - CM script: [app-mlperf-inference-cpp](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-cpp)
       - CM script: [get-qaic-apps-sdk](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-qaic-apps-sdk)
       - CM script: [get-dataset-openimages-calibration](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages-calibration)
       - CM script: [get-dataset-openimages](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages)
       - CM script: [get-microtvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-microtvm)
       - CM script: [add-custom-nvidia-system](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/add-custom-nvidia-system)
       - CM script: [get-dataset-openorca](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openorca)
       - CM script: [generate-mlperf-inference-user-conf](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-user-conf)
       - CM script: [get-aws-cli](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-aws-cli)
       - CM script: [get-tvm-model](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm-model)
       - CM script: [get-mlcommons-croissant](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlcommons-croissant)
       - CM script: [run-python](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-python)
       - CM script: [app-loadgen-generic-python](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-loadgen-generic-python)
       - CM script: [install-terraform-from-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-terraform-from-src)
       - CM script: [benchmark-object-detection-loadgen](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/benchmark-object-detection-loadgen)
       - CM script: [get-cmake](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cmake)
       - CM script: [get-javac](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-javac)
       - CM script: [get-mlperf-inference-sut-description](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-description)
       - CM script: [app-mlperf-training-nvidia](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-training-nvidia)
       - CM script: [extract-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/extract-file)
       - CM script: [get-ml-model-efficientnet-lite](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-efficientnet-lite)
       - CM script: [get-ipol-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ipol-src)
       - CM script: [get-ml-model-using-imagenet-from-model-zoo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-using-imagenet-from-model-zoo)
       - CM script: [app-generate-image-stable-diffusion2-pytorch-cuda-py](https://github.com/cknowledge/tests/tree/master/cm/script/app-generate-image-stable-diffusion2-pytorch-cuda-py)
       - CM script: [get-dataset-kits19](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-kits19)
       - CM script: [get-ml-model-mobilenet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-mobilenet)
       - CM script: [get-cuda-devices](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda-devices)
       - CM script: [convert-csv-to-md](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/convert-csv-to-md)
       - CM script: [install-gcc-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-gcc-src)
       - CM script: [get-tensorrt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tensorrt)
       - CM script: [get-conda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-conda)
       - CM script: [install-cuda-package-manager](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-cuda-package-manager)
       - CM script: [get-preprocessed-dataset-kits19](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-kits19)
       - CM script: [get-spec-ptd](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-spec-ptd)
       - CM script: [compile-program](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-program)
       - CM script: [prepare-training-data-resnet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/prepare-training-data-resnet)
       - CM script: [run-mlperf-power-server](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-power-server)
       - CM script: [install-generic-conda-package](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-conda-package)
       - CM script: [get-preprocessed-dataset-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-squad)
       - CM script: [get-nvidia-docker](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-nvidia-docker)
       - CM script: [get-preprocessed-dataset-openimages](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-openimages)
       - CM script: [set-device-settings-qaic](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/set-device-settings-qaic)
       - CM script: [reproduce-ieee-acm-micro2023-paper-8](https://github.com/ctuning/cm-reproduce-research-projects/tree/master/script/reproduce-ieee-acm-micro2023-paper-8)
       - CM script: [test-mlperf-inference-retinanet-win](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-mlperf-inference-retinanet-win)
       - CM script: [reproduce-ipol-paper-2022-439a](https://github.com/ctuning/cm-reproduce-research-projects/tree/master/script/reproduce-ipol-paper-2022-439a)
       - CM script: [get-target-device](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-target-device)
       - CM script: [process-mlperf-accuracy](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/process-mlperf-accuracy)
       - CM script: [get-onnxruntime-prebuilt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-onnxruntime-prebuilt)
       - CM script: [run-mlperf-inference-app](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-app)
       - CM script: [app-generate-image-dalle-mini-jax-py](https://github.com/cknowledge/tests/tree/master/cm/script/app-generate-image-dalle-mini-jax-py)
       - CM script: [get-dlrm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dlrm)
       - CM script: [benchmark-program](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/benchmark-program)
       - CM script: [install-bazel](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-bazel)
       - CM script: [get-qaic-platform-sdk](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-qaic-platform-sdk)
       - CM script: [benchmark-program-mlperf](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/benchmark-program-mlperf)
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
       - CM script: [gui-llm](https://github.com/cknowledge/cm-private/tree/master/script/gui-llm)
       - CM script: [app-ipol-demo](https://github.com/cknowledge/tests/tree/master/cm/script/app-ipol-demo)
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
       - CM script: [test-script2](https://github.com/gfursin/cm-tests/tree/master/script/test-script2)
       - CM script: [get-mlperf-inference-sut-configs](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-configs)
       - CM script: [get-cmsis_5](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cmsis_5)
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
       - CM script: [build-docker-image](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-docker-image)
       - CM script: [install-tensorflow-from-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-tensorflow-from-src)
       - CM script: [test-script4](https://github.com/gfursin/cm-tests/tree/master/script/test-script4)
       - CM script: [get-bert-squad-vocab](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-bert-squad-vocab)
       - CM script: [generate-mlperf-inference-submission](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-submission)
       - CM script: [compile-model-for.qaic](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-model-for.qaic)
       - CM script: [install-aws-cli](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-aws-cli)
       - CM script: [gui](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/gui)
       - CM script: [get-gcc](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-gcc)
       - CM script: [app-stable-diffusion-pytorch-cuda-py](https://github.com/cknowledge/tests/tree/master/cm/script/app-stable-diffusion-pytorch-cuda-py)
       - CM script: [install-llvm-prebuilt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-llvm-prebuilt)
       - CM script: [app-image-classification-tvm-onnx-py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-tvm-onnx-py)
       - CM script: [flash-tinyml-binary](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/flash-tinyml-binary)
       - CM script: [app-mlperf-inference-nvidia](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-nvidia)
       - CM script: [reproduce-ieee-acm-micro2023-paper-28](https://github.com/ctuning/cm-reproduce-research-projects/tree/master/script/reproduce-ieee-acm-micro2023-paper-28)
       - CM script: [get-blis](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-blis)
       - CM script: [install-gflags](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-gflags)
       - CM script: [get-dataset-squad-vocab](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-squad-vocab)
       - CM script: [get-sys-utils-cm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
       - CM script: [reproduce-mlperf-octoml-tinyml-results](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-octoml-tinyml-results)
       - CM script: [print-hello-world-py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world-py)
       - CM script: [print-hello-world-java](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world-java)
       - CM script: [app-mlperf-training-reference](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-training-reference)
       - CM script: [install-mlperf-logging-from.src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-mlperf-logging-from.src)
       - CM script: [get-zephyr-sdk](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-zephyr-sdk)
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
       - CM script: [reproduce-ieee-acm-micro2023-paper-87](https://github.com/ctuning/cm-reproduce-research-projects/tree/master/script/reproduce-ieee-acm-micro2023-paper-87)
       - CM script: [get-ck](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ck)
       - CM script: [publish-results-to-dashboard](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/publish-results-to-dashboard)
       - CM script: [install-cmake-prebuilt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-cmake-prebuilt)
       - CM script: [get-ml-model-bert-base-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-base-squad)
       - CM script: [app-image-classification-onnx-py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-onnx-py)
       - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
       - CM script: [run-terraform](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-terraform)
       - CM script: [install-python-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-python-src)
       - CM script: [app-image-corner-detection-old](https://github.com/cknowledge/tests/tree/master/cm/script/app-image-corner-detection-old)
       - CM script: [get-mlperf-power-dev](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-power-dev)
       - CM script: [get-mlperf-training-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-training-src)
       - CM script: [get-dataset-librispeech](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-librispeech)
       - CM script: [get-ml-model-dlrm-terabyte](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-dlrm-terabyte)
       - CM script: [get-ml-model-abtf-ssd-pytorch](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-abtf-ssd-pytorch)
       - CM script: [app-mlperf-inference](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference)
       - CM script: [get-bazel](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-bazel)
       - CM script: [get-mlperf-inference-loadgen](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-loadgen)
       - CM script: [get-dataset-cifar10](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-cifar10)
       - CM script: [get-tvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm)
       - CM script: [detect-sudo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-sudo)
       - CM script: [get-preprocessed-dataset-criteo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-criteo)
       - CM script: [get-ml-model-llama2](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-llama2)
       - CM script: [get-dataset-openimages-annotations](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages-annotations)
       - CM script: [reproduce-ieee-acm-micro2023-paper-22](https://github.com/ctuning/cm-reproduce-research-projects/tree/master/script/reproduce-ieee-acm-micro2023-paper-22)
       - CM script: [get-ck-repo-mlops](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ck-repo-mlops)
       - CM script: [preprocess-mlperf-inference-submission](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/preprocess-mlperf-inference-submission)
       - CM script: [push-csv-to-spreadsheet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/push-csv-to-spreadsheet)
       - CM script: [get-lib-armnn](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-lib-armnn)
       - CM script: [get-qaic-software-kit](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-qaic-software-kit)
       - CM script: [get-dataset-coco2014](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-coco2014)
       - CM script: [run-mlperf-training-submission-checker](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-training-submission-checker)
       - CM script: [get-git-repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo)
       - CM script: [install-rocm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-rocm)
       - CM script: [reproduce-neurips-paper-2022-arxiv-2204.09656](https://github.com/ctuning/cm-reproduce-research-projects/tree/master/script/reproduce-neurips-paper-2022-arxiv-2204.09656)
       - CM script: [get-compiler-flags](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-compiler-flags)
       - CM script: [get-dataset-imagenet-calibration](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-calibration)
       - CM script: [get-lib-dnnl](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-lib-dnnl)
       - CM script: [get-dataset-imagenet-train](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-train)
       - CM script: [test-script5](https://github.com/gfursin/cm-tests/tree/master/script/test-script5)
       - CM script: [get-preprocessed-dataset-openorca](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-openorca)
       - CM script: [create-conda-env](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/create-conda-env)
       - CM script: [install-ipex-from.src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-ipex-from.src)
       - CM script: [install-onednn-from.src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-onednn-from.src)
       - CM script: [install-onnxruntime-from.src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-onnxruntime-from.src)
       - CM script: [install-transformers-from.src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-transformers-from.src)
</details>

___
### Script output
`cmr "generate submission mlperf mlperf-tiny tiny mlcommons tiny-submission mlperf-tiny-submission mlcommons-tiny-submission"  -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)