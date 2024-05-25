# copy-to-clipboard
Automatically generated README for this automation recipe: **copy-to-clipboard**

Category: **[DevOps automation](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/copy-to-clipboard/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "copy to clipboard copy-to-clipboard" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=copy,to,clipboard,copy-to-clipboard`

    `cm run script --tags=copy,to,clipboard,copy-to-clipboard [--input_flags]`

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "copy to clipboard copy-to-clipboard"`

    `cmr "copy to clipboard copy-to-clipboard " [--input_flags]`


=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'copy,to,clipboard,copy-to-clipboard'
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

    `cm docker script "copy to clipboard copy-to-clipboard" [--input_flags]`

___


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--add_quotes=value`  &rarr;  `CM_COPY_TO_CLIPBOARD_TEXT_ADD_QUOTES=value`
* `--q=value`  &rarr;  `CM_COPY_TO_CLIPBOARD_TEXT_ADD_QUOTES=value`
* `--t=value`  &rarr;  `CM_COPY_TO_CLIPBOARD_TEXT=value`
* `--text=value`  &rarr;  `CM_COPY_TO_CLIPBOARD_TEXT=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "add_quotes":...}
```

</details>


##### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/copy-to-clipboard/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/copy-to-clipboard/run.bat)
___
#### Script output
`cmr "copy to clipboard copy-to-clipboard " [--input_flags] -j`