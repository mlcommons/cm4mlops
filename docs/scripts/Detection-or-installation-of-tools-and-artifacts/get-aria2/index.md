# get-aria2
Automatically generated README for this automation recipe: **get-aria2**

Category: **[Detection or installation of tools and artifacts](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-aria2/README-extra.md)

* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/get-aria2/_cm.yaml)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get aria2 get-aria2" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=get,aria2,get-aria2`

    `cm run script --tags=get,aria2,get-aria2 [--input_flags]`

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "get aria2 get-aria2"`

    `cmr "get aria2 get-aria2 " [--input_flags]`


=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,aria2,get-aria2'
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

    `cm docker script "get aria2 get-aria2" [--input_flags]`

___


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--install=value`  &rarr;  `CM_FORCE_INSTALL=value`
* `--src=value`  &rarr;  `CM_ARIA2_BUILD_FROM_SRC=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "install":...}
```

</details>


##### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-aria2/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/get-aria2/run.bat)
___
#### Script output
`cmr "get aria2 get-aria2 " [--input_flags] -j`