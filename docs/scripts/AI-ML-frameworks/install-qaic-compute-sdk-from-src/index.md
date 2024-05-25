# install-qaic-compute-sdk-from-src
Automatically generated README for this automation recipe: **install-qaic-compute-sdk-from-src**

Category: **[AI/ML frameworks](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/install-qaic-compute-sdk-from-src/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get qaic from.src software compute compute-sdk qaic-compute-sdk sdk" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=get,qaic,from.src,software,compute,compute-sdk,qaic-compute-sdk,sdk`

    `cm run script --tags=get,qaic,from.src,software,compute,compute-sdk,qaic-compute-sdk,sdk[,variations] `

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "get qaic from.src software compute compute-sdk qaic-compute-sdk sdk"`

    `cmr "get qaic from.src software compute compute-sdk qaic-compute-sdk sdk [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,qaic,from.src,software,compute,compute-sdk,qaic-compute-sdk,sdk'
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

    `cm docker script "get qaic from.src software compute compute-sdk qaic-compute-sdk sdk[variations]" `

___


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_branch.#`
      - Environment variables:
        - *CM_GIT_CHECKOUT*: `#`
      - Workflow:

    </details>


  * Group "**installation-mode**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_debug`
      - Environment variables:
        - *CM_QAIC_COMPUTE_SDK_INSTALL_MODE*: `debug`
      - Workflow:
    * **`_release`** (default)
      - Environment variables:
        - *CM_QAIC_COMPUTE_SDK_INSTALL_MODE*: `release`
      - Workflow:
    * `_release-assert`
      - Environment variables:
        - *CM_QAIC_COMPUTE_SDK_INSTALL_MODE*: `release-assert`
      - Workflow:

    </details>


  * Group "**repo-source**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_repo.#`
      - Environment variables:
        - *CM_GIT_URL*: `#`
      - Workflow:
    * **`_repo.quic`** (default)
      - Environment variables:
        - *CM_GIT_URL*: `https://github.com/quic/software-kit-for-qualcomm-cloud-ai-100-cc`
      - Workflow:

    </details>


#### Default variations

`_release,_repo.quic`

##### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/install-qaic-compute-sdk-from-src/run.sh)
=== "Windows"

No run file exists for Windows
___
#### Script output
`cmr "get qaic from.src software compute compute-sdk qaic-compute-sdk sdk [,variations]"  -j`