# Build IPEX from sources
Automatically generated README for this automation recipe: **install-ipex-from-src**

Category: **[Compiler automation](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/install-ipex-from-src/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "install get src from.src ipex src-ipex" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=install,get,src,from.src,ipex,src-ipex`

    `cm run script --tags=install,get,src,from.src,ipex,src-ipex[,variations] `

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "install get src from.src ipex src-ipex"`

    `cmr "install get src from.src ipex src-ipex [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'install,get,src,from.src,ipex,src-ipex'
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

    `cm docker script "install get src from.src ipex src-ipex[variations]" `

___


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_branch.#`
      - Environment variables:
        - *CM_GIT_CHECKOUT*: `#`
      - Workflow:
    * `_for-intel-mlperf-inference-v3.1-gptj`
      - Environment variables:
        - *CM_CONDA_ENV*: `yes`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,conda,_name.gptj-pt
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
           * get,generic,conda-package,_package.typing-extensions,_source.conda-forge
             * CM names: `--adr.['conda-package', 'typing-extensions']...`
             - CM script: [install-generic-conda-package](https://github.com/mlcommons/cm4mlops/tree/master/script/install-generic-conda-package)
           * get,generic,conda-package,_package.sympy,_source.conda-forge
             * CM names: `--adr.['conda-package', 'sympy']...`
             - CM script: [install-generic-conda-package](https://github.com/mlcommons/cm4mlops/tree/master/script/install-generic-conda-package)
           * install,llvm,src,_for-intel-mlperf-inference-v3.1-gptj
             - CM script: [install-llvm-src](https://github.com/mlcommons/cm4mlops/tree/master/script/install-llvm-src)
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
    * **`_repo.https://github.com/intel/intel-extension-for-pytorch`** (default)
      - Environment variables:
        - *CM_GIT_URL*: `https://github.com/intel/intel-extension-for-pytorch`
      - Workflow:

    </details>


#### Default variations

`_repo.https://github.com/intel/intel-extension-for-pytorch`

##### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/install-ipex-from-src/run.sh)
=== "Windows"

No run file exists for Windows
___
#### Script output
`cmr "install get src from.src ipex src-ipex [,variations]"  -j`