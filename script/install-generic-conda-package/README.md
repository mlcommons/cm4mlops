Automatically generated README for this automation recipe: **install-generic-conda-package**

Category: **Python automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=install-generic-conda-package,d9275487f5314195) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@cm4mlops](https://github.com/mlcommons/cm4mlops/tree/dev)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/cm4mlops/tree/dev/script/install-generic-conda-package)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,install,generic,generic-conda-lib,conda-lib,conda-package,generic-conda-package*
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

````cmr "get install generic generic-conda-lib conda-lib conda-package generic-conda-package" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,install,generic,generic-conda-lib,conda-lib,conda-package,generic-conda-package`

`cm run script --tags=get,install,generic,generic-conda-lib,conda-lib,conda-package,generic-conda-package[,variations] `

*or*

`cmr "get install generic generic-conda-lib conda-lib conda-package generic-conda-package"`

`cmr "get install generic generic-conda-lib conda-lib conda-package generic-conda-package [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,install,generic,generic-conda-lib,conda-lib,conda-package,generic-conda-package'
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

```cmr "cm gui" --script="get,install,generic,generic-conda-lib,conda-lib,conda-package,generic-conda-package"```

#### Run this script via Docker (beta)

`cm docker script "get install generic generic-conda-lib conda-lib conda-package generic-conda-package[variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_name.#`
      - Workflow:
    * `_package.#`
      - Environment variables:
        - *CM_CONDA_PKG_NAME*: `#`
      - Workflow:

    </details>


  * Group "**package-source**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_source.#`
      - Environment variables:
        - *CM_CONDA_PKG_SRC*: `#`
      - Workflow:

    </details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/install-generic-conda-package/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/cm4mlops/tree/master/script/detect-os)
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/cm4mlops/tree/master/script/detect-cpu)
     * get,conda
       * CM names: `--adr.['conda']...`
       - CM script: [get-conda](https://github.com/mlcommons/cm4mlops/tree/master/script/get-conda)
     * get,conda
       * CM names: `--adr.['conda']...`
       - CM script: [get-conda](https://github.com/mlcommons/cm4mlops/tree/master/script/get-conda)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/cm4mlops/tree/dev/script/install-generic-conda-package/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/install-generic-conda-package/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/dev/script/install-generic-conda-package/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/install-generic-conda-package/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/cm4mlops/tree/dev/script/install-generic-conda-package/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/install-generic-conda-package/_cm.json)

___
### Script output
`cmr "get install generic generic-conda-lib conda-lib conda-package generic-conda-package [,variations]"  -j`
#### New environment keys (filter)

* `CM_PYTHONLIB_*`
#### New environment keys auto-detected from customize
