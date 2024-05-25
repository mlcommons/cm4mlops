# prepare-training-data-resnet
Automatically generated README for this automation recipe: **prepare-training-data-resnet**

Category: **[MLPerf benchmark support](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/prepare-training-data-resnet/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "prepare mlperf training data input resnet" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=prepare,mlperf,training,data,input,resnet`

    `cm run script --tags=prepare,mlperf,training,data,input,resnet[,variations] [--input_flags]`

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "prepare mlperf training data input resnet"`

    `cmr "prepare mlperf training data input resnet [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'prepare,mlperf,training,data,input,resnet'
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

    `cm docker script "prepare mlperf training data input resnet[variations]" [--input_flags]`

___


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_mxnet.#`
      - Environment variables:
        - *CM_MXNET_VERSION*: `#`
      - Workflow:

    </details>


  * Group "**implementation**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_nvidia`** (default)
      - Environment variables:
        - *CM_TMP_VARIATION*: `nvidia`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,mlperf,training,nvidia,code
             * CM names: `--adr.['nvidia-training-code']...`
             - CM script: [get-mlperf-training-nvidia-code](https://github.com/mlcommons/cm4mlops/tree/master/script/get-mlperf-training-nvidia-code)
           * get,git,repo,_repo.https://github.com/NVIDIA/DeepLearningExamples,_sha.81ee705868a11d6fe18c12d237abe4a08aab5fd6
             - CM script: [get-git-repo](https://github.com/mlcommons/cm4mlops/tree/master/script/get-git-repo)
    * `_reference`
      - Environment variables:
        - *CM_TMP_VARIATION*: `reference`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,mlperf,training,src
             * CM names: `--adr.['mlperf-training-src']...`
             - CM script: [get-mlperf-training-src](https://github.com/mlcommons/cm4mlops/tree/master/script/get-mlperf-training-src)
           * get,python3
             * CM names: `--adr.['python3']...`
             - CM script: [get-python3](https://github.com/mlcommons/cm4mlops/tree/master/script/get-python3)
           * get,generic-python-lib,_tensorflow
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/cm4mlops/tree/master/script/get-generic-python-lib)
           * get,generic-python-lib,_protobuf
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/cm4mlops/tree/master/script/get-generic-python-lib)

    </details>


#### Default variations

`_nvidia`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--data_dir=value`  &rarr;  `CM_DATA_DIR=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "data_dir":...}
```

</details>


##### Native script being run
=== "Linux/macOS"
     * [run-nvidia.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/prepare-training-data-resnet/run-nvidia.sh)
     * [run-reference.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/prepare-training-data-resnet/run-reference.sh)
=== "Windows"

No run file exists for Windows
___
#### Script output
`cmr "prepare mlperf training data input resnet [,variations]" [--input_flags] -j`