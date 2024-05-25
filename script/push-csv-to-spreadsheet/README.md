# push-csv-to-spreadsheet
Automatically generated README for this automation recipe: **push-csv-to-spreadsheet**

Category: **[DevOps automation](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/push-csv-to-spreadsheet/_cm.json)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "push google-spreadsheet spreadsheet push-to-google-spreadsheet" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=push,google-spreadsheet,spreadsheet,push-to-google-spreadsheet`

    `cm run script --tags=push,google-spreadsheet,spreadsheet,push-to-google-spreadsheet [--input_flags]`

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "push google-spreadsheet spreadsheet push-to-google-spreadsheet"`

    `cmr "push google-spreadsheet spreadsheet push-to-google-spreadsheet " [--input_flags]`


=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'push,google-spreadsheet,spreadsheet,push-to-google-spreadsheet'
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

    `cm docker script "push google-spreadsheet spreadsheet push-to-google-spreadsheet" [--input_flags]`

___


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--csv_file=value`  &rarr;  `CM_CSV_FILE_PATH=value`
* `--sheet_name=value`  &rarr;  `CM_GOOGLE_SHEET_NAME=value`
* `--spreadsheet_id=value`  &rarr;  `CM_GOOGLE_SPREADSHEET_ID=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "csv_file":...}
```

</details>

#### Default environment


These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_GOOGLE_SPREADSHEET_ID: `1gMHjXmFmwZR4-waPPyxy5Pc3VARqX3kKUWxkP97Xa6Y`



##### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/push-csv-to-spreadsheet/run.sh)
=== "Windows"

No run file exists for Windows
___
#### Script output
`cmr "push google-spreadsheet spreadsheet push-to-google-spreadsheet " [--input_flags] -j`