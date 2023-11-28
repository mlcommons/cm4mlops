<details>
<summary>Click here to see the table of contents.</summary>

* [About](#about)
* [Summary](#summary)
* [Reuse this script in your project](#reuse-this-script-in-your-project)
  * [ Install CM automation language](#install-cm-automation-language)
  * [ Check CM script flags](#check-cm-script-flags)
  * [ Run this script from command line](#run-this-script-from-command-line)
  * [ Run this script from Python](#run-this-script-from-python)
  * [ Run this script via GUI](#run-this-script-via-gui)
  * [ Run this script via Docker (beta)](#run-this-script-via-docker-(beta))
* [Customization](#customization)
  * [ Variations](#variations)
  * [ Default environment](#default-environment)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit!*

### About

#### Summary

* Category: *AI/ML models.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-base-squad)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,ml-model,raw,bert,bert-base,bert-squad,language,language-processing*
* Output cached? *True*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=get,ml-model,raw,bert,bert-base,bert-squad,language,language-processing[,variations] `

2. `cmr "get ml-model raw bert bert-base bert-squad language language-processing[ variations]" `

* `variations` can be seen [here](#variations)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ml-model,raw,bert,bert-base,bert-squad,language,language-processing'
                  'out':'con',
                  ...
                  (other input keys for this script)
                  ...
                 })

if r['return']>0:
    print (r['error'])

```

</details>


#### Run this script via GUI

```cmr "cm gui" --script="get,ml-model,raw,bert,bert-base,bert-squad,language,language-processing"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,ml-model,raw,bert,bert-base,bert-squad,language,language-processing) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get ml-model raw bert bert-base bert-squad language language-processing[ variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_deepsparse,int8`
      - Environment variables:
        - *CM_ML_MODEL_F1*: `87.89`
        - *CM_ML_MODEL_FILE*: `model.onnx`
        - *CM_PRUNING_PERCENTAGE*: `95`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,ml-model,zoo,deepsparse,_pruned95_obs_quant-none
             * CM names: `--adr.['neural-magic-zoo-downloader']...`
             - *Warning: no scripts found*

    </details>


  * Group "**framework**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_deepsparse`
      - Environment variables:
        - *CM_ML_MODEL_FRAMEWORK*: `deepsparse`
        - *CM_ML_MODEL_INPUT_IDS_NAME*: `input_ids`
        - *CM_ML_MODEL_INPUT_MASK_NAME*: `input_mask`
        - *CM_ML_MODEL_INPUT_SEGMENTS_NAME*: `segment_ids`
        - *CM_ML_MODEL_OUTPUT_END_LOGITS_NAME*: `output_end_logits`
        - *CM_ML_MODEL_OUTPUT_START_LOGITS_NAME*: `output_start_logits`
      - Workflow:

    </details>


  * Group "**precision**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_fp32`** (default)
      - Environment variables:
        - *CM_ML_MODEL_PRECISION*: `fp32`
      - Workflow:
    * `_int8`
      - Environment variables:
        - *CM_ML_MODEL_PRECISION*: `int8`
        - *CM_ML_MODEL_QUANTIZED*: `yes`
      - Workflow:

    </details>


#### Default variations

`_fp32`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-base-squad/_cm.json)
  1. Run "preprocess" function from customize.py
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-base-squad/_cm.json)***
     * download-and-extract
       * `if (CM_TMP_ML_MODEL_REQUIRE_DOWNLOAD in yes)`
       - CM script: [download-and-extract](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-and-extract)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-base-squad/_cm.json)
  1. Run "postrocess" function from customize.py
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-base-squad/_cm.json)***
     * get,bert,squad,vocab
       - CM script: [get-bert-squad-vocab](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-bert-squad-vocab)
</details>

___
### Script output
`cmr "get ml-model raw bert bert-base bert-squad language language-processing[,variations]"  -j`
#### New environment keys (filter)

* `CM_ML_MODEL*`
#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)