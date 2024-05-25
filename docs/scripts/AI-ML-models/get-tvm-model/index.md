# get-tvm-model
Automatically generated README for this automation recipe: **get-tvm-model**

Category: **[AI/ML models](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-tvm-model/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-tvm-model/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get ml-model-tvm tvm-model" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=get,ml-model-tvm,tvm-model`

    `cm run script --tags=get,ml-model-tvm,tvm-model[,variations] `

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "get ml-model-tvm tvm-model"`

    `cmr "get ml-model-tvm tvm-model [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ml-model-tvm,tvm-model'
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

    `cm docker script "get ml-model-tvm tvm-model[variations]" `

___


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_tune-model`
      - Environment variables:
        - *CM_TUNE_TVM_MODEL*: `yes`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_xgboost
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/cm4mlops/tree/master/script/get-generic-python-lib)
           * get,generic-python-lib,_pandas
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/cm4mlops/tree/master/script/get-generic-python-lib)
           * get,generic-python-lib,_tornado
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/cm4mlops/tree/master/script/get-generic-python-lib)

    </details>


  * Group "**batchsize**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_batch_size.#`
      - Environment variables:
        - *CM_ML_MODEL_MAX_BATCH_SIZE*: `#`
      - Workflow:

    </details>


  * Group "**frontend**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_onnx`** (default)
      - Environment variables:
        - *CM_TVM_FRONTEND_FRAMEWORK*: `onnx`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_onnx
             * CM names: `--adr.['onnx']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/cm4mlops/tree/master/script/get-generic-python-lib)
    * `_pytorch`
      - Aliases: `_torch`
      - Environment variables:
        - *CM_TVM_FRONTEND_FRAMEWORK*: `pytorch`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_torch
             * CM names: `--adr.['pytorch', 'torch']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/cm4mlops/tree/master/script/get-generic-python-lib)
           * get,generic-python-lib,_torchvision
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/cm4mlops/tree/master/script/get-generic-python-lib)
    * `_tensorflow`
      - Aliases: `_tf`
      - Environment variables:
        - *CM_TVM_FRONTEND_FRAMEWORK*: `tensorflow`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_tensorflow
             * CM names: `--adr.['tensorflow']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/cm4mlops/tree/master/script/get-generic-python-lib)
    * `_tflite`
      - Environment variables:
        - *CM_TVM_FRONTEND_FRAMEWORK*: `tflite`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_tflite
             * CM names: `--adr.['tflite']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/cm4mlops/tree/master/script/get-generic-python-lib)

    </details>


  * Group "**model**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_model.#`
      - Environment variables:
        - *CM_ML_MODEL*: `#`
      - Workflow:

    </details>


  * Group "**precision**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_fp32`** (default)
      - Workflow:
    * `_int8`
      - Workflow:
    * `_uint8`
      - Workflow:

    </details>


  * Group "**runtime**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_graph_executor`
      - Environment variables:
        - *CM_TVM_USE_VM*: `no`
      - Workflow:
    * **`_virtual_machine`** (default)
      - Environment variables:
        - *CM_TVM_USE_VM*: `yes`
      - Workflow:

    </details>


#### Default variations

`_fp32,_onnx,_virtual_machine`
#### Default environment


These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_ML_MODEL_MAX_BATCH_SIZE: `1`
* CM_TUNE_TVM_MODEL: `no`
* CM_TVM_USE_VM: `yes`
* CM_TVM_FRONTEND_FRAMEWORK: `onnx`



##### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-tvm-model/run.sh)
=== "Windows"

No run file exists for Windows
___
#### Script output
`cmr "get ml-model-tvm tvm-model [,variations]"  -j`