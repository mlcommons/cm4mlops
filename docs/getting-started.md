# cm-docs

## CM Framework

**CM** (Collective Mind) is a Python package with a CLI and API designed to create and manage automations. Two key automations developed using CM are **Script** and **Cache**, which streamline ML workflows, including managing Docker runs.
The **CM Python** package was developed by **Grigori Fursin**. The **Script** and **Cache** automations are part of the [cm4mlops](https://github.com/mlcommons/cm4mlops/tree/mlperf-inference) repository, created by **Grigori Fursin** and **Arjun Suresh** and sponsored by OctoML, cKnowledge, cTuning and MLCommons.
The **CM scripts**, also housed in the [cm4mlops](https://github.com/mlcommons/cm4mlops/tree/mlperf-inference) repository, are created and maintained by **Arjun Suresh**, **Anandhu Sooraj**, and **Grigori Fursin** with the help of the MLCommons community.

## Simple script automation execution in cm

A simple script automation execution in CM is as follows:

```
cm run script --tags=detect,os -j
```

This would capture the OS details of the system which it is run. Example details could be found here:
```
    "CM_HOST_OS_TYPE": "linux",
    "CM_HOST_OS_BITS": "64",
    "CM_HOST_OS_FLAVOR": "ubuntu",
    "CM_HOST_OS_FLAVOR_LIKE": "debian",
    "CM_HOST_OS_VERSION": "24.04",
    "CM_HOST_OS_KERNEL_VERSION": "6.8.0-45-generic",
    "CM_HOST_OS_GLIBC_VERSION": "2.39",
    "CM_HOST_OS_MACHINE": "x86_64",
    "CM_HOST_OS_PACKAGE_MANAGER": "apt",
    "CM_HOST_OS_PACKAGE_MANAGER_INSTALL_CMD": "DEBIAN_FRONTEND=noninteractive apt-get install -y",
    "CM_HOST_OS_PACKAGE_MANAGER_UPDATE_CMD": "apt-get update -y",
    "+CM_HOST_OS_DEFAULT_LIBRARY_PATH": [
      "/usr/local/lib/x86_64-linux-gnu",
      "/lib/x86_64-linux-gnu",
      "/usr/lib/x86_64-linux-gnu",
      "/usr/lib/x86_64-linux-gnu64",
      "/usr/local/lib64",
      "/lib64",
      "/usr/lib64",
      "/usr/local/lib",
      "/lib",
      "/usr/lib",
      "/usr/x86_64-linux-gnu/lib64",
      "/usr/x86_64-linux-gnu/lib"
    ],
    "CM_HOST_PLATFORM_FLAVOR": "x86_64",
    "CM_HOST_PYTHON_BITS": "64",
    "CM_HOST_SYSTEM_NAME": "intel-spr-i9"
```

## CM automation recipe for reproducing nvidia r4.0 GPT-J implementation

We designed CM as a [small Python library](https://github.com/mlcommons/ck/tree/master/cm) 
with a human-friendly command line, simple Python API and minimal dependencies 
needed to implement automation recipes (Python 3.7+, PIP, pyyaml, git, wget)
and chain them into portable workflows. CM scripts can run natively (development mode) 
or inside containers that CM generates on the fly (stable mode).

Most of the time, these dependencies are already installed on your platform.
In such case, you should be able to prepare and run image classification with ONNX,
ImageNet validation data set and ResNet-50 on Linux, MacOS, Windows and any other
operating system using a few CM commands:

<sup>

```bash
pip install cm4mlops
cm run script --tags=run-mlperf,inference,_find-performance,_full,_r4.1-dev --model=gptj-99 --implementation=nvidia --framework=tensorrt --category=datacenter --scenario=Offline --execution_mode=test --device=cuda  --docker --quiet --test_query_count=50
```

</sup>

*Note that you may need to re-login when you install cmind for the first time
 to let your platform pick up path to the `cm` command line front-end.*

## How CM scripts works?

Next, we briefly explain how CM commands work.

Whenever you run `cm run script --tags=run-mlperf,inference,_find-performance,_full,_r4.1-dev --model=gptj-99 --implementation=nvidia --framework=tensorrt --category=datacenter --scenario=Offline --execution_mode=test --device=cuda  --docker --quiet --test_query_count=50`,
the [CM script automation](https://github.com/mlcommons/ck/blob/master/cm-mlops/automation/script/module.py) 
will simply search for `_cm.yaml` and `_cm.json` files (CM meta-description dictionary) in all `script` 
directories in all software projects registered in CM via `cm pull repo`.

In our case, when we installed CM through `pip install cm4mlops`, we have installed `cmind` and have pulled [github.com/mlcommons/cm4mlops](https://github.com/mlcommons/cm4mlops)
that has MLCommons' MLPerf CM automation recipes embedded 
in a [`script` directory](https://github.com/mlcommons/cm4mlops/tree/mlperf-inference/script). 

*Note that you can pull any public or private Git repository, download any software project
 or register any local directory in the CM to search for embedded automation recipes.*

CM will then try to match all your tags without `_` prefix (`_` in tags mark 
the so-called CM script variations that customize a give script behavior 
and will be described later)  with a `tags` list in the CM meta-description dictionary.
In our case, it will match the corresponding [`_cm.yaml`](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-image-classification-onnx-py/_cm.yaml#L9) 
in `$HOME/CM/repos/mlcommons@cm4mlops/script/app-image-classification-onnx-py/_cm.yaml` - 
a wrapper for a given CM automation recipe.

*Note that if you use unique ID instead of tags to identify automation (such as `3d5e908e472b417e`), 
 CM will try to match `uid` string in the CM meta descriptions instead of tags.*

## How CM runs automation recipes?

Whenever CM finds a directory with a requested automation recipe, 
it performs the following steps:
* run `preprocess` function in `customize.py` if exists
* run `run.sh` (Linux) or `run.bat` (Windows) if exists
* run `postprocess` function in `customize.py` if exists

Such organization makes it possible to use either Python or native OS scripts or
both to implement CM automation recipes while minimizing the learning curve
for CM understanding, development and debugging as requested by CM users.

Furthermore, CM scripts can keep the source code of implementations example - 
image classification (as shown [here](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-onnx-py/src))
that we can easily move around
between projects without hardwiring paths and names.

## How CM unifies inputs, outputs and environment variables?

CM allows you to pass environment variables to `customize.py`
and native scripts using `--env.ENV=VALUE`. 

When you use some flags such as `--model` in previouslyu mentioned MLPerf Inference GPT-J
example, it will be also converted into an environment variable
using [`input_mapping` dictionary](https://github.com/anandhu-eng/cm4mlops/blob/a7abc554cfee99f7de4eb508c34f8abbe4cdd663/script/run-mlperf-inference-app/_cm.yaml#L69) 
in the CM meta description of this script.

All environment variables are aggregated in `env` dictionary inside CM
and then passed to `preprocess` function in `customize.py` where you can modify
it programmatically. 

They are then passed to the `run` script. 

**Note:**

Since new environment variables
are not preserved after `run` script, one can pass new environment variables
back to CM using `tmp-run-env.out` with ENV=KEY strings as shown [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-image-classification-onnx-py/run.sh#L37)
or using `tmp-run-state.json` as shown [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-image-classification-onnx-py/src/onnx_classify.py#L171).

## How CM chains automation recipes into portable workflows?

CM scripts provide a technology-agnostic wrapper with simple tags, CLI and Python API to prepare and run 
user code snippets and native scripts/tools while unifying their inputs and outputs, paths and environment variables.

Such architecture makes it possible to easily chain existing user scripts and tools into portable, technology-agnostic and powerful workflows
instead of substituting or rewriting them.

It is possible to chain CM scripts using simple 
[`deps` list](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-image-classification-onnx-py/_cm.yaml#L23) 
in a meta description of a given script:

<sup>

```yaml
deps:
- tags: detect,os
- tags: get,sys-utils-cm
- names:
  - python
  - python3
  tags: get,python3

- tags: get,cuda
  names:
  - cuda
  enable_if_env:
    USE_CUDA:
    - yes
- tags: get,cudnn
  names:
  - cudnn
  enable_if_env:
    USE_CUDA:
    - yes

- tags: get,dataset,imagenet,image-classification,original
- tags: get,dataset-aux,imagenet-aux,image-classification
- tags: get,ml-model,resnet50,_onnx,image-classification
  names:
  - ml-model

- tags: get,generic-python-lib,_package.Pillow
- tags: get,generic-python-lib,_package.numpy
- tags: get,generic-python-lib,_package.opencv-python


- tags: get,generic-python-lib,_onnxruntime
  names:
  - onnxruntime
  skip_if_env:
    USE_CUDA:
    - yes
- tags: get,generic-python-lib,_onnxruntime_gpu
  names:
  - onnxruntime
  enable_if_env:
    USE_CUDA:
    - yes

```

</sup>

Each entry in this list is a dictionary that specifies which CM script to run using `tags`.
Internally, CM will be updating `env` dictionary (flat environment) and `state` dictionary 
(to let scripts exchange complex data structures besides environment variables).

If you run CM via command line, you can see internal `env` and `state` dictionaries by adding `-j` flag:

```bash
cmr "python app image-classification onnx _cpu" --input=computer_mouse.jpg -j
```

*Note that we use similar approach for updating environment variables similar 
 to calling native scripts - by default, they do not alter environment
 variables at the host. However, CM allows you to do that 
 by explicitly specifying which environment variables and state keys
 will be updated at the host using `new_env_keys` and `new_state_keys`
 in the meta of a given script as shown [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-image-classification-onnx-py/_cm.yaml#L88).
 This helped us make behavior of complex CM workflows more deterministic
 and reproducible.*

Each sub-dependency can be turned on or off using environment variables
using `enable_if_env` dictionary or `disable_if_env` dictionary.

You can also specify `version_min`, `version_max` and `version` in these
dependencies. You can also give them some specific names such as `python`
and pass versions and environment variables only to a specific script in a pipeline as follows:
```bash
cmr "python app image-classification onnx _cpu" --input=computer_mouse.jpg --adr.python.version_min=3.9
```

This functionality is usually implemented inside ad-hoc bash or shell scripts 
with many hardwired paths and names - CM simply makes such scripts and tools 
portable and reusable while enabling technology-agnostic automation workflows 
with a unified interface that can adapt to any operating system and are easy 
to understand.

We can now assemble complex automation workflows by reusing all portable
scripts from [the community](https://access.cknowledge.org/playground/?action=scripts).

In our example, we reused CM scripts to [detect OS features](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os), 
install system dependencies on [any supported OS](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm) 
(Ubuntu, MacOS, RHEL, Arch, Debian, SLES, Windows, etc),
detect or install Python and PIP packages, download and preprocess data sets and models, etc.

## CM Script Automation

CM script automation manages the creation and execution of CM scripts. It closely relates to CM cache automation as the output of any CM script can be cached.
It also has extensions:

1. Docker: allows CM script to be run inside a docker container
2. Docs: used to automatically generate the README file for a CM script

More theoretical explanation on CM Script and it's workflows could be found [here](https://github.com/mlcommons/cm4mlops/blob/anandhu-eng-patch-1/docs/index.md)

### How to add new CM scripts?

One of the main requirement for CM was to provide a very light-weight connectors 
between existing automation scripts and tools rather than substituting them.

You can add your own scripts and tools to CM using the following command
that will create a ready-to-use dummy CM script named `hello-world`:

```bash
cm add script hello-world --tags=hello-world,display,test
```

This creates a bare cm script inside the local repo. The new folder structure would look something like this:
```
├── CM
│   ├── index.json
│   ├── repos
│   │   ├── local
│   │   │   ├── cfg
│   │   │   ├── cache
│   │   │   ├── cmr.yaml
│   │   │   └── script
│   │   │   	├── hello-world
│   │   │       	├── _cm.yaml
│   │   │       	├── customize.py
│   │   │       	├── README-extra.md
│   │   │       	├── run.bat
│   │   │       	└── run.sh
│   │   └── mlcommons@cm4mlops
│   └── repos.json
```

You can also run it from python as follows:
```bash
import cmind
output=cmind.access({'action':'run', 
                     'automation':'script', 
                     'tags':'hello-world,display,test`})
if output['return']==0: print (output)
```

If you find that the script you are newly creating is similar to any existing scripts in any cm repository, 
you could create a new script by copying another script entirely using the following command:

```
cm copy script <source_script> .:<target_script>
```

The `source_script` contains the name of the script that you want to make a copy and `target_script` contains the name of the new script that will be created as a copy of the `source_script`.
The existing script names in `cm4mlops` repo could be found [here](https://github.com/mlcommons/cm4mlops/tree/mlperf-inference/script).

## How to customize CM scripts using variations?

Sometimes we need to set multiple environment variables or run a set of extra CM scripts
for a specific purpose (different hardware target or model or dataset).

We introduced special tags with `_`, called *variations* or *variation tags*, 
that allow you to update a set of environment variables and add extra scripts
to the chain of dependencies.

Such variations are defined using [`variations` dictionary](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-image-classification-onnx-py/_cm.yaml#L69) 
in the meta description of a given CM script.

For example, our script has 2 variations `_cuda` and `_cpu`.

If you want to use CUDA implementation of the image classification example, 
you can add this variation to the tags that will set `USE_CUDA` environment to `yes`
and will turn on a specific CM script in `deps` to install ONNX for CUDA:

```bash
cmr "python app image-classification onnx _cuda" --input=computer_mouse.jpg
```



