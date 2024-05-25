# install-nccl-libs
Automatically generated README for this automation recipe: **install-nccl-libs**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/install-nccl-libs/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "install nccl libs" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=install,nccl,libs`

    `cm run script --tags=install,nccl,libs[,variations] `

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "install nccl libs"`

    `cmr "install nccl libs [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'install,nccl,libs'
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

    `cm docker script "install nccl libs[variations]" `

___


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_cuda`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,cuda
             - CM script: [get-cuda](https://github.com/mlcommons/cm4mlops/tree/master/script/get-cuda)

    </details>


##### Native script being run
=== "Linux/macOS"
     * [run-ubuntu.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/install-nccl-libs/run-ubuntu.sh)
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/install-nccl-libs/run.sh)
=== "Windows"

No run file exists for Windows
___
#### Script output
`cmr "install nccl libs [,variations]"  -j`