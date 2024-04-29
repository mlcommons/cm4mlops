Automatically generated README for this automation recipe: **get-mlperf-inference-results-dir**

Category: **MLPerf benchmark support**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-mlperf-inference-results-dir,84f3c5aad5e1444b) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@cm4mlops](https://github.com/mlcommons/cm4mlops/tree/dev)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/cm4mlops/tree/dev/script/get-mlperf-inference-results-dir)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,mlperf,inference,results,dir,directory*
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

````cmr "get mlperf inference results dir directory" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,mlperf,inference,results,dir,directory`

`cm run script --tags=get,mlperf,inference,results,dir,directory[,variations] [--input_flags]`

*or*

`cmr "get mlperf inference results dir directory"`

`cmr "get mlperf inference results dir directory [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,mlperf,inference,results,dir,directory'
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

```cmr "cm gui" --script="get,mlperf,inference,results,dir,directory"```

#### Run this script via Docker (beta)

`cm docker script "get mlperf inference results dir directory[variations]" [--input_flags]`

___
### Customization


#### Variations

  * Group "**version**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_version.#`
      - Environment variables:
        - *CM_MLPERF_INFERENCE_RESULTS_VERSION*: `#`
      - Workflow:
    * **`_version.4_0`** (default)
      - Environment variables:
        - *CM_MLPERF_INFERENCE_RESULTS_VERSION*: `4_0`
      - Workflow:

    </details>


#### Default variations

`_version.4_0`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--results_dir=value`  &rarr;  `CM_MLPERF_INFERENCE_RESULTS_DIR=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "results_dir":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/get-mlperf-inference-results-dir/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/cm4mlops/tree/dev/script/get-mlperf-inference-results-dir/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/get-mlperf-inference-results-dir/_cm.json)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/get-mlperf-inference-results-dir/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/cm4mlops/tree/dev/script/get-mlperf-inference-results-dir/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/get-mlperf-inference-results-dir/_cm.json)

___
### Script output
`cmr "get mlperf inference results dir directory [,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `CM_MLPERF_INFERENCE_RESULTS_DIR`
* `CM_MLPERF_INFERENCE_RESULTS_VERSION`
#### New environment keys auto-detected from customize

* `CM_MLPERF_INFERENCE_RESULTS_DIR`