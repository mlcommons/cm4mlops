# get-cuda
Automatically generated README for this automation recipe: **get-cuda**

Category: **[CUDA automation](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-cuda/README-extra.md)


---

# System dependencies

* Download [CUDA toolkit](https://developer.nvidia.com/cuda-toolkit).
* Download [cuDNN](https://developer.nvidia.com/rdp/cudnn-download).
* Download [TensorRT](https://developer.nvidia.com/nvidia-tensorrt-8x-download).


* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/get-cuda/_cm.yaml)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get cuda cuda-compiler cuda-lib toolkit lib nvcc get-nvcc get-cuda 46d133d9ef92422d" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=get,cuda,cuda-compiler,cuda-lib,toolkit,lib,nvcc,get-nvcc,get-cuda,46d133d9ef92422d`

    `cm run script --tags=get,cuda,cuda-compiler,cuda-lib,toolkit,lib,nvcc,get-nvcc,get-cuda,46d133d9ef92422d[,variations] [--input_flags]`

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "get cuda cuda-compiler cuda-lib toolkit lib nvcc get-nvcc get-cuda 46d133d9ef92422d"`

    `cmr "get cuda cuda-compiler cuda-lib toolkit lib nvcc get-nvcc get-cuda 46d133d9ef92422d [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,cuda,cuda-compiler,cuda-lib,toolkit,lib,nvcc,get-nvcc,get-cuda,46d133d9ef92422d'
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

    `cm docker script "get cuda cuda-compiler cuda-lib toolkit lib nvcc get-nvcc get-cuda 46d133d9ef92422d[variations]" [--input_flags]`

___


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_cudnn`
      - Environment variables:
        - *CM_CUDA_NEEDS_CUDNN*: `yes`
      - Workflow:
        1. ***Read "post_deps" on other CM scripts***
           * get,nvidia,cudnn
             * CM names: `--adr.['cudnn']...`
             - CM script: [get-cudnn](https://github.com/mlcommons/cm4mlops/tree/master/script/get-cudnn)
    * `_package-manager`
      - Environment variables:
        - *CM_CUDA_PACKAGE_MANAGER_INSTALL*: `yes`
      - Workflow:

    </details>


  * Group "**installation-mode**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_lib-only`
      - Environment variables:
        - *CM_CUDA_FULL_TOOLKIT_INSTALL*: `no`
        - *CM_TMP_FILE_TO_CHECK_UNIX*: `libcudart.so`
        - *CM_TMP_FILE_TO_CHECK_WINDOWS*: `libcudart.dll`
      - Workflow:
    * **`_toolkit`** (default)
      - Environment variables:
        - *CM_CUDA_FULL_TOOLKIT_INSTALL*: `yes`
        - *CM_TMP_FILE_TO_CHECK_UNIX*: `nvcc`
        - *CM_TMP_FILE_TO_CHECK_WINDOWS*: `nvcc.exe`
      - Workflow:

    </details>


#### Default variations

`_toolkit`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--cudnn_tar_file=value`  &rarr;  `CM_CUDNN_TAR_FILE_PATH=value`
* `--cudnn_tar_path=value`  &rarr;  `CM_CUDNN_TAR_FILE_PATH=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "cudnn_tar_file":...}
```

</details>

#### Default environment


These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_CUDA_PATH_LIB_CUDNN_EXISTS: `no`
* CM_REQUIRE_INSTALL: `no`



##### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-cuda/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/get-cuda/run.bat)
___
#### Script output
`cmr "get cuda cuda-compiler cuda-lib toolkit lib nvcc get-nvcc get-cuda 46d133d9ef92422d [,variations]" [--input_flags] -j`