# get-mlperf-power-dev
Automatically generated README for this automation recipe: **get-mlperf-power-dev**

Category: **[MLPerf benchmark support](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-mlperf-power-dev/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get src source power power-dev mlperf mlcommons" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=get,src,source,power,power-dev,mlperf,mlcommons`

    `cm run script --tags=get,src,source,power,power-dev,mlperf,mlcommons[,variations] `

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "get src source power power-dev mlperf mlcommons"`

    `cmr "get src source power power-dev mlperf mlcommons [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,src,source,power,power-dev,mlperf,mlcommons'
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

    `cm docker script "get src source power power-dev mlperf mlcommons[variations]" `

___


#### Variations

  * Group "**checkout**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_branch.#`
      - Environment variables:
        - *CM_GIT_CHECKOUT*: `#`
      - Workflow:
    * `_sha.#`
      - Environment variables:
        - *CM_GIT_SHA*: `#`
      - Workflow:
    * `_tag.#`
      - Environment variables:
        - *CM_GIT_CHECKOUT_TAG*: `#`
      - Workflow:

    </details>


  * Group "**repo**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_mlcommons`** (default)
      - Environment variables:
        - *CM_GIT_URL*: `https://github.com/mlcommons/power-dev.git`
      - Workflow:
    * `_octoml`
      - Environment variables:
        - *CM_GIT_URL*: `https://github.com/octoml/power-dev.git`
      - Workflow:
    * `_repo.#`
      - Environment variables:
        - *CM_GIT_URL*: `#`
      - Workflow:

    </details>


#### Default variations

`_mlcommons`
#### Default environment


These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_GIT_DEPTH: `--depth 1`
* CM_GIT_PATCH: `no`
* CM_GIT_CHECKOUT_FOLDER: `power-dev`



___
#### Script output
`cmr "get src source power power-dev mlperf mlcommons [,variations]"  -j`