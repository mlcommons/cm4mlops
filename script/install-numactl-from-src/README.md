# Build numactl from sources
Automatically generated README for this automation recipe: **install-numactl-from-src**

Category: **[Detection or installation of tools and artifacts](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/install-numactl-from-src/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "install src from.src numactl src-numactl" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=install,src,from.src,numactl,src-numactl`

    `cm run script --tags=install,src,from.src,numactl,src-numactl[,variations] `

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "install src from.src numactl src-numactl"`

    `cmr "install src from.src numactl src-numactl [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'install,src,from.src,numactl,src-numactl'
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

    `cm docker script "install src from.src numactl src-numactl[variations]" `

___


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_branch.#`
      - Environment variables:
        - *CM_GIT_CHECKOUT*: `#`
      - Workflow:
    * `_sha.#`
      - Environment variables:
        - *CM_GIT_CHECKOUT_SHA*: `#`
      - Workflow:
    * `_tag.#`
      - Environment variables:
        - *CM_GIT_CHECKOUT_TAG*: `#`
      - Workflow:

    </details>


  * Group "**repo**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_repo.#`
      - Environment variables:
        - *CM_GIT_URL*: `#`
      - Workflow:
    * **`_repo.https://github.com/numactl/numactl`** (default)
      - Environment variables:
        - *CM_GIT_URL*: `https://github.com/numactl/numactl`
      - Workflow:

    </details>


#### Default variations

`_repo.https://github.com/numactl/numactl`

##### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/install-numactl-from-src/run.sh)
=== "Windows"

No run file exists for Windows
___
#### Script output
`cmr "install src from.src numactl src-numactl [,variations]"  -j`