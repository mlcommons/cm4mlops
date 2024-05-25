# reproduce-mlperf-training-nvidia
Automatically generated README for this automation recipe: **reproduce-mlperf-training-nvidia**

Category: **[Reproduce MLPerf benchmarks](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/reproduce-mlperf-training-nvidia/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "reproduce mlcommons mlperf train training nvidia-training nvidia" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=reproduce,mlcommons,mlperf,train,training,nvidia-training,nvidia`

    `cm run script --tags=reproduce,mlcommons,mlperf,train,training,nvidia-training,nvidia[,variations] [--input_flags]`

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "reproduce mlcommons mlperf train training nvidia-training nvidia"`

    `cmr "reproduce mlcommons mlperf train training nvidia-training nvidia [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'reproduce,mlcommons,mlperf,train,training,nvidia-training,nvidia'
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

    `cm docker script "reproduce mlcommons mlperf train training nvidia-training nvidia[variations]" [--input_flags]`

___


#### Variations

  * Group "**benchmark**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_resnet`
      - Environment variables:
        - *CM_MLPERF_TRAINING_BENCHMARK*: `resnet`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * prepare,mlperf,training,resnet,_nvidia
             * CM names: `--adr.['prepare-training-data', 'nvidia-training-data']...`
             - CM script: [prepare-training-data-resnet](https://github.com/mlcommons/cm4mlops/tree/master/script/prepare-training-data-resnet)
           * get,nvidia,training,code
             * CM names: `--adr.['nvidia-training-code']...`
             - CM script: [get-mlperf-training-nvidia-code](https://github.com/mlcommons/cm4mlops/tree/master/script/get-mlperf-training-nvidia-code)

    </details>


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--results_dir=value`  &rarr;  `CM_MLPERF_RESULTS_DIR=value`
* `--system_conf_name=value`  &rarr;  `CM_MLPERF_NVIDIA_TRAINING_SYSTEM_CONF_NAME=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "results_dir":...}
```

</details>

#### Versions
* `r2.1`
* `r3.0`

##### Native script being run
=== "Linux/macOS"
     * [run-resnet.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/reproduce-mlperf-training-nvidia/run-resnet.sh)
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/reproduce-mlperf-training-nvidia/run.sh)
=== "Windows"

No run file exists for Windows
___
#### Script output
`cmr "reproduce mlcommons mlperf train training nvidia-training nvidia [,variations]" [--input_flags] -j`