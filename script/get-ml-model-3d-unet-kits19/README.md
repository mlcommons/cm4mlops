# get-ml-model-3d-unet-kits19
Automatically generated README for this automation recipe: **get-ml-model-3d-unet-kits19**

Category: **[AI/ML models](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-3d-unet-kits19/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get ml-model raw 3d-unet kits19 medical-imaging" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=get,ml-model,raw,3d-unet,kits19,medical-imaging`

    `cm run script --tags=get,ml-model,raw,3d-unet,kits19,medical-imaging[,variations] `

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "get ml-model raw 3d-unet kits19 medical-imaging"`

    `cmr "get ml-model raw 3d-unet kits19 medical-imaging [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ml-model,raw,3d-unet,kits19,medical-imaging'
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

    `cm docker script "get ml-model raw 3d-unet kits19 medical-imaging[variations]" `

___


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_onnx,fp32`
      - Environment variables:
        - *CM_ML_MODEL_ACCURACY*: `0.86170`
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/5597155/files/3dunet_kits19_128x128x128_dynbatch.onnx?download=1`
      - Workflow:
    * `_pytorch,fp32`
      - Environment variables:
        - *CM_ML_MODEL_ACCURACY*: `0.86170`
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/5597155/files/3dunet_kits19_pytorch.ptc?download=1`
      - Workflow:
    * `_pytorch,fp32,weights`
      - Environment variables:
        - *CM_ML_MODEL_ACCURACY*: `0.86170`
        - *CM_ML_MODEL_FILE*: `retinanet_model_10.pth`
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/5597155/files/3dunet_kits19_pytorch_checkpoint.pth?download=1`
        - *CM_UNZIP*: `yes`
      - Workflow:
    * `_tf,fp32`
      - Environment variables:
        - *CM_ML_MODEL_ACCURACY*: `0.86170`
        - *CM_ML_MODEL_FILE*: `3dunet_kits19_128x128x128.tf`
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/5597155/files/3dunet_kits19_128x128x128.tf.zip?download=1`
        - *CM_UNZIP*: `yes`
      - Workflow:
    * `_weights`
      - Environment variables:
        - *CM_MODEL_WEIGHTS_FILE*: `yes`
      - Workflow:

    </details>


  * Group "**framework**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_onnx`** (default)
      - Environment variables:
        - *CM_ML_MODEL_FRAMEWORK*: `onnx`
      - Workflow:
    * `_pytorch`
      - Environment variables:
        - *CM_ML_MODEL_FRAMEWORK*: `pytorch`
      - Workflow:
    * `_tf`
      - Aliases: `_tensorflow`
      - Environment variables:
        - *CM_ML_MODEL_FRAMEWORK*: `tensorflow`
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

`_fp32,_onnx`

___
#### Script output
`cmr "get ml-model raw 3d-unet kits19 medical-imaging [,variations]"  -j`