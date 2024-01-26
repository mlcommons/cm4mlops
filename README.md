[![PyPI version](https://badge.fury.io/py/cmind.svg)](https://pepy.tech/project/cmind)
[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/cm/cmind)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE.md)
[![Downloads](https://static.pepy.tech/badge/cmind)](https://pepy.tech/project/cmind)

[![CM test](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml)
[![CM script automation features test](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml)
[![Dockerfile update for CM scripts](https://github.com/mlcommons/ck/actions/workflows/update-script-dockerfiles.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/update-script-dockerfiles.yml)

### About

[Collective Mind (CM)](https://github.com/mlcommons/ck) is a human-friendly interface
to run a growing number of ad-hoc MLPerf, MLOps, and DevOps scripts
in a unified way on any operating system with any software and hardware 
as [portable and reusable automation recipes (CM scripts)](https://github.com/mlcommons/ck/tree/master/cm-mlops/script):

```bash
pip install cmind

cm pull repo mlcommons@ck

cm run script "python app image-classification onnx"

cm run script "download file _wget" --url=https://cKnowledge.org/ai/data/computer_mouse.jpg --verify=no --env.CM_DOWNLOAD_CHECKSUM=45ae5c940233892c2f860efdf0b66e7e

cm run script "python app image-classification onnx" --input=computer_mouse.jpg

cm docker script "python app image-classification onnx" --input=computer_mouse.jpg
cm docker script "python app image-classification onnx" --input=computer_mouse.jpg -j -docker_it

cm run script "get generic-python-lib _package.onnxruntime"
cm run script "get coco dataset _val _2014"
cm run script "get ml-model stable-diffusion"
cm run script "get ml-model huggingface zoo _model-stub.alpindale/Llama-2-13b-ONNX" --model_filename=FP32/LlamaV2_13B_float32.onnx --skip_cache

cm show cache
cm show cache "get ml-model stable-diffusion"

cm run script "run common mlperf inference" --implementation=nvidia --model=bert-99 --category=datacenter --division=closed
cm find script "run common mlperf inference"

cm pull repo ctuning@cm-reproduce-research-projects
cmr "reproduce paper micro-2023 victima _install_deps"
cmr "reproduce paper micro-2023 victima _run" 

...

```

Collective Mind is a community project being developed by the [MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)
with great help from [MLCommons (70+ AI organizations)](https://mlcommons.org/),
[research community]( https://www.youtube.com/watch?v=7zpeIVwICa4 )
and [individual contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md) -
we want to have a common, non-intrusive, technology-agnostic, portable and easily-extensible interface 
that requires minimal learning curve to start automating all manual and repetitive tasks including 
downloading artifacts, installing tools, resolving dependencies, 
running experiments, processing logs, and reproducing results.

That is why we implemented CM as a [small Python library](https://github.com/mlcommons/ck/tree/master/cm) 
with minimal dependencies (Python 3.7+, git, wget), simple Python API and human-friendly command line
that simply searches for CM scripts by tags in all pulled Git repositories, automatically generates command lines 
for a given script or tool on a given platform, updates all paths and environment variables, 
runs a given automation either natively or inside automatically-generated containers
and unifies input and output as a Python dictionary or JSON/YAML file.

Our goal is to make it easier to prototype, build, run, benchmark and optimize complex AI/ML applications
across diverse and rapidly evolving models, data sets, software and hardware simply by chaining these 
unified CM scripts into [portable, human-readable and reusable workflows](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-image-classification-onnx-py/_cm.yaml).

Please check this [Getting Started tutorial](docs/getting-started.md) 
to understand how CM works and start using it.

Feel free to join [public Discord server](https://discord.gg/JjWNWXKxwT) 
if you would like to participate in collaborative developments
or have questions and suggestions.

### Documentation

* [Getting Started tutorial](docs/getting-started.md)
  * [CM interface for MLPerf benchmarks](docs/mlperf)
  * [CM interface for ML and Systems conferences](docs/tutorials/common-interface-to-reproduce-research-projects.md)
  * [CM automation recipes for MLOps and DevOps](cm-mlops/script)
  * [Other CM tutorials](docs/tutorials)
* [Full documentation](docs/README.md)
* [CM and CK history](docs/history.md)

### Motivation and concepts

* ACM REP'23 keynote about MLCommons CM: [slides](https://doi.org/10.5281/zenodo.8105339)
* ACM TechTalk'21 about automating research projects: [YouTube](https://www.youtube.com/watch?v=7zpeIVwICa4)
* MLPerf inference submitter orientation: [slides](https://doi.org/10.5281/zenodo.8144274) 

### Copyright

2022-2024 [MLCommons](https://mlcommons.org)

### License

[Apache 2.0](LICENSE.md)
