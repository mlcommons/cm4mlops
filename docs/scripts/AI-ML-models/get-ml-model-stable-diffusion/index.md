# get-ml-model-stable-diffusion
Automatically generated README for this automation recipe: **get-ml-model-stable-diffusion**

Category: **[AI/ML models](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-stable-diffusion/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get raw ml-model stable-diffusion sdxl text-to-image" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=get,raw,ml-model,stable-diffusion,sdxl,text-to-image`

    `cm run script --tags=get,raw,ml-model,stable-diffusion,sdxl,text-to-image[,variations] [--input_flags]`

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "get raw ml-model stable-diffusion sdxl text-to-image"`

    `cmr "get raw ml-model stable-diffusion sdxl text-to-image [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,raw,ml-model,stable-diffusion,sdxl,text-to-image'
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

    `cm docker script "get raw ml-model stable-diffusion sdxl text-to-image[variations]" [--input_flags]`

___


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_batch_size.#`
      - Environment variables:
        - *CM_ML_MODEL_BATCH_SIZE*: `#`
      - Workflow:
    * `_pytorch,fp16`
      - Workflow:
    * `_pytorch,fp32`
      - Environment variables:
        - *CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0`
      - Workflow:
    * `_rclone,fp16`
      - Environment variables:
        - *CM_DOWNLOAD_URL*: `mlc-inference:mlcommons-inference-wg-public/stable_diffusion_fp16`
      - Workflow:
    * `_rclone,fp32`
      - Environment variables:
        - *CM_DOWNLOAD_URL*: `mlc-inference:mlcommons-inference-wg-public/stable_diffusion_fp32`
      - Workflow:

    </details>


  * Group "**download-source**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_huggingface`
      - Workflow:
    * **`_mlcommons`** (default)
      - Workflow:

    </details>


  * Group "**download-tool**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_git`
      - Environment variables:
        - *CM_DOWNLOAD_TOOL*: `git`
      - Workflow:
    * `_rclone`
      - Environment variables:
        - *CM_RCLONE_CONFIG_CMD*: `rclone config create mlc-inference s3 provider=Cloudflare access_key_id=f65ba5eef400db161ea49967de89f47b secret_access_key=fbea333914c292b854f14d3fe232bad6c5407bf0ab1bebf78833c2b359bdfd2b endpoint=https://c2686074cb2caf5cbaf6d134bdba8b47.r2.cloudflarestorage.com`
        - *CM_DOWNLOAD_TOOL*: `rclone`
      - Workflow:
    * `_wget`
      - Environment variables:
        - *CM_DOWNLOAD_TOOL*: `wget`
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

    * `_fp16`
      - Environment variables:
        - *CM_ML_MODEL_INPUT_DATA_TYPES*: `fp16`
        - *CM_ML_MODEL_PRECISION*: `fp16`
        - *CM_ML_MODEL_WEIGHT_DATA_TYPES*: `fp16`
      - Workflow:
    * **`_fp32`** (default)
      - Environment variables:
        - *CM_ML_MODEL_INPUT_DATA_TYPES*: `fp32`
        - *CM_ML_MODEL_PRECISION*: `fp32`
        - *CM_ML_MODEL_WEIGHT_DATA_TYPES*: `fp32`
      - Workflow:
    * `_int8`
      - Environment variables:
        - *CM_ML_MODEL_INPUT_DATA_TYPES*: `int8`
        - *CM_ML_MODEL_PRECISION*: `int8`
        - *CM_ML_MODEL_WEIGHT_DATA_TYPES*: `int8`
      - Workflow:
    * `_uint8`
      - Environment variables:
        - *CM_ML_MODEL_INPUT_DATA_TYPES*: `uint8`
        - *CM_ML_MODEL_PRECISION*: `uint8`
        - *CM_ML_MODEL_WEIGHT_DATA_TYPES*: `uint8`
      - Workflow:

    </details>


#### Default variations

`_fp32,_mlcommons,_pytorch`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--checkpoint=value`  &rarr;  `SDXL_CHECKPOINT_PATH=value`
* `--download_path=value`  &rarr;  `CM_DOWNLOAD_PATH=value`
* `--to=value`  &rarr;  `CM_DOWNLOAD_PATH=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "checkpoint":...}
```

</details>


___
#### Script output
`cmr "get raw ml-model stable-diffusion sdxl text-to-image [,variations]" [--input_flags] -j`