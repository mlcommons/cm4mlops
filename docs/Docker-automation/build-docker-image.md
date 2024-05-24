Automatically generated README for this automation recipe: **build-docker-image**

Category: **Docker automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=build-docker-image,2c3c4ba2413442e7) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@cm4mlops](https://github.com/mlcommons/cm4mlops/tree/dev)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/cm4mlops/tree/dev/script/build-docker-image)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* All CM tags to find and reuse this script (see in above meta description): *build,docker,image,docker-image,dockerimage*
* Output cached? *False*
* See [pipeline of dependencies](#dependencies-on-other-cm-scripts) on other CM scripts


---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://access.cknowledge.org/playground/?action=install)
* [CM Getting Started Guide](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "build docker image docker-image dockerimage" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=build,docker,image,docker-image,dockerimage`

`cm run script --tags=build,docker,image,docker-image,dockerimage [--input_flags]`

*or*

`cmr "build docker image docker-image dockerimage"`

`cmr "build docker image docker-image dockerimage " [--input_flags]`


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'build,docker,image,docker-image,dockerimage'
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

```cmr "cm gui" --script="build,docker,image,docker-image,dockerimage"```

#### Run this script via Docker (beta)

`cm docker script "build docker image docker-image dockerimage" [--input_flags]`

___
### Customization


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--cache=value`  &rarr;  `CM_DOCKER_CACHE=value`
* `--cm_repo=value`  &rarr;  `CM_MLOPS_REPO=value`
* `--docker_os=value`  &rarr;  `CM_DOCKER_OS=value`
* `--docker_os_version=value`  &rarr;  `CM_DOCKER_OS_VERSION=value`
* `--dockerfile=value`  &rarr;  `CM_DOCKERFILE_WITH_PATH=value`
* `--gh_token=value`  &rarr;  `CM_GH_TOKEN=value`
* `--image_name=value`  &rarr;  `CM_DOCKER_IMAGE_NAME=value`
* `--image_repo=value`  &rarr;  `CM_DOCKER_IMAGE_REPO=value`
* `--image_tag=value`  &rarr;  `CM_DOCKER_IMAGE_TAG=value`
* `--post_run_cmds=value`  &rarr;  `CM_DOCKER_POST_RUN_COMMANDS=value`
* `--pre_run_cmds=value`  &rarr;  `CM_DOCKER_PRE_RUN_COMMANDS=value`
* `--push_image=value`  &rarr;  `CM_DOCKER_PUSH_IMAGE=value`
* `--real_run=value`  &rarr;  `CM_REAL_RUN=value`
* `--script_tags=value`  &rarr;  `CM_DOCKER_RUN_SCRIPT_TAGS=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "cache":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_DOCKER_IMAGE_REPO: `local`
* CM_DOCKER_IMAGE_TAG: `latest`

</details>

___
### Dependencies on other CM scripts


  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/build-docker-image/_cm.yaml)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/cm4mlops/tree/dev/script/build-docker-image/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/build-docker-image/_cm.yaml)***
     * build,dockerfile
       * Enable this dependency only if all ENV vars are set:<br>
`{'CM_BUILD_DOCKERFILE': ['yes', '1']}`
       - CM script: [build-dockerfile](https://github.com/mlcommons/cm4mlops/tree/master/script/build-dockerfile)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/dev/script/build-docker-image/run.bat)
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/dev/script/build-docker-image/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/build-docker-image/_cm.yaml)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/cm4mlops/tree/dev/script/build-docker-image/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/build-docker-image/_cm.yaml)

___
### Script output
`cmr "build docker image docker-image dockerimage " [--input_flags] -j`
#### New environment keys (filter)

* `CM_DOCKER_*`
#### New environment keys auto-detected from customize

* `CM_DOCKER_BUILD_ARGS`
* `CM_DOCKER_BUILD_CMD`
* `CM_DOCKER_CACHE_ARG`
* `CM_DOCKER_IMAGE_NAME`
* `CM_DOCKER_IMAGE_REPO`
* `CM_DOCKER_IMAGE_TAG`