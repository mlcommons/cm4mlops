# build-mlperf-inference-server-nvidia
Automatically generated README for this automation recipe: **build-mlperf-inference-server-nvidia**

Category: **[MLPerf benchmark support](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/build-mlperf-inference-server-nvidia/README-extra.md)

* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/build-mlperf-inference-server-nvidia/_cm.yaml)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "build mlcommons mlperf inference inference-server server nvidia-harness nvidia" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=build,mlcommons,mlperf,inference,inference-server,server,nvidia-harness,nvidia`

    `cm run script --tags=build,mlcommons,mlperf,inference,inference-server,server,nvidia-harness,nvidia[,variations] [--input_flags]`

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "build mlcommons mlperf inference inference-server server nvidia-harness nvidia"`

    `cmr "build mlcommons mlperf inference inference-server server nvidia-harness nvidia [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'build,mlcommons,mlperf,inference,inference-server,server,nvidia-harness,nvidia'
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

    `cm docker script "build mlcommons mlperf inference inference-server server nvidia-harness nvidia[variations]" [--input_flags]`

___


#### Variations

  * Group "**code**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_ctuning`** (default)
      - Workflow:
    * `_custom`
      - Workflow:
    * `_go`
      - Workflow:
    * `_mlcommons`
      - Workflow:
    * `_nvidia-only`
      - Workflow:

    </details>


  * Group "**device**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_cpu`
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `cpu`
      - Workflow:
    * **`_cuda`** (default)
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `cuda`
        - *CM_MLPERF_DEVICE_LIB_NAMESPEC*: `cudart`
      - Workflow:
    * `_inferentia`
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `inferentia`
      - Workflow:

    </details>


  * Group "**version**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_r4.0`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic,sys-util,_git-lfs
             - CM script: [get-generic-sys-util](https://github.com/mlcommons/cm4mlops/tree/master/script/get-generic-sys-util)
           * install,pytorch,from.src,_for-nvidia-mlperf-inference-v4.0
             * CM names: `--adr.['pytorch', 'torch']...`
             - CM script: [install-pytorch-from-src](https://github.com/mlcommons/cm4mlops/tree/master/script/install-pytorch-from-src)
           * install,torchvision,from.src,_for-nvidia-mlperf-inference-v4.0
             * CM names: `--adr.['pytorchvision', 'torchvision']...`
             - CM script: [install-torchvision-from-src](https://github.com/mlcommons/cm4mlops/tree/master/script/install-torchvision-from-src)

    </details>


#### Default variations

`_ctuning,_cuda`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--clean=value`  &rarr;  `CM_MAKE_CLEAN=value`
* `--custom_system=value`  &rarr;  `CM_CUSTOM_SYSTEM_NVIDIA=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "clean":...}
```

</details>

#### Default environment


These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_MAKE_BUILD_COMMAND: `build`
* CM_MAKE_CLEAN: `no`
* CM_CUSTOM_SYSTEM_NVIDIA: `yes`


#### Versions
Default version: `r3.1`

* `r2.1`
* `r3.0`
* `r3.1`
* `r4.0`

##### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/build-mlperf-inference-server-nvidia/run.sh)
=== "Windows"

No run file exists for Windows
___
#### Script output
`cmr "build mlcommons mlperf inference inference-server server nvidia-harness nvidia [,variations]" [--input_flags] -j`