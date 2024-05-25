# app-image-classification-torch-py
Automatically generated README for this automation recipe: **app-image-classification-torch-py**

Category: **[Modular AI/ML application pipeline](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/app-image-classification-torch-py/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/app-image-classification-torch-py/_cm.json)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "app image-classification python torch" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=app,image-classification,python,torch`

    `cm run script --tags=app,image-classification,python,torch[,variations] `

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "app image-classification python torch"`

    `cmr "app image-classification python torch [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'app,image-classification,python,torch'
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

    `cm docker script "app image-classification python torch[variations]" `

___


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_cuda`
      - Environment variables:
        - *USE_CUDA*: `yes`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,cuda
             - CM script: [get-cuda](https://github.com/mlcommons/cm4mlops/tree/master/script/get-cuda)

    </details>

#### Default environment


These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_BATCH_COUNT: `1`
* CM_BATCH_SIZE: `1`



##### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/app-image-classification-torch-py/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/app-image-classification-torch-py/run.bat)
___
#### Script output
`cmr "app image-classification python torch [,variations]"  -j`