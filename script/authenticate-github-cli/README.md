# authenticate-github-cli
Automatically generated README for this automation recipe: **authenticate-github-cli**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/authenticate-github-cli/_cm.yaml)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "auth authenticate github gh cli" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=auth,authenticate,github,gh,cli`

    `cm run script --tags=auth,authenticate,github,gh,cli [--input_flags]`

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "auth authenticate github gh cli"`

    `cmr "auth authenticate github gh cli " [--input_flags]`


=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'auth,authenticate,github,gh,cli'
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

    `cm docker script "auth authenticate github gh cli" [--input_flags]`

___


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--with-token=value`  &rarr;  `CM_GH_AUTH_TOKEN=value`
* `--with_token=value`  &rarr;  `CM_GH_AUTH_TOKEN=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "with-token":...}
```

</details>


##### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/authenticate-github-cli/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/authenticate-github-cli/run.bat)
___
#### Script output
`cmr "auth authenticate github gh cli " [--input_flags] -j`