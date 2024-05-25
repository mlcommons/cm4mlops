# get-cudnn
Automatically generated README for this automation recipe: **get-cudnn**

Category: **[CUDA automation](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-cudnn/README-extra.md)

* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/get-cudnn/_cm.yaml)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get cudnn nvidia" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=get,cudnn,nvidia`

    `cm run script --tags=get,cudnn,nvidia [--input_flags]`

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "get cudnn nvidia"`

    `cmr "get cudnn nvidia " [--input_flags]`



#### Input Flags

* --**input**=Full path to the installed cuDNN library
* --**tar_file**=Full path to the cuDNN Tar file downloaded from Nvidia website (https://developer.nvidia.com/cudnn)

=== "Python"

    ```python
r=cm.access({... , "input":...}
```
=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,cudnn,nvidia'
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

    `cm docker script "get cudnn nvidia" [--input_flags]`

___


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--input=value`  &rarr;  `CM_INPUT=value`
* `--tar_file=value`  &rarr;  `CM_CUDNN_TAR_FILE_PATH=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "input":...}
```

</details>

#### Default environment


These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_INPUT: ``
* CM_SUDO: `sudo`



##### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-cudnn/run.sh)
=== "Windows"

No run file exists for Windows
___
#### Script output
`cmr "get cudnn nvidia " [--input_flags] -j`