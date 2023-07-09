<details>
<summary>Click here to see the table of contents.</summary>

* [Description](#description)
* [Information](#information)
* [Usage](#usage)
  * [ CM installation](#cm-installation)
  * [ CM script automation help](#cm-script-automation-help)
  * [ CM CLI](#cm-cli)
  * [ CM Python API](#cm-python-api)
  * [ CM GUI](#cm-gui)
  * [ CM modular Docker container](#cm-modular-docker-container)
* [Customization](#customization)
  * [ Variations](#variations)
  * [ Default environment](#default-environment)
* [Versions](#versions)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit! See [more info](README-extra.md).*

### Description


See [more info](README-extra.md).

#### Information

* Category: *Modular MLPerf benchmarks.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,src,source,inference,inference-src,inference-source,mlperf,mlcommons*
* Output cached?: *True*
___
### Usage

#### CM installation

[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

##### CM pull repository

```cm pull repo mlcommons@ck```

##### CM script automation help

```cm run script --help```

#### CM CLI

1. `cm run script --tags=get,src,source,inference,inference-src,inference-source,mlperf,mlcommons[,variations] `

2. `cm run script "get src source inference inference-src inference-source mlperf mlcommons[,variations]" `

3. `cm run script 4b57186581024797 `

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,src,source,inference,inference-src,inference-source,mlperf,mlcommons'
                  'out':'con',
                  ...
                  (other input keys for this script)
                  ...
                 })

if r['return']>0:
    print (r['error'])

```

</details>


#### CM GUI

```cm run script --tags=gui --script="get,src,source,inference,inference-src,inference-source,mlperf,mlcommons"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,src,source,inference,inference-src,inference-source,mlperf,mlcommons) to generate CM CMD.

#### CM modular Docker container

*TBD*

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_3d-unet`
      - Environment variables:
        - *CM_SUBMODULE_3D_UNET*: `yes`
      - Workflow:
    * `_deeplearningexamples`
      - Environment variables:
        - *CM_SUBMODULE_DEEPLEARNINGEXAMPLES*: `yes`
      - Workflow:
    * `_deepsparse`
      - Environment variables:
        - *CM_GIT_URL*: `https://github.com/neuralmagic/inference`
        - *CM_GIT_CHECKOUT*: `deepsparse`
        - *CM_MLPERF_LAST_RELEASE*: `v3.0`
      - Workflow:
    * **`_default`** (default)
      - Environment variables:
        - *CM_GIT_PATCH*: `no`
      - Workflow:
    * `_full-history`
      - Environment variables:
        - *CM_GIT_DEPTH*: ``
      - Workflow:
    * `_gn`
      - Environment variables:
        - *CM_SUBMODULE_GN*: `yes`
      - Workflow:
    * `_no-recurse-submodules`
      - Environment variables:
        - *CM_GIT_RECURSE_SUBMODULES*: ``
      - Workflow:
    * `_nvidia-pycocotools`
      - Environment variables:
        - *CM_GIT_PATCH_FILENAME*: `coco.patch`
      - Workflow:
    * `_octoml`
      - Environment variables:
        - *CM_GIT_URL*: `https://github.com/octoml/inference`
      - Workflow:
    * `_patch`
      - Environment variables:
        - *CM_GIT_PATCH*: `yes`
      - Workflow:
    * `_pybind`
      - Environment variables:
        - *CM_SUBMODULE_PYBIND*: `yes`
      - Workflow:
    * `_recurse-submodules`
      - Environment variables:
        - *CM_GIT_RECURSE_SUBMODULES*: ` --recurse-submodules`
      - Workflow:
    * `_short-history`
      - Environment variables:
        - *CM_GIT_DEPTH*: `--depth 10`
      - Workflow:

    </details>


#### Default variations

`_default`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_GIT_DEPTH: `--depth 4`
* CM_GIT_PATCH: `no`
* CM_GIT_URL: `https://github.com/mlcommons/inference.git`
* CM_GIT_RECURSE_SUBMODULES: ``
* CM_GIT_CHECKOUT: `master`
* CM_GIT_CHECKOUT_FOLDER: `inference`

</details>

#### Versions
Default version: `master`

* `custom`
* `deepsparse`
* `master`
* `pybind_fix`
* `r2.1`
* `tvm`
___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src/_cm.json)***
     * get,git,repo
       * CM names: `--adr.['inference-git-repo']...`
       - CM script: [get-git-repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src/run.bat)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src/_cm.json)
</details>

___
### Script output
#### New environment keys (filter)

* `+PYTHONPATH`
* `CM_MLPERF_INFERENCE_*`
* `CM_MLPERF_LAST_RELEASE`
#### New environment keys auto-detected from customize

* `CM_MLPERF_INFERENCE_3DUNET_PATH`
* `CM_MLPERF_INFERENCE_BERT_PATH`
* `CM_MLPERF_INFERENCE_CLASSIFICATION_AND_DETECTION_PATH`
* `CM_MLPERF_INFERENCE_CONF_PATH`
* `CM_MLPERF_INFERENCE_DLRM_PATH`
* `CM_MLPERF_INFERENCE_DLRM_V2_PATH`
* `CM_MLPERF_INFERENCE_GPTJ_PATH`
* `CM_MLPERF_INFERENCE_RNNT_PATH`
* `CM_MLPERF_INFERENCE_VISION_PATH`
___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)