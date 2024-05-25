# get-dataset-openimages-calibration
Automatically generated README for this automation recipe: **get-dataset-openimages-calibration**

Category: **[AI/ML datasets](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dataset-openimages-calibration/_cm.yaml)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get dataset openimages calibration" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=get,dataset,openimages,calibration`

    `cm run script --tags=get,dataset,openimages,calibration[,variations] `

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "get dataset openimages calibration"`

    `cmr "get dataset openimages calibration [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,dataset,openimages,calibration'
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

    `cm docker script "get dataset openimages calibration[variations]" `

___


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_filter`
      - Environment variables:
        - *CM_CALIBRATE_FILTER*: `yes`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,python3
             * CM names: `--adr.['python', 'python3']...`
             - CM script: [get-python3](https://github.com/mlcommons/cm4mlops/tree/master/script/get-python3)
           * get,openimages,dataset,original,_calibration
             - CM script: [get-dataset-openimages](https://github.com/mlcommons/cm4mlops/tree/master/script/get-dataset-openimages)

    </details>


  * Group "**calibration-option**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_mlperf.option1`** (default)
      - Environment variables:
        - *CM_MLPERF_OPENIMAGES_CALIBRATION_OPTION*: `one`
        - *CM_DOWNLOAD_CHECKSUM1*: `f09719174af3553119e2c621157773a6`
      - Workflow:

    </details>


  * Group "**filter-size**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_filter-size.#`
      - Environment variables:
        - *CM_CALIBRATION_FILTER_SIZE*: `#`
      - Workflow:
    * `_filter-size.400`
      - Environment variables:
        - *CM_CALIBRATION_FILTER_SIZE*: `400`
      - Workflow:

    </details>


#### Default variations

`_mlperf.option1`

##### Native script being run
=== "Linux/macOS"
     * [run-filter.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dataset-openimages-calibration/run-filter.sh)
=== "Windows"

No run file exists for Windows
___
#### Script output
`cmr "get dataset openimages calibration [,variations]"  -j`