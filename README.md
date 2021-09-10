# Collective Knowledge framework (CK)

[![Downloads](https://pepy.tech/badge/ck)](https://pepy.tech/project/ck)
[![PyPI version](https://badge.fury.io/py/ck.svg)](https://badge.fury.io/py/ck)
[![Python Version](https://img.shields.io/badge/python-2.7%20|%203.4+-blue.svg)](https://pypi.org/project/ck)

Linux/MacOS: [![Build Status](https://travis-ci.com/ctuning/ck.svg?branch=master)](https://travis-ci.com/ctuning/ck)
Windows: [![Windows Build status](https://ci.appveyor.com/api/projects/status/iw2k4eajy54xrvqc?svg=true)](https://ci.appveyor.com/project/gfursin/ck)

[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Fp6uxCqTazmCSSl8v-nY93VVmcOoLiXi?usp=sharing)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1a761nKgoHlJAy6gOXh-c9H4WkLV8nzRU?usp=sharing)
[![Documentation Status](https://readthedocs.org/projects/ck/badge/?version=latest)](https://ck.readthedocs.io/en/latest/?badge=latest)
[![Coverage Status](https://coveralls.io/repos/github/ctuning/ck/badge.svg)](https://coveralls.io/github/ctuning/ck)


## Releases

### Stable versions

The latest version of the CK automation suite supported by MLCommons: **v2.5.8** (Apache 2.0 license):
* [MLCommons CK framework](https://github.com/mlcommons/ck/releases/tag/V2.5.8)
* [MLCommons CK automation suite for MLPerf and ML/SW/HW co-design](https://github.com/mlcommons/ck-mlops)

### Development versions

We plan to develop a new version of the CK framework (v3) 
as a collaborative effort within different MLCommons workgroups - 
please feel free to join this community effort!

### Deprecated versions

**Versions 1.x including v1.17.0 and 1.55.5 (BSD license)** are stable but not officially supported anymore. 
Please get in touch and we will help you to upgrade your infrastructure to use the latest MLCommons technology!


## Overview

Collective Knowledge framework (CK) helps to organize software projects
as a database of reusable components with common automation actions
and extensible meta descriptions based on [FAIR principles](https://www.nature.com/articles/sdata201618)
(findability, accessibility, interoperability and reusability)
as described in our [journal article](https://arxiv.org/pdf/2011.01149.pdf) ([shorter pre-print](https://arxiv.org/abs/2006.07161)).

Our goal is to help researchers and practitioners share, reuse and extend their knowledge
in the form of portable workflows, automation actions and reusable artifacts with a common API, CLI,
and meta description. See how CK helps to automate benchmarking, optimization and design space
exploration of [AI/ML/software/hardware stacks](https://cknowledge.io/result/crowd-benchmarking-mlperf-inference-classification-mobilenets-all/), 
simplifies [MLPerf&trade; inference benchmark](https://github.com/mlcommons/ck/blob/master/docs/mlperf-automation/README.md) submissions 
and supports collaborative, reproducible and reusable ML Systems research:

* [ACM TechTalk](https://www.youtube.com/watch?v=7zpeIVwICa4)
* [AI/ML/MLPerf&trade; automation workflows and components from the community](https://github.com/mlcommons/ck-mlops);
* [Reddit discussion about reproducing 150 papers](https://www.reddit.com/r/MachineLearning/comments/ioq8do/n_reproducing_150_research_papers_the_problems);
* Our reproducibility initiatives: [methodology](https://cTuning.org/ae), [checklist](https://ctuning.org/ae/submission_extra.html), [events](https://cKnowledge.io/events).

## Current projects
* [Automating MLPerf(tm) inference benchmark and packing ML models, data sets and frameworks as CK components with a unified API and meta description](https://github.com/mlcommons/ck/blob/master/docs/mlperf-automation/README.md)
* Developing customizable dashboards for MLPerf&trade; to help end-users select ML/SW/HW stacks on a Pareto frontier: [aggregated MLPerf&trade; results]( https://cknowledge.io/?q="mlperf-inference-all" )
* Providing a common format to share artifacts at ML, systems and other conferences: [video](https://youtu.be/DIkZxraTmGM), [Artifact Evaluation](https://cTuning.org/ae)
* Redesigning CK together with the community based on user feedback: [incubator](https://github.com/mlcommons/ck/tree/master/incubator)
* [Other real-world use cases](https://cKnowledge.org/partners.html) from MLPerf&trade;, Qualcomm, Arm, General Motors, IBM, the Raspberry Pi foundation, ACM and other great partners;

## Documentation

* [Online CK documentation]( https://ck.readthedocs.io ) 
  * [Why CK?]( https://ck.readthedocs.io/en/latest/src/introduction.html ) 
  * [CK Basics](https://michel-steuwer.github.io/About-CK)
  * [Try CK]( https://ck.readthedocs.io/en/latest/src/first-steps.html )
* [Publications](https://github.com/mlcommons/ck/wiki/Publications)

## Installation

Follow [this guide](https://ck.readthedocs.io/en/latest/src/installation.html) 
to install CK framework on your platform.

CK supports the following platforms:

|               | As a host platform | As a target platform |
|---------------|:------------------:|:--------------------:|
| Generic Linux | ✓ | ✓ |
| Linux (Arm)   | ✓ | ✓ |
| Raspberry Pi  | ✓ | ✓ |
| MacOS         | ✓ | ± |
| Windows       | ✓ | ✓ |
| Android       | ± | ✓ |
| iOS           | TBD | TBD |
| Bare-metal (edge devices)   | - | ± |

## Examples

### Portable CK workflow (native environment without Docker)

Here we show how to pull a GitHub repo in the CK format 
and use a unified CK interface to compile and run 
any program (image corner detection in our case)
with any compatible data set on any compatible platform:

```bash
python3 -m pip install ck

ck pull repo:mlcommons@ck-mlops

ck ls program:*susan*

ck search dataset --tags=jpeg

ck detect soft --tags=compiler,gcc
ck detect soft --tags=compiler,llvm

ck show env --tags=compiler

ck compile program:image-corner-detection --speed

ck run program:image-corner-detection --repeat=1 --env.MY_ENV=123 --env.TEST=xyz
```

You can check output of this program in the following directory:
```bash
cd `ck find program:image-corner-detection`/tmp
ls

processed-image.pgm
```

You can now view this image with detected corners.


Check [CK docs](https://ck.readthedocs.io/en/latest/src/introduction.html) for further details.

### MLPerf&trade; benchmark workflows

* [Image classification](https://github.com/mlcommons/ck/blob/master/docs/mlperf-automation/tasks/task-image-classification.md)
* [Object detection](https://github.com/mlcommons/ck/blob/master/docs/mlperf-automation/tasks/task-object-detection.md)

### Portable CK workflows inside containers

We have prepared adaptive CK containers to demonstrate MLOps capabilities:
* https://github.com/mlcommons/ck-mlops/tree/main/docker

You can run them as follows:

```bash
ck pull repo:mlcommons@ck-mlops
ck build docker:ck-template-mlperf --tag=ubuntu-20.04
ck run docker:ck-template-mlperf --tag=ubuntu-20.04
```

### Portable workflow example with virtual CK environments

You can create multiple [virtual CK environments](https://github.com/mlcommons/ck-venv) with templates
to automatically install different CK packages and workflows, for example for MLPerf&trade; inference:

```
ck pull repo:mlcommons@ck-venv
ck create venv:test --template=mlperf-inference-main
ck ls venv
ck activate venv:test

ck pull repo:mlcommons@ck-mlops
ck install package --ask --tags=dataset,coco,val,2017,full
ck show env

```

### Integration with web services and CI platforms

All CK modules, automation actions and workflows are accessible as a micro-service with a unified JSON I/O API
to make it easier to integrate them with web services and CI platforms as described 
[here](https://github.com/mlcommons/ck/blob/master/docs/mlperf-automation/tools/continuous-integration.md).




### More examples

* See [docs](https://ck.readthedocs.io/en/latest/src/introduction.html#ck-showroom)







## CK portal 

We have developed the [cKnowledge.io portal](https://cKnowledge.io) to help the community
organize and find all the CK workflows and components similar to PyPI:

* [Search CK components](https://cKnowledge.io)
* [Browse CK components](https://cKnowledge.io/browse)
* [Find reproduced results from papers]( https://cKnowledge.io/reproduced-results )
* [Test CK workflows to benchmark and optimize ML Systems]( https://cKnowledge.io/demo )



## Testing CK internals and workflows

The community provides Docker containers to test CK and components using different ML/SW/HW stacks (DSE).

* A set of  Docker containers to test the basic CK functionality
  using some MLPerf inference benchmark workflows: https://github.com/mlcommons/ck-mlops/tree/main/docker/test-ck


## Contributions

Users can extend the CK functionality via [CK modules](https://github.com/mlcommons/ck/tree/master/ck/repo/module) 
or external [GitHub reposities](https://cKnowledge.io/repos) in the CK format
as described [here](https://ck.readthedocs.io/en/latest/src/typical-usage.html).

Please check [this documentation](https://ck.readthedocs.io/en/latest/src/how-to-contribute.html)
if you want to extend the CK core functionality and [modules](https://github.com/mlcommons/ck/tree/master/ck/repo/module). 

Note, that we plan to [redesign the CK core](https://github.com/mlcommons/ck/projects/1) 
to be more pythonic (we wrote the first prototype without OO to be able 
to port it to bare-metal devices in C but eventually we decided to drop this idea).


## Author and coordinator

* [Grigori Fursin](https://fursin.net)

## Acknowledgments

We would like to thank all [contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md) 
and [collaborators](https://cKnowledge.org/partners.html) for their support, fruitful discussions, 
and useful feedback! See more acknowledgments in the [CK journal article](https://arxiv.org/abs/2011.01149).
