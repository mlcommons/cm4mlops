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
  * [ Script flags mapped to environment](#script-flags-mapped-to-environment)
  * [ Default environment](#default-environment)
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

* Category: *Docker automation.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-docker-container)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *run,docker,container*
* Output cached? *False*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=run,docker,container [--input_flags]`

2. `cmr "run docker container" [--input_flags]`

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'run,docker,container'
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

```cmr "cm gui" --script="run,docker,container"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=run,docker,container) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "run docker container" [--input_flags]`

___
### Customization


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--all_gpus=value`  &rarr;  `CM_DOCKER_ADD_ALL_GPUS=value`
* `--base=value`  &rarr;  `CM_DOCKER_IMAGE_BASE=value`
* `--cache=value`  &rarr;  `CM_DOCKER_CACHE=value`
* `--cm_repo=value`  &rarr;  `CM_MLOPS_REPO=value`
* `--detached=value`  &rarr;  `CM_DOCKER_DETACHED_MODE=value`
* `--device=value`  &rarr;  `CM_DOCKER_ADD_DEVICE=value`
* `--docker_os=value`  &rarr;  `CM_DOCKER_OS=value`
* `--docker_os_version=value`  &rarr;  `CM_DOCKER_OS_VERSION=value`
* `--gh_token=value`  &rarr;  `CM_GH_TOKEN=value`
* `--image_name=value`  &rarr;  `CM_DOCKER_IMAGE_NAME=value`
* `--image_repo=value`  &rarr;  `CM_DOCKER_IMAGE_REPO=value`
* `--image_tag=value`  &rarr;  `CM_DOCKER_IMAGE_TAG=value`
* `--it=value`  &rarr;  `CM_DOCKER_INTERACTIVE=value`
* `--mounts=value`  &rarr;  `CM_DOCKER_VOLUME_MOUNTS=value`
* `--pass_user_group=value`  &rarr;  `CM_DOCKER_PASS_USER_GROUP=value`
* `--port_maps=value`  &rarr;  `CM_DOCKER_PORT_MAPS=value`
* `--post_run_cmds=value`  &rarr;  `CM_DOCKER_POST_RUN_COMMANDS=value`
* `--pre_run_cmds=value`  &rarr;  `CM_DOCKER_PRE_RUN_COMMANDS=value`
* `--real_run=value`  &rarr;  `CM_REAL_RUN=value`
* `--recreate=value`  &rarr;  `CM_DOCKER_IMAGE_RECREATE=value`
* `--run_cmd=value`  &rarr;  `CM_DOCKER_RUN_CMD=value`
* `--run_cmd_extra=value`  &rarr;  `CM_DOCKER_RUN_CMD_EXTRA=value`
* `--script_tags=value`  &rarr;  `CM_DOCKER_RUN_SCRIPT_TAGS=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "all_gpus":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_DOCKER_DETACHED_MODE: `yes`

</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-docker-container/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-docker-container/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-docker-container/_cm.json)***
     * build,docker,image
       * `if (CM_DOCKER_IMAGE_EXISTS  != yes)`
       * CM names: `--adr.['build-docker-image']...`
       - CM script: [build-docker-image](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-docker-image)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-docker-container/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-docker-container/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-docker-container/_cm.json)
</details>

___
### Script output
`cmr "run docker container" [--input_flags] -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)