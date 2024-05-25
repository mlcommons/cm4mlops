# get-preprocessed-dataset-criteo
Automatically generated README for this automation recipe: **get-preprocessed-dataset-criteo**

Category: **[AI/ML datasets](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-preprocessed-dataset-criteo/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-preprocessed-dataset-criteo/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get dataset criteo recommendation dlrm preprocessed" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=get,dataset,criteo,recommendation,dlrm,preprocessed`

    `cm run script --tags=get,dataset,criteo,recommendation,dlrm,preprocessed[,variations] [--input_flags]`

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "get dataset criteo recommendation dlrm preprocessed"`

    `cmr "get dataset criteo recommendation dlrm preprocessed [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,dataset,criteo,recommendation,dlrm,preprocessed'
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

    `cm docker script "get dataset criteo recommendation dlrm preprocessed[variations]" [--input_flags]`

___


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_1`
      - Environment variables:
        - *CM_DATASET_SIZE*: `1`
      - Workflow:
    * `_50`
      - Environment variables:
        - *CM_DATASET_SIZE*: `50`
      - Workflow:
    * `_fake`
      - Environment variables:
        - *CM_CRITEO_FAKE*: `yes`
      - Workflow:
    * `_full`
      - Workflow:
    * `_validation`
      - Workflow:

    </details>


  * Group "**type**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_multihot`** (default)
      - Environment variables:
        - *CM_DATASET_CRITEO_MULTIHOT*: `yes`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,mlperf,training,src
             * CM names: `--adr.['mlperf-training', 'training-src']...`
             - CM script: [get-mlperf-training-src](https://github.com/mlcommons/cm4mlops/tree/master/script/get-mlperf-training-src)
           * get,generic-python-lib,_package.typing_inspect
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/cm4mlops/tree/master/script/get-generic-python-lib)
           * get,generic-python-lib,_package.iopath
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/cm4mlops/tree/master/script/get-generic-python-lib)
           * get,generic-python-lib,_package.fbgemm_gpu
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/cm4mlops/tree/master/script/get-generic-python-lib)
           * get,generic-python-lib,_package.torchrec
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/cm4mlops/tree/master/script/get-generic-python-lib)
           * get,generic-python-lib,_package.pyre_extensions
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/cm4mlops/tree/master/script/get-generic-python-lib)

    </details>


#### Default variations

`_multihot`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--dir=value`  &rarr;  `CM_DATASET_PREPROCESSED_PATH=value`
* `--output_dir=value`  &rarr;  `CM_DATASET_PREPROCESSED_OUTPUT_PATH=value`
* `--threads=value`  &rarr;  `CM_NUM_PREPROCESS_THREADS=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "dir":...}
```

</details>


##### Native script being run
=== "Linux/macOS"
     * [run-multihot.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-preprocessed-dataset-criteo/run-multihot.sh)
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-preprocessed-dataset-criteo/run.sh)
=== "Windows"

No run file exists for Windows
___
#### Script output
`cmr "get dataset criteo recommendation dlrm preprocessed [,variations]" [--input_flags] -j`