# get-mlperf-inference-utils
Automatically generated README for this automation recipe: **get-mlperf-inference-utils**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/get-mlperf-inference-utils/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get mlperf inference util utils functions" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=get,mlperf,inference,util,utils,functions`

    `cm run script --tags=get,mlperf,inference,util,utils,functions `

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "get mlperf inference util utils functions"`

    `cmr "get mlperf inference util utils functions " `


=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,mlperf,inference,util,utils,functions'
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

    `cm docker script "get mlperf inference util utils functions" `

___


___
#### Script output
`cmr "get mlperf inference util utils functions "  -j`