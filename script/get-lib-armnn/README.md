Automatically generated README for this automation recipe: **get-lib-armnn**

Category: **Detection or installation of tools and artifacts**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-lib-armnn,9603a2e90fd44587) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@cm4mlops](https://github.com/mlcommons/cm4mlops/tree/dev)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/cm4mlops/tree/dev/script/get-lib-armnn)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,lib-armnn,lib,armnn*
* Output cached? *True*
* See [pipeline of dependencies](#dependencies-on-other-cm-scripts) on other CM scripts


---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://access.cknowledge.org/playground/?action=install)
* [CM Getting Started Guide](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get lib-armnn lib armnn" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,lib-armnn,lib,armnn`

`cm run script --tags=get,lib-armnn,lib,armnn `

*or*

`cmr "get lib-armnn lib armnn"`

`cmr "get lib-armnn lib armnn " `


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,lib-armnn,lib,armnn'
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

```cmr "cm gui" --script="get,lib-armnn,lib,armnn"```

#### Run this script via Docker (beta)

`cm docker script "get lib-armnn lib armnn" `

___
### Customization

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

#### Versions
Default version: `23.11`

* `22.11`
* `23.05`
* `23.11`
___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/get-lib-armnn/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/cm4mlops/tree/master/script/detect-os)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/cm4mlops/tree/dev/script/get-lib-armnn/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/get-lib-armnn/_cm.json)***
     * get,git,repo,_repo.https://github.com/ARM-software/armnn
       - CM script: [get-git-repo](https://github.com/mlcommons/cm4mlops/tree/master/script/get-git-repo)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/dev/script/get-lib-armnn/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/get-lib-armnn/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/cm4mlops/tree/dev/script/get-lib-armnn/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/get-lib-armnn/_cm.json)

___
### Script output
`cmr "get lib-armnn lib armnn "  -j`
#### New environment keys (filter)

* `+CPLUS_INCLUDE_PATH`
* `+C_INCLUDE_PATH`
* `+LD_LIBRARY_PATH`
* `CM_LIB_ARMNN_VERSION`
* `CM_LIB_DNNL_*`
#### New environment keys auto-detected from customize
