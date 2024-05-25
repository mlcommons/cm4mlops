# get-mlperf-inference-intel-scratch-space
Automatically generated README for this automation recipe: **get-mlperf-inference-intel-scratch-space**

Category: **[MLPerf benchmark support](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-mlperf-inference-intel-scratch-space/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get mlperf inference intel scratch space" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=get,mlperf,inference,intel,scratch,space`

    `cm run script --tags=get,mlperf,inference,intel,scratch,space[,variations] [--input_flags]`

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "get mlperf inference intel scratch space"`

    `cmr "get mlperf inference intel scratch space [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,mlperf,inference,intel,scratch,space'
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

    `cm docker script "get mlperf inference intel scratch space[variations]" [--input_flags]`

___


#### Variations

  * Group "**version**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_version.#`
      - Environment variables:
        - *CM_INTEL_SCRATCH_SPACE_VERSION*: `#`
      - Workflow:
    * **`_version.4_0`** (default)
      - Environment variables:
        - *CM_INTEL_SCRATCH_SPACE_VERSION*: `4_0`
      - Workflow:

    </details>


#### Default variations

`_version.4_0`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--scratch_path=value`  &rarr;  `MLPERF_INTEL_SCRATCH_PATH=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "scratch_path":...}
```

</details>


##### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-mlperf-inference-intel-scratch-space/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/get-mlperf-inference-intel-scratch-space/run.bat)
___
#### Script output
`cmr "get mlperf inference intel scratch space [,variations]" [--input_flags] -j`