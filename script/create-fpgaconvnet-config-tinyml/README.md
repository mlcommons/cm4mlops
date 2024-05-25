# create-fpgaconvnet-config-tinyml
Automatically generated README for this automation recipe: **create-fpgaconvnet-config-tinyml**

Category: **[TinyML automation](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/create-fpgaconvnet-config-tinyml/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "create config fpgaconvnet" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=create,config,fpgaconvnet`

    `cm run script --tags=create,config,fpgaconvnet[,variations] `

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "create config fpgaconvnet"`

    `cmr "create config fpgaconvnet [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'create,config,fpgaconvnet'
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

    `cm docker script "create config fpgaconvnet[variations]" `

___


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_zc706,ic`
      - Environment variables:
        - *CM_TINY_NETWORK_NAME*: `zc706-resnet`
      - Workflow:

    </details>


  * Group "**benchmark**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_ic`** (default)
      - Workflow:

    </details>


  * Group "**board**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_zc706`** (default)
      - Environment variables:
        - *CM_TINY_BOARD*: `zc706`
      - Workflow:

    </details>


#### Default variations

`_ic,_zc706`

##### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/create-fpgaconvnet-config-tinyml/run.sh)
=== "Windows"

No run file exists for Windows
___
#### Script output
`cmr "create config fpgaconvnet [,variations]"  -j`