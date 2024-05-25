# get-conda
Automatically generated README for this automation recipe: **get-conda**

Category: **[DevOps automation](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-conda/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get conda get-conda" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=get,conda,get-conda`

    `cm run script --tags=get,conda,get-conda[,variations] `

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "get conda get-conda"`

    `cmr "get conda get-conda [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,conda,get-conda'
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

    `cm docker script "get conda get-conda[variations]" `

___


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_name.#`
      - Environment variables:
        - *CM_CONDA_PREFIX_NAME*: `#`
      - Workflow:

    </details>


  * Group "**conda-python**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_python-3.#`
      - Environment variables:
        - *CM_CONDA_PYTHON_VERSION*: `3.#`
      - Workflow:
    * `_python-3.8`
      - Environment variables:
        - *CM_CONDA_PYTHON_VERSION*: `3.8`
      - Workflow:

    </details>


##### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-conda/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/get-conda/run.bat)
___
#### Script output
`cmr "get conda get-conda [,variations]"  -j`