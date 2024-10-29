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
