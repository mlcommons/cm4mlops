# get-ml-model-using-imagenet-from-model-zoo
Automatically generated README for this automation recipe: **get-ml-model-using-imagenet-from-model-zoo**

Category: **[AI/ML models](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-using-imagenet-from-model-zoo/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get ml-model model-zoo zoo imagenet image-classification" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=get,ml-model,model-zoo,zoo,imagenet,image-classification`

    `cm run script --tags=get,ml-model,model-zoo,zoo,imagenet,image-classification[,variations] `

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "get ml-model model-zoo zoo imagenet image-classification"`

    `cmr "get ml-model model-zoo zoo imagenet image-classification [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ml-model,model-zoo,zoo,imagenet,image-classification'
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

    `cm docker script "get ml-model model-zoo zoo imagenet image-classification[variations]" `

___


#### Variations

  * Group "**model-source**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_model.#`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,ml-model,zoo,deepsparse,_model-stub.#
             * CM names: `--adr.['neural-magic-zoo-downloader']...`
             - CM script: [get-ml-model-neuralmagic-zoo](https://github.com/mlcommons/cm4mlops/tree/master/script/get-ml-model-neuralmagic-zoo)
    * `_model.resnet101-pytorch-base`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,ml-model,zoo,deepsparse,_model-stub.zoo:cv/classification/resnet_v1-101/pytorch/sparseml/imagenet/base-none
             * CM names: `--adr.['neural-magic-zoo-downloader']...`
             - CM script: [get-ml-model-neuralmagic-zoo](https://github.com/mlcommons/cm4mlops/tree/master/script/get-ml-model-neuralmagic-zoo)
    * `_model.resnet50-pruned95-uniform-quant`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,ml-model,zoo,deepsparse,_model-stub.zoo:cv/classification/resnet_v1-50/pytorch/sparseml/imagenet/pruned95_uniform_quant-none
             * CM names: `--adr.['neural-magic-zoo-downloader']...`
             - CM script: [get-ml-model-neuralmagic-zoo](https://github.com/mlcommons/cm4mlops/tree/master/script/get-ml-model-neuralmagic-zoo)

    </details>


___
#### Script output
`cmr "get ml-model model-zoo zoo imagenet image-classification [,variations]"  -j`