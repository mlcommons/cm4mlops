# get-ml-model-retinanet-nvidia
Automatically generated README for this automation recipe: **get-ml-model-retinanet-nvidia**

Category: **[AI/ML models](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-retinanet-nvidia/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get ml-model nvidia-retinanet nvidia" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=get,ml-model,nvidia-retinanet,nvidia`

    `cm run script --tags=get,ml-model,nvidia-retinanet,nvidia[,variations] `

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "get ml-model nvidia-retinanet nvidia"`

    `cmr "get ml-model nvidia-retinanet nvidia [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ml-model,nvidia-retinanet,nvidia'
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

    `cm docker script "get ml-model nvidia-retinanet nvidia[variations]" `

___


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_efficient-nms`
      - Environment variables:
        - *CM_NVIDIA_EFFICIENT_NMS*: `yes`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_polygraphy
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/cm4mlops/tree/master/script/get-generic-python-lib)

    </details>

#### Default environment


These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_TORCH_DEVICE: `cpu`



##### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-retinanet-nvidia/run.sh)
=== "Windows"

No run file exists for Windows
___
#### Script output
`cmr "get ml-model nvidia-retinanet nvidia [,variations]"  -j`