# benchmark-any-mlperf-inference-implementation
Automatically generated README for this automation recipe: **benchmark-any-mlperf-inference-implementation**

Category: **[MLPerf benchmark support](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/benchmark-any-mlperf-inference-implementation/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "benchmark run natively all inference any mlperf mlperf-implementation implementation mlperf-models" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=benchmark,run,natively,all,inference,any,mlperf,mlperf-implementation,implementation,mlperf-models`

    `cm run script --tags=benchmark,run,natively,all,inference,any,mlperf,mlperf-implementation,implementation,mlperf-models[,variations] [--input_flags]`

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "benchmark run natively all inference any mlperf mlperf-implementation implementation mlperf-models"`

    `cmr "benchmark run natively all inference any mlperf mlperf-implementation implementation mlperf-models [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'benchmark,run,natively,all,inference,any,mlperf,mlperf-implementation,implementation,mlperf-models'
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

    `cm docker script "benchmark run natively all inference any mlperf mlperf-implementation implementation mlperf-models[variations]" [--input_flags]`

___


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_aws-dl2q.24xlarge,qualcomm`
      - Workflow:
    * `_mini,power`
      - Workflow:
    * `_orin,power`
      - Workflow:
    * `_phoenix,nvidia`
      - Workflow:
    * `_phoenix,power`
      - Workflow:
    * `_phoenix,reference`
      - Workflow:
    * `_rb6,power`
      - Workflow:
    * `_rb6,qualcomm`
      - Workflow:
    * `_rpi4,power`
      - Workflow:
    * `_sapphire-rapids.24c,nvidia`
      - Workflow:

    </details>


  * Group "**implementation**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_deepsparse`
      - Environment variables:
        - *DIVISION*: `open`
        - *IMPLEMENTATION*: `deepsparse`
      - Workflow:
    * `_intel`
      - Environment variables:
        - *IMPLEMENTATION*: `intel`
      - Workflow:
    * `_mil`
      - Environment variables:
        - *IMPLEMENTATION*: `mil`
      - Workflow:
    * `_nvidia`
      - Environment variables:
        - *IMPLEMENTATION*: `nvidia-original`
      - Workflow:
    * `_qualcomm`
      - Environment variables:
        - *IMPLEMENTATION*: `qualcomm`
      - Workflow:
    * `_reference`
      - Environment variables:
        - *IMPLEMENTATION*: `reference`
      - Workflow:
    * `_tflite-cpp`
      - Environment variables:
        - *IMPLEMENTATION*: `tflite_cpp`
      - Workflow:

    </details>


  * Group "**power**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_performance-only`** (default)
      - Workflow:
    * `_power`
      - Environment variables:
        - *POWER*: `True`
      - Workflow:

    </details>


  * Group "**sut**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_aws-dl2q.24xlarge`
      - Workflow:
    * `_macbookpro-m1`
      - Environment variables:
        - *CATEGORY*: `edge`
        - *DIVISION*: `closed`
      - Workflow:
    * `_mini`
      - Workflow:
    * `_orin`
      - Workflow:
    * `_orin.32g`
      - Environment variables:
        - *CATEGORY*: `edge`
        - *DIVISION*: `closed`
      - Workflow:
    * `_phoenix`
      - Environment variables:
        - *CATEGORY*: `edge`
        - *DIVISION*: `closed`
      - Workflow:
    * `_rb6`
      - Workflow:
    * `_rpi4`
      - Workflow:
    * `_sapphire-rapids.24c`
      - Environment variables:
        - *CATEGORY*: `edge`
        - *DIVISION*: `closed`
      - Workflow:

    </details>


#### Default variations

`_performance-only`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--backends=value`  &rarr;  `BACKENDS=value`
* `--category=value`  &rarr;  `CATEGORY=value`
* `--devices=value`  &rarr;  `DEVICES=value`
* `--division=value`  &rarr;  `DIVISION=value`
* `--extra_args=value`  &rarr;  `EXTRA_ARGS=value`
* `--models=value`  &rarr;  `MODELS=value`
* `--power_server=value`  &rarr;  `POWER_SERVER=value`
* `--power_server_port=value`  &rarr;  `POWER_SERVER_PORT=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "backends":...}
```

</details>

#### Default environment


These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* DIVISION: `open`
* CATEGORY: `edge`



##### Native script being run
=== "Linux/macOS"
     * [run-template.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/benchmark-any-mlperf-inference-implementation/run-template.sh)
=== "Windows"

No run file exists for Windows
___
#### Script output
`cmr "benchmark run natively all inference any mlperf mlperf-implementation implementation mlperf-models [,variations]" [--input_flags] -j`