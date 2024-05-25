# set-venv
Automatically generated README for this automation recipe: **set-venv**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/set-venv/README-extra.md)

* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/set-venv/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "set venv" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=set,venv`

    `cm run script --tags=set,venv [--input_flags]`

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "set venv"`

    `cmr "set venv " [--input_flags]`


=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'set,venv'
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

    `cm docker script "set venv" [--input_flags]`

___


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--python=value`  &rarr;  `CM_SET_VENV_PYTHON=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "python":...}
```

</details>


___
#### Script output
`cmr "set venv " [--input_flags] -j`