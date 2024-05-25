# Build pytorch kineto from sources
Automatically generated README for this automation recipe: **install-pytorch-kineto-from-src**

Category: **[Compiler automation](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/install-pytorch-kineto-from-src/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "install get src from.src pytorch-kineto kineto src-pytorch-kineto" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=install,get,src,from.src,pytorch-kineto,kineto,src-pytorch-kineto`

    `cm run script --tags=install,get,src,from.src,pytorch-kineto,kineto,src-pytorch-kineto[,variations] `

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "install get src from.src pytorch-kineto kineto src-pytorch-kineto"`

    `cmr "install get src from.src pytorch-kineto kineto src-pytorch-kineto [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'install,get,src,from.src,pytorch-kineto,kineto,src-pytorch-kineto'
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

    `cm docker script "install get src from.src pytorch-kineto kineto src-pytorch-kineto[variations]" `

___


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_branch.#`
      - Environment variables:
        - *CM_GIT_CHECKOUT*: `#`
      - Workflow:
    * `_cuda`
      - Environment variables:
        - *CUDA_HOME*: `<<<CM_CUDA_INSTALLED_PATH>>>`
        - *CUDA_NVCC_EXECUTABLE*: `<<<CM_NVCC_BIN_WITH_PATH>>>`
        - *CUDNN_INCLUDE_PATH*: `<<<CM_CUDA_PATH_INCLUDE_CUDNN>>>`
        - *CUDNN_LIBRARY_PATH*: `<<<CM_CUDA_PATH_LIB_CUDNN>>>`
        - *TORCH_CUDA_ARCH_LIST*: `Ampere Ada Hopper`
        - *TORCH_CXX_FLAGS*: `-D_GLIBCXX_USE_CXX11_ABI=1`
        - *USE_CUDA*: `1`
        - *USE_CUDNN*: `1`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,cuda,_cudnn
             * CM names: `--adr.['cuda']...`
             - CM script: [get-cuda](https://github.com/mlcommons/cm4mlops/tree/master/script/get-cuda)
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
    * **`_repo.https://github.com/pytorch/kineto`** (default)
      - Environment variables:
        - *CM_GIT_URL*: `https://github.com/pytorch/kineto`
      - Workflow:

    </details>


#### Default variations

`_repo.https://github.com/pytorch/kineto`

##### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/install-pytorch-kineto-from-src/run.sh)
=== "Windows"

No run file exists for Windows
___
#### Script output
`cmr "install get src from.src pytorch-kineto kineto src-pytorch-kineto [,variations]"  -j`