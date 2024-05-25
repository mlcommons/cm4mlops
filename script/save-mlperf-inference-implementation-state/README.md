# save-mlperf-inference-implementation-state
Automatically generated README for this automation recipe: **save-mlperf-inference-implementation-state**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/save-mlperf-inference-implementation-state/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "save mlperf inference implementation state" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=save,mlperf,inference,implementation,state`

    `cm run script --tags=save,mlperf,inference,implementation,state `

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "save mlperf inference implementation state"`

    `cmr "save mlperf inference implementation state " `


=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'save,mlperf,inference,implementation,state'
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

    `cm docker script "save mlperf inference implementation state" `

___


___
#### Script output
`cmr "save mlperf inference implementation state "  -j`