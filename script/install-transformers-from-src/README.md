# Build transformers from sources
Automatically generated README for this automation recipe: **install-transformers-from-src**

Category: **[Compiler automation](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/install-transformers-from-src/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "install src from.src transformers src-transformers" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=install,src,from.src,transformers,src-transformers`

    `cm run script --tags=install,src,from.src,transformers,src-transformers[,variations] `

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "install src from.src transformers src-transformers"`

    `cmr "install src from.src transformers src-transformers [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


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


=== "Docker"
    ##### Run this script via Docker (beta)

    `cm docker script "install src from.src transformers src-transformers[variations]" `

___


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

##### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/install-transformers-from-src/run.sh)
=== "Windows"

No run file exists for Windows
___
#### Script output
`cmr "install src from.src transformers src-transformers [,variations]"  -j`