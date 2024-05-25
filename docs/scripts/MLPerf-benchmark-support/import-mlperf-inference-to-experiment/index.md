# import-mlperf-inference-to-experiment
Automatically generated README for this automation recipe: **import-mlperf-inference-to-experiment**

Category: **[MLPerf benchmark support](..)**

License: **Apache 2.0**

Developers: [Grigori Fursin](https://cKnowledge.org/gfursin)
* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/import-mlperf-inference-to-experiment/README-extra.md)

* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/import-mlperf-inference-to-experiment/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "import mlperf inference mlperf-inference experiment 2experiment to-experiment" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=import,mlperf,inference,mlperf-inference,experiment,2experiment,to-experiment`

    `cm run script --tags=import,mlperf,inference,mlperf-inference,experiment,2experiment,to-experiment[,variations] [--input_flags]`

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "import mlperf inference mlperf-inference experiment 2experiment to-experiment"`

    `cmr "import mlperf inference mlperf-inference experiment 2experiment to-experiment [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'import,mlperf,inference,mlperf-inference,experiment,2experiment,to-experiment'
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

    `cm docker script "import mlperf inference mlperf-inference experiment 2experiment to-experiment[variations]" [--input_flags]`

___


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_skip_checker`
      - Environment variables:
        - *CM_SKIP_SUBMISSION_CHECKER*: `True`
      - Workflow:

    </details>


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--submitter=value`  &rarr;  `CM_MLPERF_SUBMITTER=value`
* `--target_repo=value`  &rarr;  `CM_IMPORT_MLPERF_INFERENCE_TARGET_REPO=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "submitter":...}
```

</details>


___
#### Script output
`cmr "import mlperf inference mlperf-inference experiment 2experiment to-experiment [,variations]" [--input_flags] -j`