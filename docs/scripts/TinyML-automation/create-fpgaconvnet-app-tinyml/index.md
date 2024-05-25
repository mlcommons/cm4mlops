# create-fpgaconvnet-app-tinyml
Automatically generated README for this automation recipe: **create-fpgaconvnet-app-tinyml**

Category: **[TinyML automation](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/create-fpgaconvnet-app-tinyml/_cm.json)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "create app fpgaconvnet" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=create,app,fpgaconvnet`

    `cm run script --tags=create,app,fpgaconvnet[,variations] `

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "create app fpgaconvnet"`

    `cmr "create app fpgaconvnet [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'create,app,fpgaconvnet'
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

    `cm docker script "create app fpgaconvnet[variations]" `

___


#### Variations

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
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/create-fpgaconvnet-app-tinyml/run.sh)
=== "Windows"

No run file exists for Windows
___
#### Script output
`cmr "create app fpgaconvnet [,variations]"  -j`