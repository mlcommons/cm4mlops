# get-ml-model-huggingface-zoo
Automatically generated README for this automation recipe: **get-ml-model-huggingface-zoo**

Category: **[AI/ML models](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-huggingface-zoo/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-huggingface-zoo/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get ml-model huggingface zoo" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=get,ml-model,huggingface,zoo`

    `cm run script --tags=get,ml-model,huggingface,zoo[,variations] [--input_flags]`

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "get ml-model huggingface zoo"`

    `cmr "get ml-model huggingface zoo [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ml-model,huggingface,zoo'
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

    `cm docker script "get ml-model huggingface zoo[variations]" [--input_flags]`

___


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_model-stub.#`
      - Environment variables:
        - *CM_MODEL_ZOO_STUB*: `#`
      - Workflow:
    * `_onnx-subfolder`
      - Environment variables:
        - *CM_HF_SUBFOLDER*: `onnx`
      - Workflow:
    * `_pierreguillou_bert_base_cased_squad_v1.1_portuguese`
      - Environment variables:
        - *CM_MODEL_ZOO_STUB*: `pierreguillou/bert-base-cased-squad-v1.1-portuguese`
      - Workflow:
    * `_prune`
      - Environment variables:
        - *CM_MODEL_TASK*: `prune`
      - Workflow:

    </details>


  * Group "**download-type**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_clone-repo`
      - Environment variables:
        - *CM_GIT_CLONE_REPO*: `yes`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,git,repo,_lfs
             - CM script: [get-git-repo](https://github.com/mlcommons/cm4mlops/tree/master/script/get-git-repo)

    </details>


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--download_path=value`  &rarr;  `CM_DOWNLOAD_PATH=value`
* `--env_key=value`  &rarr;  `CM_MODEL_ZOO_ENV_KEY=value`
* `--full_subfolder=value`  &rarr;  `CM_HF_FULL_SUBFOLDER=value`
* `--model_filename=value`  &rarr;  `CM_MODEL_ZOO_FILENAME=value`
* `--revision=value`  &rarr;  `CM_HF_REVISION=value`
* `--subfolder=value`  &rarr;  `CM_HF_SUBFOLDER=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "download_path":...}
```

</details>


##### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-huggingface-zoo/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-huggingface-zoo/run.bat)
___
#### Script output
`cmr "get ml-model huggingface zoo [,variations]" [--input_flags] -j`