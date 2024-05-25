# get-dlrm-data-mlperf-inference
Automatically generated README for this automation recipe: **get-dlrm-data-mlperf-inference**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dlrm-data-mlperf-inference/_cm.yaml)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get dlrm data mlperf inference" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=get,dlrm,data,mlperf,inference`

    `cm run script --tags=get,dlrm,data,mlperf,inference[,variations] [--input_flags]`

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "get dlrm data mlperf inference"`

    `cmr "get dlrm data mlperf inference [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,dlrm,data,mlperf,inference'
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

    `cm docker script "get dlrm data mlperf inference[variations]" [--input_flags]`

___


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_intel`
      - Environment variables:
        - *CM_DLRM_DATA_VARIATION*: `intel`
      - Workflow:
    * `_nvidia`
      - Environment variables:
        - *CM_DLRM_DATA_VARIATION*: `nvidia`
      - Workflow:

    </details>


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--dlrm_data_path=value`  &rarr;  `CM_DLRM_DATA_PATH=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "dlrm_data_path":...}
```

</details>


##### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dlrm-data-mlperf-inference/run.sh)
=== "Windows"

No run file exists for Windows
___
#### Script output
`cmr "get dlrm data mlperf inference [,variations]" [--input_flags] -j`