# pull-git-repo
Automatically generated README for this automation recipe: **pull-git-repo**

Category: **[DevOps automation](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/pull-git-repo/_cm.json)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "pull git repo repository" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=pull,git,repo,repository`

    `cm run script --tags=pull,git,repo,repository [--input_flags]`

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "pull git repo repository"`

    `cmr "pull git repo repository " [--input_flags]`


=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'pull,git,repo,repository'
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

    `cm docker script "pull git repo repository" [--input_flags]`

___


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--path=value`  &rarr;  `CM_GIT_CHECKOUT_PATH=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "path":...}
```

</details>


##### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/pull-git-repo/run.sh)
=== "Windows"

No run file exists for Windows
___
#### Script output
`cmr "pull git repo repository " [--input_flags] -j`