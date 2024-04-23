## Unified and cross-platform CM interface for DevOps, MLOps and MLPerf

[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE.md)
[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/cm/cmind)
[![Powered by CM](https://img.shields.io/badge/Powered_by-MLCommons%20CM-blue)](https://github.com/mlcommons/ck).
[![Downloads](https://static.pepy.tech/badge/cmind)](https://pepy.tech/project/cmind)

This repository contains reusable and cross-platform automation recipes to run DevOps, MLOps, AIOps and MLPerf 
via a simple and human-readable [Collective Mind interface (CM)](https://github.com/mlcommons/ck) 
while adapting to different opearting systems, software and hardware.

All СM scripts have a simple Python API, extensible JSON/YAML meta description
and unifed input/output to make them reusable in different projects either individually 
or by chaining them together into portable automation workflows, applications 
and web services adaptable to continuously changing models, data sets, software and hardware.

These automation recipes are being developed and maintained 
by the [MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)
with [great contributions](CONTRIBUTING.md) from the community.

## Tests

[![CM script automation test](https://github.com/mlcommons/cm4mlops/actions/workflows/test-cm-scripts.yml/badge.svg)](https://github.com/mlcommons/cm4mlops/actions/workflows/test-cm-scripts.yml)
[![CM script automation features test](https://github.com/mlcommons/cm4mlops/actions/workflows/test-cm-script-features.yml/badge.svg)](https://github.com/mlcommons/cm4mlops/actions/workflows/test-cm-script-features.yml)
[![MLPerf loadgen with HuggingFace bert onnx fp32 squad model](https://github.com/mlcommons/cm4mlops/actions/workflows/test-mlperf-loadgen-onnx-huggingface-bert-fp32-squad.yml/badge.svg)](https://github.com/mlcommons/cm4mlops/actions/workflows/test-mlperf-loadgen-onnx-huggingface-bert-fp32-squad.yml)
[![MLPerf inference MLCommons C++ ResNet50](https://github.com/mlcommons/cm4mlops/actions/workflows/test-mlperf-inference-mlcommons-cpp-resnet50.yml/badge.svg)](https://github.com/mlcommons/cm4mlops/actions/workflows/test-mlperf-inference-mlcommons-cpp-resnet50.yml)
[![image classification with ONNX](https://github.com/mlcommons/cm4mlops/actions/workflows/test-image-classification-onnx.yml/badge.svg)](https://github.com/mlcommons/cm4mlops/actions/workflows/test-image-classification-onnx.yml)


## Catalog

See the automatically generated catalog [online](https://access.cknowledge.org/playground/?action=scripts).

## License

[Apache 2.0](LICENSE.md)

## Copyright

2022-2024 [MLCommons](https://mlcommons.org)
