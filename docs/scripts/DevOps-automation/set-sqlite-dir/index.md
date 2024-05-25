# set-sqlite-dir
Automatically generated README for this automation recipe: **set-sqlite-dir**

Category: **[DevOps automation](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/set-sqlite-dir/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "set sqlite dir sqlite-dir" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=set,sqlite,dir,sqlite-dir`

    `cm run script --tags=set,sqlite,dir,sqlite-dir [--input_flags]`

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "set sqlite dir sqlite-dir"`

    `cmr "set sqlite dir sqlite-dir " [--input_flags]`


=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'set,sqlite,dir,sqlite-dir'
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

    `cm docker script "set sqlite dir sqlite-dir" [--input_flags]`

___


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--path=value`  &rarr;  `CM_SQLITE_PATH=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "path":...}
```

</details>


##### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/set-sqlite-dir/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/set-sqlite-dir/run.bat)
___
#### Script output
`cmr "set sqlite dir sqlite-dir " [--input_flags] -j`