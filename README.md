## Unified and cross-platform CM interface for DevOps, MLOps and MLPerf

[![arXiv](https://img.shields.io/badge/arXiv-2406.16791-b31b1b.svg)](https://arxiv.org/abs/2406.16791)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE.md)
[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/cm/cmind)
[![Powered by CM](https://img.shields.io/badge/Powered_by-MLCommons%20CM-blue)](https://github.com/mlcommons/ck).
[![Downloads](https://static.pepy.tech/badge/cm4mlops)](https://pepy.tech/project/cm4mlops)

[![CM script automation test](https://github.com/mlcommons/cm4mlops/actions/workflows/test-cm-scripts.yml/badge.svg)](https://github.com/mlcommons/cm4mlops/actions/workflows/test-cm-scripts.yml)
[![CM script automation features test](https://github.com/mlcommons/cm4mlops/actions/workflows/test-cm-script-features.yml/badge.svg)](https://github.com/mlcommons/cm4mlops/actions/workflows/test-cm-script-features.yml)
[![MLPerf inference MLCommons C++ ResNet50](https://github.com/mlcommons/cm4mlops/actions/workflows/test-mlperf-inference-mlcommons-cpp-resnet50.yml/badge.svg)](https://github.com/mlcommons/cm4mlops/actions/workflows/test-mlperf-inference-mlcommons-cpp-resnet50.yml)

This repository contains reusable and cross-platform automation recipes to run DevOps, MLOps, and MLPerf 
via a simple and human-readable [Collective Mind interface (CM)](https://github.com/mlcommons/ck) 
while adapting to different operating systems, software and hardware.

All СM scripts have a simple Python API, extensible JSON/YAML meta description
and unified input/output to make them reusable in different projects either individually 
or by chaining them together into portable automation workflows, applications 
and web services adaptable to continuously changing models, data sets, software and hardware.

We develop and test [CM scripts](script) as a community effort to support the following projects:
* [CM for MLPerf](https://docs.mlcommons.org/inference): modularize and automate MLPerf benchmarks 
  * [Modular C++ harness for MLPerf loadgen](https://github.com/mlcommons/cm4mlops/tree/main/script/app-mlperf-inference-mlcommons-cpp)
  * [Modular Python harness for MLPerf loadgen](https://github.com/mlcommons/cm4mlops/tree/main/script/app-loadgen-generic-python)
* [CM for research and education](https://cTuning.org/ae): provide a common interface to automate and reproduce results from research papers 
  and MLPerf benchmarks;
* [CM for ABTF](https://github.com/mlcommons/cm4abtf): provide a unified CM interface to run automotive benchmarks;
* [CM for optimization](https://access.cknowledge.org/playground/?action=challenges): co-design efficient and cost-effective 
  software and hardware for AI, ML and other emerging workloads via open challenges. 

You can read this [ArXiv paper](https://arxiv.org/abs/2406.16791) to learn more about the CM motivation and long-term vision.

Please provide your feedback or submit your issues [here](https://github.com/mlcommons/cm4mlops/issues).


## Catalog

Online catalog: [cKnowledge](https://access.cknowledge.org/playground/?action=scripts), [MLCommons](https://docs.mlcommons.org/cm4mlops/scripts).

## Citation

Please use this [BibTeX file](https://github.com/mlcommons/ck/blob/master/citation.bib) to cite this project.

## A few demos

### Install CM and virtual env

Install the [MLCommons CM automation language](https://access.cknowledge.org/playground/?action=install).

### Pull this repository

```bash
cm pull repo mlcommons@cm4mlops --branch=dev
```

### Run image classification using CM

```bash

cm run script "python app image-classification onnx _cpu" --help

cm run script "download file _wget" --url=https://cKnowledge.org/ai/data/computer_mouse.jpg --verify=no --env.CM_DOWNLOAD_CHECKSUM=45ae5c940233892c2f860efdf0b66e7e
cm run script "python app image-classification onnx _cpu" --input=computer_mouse.jpg

cmr "python app image-classification onnx _cpu" --input=computer_mouse.jpg
cmr --tags=python,app,image-classification,onnx,_cpu --input=computer_mouse.jpg
cmr 3d5e908e472b417e --input=computer_mouse.jpg

cm docker script "python app image-classification onnx _cpu" --input=computer_mouse.jpg

cm gui script "python app image-classification onnx _cpu"
```

### Re-run experiments from the ACM/IEEE MICRO'23 paper

Check this [script/reproduce-ieee-acm-micro2023-paper-96](README.md).

### Run MLPerf ResNet CPU inference benchmark via CM

```bash
cm run script --tags=run-mlperf,inference,_performance-only,_short  \
   --division=open \
   --category=edge \
   --device=cpu \
   --model=resnet50 \
   --precision=float32 \
   --implementation=mlcommons-python \
   --backend=onnxruntime \
   --scenario=Offline \
   --execution_mode=test \
   --power=no \
   --adr.python.version_min=3.8 \
   --clean \
   --compliance=no \
   --quiet \
   --time
```

### Run MLPerf BERT CUDA inference benchmark v4.1 via CM

```bash
cmr "run-mlperf inference _find-performance _full _r4.1" \
   --model=bert-99 \
   --implementation=nvidia \
   --framework=tensorrt \
   --category=datacenter \
   --scenario=Offline \
   --execution_mode=test \
   --device=cuda  \
   --docker \
   --docker_cm_repo=mlcommons@cm4mlops \
   --docker_cm_repo_flags="--branch=mlperf-inference" \
   --test_query_count=100 \
   --quiet
```

### Run MLPerf SDXL reference inference benchmark v4.1 via CM

```bash
cm run script \
	--tags=run-mlperf,inference,_r4.1 \
	--model=sdxl \
	--implementation=reference \
	--framework=pytorch \
	--category=datacenter \
	--scenario=Offline \
	--execution_mode=valid \
	--device=cuda \
	--quiet
```


## License

[Apache 2.0](LICENSE.md)

## Authors

[Grigori Fursin](https://cKnowledge.org/gfursin) and [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh)

## Funding

We thank [cKnowledge.org](https://cKnowledge.org), [cTuning foundation](https://cTuning.org)
and [MLCommons](https://mlcommons.org) for sponsoring this project!

## Acknowledgments

We thank all [volunteers, collaborators and contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md) 
for their support, fruitful discussions, and useful feedback! 
