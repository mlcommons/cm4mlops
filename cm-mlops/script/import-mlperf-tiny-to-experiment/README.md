Automatically generated README for this automation recipe: **import-mlperf-tiny-to-experiment**

Category: **MLPerf benchmark support**

License: **Apache 2.0**

Developers: [Grigori Fursin](https://cKnowledge.org/gfursin)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=import-mlperf-tiny-to-experiment,83e3efd7611f469b) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/import-mlperf-tiny-to-experiment)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* All CM tags to find and reuse this script (see in above meta description): *import,mlperf,tiny,mlperf-tiny,experiment,2experiment,to-experiment*
* Output cached? *False*
* See [pipeline of dependencies](#dependencies-on-other-cm-scripts) on other CM scripts


---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://access.cknowledge.org/playground/?action=install)
* [CM Getting Started Guide](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@ck```

#### Print CM help from the command line

````cmr "import mlperf tiny mlperf-tiny experiment 2experiment to-experiment" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=import,mlperf,tiny,mlperf-tiny,experiment,2experiment,to-experiment`

`cm run script --tags=import,mlperf,tiny,mlperf-tiny,experiment,2experiment,to-experiment [--input_flags]`

*or*

`cmr "import mlperf tiny mlperf-tiny experiment 2experiment to-experiment"`

`cmr "import mlperf tiny mlperf-tiny experiment 2experiment to-experiment " [--input_flags]`


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'import,mlperf,tiny,mlperf-tiny,experiment,2experiment,to-experiment'
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

```cmr "cm gui" --script="import,mlperf,tiny,mlperf-tiny,experiment,2experiment,to-experiment"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=import,mlperf,tiny,mlperf-tiny,experiment,2experiment,to-experiment) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "import mlperf tiny mlperf-tiny experiment 2experiment to-experiment" [--input_flags]`

___
### Customization


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--target_repo=value`  &rarr;  `CM_IMPORT_TINYMLPERF_TARGET_REPO=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "target_repo":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/import-mlperf-tiny-to-experiment/_cm.yaml)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * get,sys-utils-cm
       - CM script: [get-sys-utils-cm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/import-mlperf-tiny-to-experiment/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/import-mlperf-tiny-to-experiment/_cm.yaml)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/import-mlperf-tiny-to-experiment/_cm.yaml)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/import-mlperf-tiny-to-experiment/_cm.yaml)

___
### Script output
`cmr "import mlperf tiny mlperf-tiny experiment 2experiment to-experiment " [--input_flags] -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
