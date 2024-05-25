# get-preprocessed-dataset-kits19
Automatically generated README for this automation recipe: **get-preprocessed-dataset-kits19**

Category: **[AI/ML datasets](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-preprocessed-dataset-kits19/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get dataset medical-imaging kits19 preprocessed" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=get,dataset,medical-imaging,kits19,preprocessed`

    `cm run script --tags=get,dataset,medical-imaging,kits19,preprocessed[,variations] [--input_flags]`

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "get dataset medical-imaging kits19 preprocessed"`

    `cmr "get dataset medical-imaging kits19 preprocessed [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,dataset,medical-imaging,kits19,preprocessed'
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

    `cm docker script "get dataset medical-imaging kits19 preprocessed[variations]" [--input_flags]`

___


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_nvidia`
      - Environment variables:
        - *CM_PREPROCESSING_BY_NVIDIA*: `yes`
      - Workflow:

    </details>


  * Group "**dataset-count**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_1`
      - Environment variables:
        - *CM_DATASET_SIZE*: `1`
      - Workflow:
    * `_5`
      - Environment variables:
        - *CM_DATASET_SIZE*: `5`
      - Workflow:
    * `_50`
      - Environment variables:
        - *CM_DATASET_SIZE*: `50`
      - Workflow:
    * `_500`
      - Environment variables:
        - *CM_DATASET_SIZE*: `500`
      - Workflow:
    * `_full`
      - Environment variables:
        - *CM_DATASET_SIZE*: ``
      - Workflow:

    </details>


  * Group "**dataset-precision**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_fp32`** (default)
      - Environment variables:
        - *CM_DATASET_DTYPE*: `fp32`
      - Workflow:
    * `_int8`
      - Environment variables:
        - *CM_DATASET_DTYPE*: `int8`
      - Workflow:

    </details>


  * Group "**dataset-type**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_calibration`
      - Environment variables:
        - *CM_DATASET_PATH*: `<<<CM_CALIBRATION_DATASET_PATH>>>`
      - Workflow:
    * **`_validation`** (default)
      - Workflow:

    </details>


#### Default variations

`_fp32,_validation`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--dir=value`  &rarr;  `CM_DATASET_PREPROCESSED_PATH=value`
* `--threads=value`  &rarr;  `CM_NUM_PREPROCESS_THREADS=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "dir":...}
```

</details>

#### Default environment


These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_DATASET: `kits19`
* CM_DATASET_DTYPE: `fp32`



##### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-preprocessed-dataset-kits19/run.sh)
=== "Windows"

No run file exists for Windows
___
#### Script output
`cmr "get dataset medical-imaging kits19 preprocessed [,variations]" [--input_flags] -j`