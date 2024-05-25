# benchmark-program-mlperf
Automatically generated README for this automation recipe: **benchmark-program-mlperf**

Category: **[Modular MLPerf inference benchmark pipeline](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/benchmark-program-mlperf/_cm.json)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "mlperf benchmark-mlperf" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=mlperf,benchmark-mlperf`

    `cm run script --tags=mlperf,benchmark-mlperf[,variations] `

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "mlperf benchmark-mlperf"`

    `cmr "mlperf benchmark-mlperf [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'mlperf,benchmark-mlperf'
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

    `cm docker script "mlperf benchmark-mlperf[variations]" `

___


#### Variations

  * Group "**power-mode**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_no-power`** (default)
      - Workflow:
        1. ***Read "post_deps" on other CM scripts***
           * benchmark-program,program
             * CM names: `--adr.['benchmark-program']...`
             - CM script: [benchmark-program](https://github.com/mlcommons/cm4mlops/tree/master/script/benchmark-program)
    * `_power`
      - Environment variables:
        - *CM_MLPERF_POWER*: `yes`
      - Workflow:
        1. ***Read "prehook_deps" on other CM scripts***
           * benchmark-program,program
             * CM names: `--adr.['benchmark-program']...`
             - CM script: [benchmark-program](https://github.com/mlcommons/cm4mlops/tree/master/script/benchmark-program)
        1. ***Read "post_deps" on other CM scripts***
           * run,mlperf,power,client
             * Enable this dependency only if all ENV vars are set:<br>
`{'CM_MLPERF_LOADGEN_MODE': ['performance']}`
             * CM names: `--adr.['mlperf-power-client']...`
             - CM script: [run-mlperf-power-client](https://github.com/mlcommons/cm4mlops/tree/master/script/run-mlperf-power-client)

    </details>


#### Default variations

`_no-power`

___
#### Script output
`cmr "mlperf benchmark-mlperf [,variations]"  -j`