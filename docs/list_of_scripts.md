[ [Back to index](README.md) ]

<!--
This file is generated automatically - don't edit!
-->

This is an automatically generated list of reusable CM scripts being developed
by the [open taskforce on automation and reproducibility](https://github.com/mlcommons/ck/issues/536) 
to make MLOps and DevOps tools more interoperable, portable, deterministic and reproducible.
These scripts suppport the community effort to modularize ML Systems and automate their bechmarking, optimization,
design space exploration and deployment across continuously changing software and hardware. 

# List of CM scripts by categories

<details>
<summary>Click here to see the table of contents.</summary>

* [Application automation](#application-automation)
* [CUDA automation](#cuda-automation)
* [Cloud automation](#cloud-automation)
* [Compiler automation](#compiler-automation)
* [Dashboards](#dashboards)
* [Detection or installation of tools and artifacts](#detection-or-installation-of-tools-and-artifacts)
* [Docker automation](#docker-automation)
* [GUI](#gui)
* [Legacy CK support](#legacy-ck-support)
* [ML/AI datasets](#mlai-datasets)
* [ML/AI frameworks](#mlai-frameworks)
* [ML/AI models](#mlai-models)
* [Misc automation](#misc-automation)
* [Modular ML/AI applications](#modular-mlai-applications)
* [Modular MLPerf benchmarks](#modular-mlperf-benchmarks)
* [Modular applications](#modular-applications)
* [Platform information](#platform-information)
* [Python automation](#python-automation)
* [Remote automation](#remote-automation)
* [Reproduced papers](#reproduced-papers)
* [Reproducible papers](#reproducible-papers)
* [Tests](#tests)
* [TinyML automation](#tinyml-automation)


</details>

### GUI

* [gui](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/gui)

### Modular MLPerf benchmarks

* [add-custom-nvidia-system](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/add-custom-nvidia-system)
* [app-loadgen-generic-python](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-loadgen-generic-python)
* [app-mlperf-inference](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference)
* [app-mlperf-inference-cpp](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-cpp)
* [app-mlperf-inference-nvidia](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-nvidia)
* [app-mlperf-inference-reference](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-reference)
* [app-mlperf-inference-tflite-cpp](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-tflite-cpp)
* [build-mlperf-inference-server-nvidia](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-mlperf-inference-server-nvidia)
* [generate-mlperf-inference-submission](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-submission)
* [generate-mlperf-inference-user-conf](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-user-conf)
* [generate-mlperf-tiny-submission](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-tiny-submission)
* [generate-nvidia-engine](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-nvidia-engine)
* [get-dataset-kits19](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-kits19)
* [get-git-repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo)
* [get-mlperf-inference-loadgen](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-loadgen)
* [get-mlperf-inference-results](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-results)
* [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
* [get-mlperf-inference-sut-configs](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-configs)
* [get-mlperf-inference-sut-description](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-description)
* [get-mlperf-power-dev](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-power-dev)
* [get-mlperf-training-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-training-src)
* [get-spec-ptd](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-spec-ptd)
* [import-mlperf-inference-to-experiment](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/import-mlperf-inference-to-experiment)
* [import-mlperf-tiny-to-experiment](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/import-mlperf-tiny-to-experiment)
* [process-mlperf-accuracy](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/process-mlperf-accuracy)
* [push-mlperf-inference-results-to-github](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/push-mlperf-inference-results-to-github)
* [reproduce-mlperf-inference-nvidia](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-nvidia)
* [reproduce-mlperf-octoml-tinyml-results](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-octoml-tinyml-results)
* [run-mlperf-inference-app](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-app)
* [run-mlperf-inference-submission-checker](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-submission-checker)
* [run-mlperf-power-client](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-power-client)
* [run-mlperf-power-server](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-power-server)
* [test-mlperf-inference-retinanet-win](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-mlperf-inference-retinanet-win)
* [truncate-mlperf-inference-accuracy-log](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/truncate-mlperf-inference-accuracy-log)
* [wrapper-reproduce-octoml-tinyml-submission](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/wrapper-reproduce-octoml-tinyml-submission)

### Modular ML/AI applications

* [app-image-classification-onnx-py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-onnx-py)
* [app-image-classification-tf-onnx-cpp](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-tf-onnx-cpp)
* [app-image-classification-torch-py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-torch-py)
* [app-image-classification-tvm-onnx-py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-tvm-onnx-py)

### Modular applications

* [app-image-corner-detection](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-corner-detection)

### ML/AI datasets

* [get-dataset-criteo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-criteo)
* [get-dataset-imagenet-aux](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-aux)
* [get-dataset-imagenet-helper](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-helper)
* [get-dataset-imagenet-val](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val)
* [get-dataset-librispeech](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-librispeech)
* [get-dataset-openimages](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages)
* [get-dataset-openimages-annotations](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages-annotations)
* [get-dataset-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-squad)
* [get-dataset-squad-vocab](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-squad-vocab)
* [get-preprocessed-dataset-criteo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-criteo)
* [get-preprocessed-dataset-imagenet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet)
* [get-preprocessed-dataset-kits19](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-kits19)
* [get-preprocessed-dataset-librispeech](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-librispeech)
* [get-preprocessed-dataset-openimages](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-openimages)
* [get-preprocesser-script-generic](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocesser-script-generic)

### ML/AI models

* [convert-ml-model-huggingface-to-onnx](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/convert-ml-model-huggingface-to-onnx)
* [get-dlrm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dlrm)
* [get-ml-model-3d-unet-kits19](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-3d-unet-kits19)
* [get-ml-model-bert-base-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-base-squad)
* [get-ml-model-bert-large-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-large-squad)
* [get-ml-model-dlrm-terabyte](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-dlrm-terabyte)
* [get-ml-model-efficientnet-lite](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-efficientnet-lite)
* [get-ml-model-huggingface-zoo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-huggingface-zoo)
* [get-ml-model-mobilenet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-mobilenet)
* [get-ml-model-neuralmagic-zoo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-neuralmagic-zoo)
* [get-ml-model-resnet50](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50)
* [get-ml-model-resnet50-tvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50-tvm)
* [get-ml-model-retinanet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-retinanet)
* [get-ml-model-retinanet-nvidia](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-retinanet-nvidia)
* [get-ml-model-rnnt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-rnnt)
* [get-ml-model-using-imagenet-from-model-zoo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-using-imagenet-from-model-zoo)

### ML/AI frameworks

* [get-onnxruntime-prebuilt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-onnxruntime-prebuilt)
* [get-tvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm)
* [install-tensorflow-for-c](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-tensorflow-for-c)
* [install-tensorflow-from-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-tensorflow-from-src)
* [install-tflite-from-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-tflite-from-src)

### Platform information

* [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
* [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)

### Compiler automation

* [get-cl](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cl) *(Detect or install Microsoft C compiler)*
* [get-compiler-flags](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-compiler-flags)
* [get-gcc](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-gcc) *(Detect or install GCC compiler)*
* [get-go](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-go)
* [get-llvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-llvm) *(Detect or install LLVM compiler)*
* [install-gcc-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-gcc-src)
* [install-llvm-prebuilt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-llvm-prebuilt) *(Install prebuilt LLVM compiler)*
* [install-llvm-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-llvm-src) *(Build LLVM compiler from sources (can take >30 min))*

### Detection or installation of tools and artifacts

* [get-android-sdk](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-android-sdk)
* [get-bazel](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-bazel)
* [get-cmake](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cmake)
* [get-cmsis_5](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cmsis_5)
* [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
* [get-java](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-java)
* [get-javac](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-javac)
* [get-lib-armnn](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-lib-armnn)
* [get-lib-dnnl](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-lib-dnnl)
* [get-openssl](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-openssl)
* [get-sys-utils-cm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
* [get-sys-utils-min](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-min)
* [install-bazel](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-bazel)
* [install-cmake-prebuilt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-cmake-prebuilt)
* [install-gflags](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-gflags)
* [install-github-cli](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-github-cli)
* [install-openssl](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-openssl)

### Cloud automation

* [destroy-terraform](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/destroy-terraform)
* [get-aws-cli](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-aws-cli)
* [get-rclone](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-rclone)
* [get-terraform](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-terraform)
* [install-aws-cli](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-aws-cli)
* [install-terraform-from-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-terraform-from-src)
* [run-terraform](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-terraform)

### TinyML automation

* [flash-tinyml-binary](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/flash-tinyml-binary)
* [get-microtvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-microtvm)
* [get-zephyr](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-zephyr)
* [get-zephyr-sdk](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-zephyr-sdk)

### CUDA automation

* [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
* [get-cuda-devices](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda-devices)
* [get-cudnn](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cudnn)
* [get-tensorrt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tensorrt)
* [install-cuda-package-manager](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-cuda-package-manager)
* [install-cuda-prebuilt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-cuda-prebuilt)

### Docker automation

* [build-docker-image](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-docker-image)
* [build-dockerfile](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-dockerfile)
* [run-docker-container](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-docker-container)

### Remote automation

* [remote-run-commands](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/remote-run-commands)

### Misc automation

* [get-github-cli](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-github-cli)
* [push-csv-to-spreadsheet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/push-csv-to-spreadsheet)
* [set-echo-off-win](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/set-echo-off-win)
* [tar-my-folder](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/tar-my-folder)

### Application automation

* [benchmark-program](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/benchmark-program)
* [compile-program](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-program)

### Dashboards

* [publish-results-to-dashboard](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/publish-results-to-dashboard)

### Python automation

* [activate-python-venv](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/activate-python-venv) *(Activate virtual Python environment)*
* [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
* [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
* [install-python-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-python-src)
* [install-python-venv](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-python-venv)

### Legacy CK support

* [get-ck](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ck)
* [get-ck-repo-mlops](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ck-repo-mlops)

### Tests

* [print-hello-world](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world)
* [print-hello-world-java](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world-java)
* [print-hello-world-json](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world-json)
* [print-hello-world-py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world-py)
* [print-python-version](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-python-version)
* [test-set-sys-user-cm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-set-sys-user-cm)

### Reproduced papers

* [app-ipol-reproducibility-2022-439](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-ipol-reproducibility-2022-439)

### Reproducible papers

* [get-ipol-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ipol-src)


# List of all sorted CM scripts 

* [activate-python-venv](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/activate-python-venv) *(Activate virtual Python environment)*
* [add-custom-nvidia-system](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/add-custom-nvidia-system)
* [app-image-classification-onnx-py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-onnx-py)
* [app-image-classification-tf-onnx-cpp](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-tf-onnx-cpp)
* [app-image-classification-torch-py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-torch-py)
* [app-image-classification-tvm-onnx-py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-tvm-onnx-py)
* [app-image-corner-detection](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-corner-detection)
* [app-ipol-reproducibility-2022-439](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-ipol-reproducibility-2022-439)
* [app-loadgen-generic-python](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-loadgen-generic-python)
* [app-mlperf-inference](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference)
* [app-mlperf-inference-cpp](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-cpp)
* [app-mlperf-inference-nvidia](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-nvidia)
* [app-mlperf-inference-reference](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-reference)
* [app-mlperf-inference-tflite-cpp](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-tflite-cpp)
* [benchmark-program](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/benchmark-program)
* [build-docker-image](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-docker-image)
* [build-dockerfile](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-dockerfile)
* [build-mlperf-inference-server-nvidia](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-mlperf-inference-server-nvidia)
* [compile-program](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-program)
* [convert-ml-model-huggingface-to-onnx](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/convert-ml-model-huggingface-to-onnx)
* [destroy-terraform](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/destroy-terraform)
* [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
* [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
* [download-and-extract](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-and-extract)
* [download-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-file)
* [download-torrent](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-torrent)
* [extract-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/extract-file)
* [flash-tinyml-binary](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/flash-tinyml-binary)
* [generate-mlperf-inference-submission](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-submission)
* [generate-mlperf-inference-user-conf](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-user-conf)
* [generate-mlperf-tiny-submission](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-tiny-submission)
* [generate-nvidia-engine](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-nvidia-engine)
* [get-android-sdk](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-android-sdk)
* [get-aocl](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-aocl)
* [get-aws-cli](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-aws-cli)
* [get-bazel](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-bazel)
* [get-blis](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-blis)
* [get-brew](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-brew)
* [get-ck](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ck)
* [get-ck-repo-mlops](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ck-repo-mlops)
* [get-cl](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cl) *(Detect or install Microsoft C compiler)*
* [get-cmake](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cmake)
* [get-cmsis_5](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cmsis_5)
* [get-compiler-flags](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-compiler-flags)
* [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
* [get-cuda-devices](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda-devices)
* [get-cudnn](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cudnn)
* [get-dataset-criteo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-criteo)
* [get-dataset-imagenet-aux](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-aux)
* [get-dataset-imagenet-helper](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-helper)
* [get-dataset-imagenet-train](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-train)
* [get-dataset-imagenet-val](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val)
* [get-dataset-kits19](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-kits19)
* [get-dataset-librispeech](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-librispeech)
* [get-dataset-openimages](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages)
* [get-dataset-openimages-annotations](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages-annotations)
* [get-dataset-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-squad)
* [get-dataset-squad-vocab](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-squad-vocab)
* [get-dlrm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dlrm)
* [get-gcc](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-gcc) *(Detect or install GCC compiler)*
* [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
* [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
* [get-git-repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo)
* [get-github-cli](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-github-cli)
* [get-go](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-go)
* [get-google-test](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-google-test)
* [get-ipol-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ipol-src)
* [get-java](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-java)
* [get-javac](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-javac)
* [get-lib-armnn](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-lib-armnn)
* [get-lib-dnnl](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-lib-dnnl)
* [get-llvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-llvm) *(Detect or install LLVM compiler)*
* [get-microtvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-microtvm)
* [get-ml-model-3d-unet-kits19](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-3d-unet-kits19)
* [get-ml-model-bert-base-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-base-squad)
* [get-ml-model-bert-large-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-large-squad)
* [get-ml-model-dlrm-terabyte](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-dlrm-terabyte)
* [get-ml-model-efficientnet-lite](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-efficientnet-lite)
* [get-ml-model-huggingface-zoo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-huggingface-zoo)
* [get-ml-model-mobilenet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-mobilenet)
* [get-ml-model-neuralmagic-zoo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-neuralmagic-zoo)
* [get-ml-model-resnet50](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50)
* [get-ml-model-resnet50-tvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50-tvm)
* [get-ml-model-retinanet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-retinanet)
* [get-ml-model-retinanet-nvidia](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-retinanet-nvidia)
* [get-ml-model-rnnt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-rnnt)
* [get-ml-model-using-imagenet-from-model-zoo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-using-imagenet-from-model-zoo)
* [get-mlperf-inference-loadgen](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-loadgen)
* [get-mlperf-inference-nvidia-common-code](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-nvidia-common-code)
* [get-mlperf-inference-results](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-results)
* [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
* [get-mlperf-inference-sut-configs](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-configs)
* [get-mlperf-inference-sut-description](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-description)
* [get-mlperf-power-dev](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-power-dev)
* [get-mlperf-training-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-training-src)
* [get-onnxruntime-prebuilt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-onnxruntime-prebuilt)
* [get-openssl](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-openssl)
* [get-preprocessed-dataset-criteo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-criteo)
* [get-preprocessed-dataset-imagenet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet)
* [get-preprocessed-dataset-kits19](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-kits19)
* [get-preprocessed-dataset-librispeech](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-librispeech)
* [get-preprocessed-dataset-openimages](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-openimages)
* [get-preprocesser-script-generic](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocesser-script-generic)
* [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
* [get-qaic-compute-sdk](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-qaic-compute-sdk)
* [get-qaic-software-kit](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-qaic-software-kit)
* [get-rclone](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-rclone)
* [get-spec-ptd](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-spec-ptd)
* [get-sys-utils-cm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
* [get-sys-utils-min](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-min)
* [get-tensorrt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tensorrt)
* [get-terraform](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-terraform)
* [get-tvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm)
* [get-zendnn](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-zendnn)
* [get-zephyr](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-zephyr)
* [get-zephyr-sdk](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-zephyr-sdk)
* [gui](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/gui)
* [import-mlperf-inference-to-experiment](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/import-mlperf-inference-to-experiment)
* [import-mlperf-tiny-to-experiment](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/import-mlperf-tiny-to-experiment)
* [install-aws-cli](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-aws-cli)
* [install-bazel](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-bazel)
* [install-cmake-prebuilt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-cmake-prebuilt)
* [install-cuda-package-manager](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-cuda-package-manager)
* [install-cuda-prebuilt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-cuda-prebuilt)
* [install-gcc-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-gcc-src)
* [install-gflags](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-gflags)
* [install-github-cli](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-github-cli)
* [install-llvm-prebuilt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-llvm-prebuilt) *(Install prebuilt LLVM compiler)*
* [install-llvm-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-llvm-src) *(Build LLVM compiler from sources (can take >30 min))*
* [install-openssl](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-openssl)
* [install-python-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-python-src)
* [install-python-venv](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-python-venv)
* [install-tensorflow-for-c](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-tensorflow-for-c)
* [install-tensorflow-from-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-tensorflow-from-src)
* [install-terraform-from-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-terraform-from-src)
* [install-tflite-from-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-tflite-from-src)
* [print-hello-world](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world)
* [print-hello-world-java](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world-java)
* [print-hello-world-json](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world-json)
* [print-hello-world-py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world-py)
* [print-python-version](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-python-version)
* [process-mlperf-accuracy](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/process-mlperf-accuracy)
* [publish-results-to-dashboard](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/publish-results-to-dashboard)
* [push-csv-to-spreadsheet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/push-csv-to-spreadsheet)
* [push-mlperf-inference-results-to-github](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/push-mlperf-inference-results-to-github)
* [remote-run-commands](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/remote-run-commands)
* [reproduce-mlperf-inference-nvidia](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-nvidia)
* [reproduce-mlperf-octoml-tinyml-results](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-octoml-tinyml-results)
* [run-docker-container](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-docker-container)
* [run-mlperf-inference-app](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-app)
* [run-mlperf-inference-mobilenet-models](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-mobilenet-models)
* [run-mlperf-inference-submission-checker](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-submission-checker)
* [run-mlperf-power-client](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-power-client)
* [run-mlperf-power-server](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-power-server)
* [run-terraform](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-terraform)
* [set-echo-off-win](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/set-echo-off-win)
* [tar-my-folder](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/tar-my-folder)
* [test-mlperf-inference-retinanet-win](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-mlperf-inference-retinanet-win)
* [test-set-sys-user-cm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-set-sys-user-cm)
* [truncate-mlperf-inference-accuracy-log](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/truncate-mlperf-inference-accuracy-log)
* [wrapper-reproduce-octoml-tinyml-submission](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/wrapper-reproduce-octoml-tinyml-submission)




# Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)'
