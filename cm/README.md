[![PyPI version](https://badge.fury.io/py/cmind.svg)](https://pepy.tech/project/cmind)
[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/cm/cmind)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE.md)
[![Downloads](https://static.pepy.tech/badge/cmind)](https://pepy.tech/project/cmind)

[![CM test](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml)
[![CM script automation features test](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml)
[![Dockerfile update for CM scripts](https://github.com/mlcommons/ck/actions/workflows/update-script-dockerfiles.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/update-script-dockerfiles.yml)

### About

Collective Mind (CM) is a [collection of portable, extensible, technology-agnostic and ready-to-use automation recipes
with a human-friendly interface (aka CM scripts)](https://access.cknowledge.org/playground/?action=scripts)
to automate all the manual steps required to compose, run, benchmark and optimize complex ML/AI applications 
on any platform with any software and hardware. 
They require Python 3.7+ with minimal dependencies and can run natively on Ubuntu, MacOS, Windows, RHEL, Debian, Amazon Linux
and any other operating system, in a cloud or inside automatically generated containers.
Furthermore, CM scripts are [continuously extended by the community](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md)
to encode new knowledge and best practices about AI systems while keeping backward compatibility!

CM scripts were originally developed based on the following requirements from the
[MLCommons engineers and researchers](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md) 
to help them automatically build, benchmark and optimize complex MLPerf benchmarks
across diverse and continuously changing models, data sets, software and hardware
from Nvidia, Intel, AMD, Google, Qualcomm, Amazon and other vendors:
* must work out of the box with the default options and without the need to edit some paths, environment variables and configuration files;
* must be non-intrusive, easy to debug and must reuse existing 
  user scripts and automation tools (such as cmake, make, ML workflows, 
  python poetry and containers) rather than substituting them; 
* must have a very simple and human-friendly command line with a Python API and minimal dependencies;
* must require minimal or zero learning curve by using plain Python, native scripts, environment variables 
  and simple JSON/YAML descriptions instead of inventing new workflow languages;
* must have the same interface to run all automations natively, in a cloud or inside containers.

Below you can find and try a few examples of the most-commonly used [automation recipes](https://access.cknowledge.org/playground/?action=scripts)
that can be chained into more complex automation workflows [using simple JSON or YAML](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-image-classification-onnx-py/_cm.yaml).

*Note that MLCommons CM is a collaborative engineering effort to gradually improve portability and functionality
across continuously changing models, data sets, software and hardware based on your feedback -
please check this [installation guide](installation.md), report  encountered issues [here](https://github.com/mlcommons/ck/issues) 
and contact us via [public Discord Server](https://discord.gg/JjWNWXKxwT) to help this community effort!*


#### CM human-friendly command line


```bash
pip install cmind

cm pull repo mlcommons@ck

cm run script "python app image-classification onnx"
cmr "python app image-classification onnx"

cmr "download file _wget" --url=https://cKnowledge.org/ai/data/computer_mouse.jpg --verify=no --env.CM_DOWNLOAD_CHECKSUM=45ae5c940233892c2f860efdf0b66e7e
cmr "python app image-classification onnx" --input=computer_mouse.jpg
cmr "python app image-classification onnx" --input=computer_mouse.jpg --debug

cm find script "python app image-classification onnx"
cm load script "python app image-classification onnx" --yaml

cmr "get python" --version_min=3.8.0 --name=mlperf-experiments
cmr "install python-venv" --version_max=3.10.11 --name=mlperf

cmr "get ml-model stable-diffusion"
cmr "get ml-model huggingface zoo _model-stub.alpindale/Llama-2-13b-ONNX" --model_filename=FP32/LlamaV2_13B_float32.onnx --skip_cache
cmr "get dataset coco _val _2014"
cmr "get dataset openimages" -j

cm show cache
cm show cache "get ml-model stable-diffusion"

cmr "get generic-python-lib _package.onnxruntime" --version_min=1.16.0
cmr "python app image-classification onnx" --input=computer_mouse.jpg

cmr "python app image-classification onnx" --input=computer_mouse.jpg --debug

cm rm cache -f
cmr "python app image-classification onnx" --input=computer_mouse.jpg --adr.onnxruntime.version_max=1.16.0


cmr "get cuda" --version_min=12.0.0 --version_max=12.3.1
cmr "python app image-classification onnx _cuda" --input=computer_mouse.jpg

cm gui script "python app image-classification onnx"

cm docker script "python app image-classification onnx" --input=computer_mouse.jpg
cm docker script "python app image-classification onnx" --input=computer_mouse.jpg -j -docker_it

cm docker script "get coco dataset _val _2017" --to=d:\Downloads\COCO-2017-val --store=d:\Downloads --docker_cm_repo=ctuning@mlcommons-ck

cmr "run common mlperf inference" --implementation=nvidia --model=bert-99 --category=datacenter --division=closed
cm find script "run common mlperf inference"

cmr "get generic-python-lib _package.torch" --version=2.1.2
cmr "get generic-python-lib _package.torchvision" --version=0.16.2
cmr "python app image-classification torch" --input=computer_mouse.jpg

cm rm repo mlcommons@ck
cm pull repo --url=https://zenodo.org/records/10581696/files/cm-mlops-repo-20240129.zip

cmr "install llvm prebuilt" --version=17.0.6
cmr "app image corner-detection"

cm run experiment --tags=tuning,experiment,batch_size -- echo --batch_size={{VAR1{range(1,8)}}}
cm replay experiment --tags=tuning,experiment,batch_size

cmr "get conda"

cm pull repo ctuning@cm-reproduce-research-projects
cmr "reproduce paper micro-2023 victima _install_deps"
cmr "reproduce paper micro-2023 victima _run" 

```


#### CM unified Python API


```python
import cmind
output=cmind.access({'action':'run', 'automation':'script',
                     'tags':'python,app,image-classification,onnx',
                     'input':'computer_mouse.jpg'})
if output['return']==0: print (output)
```


#### Examples of modular containers and GitHub actions with CM commands

<small>

* https://github.com/mlcommons/inference/blob/master/.github/workflows/test-bert.yml
* https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-mlperf-inference/dockerfiles/bert-99.9/ubuntu_22.04_python_onnxruntime_cpu.Dockerfile

</small>


[CM scripts](https://access.cknowledge.org/playground/?action=scripts) 
were successfully used to [modularize MLPerf inference benchmarks](https://github.com/mlcommons/ck/blob/master/docs/mlperf/inference/README.md) 
and help the community automate more than 95% of all performance and power submissions in the v3.1 round
across more than 120 system configurations (models, frameworks, hardware) 
while reducing development and maintenance costs.

Besides automating MLCommons projects, the community also started started using 
and extending [CM scripts](https://access.cknowledge.org/playground/?action=scripts) 
to modularize, run and benchmark other software projects and make it
easier to rerun, reproduce and reuse [research projects from published papers 
at Systems and ML conferences]( https://cTuning.org/ae/micro2023.html ).

Please check the [**Getting Started Guide**](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md) 
to understand how CM automation recipes work, how to use them to automate your own projects,
and how to implement and share new automations in your public or private projects.


### License

[Apache 2.0](LICENSE.md)

### Copyright

2022-2024 [MLCommons](https://mlcommons.org)
