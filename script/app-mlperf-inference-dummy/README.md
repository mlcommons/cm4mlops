# app-mlperf-inference-dummy
Automatically generated README for this automation recipe: **app-mlperf-inference-dummy**

Category: **[Modular MLPerf benchmarks](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/app-mlperf-inference-dummy/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "reproduce mlcommons mlperf inference harness dummy-harness dummy" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=reproduce,mlcommons,mlperf,inference,harness,dummy-harness,dummy`

    `cm run script --tags=reproduce,mlcommons,mlperf,inference,harness,dummy-harness,dummy[,variations] [--input_flags]`

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "reproduce mlcommons mlperf inference harness dummy-harness dummy"`

    `cmr "reproduce mlcommons mlperf inference harness dummy-harness dummy [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'reproduce,mlcommons,mlperf,inference,harness,dummy-harness,dummy'
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

    `cm docker script "reproduce mlcommons mlperf inference harness dummy-harness dummy[variations]" [--input_flags]`

___


#### Variations

  * *Internal group (variations should not be selected manually)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_bert_`
      - Workflow:
    * `_gptj_`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,ml-model,gptj
             * CM names: `--adr.['gptj-model']...`
             - CM script: [get-ml-model-gptj](https://github.com/mlcommons/cm4mlops/tree/master/script/get-ml-model-gptj)
           * get,dataset,cnndm,_validation
             - CM script: [get-dataset-cnndm](https://github.com/mlcommons/cm4mlops/tree/master/script/get-dataset-cnndm)
    * `_llama2-70b_`
      - Workflow:

    </details>


  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_pytorch,cpu`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_torch
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/cm4mlops/tree/master/script/get-generic-python-lib)
    * `_pytorch,cuda`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_torch_cuda
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/cm4mlops/tree/master/script/get-generic-python-lib)
    * `_singlestream,resnet50`
      - Workflow:
    * `_singlestream,retinanet`
      - Workflow:

    </details>


  * Group "**backend**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_pytorch`** (default)
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `pytorch`
      - Workflow:

    </details>


  * Group "**batch-size**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_bs.#`
      - Workflow:

    </details>


  * Group "**device**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_cpu`** (default)
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `cpu`
      - Workflow:
    * `_cuda`
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `gpu`
        - *CM_MLPERF_DEVICE_LIB_NAMESPEC*: `cudart`
      - Workflow:

    </details>


  * Group "**loadgen-scenario**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_multistream`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_SCENARIO*: `MultiStream`
      - Workflow:
    * `_offline`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_SCENARIO*: `Offline`
      - Workflow:
    * `_server`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_SCENARIO*: `Server`
      - Workflow:
    * `_singlestream`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_SCENARIO*: `SingleStream`
      - Workflow:

    </details>


  * Group "**model**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_bert-99`
      - Environment variables:
        - *CM_MODEL*: `bert-99`
        - *CM_SQUAD_ACCURACY_DTYPE*: `float32`
      - Workflow:
    * `_bert-99.9`
      - Environment variables:
        - *CM_MODEL*: `bert-99.9`
      - Workflow:
    * `_gptj-99`
      - Environment variables:
        - *CM_MODEL*: `gptj-99`
        - *CM_SQUAD_ACCURACY_DTYPE*: `float32`
      - Workflow:
    * `_gptj-99.9`
      - Environment variables:
        - *CM_MODEL*: `gptj-99.9`
      - Workflow:
    * `_llama2-70b-99`
      - Environment variables:
        - *CM_MODEL*: `llama2-70b-99`
      - Workflow:
    * `_llama2-70b-99.9`
      - Environment variables:
        - *CM_MODEL*: `llama2-70b-99.9`
      - Workflow:
    * **`_resnet50`** (default)
      - Environment variables:
        - *CM_MODEL*: `resnet50`
      - Workflow:
    * `_retinanet`
      - Environment variables:
        - *CM_MODEL*: `retinanet`
      - Workflow:

    </details>


  * Group "**precision**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_fp16`
      - Workflow:
    * `_fp32`
      - Workflow:
    * `_uint8`
      - Workflow:

    </details>


#### Default variations

`_cpu,_pytorch,_resnet50`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--count=value`  &rarr;  `CM_MLPERF_LOADGEN_QUERY_COUNT=value`
* `--max_batchsize=value`  &rarr;  `CM_MLPERF_LOADGEN_MAX_BATCHSIZE=value`
* `--mlperf_conf=value`  &rarr;  `CM_MLPERF_CONF=value`
* `--mode=value`  &rarr;  `CM_MLPERF_LOADGEN_MODE=value`
* `--multistream_target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_MULTISTREAM_TARGET_LATENCY=value`
* `--offline_target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_OFFLINE_TARGET_QPS=value`
* `--output_dir=value`  &rarr;  `CM_MLPERF_OUTPUT_DIR=value`
* `--performance_sample_count=value`  &rarr;  `CM_MLPERF_LOADGEN_PERFORMANCE_SAMPLE_COUNT=value`
* `--rerun=value`  &rarr;  `CM_RERUN=value`
* `--results_repo=value`  &rarr;  `CM_MLPERF_INFERENCE_RESULTS_REPO=value`
* `--scenario=value`  &rarr;  `CM_MLPERF_LOADGEN_SCENARIO=value`
* `--server_target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_SERVER_TARGET_QPS=value`
* `--singlestream_target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_SINGLESTREAM_TARGET_LATENCY=value`
* `--skip_preprocess=value`  &rarr;  `CM_SKIP_PREPROCESS_DATASET=value`
* `--skip_preprocessing=value`  &rarr;  `CM_SKIP_PREPROCESS_DATASET=value`
* `--target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_TARGET_LATENCY=value`
* `--target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_TARGET_QPS=value`
* `--user_conf=value`  &rarr;  `CM_MLPERF_USER_CONF=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "count":...}
```

</details>

#### Default environment


These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_MLPERF_LOADGEN_SCENARIO: `Offline`
* CM_MLPERF_LOADGEN_MODE: `performance`
* CM_SKIP_PREPROCESS_DATASET: `no`
* CM_SKIP_MODEL_DOWNLOAD: `no`
* CM_MLPERF_SUT_NAME_IMPLEMENTATION_PREFIX: `dummy_harness`
* CM_MLPERF_SKIP_RUN: `no`



##### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/app-mlperf-inference-dummy/run.sh)
=== "Windows"

No run file exists for Windows
___
#### Script output
`cmr "reproduce mlcommons mlperf inference harness dummy-harness dummy [,variations]" [--input_flags] -j`