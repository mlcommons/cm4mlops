# install-python-venv
Automatically generated README for this automation recipe: **install-python-venv**

Category: **[Python automation](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/install-python-venv/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "install python get-python-venv python-venv" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=install,python,get-python-venv,python-venv`

    `cm run script --tags=install,python,get-python-venv,python-venv[,variations] `

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "install python get-python-venv python-venv"`

    `cmr "install python get-python-venv python-venv [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'install,python,get-python-venv,python-venv'
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

    `cm docker script "install python get-python-venv python-venv[variations]" `

___


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

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
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/install-python-venv/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/install-python-venv/run.bat)
___
#### Script output
`cmr "install python get-python-venv python-venv [,variations]"  -j`