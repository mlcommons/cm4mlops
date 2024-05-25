# install-cuda-prebuilt
Automatically generated README for this automation recipe: **install-cuda-prebuilt**

Category: **[CUDA automation](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/install-cuda-prebuilt/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/install-cuda-prebuilt/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "install prebuilt cuda prebuilt-cuda install-prebuilt-cuda" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=install,prebuilt,cuda,prebuilt-cuda,install-prebuilt-cuda`

    `cm run script --tags=install,prebuilt,cuda,prebuilt-cuda,install-prebuilt-cuda[,variations] [--input_flags]`

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "install prebuilt cuda prebuilt-cuda install-prebuilt-cuda"`

    `cmr "install prebuilt cuda prebuilt-cuda install-prebuilt-cuda [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'install,prebuilt,cuda,prebuilt-cuda,install-prebuilt-cuda'
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

    `cm docker script "install prebuilt cuda prebuilt-cuda install-prebuilt-cuda[variations]" [--input_flags]`

___


#### Variations

  * Group "**install-driver**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_driver`
      - Environment variables:
        - *CM_CUDA_INSTALL_DRIVER*: `yes`
      - Workflow:
    * **`_no-driver`** (default)
      - Environment variables:
        - *CM_CUDA_INSTALL_DRIVER*: `no`
      - Workflow:

    </details>


#### Default variations

`_no-driver`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--local_run_file_path=value`  &rarr;  `CUDA_RUN_FILE_LOCAL_PATH=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "local_run_file_path":...}
```

</details>

#### Default environment


These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_SUDO: `sudo`


#### Versions
Default version: `11.8.0`

* `11.7.0`
* `11.8.0`
* `12.0.0`
* `12.1.1`
* `12.2.0`
* `12.3.2`
* `12.4.1`

##### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/install-cuda-prebuilt/run.sh)
=== "Windows"

No run file exists for Windows
___
#### Script output
`cmr "install prebuilt cuda prebuilt-cuda install-prebuilt-cuda [,variations]" [--input_flags] -j`