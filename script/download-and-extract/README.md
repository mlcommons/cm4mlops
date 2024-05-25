# download-and-extract
Automatically generated README for this automation recipe: **download-and-extract**

Category: **[DevOps automation](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/download-and-extract/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/download-and-extract/_cm.json)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "download-and-extract file" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=download-and-extract,file`

    `cm run script --tags=download-and-extract,file[,variations] [--input_flags]`

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "download-and-extract file"`

    `cmr "download-and-extract file [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'download-and-extract,file'
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

    `cm docker script "download-and-extract file[variations]" [--input_flags]`

___


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_extract`
      - Environment variables:
        - *CM_DAE_EXTRACT_DOWNLOADED*: `yes`
      - Workflow:
    * `_keep`
      - Environment variables:
        - *CM_EXTRACT_REMOVE_EXTRACTED*: `no`
      - Workflow:
    * `_no-remove-extracted`
      - Environment variables:
        - *CM_EXTRACT_REMOVE_EXTRACTED*: `no`
      - Workflow:
    * `_url.#`
      - Environment variables:
        - *CM_DAE_URL*: `#`
      - Workflow:

    </details>


  * Group "**download-tool**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_cmutil`** (default)
      - Workflow:
    * `_curl`
      - Workflow:
    * `_gdown`
      - Workflow:
    * `_rclone`
      - Workflow:
    * `_torrent`
      - Environment variables:
        - *CM_DAE_DOWNLOAD_USING_TORRENT*: `yes`
        - *CM_TORRENT_DOWNLOADED_FILE_NAME*: `<<<CM_DAE_FILENAME>>>`
        - *CM_TORRENT_DOWNLOADED_PATH_ENV_KEY*: `CM_DAE_FILEPATH`
        - *CM_TORRENT_WAIT_UNTIL_COMPLETED*: `yes`
      - Workflow:
        1. ***Read "prehook_deps" on other CM scripts***
           * download,torrent
             - CM script: [download-torrent](https://github.com/mlcommons/cm4mlops/tree/master/script/download-torrent)
    * `_wget`
      - Workflow:

    </details>


#### Default variations

`_cmutil`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--download_path=value`  &rarr;  `CM_DOWNLOAD_PATH=value`
* `--extra_folder=value`  &rarr;  `CM_EXTRACT_TO_FOLDER=value`
* `--extract_path=value`  &rarr;  `CM_EXTRACT_PATH=value`
* `--from=value`  &rarr;  `CM_DOWNLOAD_LOCAL_FILE_PATH=value`
* `--local_path=value`  &rarr;  `CM_DOWNLOAD_LOCAL_FILE_PATH=value`
* `--store=value`  &rarr;  `CM_DOWNLOAD_PATH=value`
* `--to=value`  &rarr;  `CM_EXTRACT_PATH=value`
* `--url=value`  &rarr;  `CM_DAE_URL=value`
* `--verify=value`  &rarr;  `CM_VERIFY_SSL=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "download_path":...}
```

</details>


___
#### Script output
`cmr "download-and-extract file [,variations]" [--input_flags] -j`