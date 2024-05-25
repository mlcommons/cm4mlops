# download-file
Automatically generated README for this automation recipe: **download-file**

Category: **[DevOps automation](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/download-file/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/download-file/_cm.json)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "download file" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=download,file`

    `cm run script --tags=download,file[,variations] [--input_flags]`

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "download file"`

    `cmr "download file [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'download,file'
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

    `cm docker script "download file[variations]" [--input_flags]`

___


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_url.#`
      - Environment variables:
        - *CM_DOWNLOAD_URL*: `#`
      - Workflow:

    </details>


  * Group "**download-tool**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_cmutil`** (default)
      - Environment variables:
        - *CM_DOWNLOAD_TOOL*: `cmutil`
      - Workflow:
    * `_curl`
      - Environment variables:
        - *CM_DOWNLOAD_TOOL*: `curl`
      - Workflow:
    * `_gdown`
      - Environment variables:
        - *CM_DOWNLOAD_TOOL*: `gdown`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_package.gdown
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/cm4mlops/tree/master/script/get-generic-python-lib)
    * `_rclone`
      - Environment variables:
        - *CM_DOWNLOAD_TOOL*: `rclone`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,rclone
             - CM script: [get-rclone](https://github.com/mlcommons/cm4mlops/tree/master/script/get-rclone)
    * `_wget`
      - Environment variables:
        - *CM_DOWNLOAD_TOOL*: `wget`
      - Workflow:

    </details>


#### Default variations

`_cmutil`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--download_path=value`  &rarr;  `CM_DOWNLOAD_PATH=value`
* `--from=value`  &rarr;  `CM_DOWNLOAD_LOCAL_FILE_PATH=value`
* `--local_path=value`  &rarr;  `CM_DOWNLOAD_LOCAL_FILE_PATH=value`
* `--md5sum=value`  &rarr;  `CM_DOWNLOAD_CHECKSUM=value`
* `--output_file=value`  &rarr;  `CM_DOWNLOAD_FILENAME=value`
* `--store=value`  &rarr;  `CM_DOWNLOAD_PATH=value`
* `--url=value`  &rarr;  `CM_DOWNLOAD_URL=value`
* `--verify=value`  &rarr;  `CM_VERIFY_SSL=value`
* `--verify_ssl=value`  &rarr;  `CM_VERIFY_SSL=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "download_path":...}
```

</details>

#### Default environment


These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_RCLONE_COPY_USING: `sync`



##### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/download-file/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/download-file/run.bat)
___
#### Script output
`cmr "download file [,variations]" [--input_flags] -j`