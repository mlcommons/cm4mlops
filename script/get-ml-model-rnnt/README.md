# get-ml-model-rnnt
Automatically generated README for this automation recipe: **get-ml-model-rnnt**

Category: **[AI/ML models](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-rnnt/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get ml-model rnnt raw librispeech speech-recognition" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=get,ml-model,rnnt,raw,librispeech,speech-recognition`

    `cm run script --tags=get,ml-model,rnnt,raw,librispeech,speech-recognition[,variations] `

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "get ml-model rnnt raw librispeech speech-recognition"`

    `cmr "get ml-model rnnt raw librispeech speech-recognition [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ml-model,rnnt,raw,librispeech,speech-recognition'
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

    `cm docker script "get ml-model rnnt raw librispeech speech-recognition[variations]" `

___


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_pytorch,fp32`
      - Environment variables:
        - *CM_ML_MODEL_ACCURACY*: `0.07452253714852645`
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/3662521/files/DistributedDataParallel_1576581068.9962234-epoch-100.pt?download=1`
      - Workflow:
    * `_pytorch,fp32,amazon-s3`
      - Workflow:
    * `_pytorch,fp32,zenodo`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/3662521/files/DistributedDataParallel_1576581068.9962234-epoch-100.pt?download=1`
      - Workflow:
    * `_weights`
      - Environment variables:
        - *CM_MODEL_WEIGHTS_FILE*: `yes`
      - Workflow:

    </details>


  * Group "**download-src**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_amazon-s3`
      - Workflow:
    * **`_zenodo`** (default)
      - Workflow:

    </details>


  * Group "**framework**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_pytorch`** (default)
      - Environment variables:
        - *CM_ML_MODEL_FRAMEWORK*: `pytorch`
      - Workflow:

    </details>


  * Group "**precision**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_fp32`** (default)
      - Environment variables:
        - *CM_ML_MODEL_INPUT_DATA_TYPES*: `fp32`
        - *CM_ML_MODEL_PRECISION*: `fp32`
        - *CM_ML_MODEL_WEIGHT_DATA_TYPES*: `fp32`
      - Workflow:

    </details>


#### Default variations

`_fp32,_pytorch,_zenodo`

___
#### Script output
`cmr "get ml-model rnnt raw librispeech speech-recognition [,variations]"  -j`