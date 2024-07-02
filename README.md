## Unified and cross-platform CM interface for DevOps, MLOps and MLPerf

[![arXiv](https://img.shields.io/badge/arXiv-2406.16791-b31b1b.svg)](https://arxiv.org/abs/2406.16791)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE.md)
[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/cm/cmind)
[![Powered by CM](https://img.shields.io/badge/Powered_by-MLCommons%20CM-blue)](https://github.com/mlcommons/ck).
[![Downloads](https://static.pepy.tech/badge/cmind)](https://pepy.tech/project/cmind)

[![CM script automation test](https://github.com/mlcommons/cm4mlops/actions/workflows/test-cm-scripts.yml/badge.svg)](https://github.com/mlcommons/cm4mlops/actions/workflows/test-cm-scripts.yml)
[![CM script automation features test](https://github.com/mlcommons/cm4mlops/actions/workflows/test-cm-script-features.yml/badge.svg)](https://github.com/mlcommons/cm4mlops/actions/workflows/test-cm-script-features.yml)
[![MLPerf inference MLCommons C++ ResNet50](https://github.com/mlcommons/cm4mlops/actions/workflows/test-mlperf-inference-mlcommons-cpp-resnet50.yml/badge.svg)](https://github.com/mlcommons/cm4mlops/actions/workflows/test-mlperf-inference-mlcommons-cpp-resnet50.yml)

This repository contains reusable and cross-platform automation recipes to run DevOps, MLOps, AIOps and MLPerf 
via a simple and human-readable [Collective Mind interface (CM)](https://github.com/mlcommons/ck) 
while adapting to different operating systems, software and hardware.

All СM scripts have a simple Python API, extensible JSON/YAML meta description
and unified input/output to make them reusable in different projects either individually 
or by chaining them together into portable automation workflows, applications 
and web services adaptable to continuously changing models, data sets, software and hardware.

### Citing this project

Please use this [BibTeX file](https://github.com/mlcommons/ck/blob/master/citation.bib).

## Catalog

Online catalog: [cKnowledge](https://access.cknowledge.org/playground/?action=scripts), [MLCommons](https://docs.mlcommons.org/cm4mlops/scripts).

## Examples

### Run image classificaiton via CM

```bash
pip install cmind -U

cm pull repo mlcommons@cm4mlops --branch=dev

cmr "python app image-classification onnx" --quiet
```

### Run MLPerf inference benchmark via CM

```bash
pip install cm4mlperf -U

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



## License

[Apache 2.0](LICENSE.md)

## Acknowledgments

We thank [cKnowledge.org](https://cKnowledge.org), [cTuning foundation](https://cTuning.org)
and [MLCommons](https://mlcommons.org) for sponsoring this project!

We also thank all [volunteers, collaborators and contributors](CONTRIBUTING.md) 
for their support, fruitful discussions, and useful feedback! 
