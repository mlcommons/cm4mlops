## Unified and cross-platform CM interface for DevOps, MLOps and MLPerf

[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE.md)
[![Powered by CM](https://img.shields.io/badge/Powered_by-MLCommons%20CM-blue)](https://pypi.org/project/cmind).

[![CM script automation features test](https://github.com/mlcommons/cm4mlops/actions/workflows/test-cm-script-features.yml/badge.svg)](https://github.com/mlcommons/cm4mlops/actions/workflows/test-cm-script-features.yml)
[![MLPerf inference bert (deepsparse, tf, onnxruntime, pytorch)](https://github.com/mlcommons/cm4mlops/actions/workflows/test-mlperf-inference-bert-deepsparse-tf-onnxruntime-pytorch.yml/badge.svg)](https://github.com/mlcommons/cm4mlops/actions/workflows/test-mlperf-inference-bert-deepsparse-tf-onnxruntime-pytorch.yml)
[![MLPerf inference MLCommons C++ ResNet50](https://github.com/mlcommons/cm4mlops/actions/workflows/test-mlperf-inference-mlcommons-cpp-resnet50.yml/badge.svg)](https://github.com/mlcommons/cm4mlops/actions/workflows/test-mlperf-inference-mlcommons-cpp-resnet50.yml)
[![MLPerf inference ABTF POC Test](https://github.com/mlcommons/cm4mlops/actions/workflows/test-mlperf-inference-abtf-poc.yml/badge.svg)](https://github.com/mlcommons/cm4mlops/actions/workflows/test-mlperf-inference-abtf-poc.yml)

# Legacy CM4MLOps repository

This repository is powered by the [Collective Mind workflow automation framework](https://github.com/mlcommons/ck/tree/master/cm).

The latest sources are available in [this repository](https://github.com/mlcommons/ck/tree/master/cm4mlops).

Two key automations developed using CM are **Script** and **Cache**, which streamline machine learning (ML) workflows, 
including managing Docker runs. Both Script and Cache automations are part of the **cm4mlops** repository.

The [CM scripts](https://access.cknowledge.org/playground/?action=scripts), 
also housed in this repository, consist of hundreds of modular Python-wrapped scripts accompanied 
by `yaml` metadata, enabling the creation of robust and flexible ML workflows.

- **CM Scripts Documentation**: [Browse](https://access.cknowledge.org/playground/?action=scripts)
- **CM CLI Documentation**: [https://docs.mlcommons.org/ck/specs/cm-cli/](https://docs.mlcommons.org/ck/specs/cm-cli)  

## License

[Apache 2.0](LICENSE.md)

## Copyright

© 2022-2025 MLCommons. All Rights Reserved.

Grigori Fursin, the cTuning foundation and OctoML donated the CK and CM projects to MLCommons to benefit everyone and encourage collaborative development.

## Maintainer(s)

* MLCommons

## Author

[Grigori Fursin](https://cKnowledge.org/gfursin).

We thank all [contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTORS.md) 
for their invaluable feedback and support!

## Concepts

Check our [ACM REP'23 keynote](https://doi.org/10.5281/zenodo.8105339) and the [white paper](https://arxiv.org/abs/2406.16791).

## Test image classification and MLPerf R-GAT inference benchmark via CMX GitHub repo

```bash
pip install cmind
cmx pull repo mlcommons@ck --dir=cm4mlops/cm4mlops
cmx run script "python app image-classification onnx" --quiet
cmx run script "run-mlperf inference _performance-only _short" --model=resnet50 --precision=float32 --backend=onnxruntime --scenario=Offline --device=cpu --env.CM_SUDO_USER=no --quiet
cmx run script --tags=run,mlperf,inference,generate-run-cmds,_submission,_short --submitter="MLCommons" --adr.inference-src.tags=_branch.dev --pull_changes=yes --pull_inference_changes=yes  --submitter="MLCommons" --hw_name=ubuntu-latest_x86 --model=rgat --implementation=python --backend=pytorch --device=cpu --scenario=Offline --test_query_count=500 --adr.compiler.tags=gcc --category=datacenter --quiet  --v --target_qps=1
```

## Parent project

Visit the [parent Collective Knowledge project](https://github.com/mlcommons/ck) for further details.

## Citing this project

If you found the CM automations helpful, kindly reference this article:
[ [ArXiv](https://arxiv.org/abs/2406.16791) ]
