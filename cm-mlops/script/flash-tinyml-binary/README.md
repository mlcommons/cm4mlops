<details>
<summary>Click here to see the table of contents.</summary>

* [About](#about)
* [Summary](#summary)
* [Reuse this script in your project](#reuse-this-script-in-your-project)
  * [ Install CM automation language](#install-cm-automation-language)
  * [ Check CM script flags](#check-cm-script-flags)
  * [ Run this script from command line](#run-this-script-from-command-line)
  * [ Run this script from Python](#run-this-script-from-python)
  * [ Run this script via GUI](#run-this-script-via-gui)
  * [ Run this script via Docker (beta)](#run-this-script-via-docker-(beta))
* [Customization](#customization)
  * [ Variations](#variations)
  * [ Script flags mapped to environment](#script-flags-mapped-to-environment)
  * [ Default environment](#default-environment)
* [Versions](#versions)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit!*

### About


See extra [notes](README-extra.md) from the authors and contributors.

#### Summary

* Category: *TinyML automation.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/flash-tinyml-binary)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *flash,tiny,mlperf,mlcommons*
* Output cached? *False*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=flash,tiny,mlperf,mlcommons[,variations] [--input_flags]`

2. `cmr "flash tiny mlperf mlcommons[ variations]" [--input_flags]`

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'flash,tiny,mlperf,mlcommons'
                  'out':'con',
                  ...
                  (other input keys for this script)
                  ...
                 })

if r['return']>0:
    print (r['error'])

```

</details>


#### Run this script via GUI

```cmr "cm gui" --script="flash,tiny,mlperf,mlcommons"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=flash,tiny,mlperf,mlcommons) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "flash tiny mlperf mlcommons[ variations]" [--input_flags]`

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_NRF`
      - Workflow:
    * `_NUCLEO`
      - Workflow:
    * `_ad`
      - Workflow:
    * `_cmsis_nn`
      - Workflow:
    * `_ic`
      - Workflow:
    * `_kws`
      - Workflow:
    * `_native`
      - Workflow:
    * `_vww`
      - Workflow:

    </details>


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--build_dir=value`  &rarr;  `CM_TINY_BUILD_DIR=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "build_dir":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

#### Versions
Default version: `r1.0`

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/flash-tinyml-binary/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * get,zephyr
       * CM names: `--adr.['zephyr']...`
       - CM script: [get-zephyr](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-zephyr)
     * get,zephyr-sdk
       * CM names: `--adr.['zephyr-sdk']...`
       - CM script: [get-zephyr-sdk](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-zephyr-sdk)
     * reproduce,tiny,mlperf
       * `if (CM_TINY_BUILD_DIR  != on)`
       - CM script: [reproduce-mlperf-octoml-tinyml-results](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-octoml-tinyml-results)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/flash-tinyml-binary/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/flash-tinyml-binary/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/flash-tinyml-binary/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/flash-tinyml-binary/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/flash-tinyml-binary/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/flash-tinyml-binary/_cm.json)
</details>

___
### Script output
`cmr "flash tiny mlperf mlcommons[,variations]" [--input_flags] -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)