# get-python3
Automatically generated README for this automation recipe: **get-python3**

Category: **[Python automation](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-python3/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-python3/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get python python3 get-python get-python3" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=get,python,python3,get-python,get-python3`

    `cm run script --tags=get,python,python3,get-python,get-python3[,variations] `

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "get python python3 get-python get-python3"`

    `cmr "get python python3 get-python get-python3 [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,python,python3,get-python,get-python3'
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

    `cm docker script "get python python3 get-python get-python3[variations]" `

___


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_conda.#`
      - Environment variables:
        - *CM_PYTHON_CONDA*: `yes`
        - *CM_PYTHON_INSTALL_CACHE_TAGS*: `_conda.#`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic,conda-package,_name.#,_package.python
             * CM names: `--adr.['conda-package', 'conda-python']...`
             - CM script: [install-generic-conda-package](https://github.com/mlcommons/cm4mlops/tree/master/script/install-generic-conda-package)
    * `_custom-path.#`
      - Environment variables:
        - *CM_PYTHON_BIN_WITH_PATH*: `#`
      - Workflow:
    * `_lto`
      - Workflow:
    * `_optimized`
      - Workflow:
    * `_shared`
      - Workflow:
    * `_with-custom-ssl`
      - Workflow:
    * `_with-ssl`
      - Workflow:

    </details>


##### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-python3/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/get-python3/run.bat)
___
#### Script output
`cmr "get python python3 get-python get-python3 [,variations]"  -j`