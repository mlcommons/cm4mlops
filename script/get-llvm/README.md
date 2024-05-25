# Detect or install LLVM compiler
Automatically generated README for this automation recipe: **get-llvm**

Category: **[Compiler automation](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-llvm/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-llvm/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get llvm compiler c-compiler cpp-compiler get-llvm" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=get,llvm,compiler,c-compiler,cpp-compiler,get-llvm`

    `cm run script --tags=get,llvm,compiler,c-compiler,cpp-compiler,get-llvm[,variations] `

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "get llvm compiler c-compiler cpp-compiler get-llvm"`

    `cmr "get llvm compiler c-compiler cpp-compiler get-llvm [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,llvm,compiler,c-compiler,cpp-compiler,get-llvm'
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

    `cm docker script "get llvm compiler c-compiler cpp-compiler get-llvm[variations]" `

___


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_from-prebuilt`
      - Workflow:
    * `_from-src`
      - Workflow:

    </details>


##### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-llvm/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/get-llvm/run.bat)
___
#### Script output
`cmr "get llvm compiler c-compiler cpp-compiler get-llvm [,variations]"  -j`