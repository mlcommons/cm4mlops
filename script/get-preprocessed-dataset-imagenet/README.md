# get-preprocessed-dataset-imagenet
Automatically generated README for this automation recipe: **get-preprocessed-dataset-imagenet**

Category: **[AI/ML datasets](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-preprocessed-dataset-imagenet/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-preprocessed-dataset-imagenet/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get dataset imagenet ILSVRC image-classification preprocessed" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=get,dataset,imagenet,ILSVRC,image-classification,preprocessed`

    `cm run script --tags=get,dataset,imagenet,ILSVRC,image-classification,preprocessed[,variations] [--input_flags]`

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "get dataset imagenet ILSVRC image-classification preprocessed"`

    `cmr "get dataset imagenet ILSVRC image-classification preprocessed [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,dataset,imagenet,ILSVRC,image-classification,preprocessed'
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

    `cm docker script "get dataset imagenet ILSVRC image-classification preprocessed[variations]" [--input_flags]`

___


#### Variations

  * *Internal group (variations should not be selected manually)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_mobilenet_`
      - Environment variables:
        - *CM_MODEL*: `mobilenet`
      - Workflow:
    * `_resnet50_`
      - Environment variables:
        - *CM_MODEL*: `resnet50`
      - Workflow:

    </details>


  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_500,validation`
      - Workflow:
    * `_default`
      - Workflow:
    * `_for.mobilenet,float32`
      - Environment variables:
        - *CM_DATASET_QUANTIZE*: `0`
        - *CM_DATASET_GIVEN_CHANNEL_MEANS*: ``
        - *CM_DATASET_NORMALIZE_DATA*: `1`
        - *CM_DATASET_SUBTRACT_MEANS*: `0`
      - Workflow:
    * `_for.mobilenet,rgb8`
      - Environment variables:
        - *CM_DATASET_GIVEN_CHANNEL_MEANS*: ``
        - *CM_DATASET_SUBTRACT_MEANS*: `0`
        - *CM_DATASET_QUANTIZE*: `0`
        - *CM_DATASET_NORMALIZE_DATA*: `0`
        - *CM_DATASET_DATA_TYPE*: `uint8`
      - Workflow:
    * `_for.resnet50,float32`
      - Workflow:
    * `_for.resnet50,rgb8`
      - Environment variables:
        - *CM_DATASET_GIVEN_CHANNEL_MEANS*: ``
        - *CM_DATASET_SUBTRACT_MEANS*: `0`
        - *CM_DATASET_NORMALIZE_DATA*: `0`
        - *CM_DATASET_QUANTIZE*: `0`
        - *CM_DATASET_DATA_TYPE*: `uint8`
      - Workflow:
    * `_for.resnet50,rgb8,uint8`
      - Environment variables:
        - *CM_DATASET_GIVEN_CHANNEL_MEANS*: `123.68 116.78 103.94`
        - *CM_DATASET_SUBTRACT_MEANS*: `1`
        - *CM_DATASET_QUANTIZE*: `1`
      - Workflow:
    * `_for.resnet50,uint8`
      - Environment variables:
        - *CM_DATASET_QUANT_SCALE*: `1.18944883`
        - *CM_DATASET_QUANT_OFFSET*: `0`
      - Workflow:
    * `_pytorch`
      - Environment variables:
        - *CM_PREPROCESS_PYTORCH*: `yes`
        - *CM_MODEL*: `resnet50`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_torchvision
             * CM names: `--adr.['torchvision']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/cm4mlops/tree/master/script/get-generic-python-lib)
    * `_tflite_tpu`
      - Environment variables:
        - *CM_MODEL*: `resnet50`
        - *CM_PREPROCESS_TFLITE_TPU*: `yes`
      - Workflow:

    </details>


  * Group "**calibration-option**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_mlperf.option1`
      - Environment variables:
        - *CM_DATASET_CALIBRATION_OPTION*: `one`
      - Workflow:
    * `_mlperf.option2`
      - Environment variables:
        - *CM_DATASET_CALIBRATION_OPTION*: `two`
      - Workflow:

    </details>


  * Group "**dataset-type**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_calibration`
      - Environment variables:
        - *CM_DATASET_TYPE*: `calibration`
      - Workflow:
    * **`_validation`** (default)
      - Environment variables:
        - *CM_DATASET_TYPE*: `validation`
      - Workflow:

    </details>


  * Group "**extension**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_rgb32`
      - Environment variables:
        - *CM_DATASET_PREPROCESSED_EXTENSION*: `rgb32`
      - Workflow:
    * `_rgb8`
      - Environment variables:
        - *CM_DATASET_PREPROCESSED_EXTENSION*: `rgb8`
      - Workflow:

    </details>


  * Group "**interpolation-method**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_inter.area`
      - Environment variables:
        - *CM_DATASET_INTERPOLATION_METHOD*: `INTER_AREA`
      - Workflow:
    * `_inter.linear`
      - Environment variables:
        - *CM_DATASET_INTERPOLATION_METHOD*: `INTER_LINEAR`
      - Workflow:

    </details>


  * Group "**layout**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_NCHW`** (default)
      - Environment variables:
        - *CM_DATASET_DATA_LAYOUT*: `NCHW`
      - Workflow:
    * `_NHWC`
      - Environment variables:
        - *CM_DATASET_DATA_LAYOUT*: `NHWC`
      - Workflow:

    </details>


  * Group "**model**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_for.mobilenet`
      - Workflow:
    * `_for.resnet50`
      - Environment variables:
        - *CM_DATASET_SUBTRACT_MEANS*: `1`
        - *CM_DATASET_GIVEN_CHANNEL_MEANS*: `123.68 116.78 103.94`
        - *CM_DATASET_NORMALIZE_DATA*: `0`
        - *CM_DATASET_INTERPOLATION_METHOD*: `INTER_AREA`
      - Workflow:

    </details>


  * Group "**precision**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_float32`
      - Environment variables:
        - *CM_DATASET_DATA_TYPE*: `float32`
        - *CM_DATASET_QUANTIZE*: `0`
        - *CM_DATASET_CONVERT_TO_UNSIGNED*: `0`
      - Workflow:
    * `_int8`
      - Environment variables:
        - *CM_DATASET_DATA_TYPE*: `int8`
        - *CM_DATASET_QUANTIZE*: `1`
        - *CM_DATASET_CONVERT_TO_UNSIGNED*: `0`
      - Workflow:
    * `_uint8`
      - Environment variables:
        - *CM_DATASET_DATA_TYPE*: `uint8`
        - *CM_DATASET_DATA_TYPE_INPUT*: `float32`
        - *CM_DATASET_QUANTIZE*: `1`
        - *CM_DATASET_CONVERT_TO_UNSIGNED*: `1`
      - Workflow:

    </details>


  * Group "**preprocessing-source**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_generic-preprocessor`
      - Environment variables:
        - *CM_DATASET_REFERENCE_PREPROCESSOR*: `0`
      - Workflow:
        1. ***Read "prehook_deps" on other CM scripts***
           * get,generic,image-preprocessor
             - CM script: [get-preprocesser-script-generic](https://github.com/mlcommons/cm4mlops/tree/master/script/get-preprocesser-script-generic)
    * **`_mlcommons-reference-preprocessor`** (default)
      - Environment variables:
        - *CM_DATASET_REFERENCE_PREPROCESSOR*: `1`
      - Workflow:

    </details>


  * Group "**resolution**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_resolution.#`
      - Environment variables:
        - *CM_DATASET_INPUT_SQUARE_SIDE*: `#`
      - Workflow:
    * **`_resolution.224`** (default)
      - Environment variables:
        - *CM_DATASET_INPUT_SQUARE_SIDE*: `224`
      - Workflow:

    </details>


  * Group "**size**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_1`
      - Environment variables:
        - *CM_DATASET_SIZE*: `1`
      - Workflow:
    * `_500`
      - Environment variables:
        - *CM_DATASET_SIZE*: `500`
      - Workflow:
    * `_full`
      - Environment variables:
        - *CM_DATASET_SIZE*: `50000`
      - Workflow:
    * `_size.#`
      - Environment variables:
        - *CM_DATASET_SIZE*: `#`
      - Workflow:

    </details>


#### Default variations

`_NCHW,_mlcommons-reference-preprocessor,_resolution.224,_validation`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--dir=value`  &rarr;  `CM_DATASET_PREPROCESSED_PATH=value`
* `--imagenet_path=value`  &rarr;  `CM_IMAGENET_PATH=value`
* `--imagenet_preprocessed_path=value`  &rarr;  `CM_IMAGENET_PREPROCESSED_PATH=value`
* `--threads=value`  &rarr;  `CM_NUM_PREPROCESS_THREADS=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "dir":...}
```

</details>

#### Default environment


These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_DATASET_CROP_FACTOR: `87.5`
* CM_DATASET_DATA_TYPE: `float32`
* CM_DATASET_DATA_LAYOUT: `NCHW`
* CM_DATASET_QUANT_SCALE: `1`
* CM_DATASET_QUANTIZE: `0`
* CM_DATASET_QUANT_OFFSET: `0`
* CM_DATASET_PREPROCESSED_EXTENSION: `npy`
* CM_DATASET_CONVERT_TO_UNSIGNED: `0`
* CM_DATASET_REFERENCE_PREPROCESSOR: `1`
* CM_PREPROCESS_VGG: `yes`
* CM_MODEL: `resnet50`



##### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-preprocessed-dataset-imagenet/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/get-preprocessed-dataset-imagenet/run.bat)
___
#### Script output
`cmr "get dataset imagenet ILSVRC image-classification preprocessed [,variations]" [--input_flags] -j`