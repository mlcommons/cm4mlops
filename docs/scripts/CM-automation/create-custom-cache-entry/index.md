# create-custom-cache-entry
Automatically generated README for this automation recipe: **create-custom-cache-entry**

Category: **[CM automation](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/create-custom-cache-entry/_cm.yaml)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "create custom cache entry" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=create,custom,cache,entry`

    `cm run script --tags=create,custom,cache,entry [--input_flags]`

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "create custom cache entry"`

    `cmr "create custom cache entry " [--input_flags]`


=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'create,custom,cache,entry'
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

    `cm docker script "create custom cache entry" [--input_flags]`

___


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--env_key=value`  &rarr;  `CM_CUSTOM_CACHE_ENTRY_ENV_KEY=value`
* `--env_key2=value`  &rarr;  `CM_CUSTOM_CACHE_ENTRY_ENV_KEY2=value`
* `--path=value`  &rarr;  `CM_CUSTOM_CACHE_ENTRY_PATH=value`
* `--to=value`  &rarr;  `CM_CUSTOM_CACHE_ENTRY_PATH=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "env_key":...}
```

</details>


___
#### Script output
`cmr "create custom cache entry " [--input_flags] -j`