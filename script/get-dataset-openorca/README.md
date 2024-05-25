# get-dataset-openorca
Automatically generated README for this automation recipe: **get-dataset-openorca**

Category: **[AI/ML datasets](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dataset-openorca/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get dataset openorca language-processing original" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=get,dataset,openorca,language-processing,original`

    `cm run script --tags=get,dataset,openorca,language-processing,original[,variations] `

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "get dataset openorca language-processing original"`

    `cmr "get dataset openorca language-processing original [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,dataset,openorca,language-processing,original'
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

    `cm docker script "get dataset openorca language-processing original[variations]" `

___


#### Variations

  * Group "**dataset-type**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_calibration`
      - Environment variables:
        - *CM_DATASET_CALIBRATION*: `yes`
      - Workflow:
    * **`_validation`** (default)
      - Environment variables:
        - *CM_DATASET_CALIBRATION*: `no`
      - Workflow:

    </details>


  * Group "**size**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_500`
      - Environment variables:
        - *CM_DATASET_SIZE*: `500`
      - Workflow:
    * **`_60`** (default)
      - Environment variables:
        - *CM_DATASET_SIZE*: `60`
      - Workflow:
    * `_full`
      - Environment variables:
        - *CM_DATASET_SIZE*: `24576`
      - Workflow:
    * `_size.#`
      - Environment variables:
        - *CM_DATASET_SIZE*: `#`
      - Workflow:

    </details>


#### Default variations

`_60,_validation`
#### Default environment


These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_DATASET_CALIBRATION: `no`



___
#### Script output
`cmr "get dataset openorca language-processing original [,variations]"  -j`