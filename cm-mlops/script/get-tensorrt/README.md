Automatically generated README for this automation recipe: **get-tensorrt**

Category: **CUDA automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-tensorrt,2a84ca505e4c408d) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-tensorrt)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,tensorrt,nvidia*
* Output cached? *True*
* See [pipeline of dependencies](#dependencies-on-other-cm-scripts) on other CM scripts


---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://access.cknowledge.org/playground/?action=install)
* [CM Getting Started Guide](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@ck```

#### Print CM help from the command line

````cmr "get tensorrt nvidia" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,tensorrt,nvidia`

`cm run script --tags=get,tensorrt,nvidia[,variations] [--input_flags]`

*or*

`cmr "get tensorrt nvidia"`

`cmr "get tensorrt nvidia [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*


#### Input Flags

* --**input**=Full path to the installed TensorRT library (nvinfer)
* --**tar_file**=Full path to the TensorRT Tar file downloaded from the Nvidia website (https://developer.nvidia.com/tensorrt)

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "input":...}
```
#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,tensorrt,nvidia'
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

```cmr "cm gui" --script="get,tensorrt,nvidia"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,tensorrt,nvidia) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get tensorrt nvidia[variations]" [--input_flags]`

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_dev`
      - Environment variables:
        - *CM_TENSORRT_REQUIRE_DEV*: `yes`
      - Workflow:

    </details>


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--input=value`  &rarr;  `CM_INPUT=value`
* `--tar_file=value`  &rarr;  `CM_TENSORRT_TAR_FILE_PATH=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "input":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-tensorrt/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-tensorrt/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-tensorrt/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-tensorrt/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-tensorrt/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-tensorrt/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-tensorrt/_cm.json)

___
### Script output
`cmr "get tensorrt nvidia [,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `+ LDFLAGS`
* `+CPLUS_INCLUDE_PATH`
* `+C_INCLUDE_PATH`
* `+DYLD_FALLBACK_LIBRARY_PATH`
* `+LD_LIBRARY_PATH`
* `+PATH`
* `CM_TENSORRT_*`
#### New environment keys auto-detected from customize

* `CM_TENSORRT_INSTALL_PATH`
* `CM_TENSORRT_LIB_PATH`
* `CM_TENSORRT_VERSION`