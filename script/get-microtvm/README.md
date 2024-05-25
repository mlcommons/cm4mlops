# get-microtvm
Automatically generated README for this automation recipe: **get-microtvm**

Category: **[TinyML automation](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-microtvm/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-microtvm/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get src source microtvm tiny" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=get,src,source,microtvm,tiny`

    `cm run script --tags=get,src,source,microtvm,tiny[,variations] [--input_flags]`

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "get src source microtvm tiny"`

    `cmr "get src source microtvm tiny [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,src,source,microtvm,tiny'
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

    `cm docker script "get src source microtvm tiny[variations]" [--input_flags]`

___


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_full-history`
      - Environment variables:
        - *CM_GIT_DEPTH*: `--depth 10`
      - Workflow:
    * `_short-history`
      - Environment variables:
        - *CM_GIT_DEPTH*: `--depth 10`
      - Workflow:

    </details>


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--ssh=value`  &rarr;  `CM_GIT_SSH=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "ssh":...}
```

</details>

#### Versions
Default version: `main`

* `custom`
* `main`

##### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-microtvm/run.sh)
=== "Windows"

No run file exists for Windows
___
#### Script output
`cmr "get src source microtvm tiny [,variations]" [--input_flags] -j`