# get-mlperf-training-src
Automatically generated README for this automation recipe: **get-mlperf-training-src**

Category: **[MLPerf benchmark support](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-mlperf-training-src/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-mlperf-training-src/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get src source training training-src training-source mlperf mlcommons" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=get,src,source,training,training-src,training-source,mlperf,mlcommons`

    `cm run script --tags=get,src,source,training,training-src,training-source,mlperf,mlcommons[,variations] `

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "get src source training training-src training-source mlperf mlcommons"`

    `cmr "get src source training training-src training-source mlperf mlcommons [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,src,source,training,training-src,training-source,mlperf,mlcommons'
                  'out':'con',
                  ...
                  (other input keys for this script)
                  ...
                 })

    if r['return']>0:
        print (r['error'])

    ```


=== "Docker"
    ##### Run this script via Docker (beta)

    `cm docker script "get src source training training-src training-source mlperf mlcommons[variations]" `

___


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_no-recurse-submodules`
      - Environment variables:
        - *CM_GIT_RECURSE_SUBMODULES*: ``
      - Workflow:
    * `_nvidia-retinanet`
      - Environment variables:
        - *CM_GIT_PATCH_FILENAMES*: `nvidia-retinanet.patch,cpu_load.patch`
      - Workflow:
    * `_patch`
      - Environment variables:
        - *CM_GIT_PATCH*: `yes`
      - Workflow:

    </details>


  * Group "**checkout**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_branch.#`
      - Environment variables:
        - *CM_GIT_CHECKOUT*: `#`
      - Workflow:
    * `_sha.#`
      - Environment variables:
        - *CM_GIT_SHA*: `#`
      - Workflow:
    * `_tag.#`
      - Environment variables:
        - *CM_GIT_CHECKOUT_TAG*: `#`
      - Workflow:

    </details>


  * Group "**git-history**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_full-history`
      - Environment variables:
        - *CM_GIT_DEPTH*: ``
      - Workflow:
    * **`_short-history`** (default)
      - Environment variables:
        - *CM_GIT_DEPTH*: `--depth 5`
      - Workflow:

    </details>


  * Group "**repo**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_repo.#`
      - Environment variables:
        - *CM_GIT_URL*: `#`
      - Workflow:

    </details>


  * Group "**src**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_cknowledge`** (default)
      - Environment variables:
        - *CM_GIT_URL*: `https://github.com/cknowledge/training.git`
      - Workflow:
    * `_mlcommons`
      - Environment variables:
        - *CM_GIT_URL*: `https://github.com/mlcommons/training.git`
      - Workflow:

    </details>


#### Default variations

`_cknowledge,_short-history`
#### Default environment


These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_GIT_CHECKOUT: `master`
* CM_GIT_DEPTH: `--depth 4`
* CM_GIT_PATCH: `no`
* CM_GIT_RECURSE_SUBMODULES: ` --recurse-submodules`
* CM_GIT_CHECKOUT_FOLDER: `training`


#### Versions
Default version: `master`

* `custom`
* `master`

___
#### Script output
`cmr "get src source training training-src training-source mlperf mlcommons [,variations]"  -j`