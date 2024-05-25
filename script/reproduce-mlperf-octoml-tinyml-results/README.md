# reproduce-mlperf-octoml-tinyml-results
Automatically generated README for this automation recipe: **reproduce-mlperf-octoml-tinyml-results**

Category: **[Reproduce MLPerf benchmarks](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/reproduce-mlperf-octoml-tinyml-results/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/reproduce-mlperf-octoml-tinyml-results/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "reproduce tiny results mlperf octoml mlcommons" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=reproduce,tiny,results,mlperf,octoml,mlcommons`

    `cm run script --tags=reproduce,tiny,results,mlperf,octoml,mlcommons[,variations] [--input_flags]`

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "reproduce tiny results mlperf octoml mlcommons"`

    `cmr "reproduce tiny results mlperf octoml mlcommons [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'reproduce,tiny,results,mlperf,octoml,mlcommons'
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

    `cm docker script "reproduce tiny results mlperf octoml mlcommons[variations]" [--input_flags]`

___


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_NRF`
      - Environment variables:
        - *CM_TINY_BOARD*: `NRF5340DK`
      - Workflow:
    * `_NUCLEO`
      - Environment variables:
        - *CM_TINY_BOARD*: `NUCLEO_L4R5ZI`
      - Workflow:
    * `_ad`
      - Environment variables:
        - *CM_TINY_MODEL*: `ad`
      - Workflow:
    * `_cmsis_nn`
      - Environment variables:
        - *CM_MICROTVM_VARIANT*: `microtvm_cmsis_nn`
      - Workflow:
    * `_ic`
      - Environment variables:
        - *CM_TINY_MODEL*: `ic`
      - Workflow:
    * `_kws`
      - Environment variables:
        - *CM_TINY_MODEL*: `kws`
      - Workflow:
    * `_native`
      - Environment variables:
        - *CM_MICROTVM_VARIANT*: `microtvm_native`
      - Workflow:
    * `_vww`
      - Environment variables:
        - *CM_TINY_MODEL*: `vww`
      - Workflow:

    </details>


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--flash=value`  &rarr;  `CM_FLASH_BOARD=value`
* `--recreate_binary=value`  &rarr;  `CM_RECREATE_BINARY=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "flash":...}
```

</details>

#### Versions
Default version: `r1.0`

* `r1.0`

##### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/reproduce-mlperf-octoml-tinyml-results/run.sh)
=== "Windows"

No run file exists for Windows
___
#### Script output
`cmr "reproduce tiny results mlperf octoml mlcommons [,variations]" [--input_flags] -j`