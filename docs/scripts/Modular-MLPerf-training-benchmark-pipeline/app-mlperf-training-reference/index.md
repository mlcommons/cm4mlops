# app-mlperf-training-reference
Automatically generated README for this automation recipe: **app-mlperf-training-reference**

Category: **[Modular MLPerf training benchmark pipeline](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/app-mlperf-training-reference/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "app vision language mlcommons mlperf training reference ref" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=app,vision,language,mlcommons,mlperf,training,reference,ref`

    `cm run script --tags=app,vision,language,mlcommons,mlperf,training,reference,ref[,variations] [--input_flags]`

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "app vision language mlcommons mlperf training reference ref"`

    `cmr "app vision language mlcommons mlperf training reference ref [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'app,vision,language,mlcommons,mlperf,training,reference,ref'
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

    `cm docker script "app vision language mlcommons mlperf training reference ref[variations]" [--input_flags]`

___


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_bert`
      - Environment variables:
        - *CM_MLPERF_MODEL*: `bert`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_protobuf
             * Enable this dependency only if all ENV vars are set:<br>
`{'CM_MLPERF_BACKEND': ['tf', 'tflite']}`
             * CM names: `--adr.['protobuf']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/cm4mlops/tree/master/script/get-generic-python-lib)
           * get,generic-python-lib,_torch
             * CM names: `--adr.['ml-engine-pytorch']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/cm4mlops/tree/master/script/get-generic-python-lib)

    </details>


  * Group "**device**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_cuda`** (default)
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `cuda`
        - *USE_CUDA*: `True`
      - Workflow:
    * `_tpu`
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `tpu`
        - *CUDA_VISIBLE_DEVICES*: ``
        - *USE_CUDA*: `False`
      - Workflow:

    </details>


  * Group "**framework**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_pytorch`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `pytorch`
        - *CM_MLPERF_BACKEND_VERSION*: `<<<CM_TORCH_VERSION>>>`
      - Workflow:
    * `_tf`
      - Aliases: `_tensorflow`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `tf`
        - *CM_MLPERF_BACKEND_VERSION*: `<<<CM_TENSORFLOW_VERSION>>>`
      - Workflow:

    </details>


#### Default variations

`_cuda`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--clean=value`  &rarr;  `CM_MLPERF_CLEAN_SUBMISSION_DIR=value`
* `--docker=value`  &rarr;  `CM_RUN_DOCKER_CONTAINER=value`
* `--hw_name=value`  &rarr;  `CM_HW_NAME=value`
* `--model=value`  &rarr;  `CM_MLPERF_CUSTOM_MODEL_PATH=value`
* `--num_threads=value`  &rarr;  `CM_NUM_THREADS=value`
* `--output_dir=value`  &rarr;  `OUTPUT_BASE_DIR=value`
* `--rerun=value`  &rarr;  `CM_RERUN=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "clean":...}
```

</details>

#### Default environment


These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_MLPERF_SUT_NAME_IMPLEMENTATION_PREFIX: `reference`
* CM_MLPERF_SUT_NAME_RUN_CONFIG_SUFFIX: ``



##### Native script being run
=== "Linux/macOS"
     * [run-bert-training.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/app-mlperf-training-reference/run-bert-training.sh)
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/app-mlperf-training-reference/run.sh)
=== "Windows"

No run file exists for Windows
___
#### Script output
`cmr "app vision language mlcommons mlperf training reference ref [,variations]" [--input_flags] -j`