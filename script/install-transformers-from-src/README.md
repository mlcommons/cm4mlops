Automatically generated README for this automation recipe: **install-transformers-from-src**

Category: **Compiler automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=install-transformers-from-src,88512c48ea5c4186) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@cm4mlops](https://github.com/mlcommons/cm4mlops/tree/dev)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/cm4mlops/tree/dev/script/install-transformers-from-src)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *install,src,from.src,transformers,src-transformers*
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

````cmr "install src from.src transformers src-transformers" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=install,src,from.src,transformers,src-transformers`

`cm run script --tags=install,src,from.src,transformers,src-transformers[,variations] `

*or*

`cmr "install src from.src transformers src-transformers"`

`cmr "install src from.src transformers src-transformers [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'install,src,from.src,transformers,src-transformers'
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

```cmr "cm gui" --script="install,src,from.src,transformers,src-transformers"```

#### Run this script via Docker (beta)

`cm docker script "install src from.src transformers src-transformers[variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_branch.#`
      - Environment variables:
        - *CM_GIT_CHECKOUT*: `#`
      - Workflow:
    * `_for-intel-mlperf-inference-v3.1-bert`
      - Environment variables:
        - *CM_CONDA_ENV*: `yes`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,conda,_name.bert-pt
             * CM names: `--adr.['conda']...`
             - CM script: [get-conda](https://github.com/mlcommons/cm4mlops/tree/master/script/get-conda)
           * get,generic,conda-package,_package.python
             * CM names: `--adr.['conda-package', 'python3']...`
             - CM script: [install-generic-conda-package](https://github.com/mlcommons/cm4mlops/tree/master/script/install-generic-conda-package)
           * get,generic,conda-package,_package.wheel,_source.conda-forge
             * CM names: `--adr.['conda-package', 'wheel']...`
             - CM script: [install-generic-conda-package](https://github.com/mlcommons/cm4mlops/tree/master/script/install-generic-conda-package)
           * get,generic,conda-package,_package.setuptools,_source.conda-forge
             * CM names: `--adr.['conda-package', 'setuptools']...`
             - CM script: [install-generic-conda-package](https://github.com/mlcommons/cm4mlops/tree/master/script/install-generic-conda-package)
    * `_sha.#`
      - Environment variables:
        - *CM_GIT_CHECKOUT_SHA*: `#`
      - Workflow:
    * `_tag.#`
      - Environment variables:
        - *CM_GIT_CHECKOUT_TAG*: `#`
      - Workflow:

    </details>


  * Group "**repo**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_repo.#`
      - Environment variables:
        - *CM_GIT_URL*: `#`
      - Workflow:
    * **`_repo.https://github.com/pytorch/pytorch`** (default)
      - Environment variables:
        - *CM_GIT_URL*: `https://github.com/huggingface/transformers`
      - Workflow:

    </details>


#### Default variations

`_repo.https://github.com/pytorch/pytorch`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/install-transformers-from-src/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/cm4mlops/tree/master/script/detect-os)
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/cm4mlops/tree/master/script/detect-cpu)
     * get,python3
       * Skip this dependenecy only if all ENV vars are set:<br>
`{'CM_CONDA_ENV': ['yes']}`
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/cm4mlops/tree/master/script/get-python3)
     * get,pytorch,from.src
       * Skip this dependenecy only if all ENV vars are set:<br>
`{'CM_CONDA_ENV': ['yes']}`
       * CM names: `--adr.['pytorch']...`
       - CM script: [install-pytorch-from-src](https://github.com/mlcommons/cm4mlops/tree/master/script/install-pytorch-from-src)
     * get,git,repo
       * CM names: `--adr.['transformers-src-repo']...`
       - CM script: [get-git-repo](https://github.com/mlcommons/cm4mlops/tree/master/script/get-git-repo)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/cm4mlops/tree/dev/script/install-transformers-from-src/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/install-transformers-from-src/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/dev/script/install-transformers-from-src/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/install-transformers-from-src/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/install-transformers-from-src/_cm.json)

___
### Script output
`cmr "install src from.src transformers src-transformers [,variations]"  -j`
#### New environment keys (filter)

* `CM_TRANSFORMERS_*`
#### New environment keys auto-detected from customize
