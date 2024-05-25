# get-tvm
Automatically generated README for this automation recipe: **get-tvm**

Category: **[AI/ML frameworks](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-tvm/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-tvm/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get tvm get-tvm" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=get,tvm,get-tvm`

    `cm run script --tags=get,tvm,get-tvm[,variations] `

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "get tvm get-tvm"`

    `cmr "get tvm get-tvm [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,tvm,get-tvm'
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

    `cm docker script "get tvm get-tvm[variations]" `

___


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_cuda`
      - Environment variables:
        - *CM_TVM_USE_CUDA*: `yes`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,cuda
             - CM script: [get-cuda](https://github.com/mlcommons/cm4mlops/tree/master/script/get-cuda)
    * `_openmp`
      - Environment variables:
        - *CM_TVM_USE_OPENMP*: `yes`
      - Workflow:

    </details>


  * Group "**installation-type**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_llvm`** (default)
      - Environment variables:
        - *CM_TVM_USE_LLVM*: `yes`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,llvm
             * CM names: `--adr.['llvm']...`
             - CM script: [get-llvm](https://github.com/mlcommons/cm4mlops/tree/master/script/get-llvm)
    * `_pip-install`
      - Environment variables:
        - *CM_TVM_PIP_INSTALL*: `yes`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_apache-tvm
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/cm4mlops/tree/master/script/get-generic-python-lib)

    </details>


#### Default variations

`_llvm`
#### Default environment


These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_GIT_CHECKOUT: `main`
* CM_GIT_URL: `https://github.com/apache/tvm`
* CM_TVM_PIP_INSTALL: `no`


#### Versions
* `main`
* `v0.10.0`
* `v0.7.0`
* `v0.8.0`
* `v0.9.0`

##### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-tvm/run.sh)
=== "Windows"

No run file exists for Windows
___
#### Script output
`cmr "get tvm get-tvm [,variations]"  -j`