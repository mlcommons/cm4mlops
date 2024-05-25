# get-blis
Automatically generated README for this automation recipe: **get-blis**

Category: **[Detection or installation of tools and artifacts](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-blis/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-blis/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get lib blis" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=get,lib,blis`

    `cm run script --tags=get,lib,blis[,variations] `

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "get lib blis"`

    `cmr "get lib blis [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,lib,blis'
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

    `cm docker script "get lib blis[variations]" `

___


#### Variations

  * Group "**source**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_amd`
      - Workflow:
    * **`_flame`** (default)
      - Workflow:

    </details>


#### Default variations

`_flame`
#### Versions
Default version: `master`

* `0.9.0`
* `master`

##### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-blis/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/get-blis/run.bat)
___
#### Script output
`cmr "get lib blis [,variations]"  -j`