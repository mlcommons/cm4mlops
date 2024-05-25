# get-generic-sys-util
Automatically generated README for this automation recipe: **get-generic-sys-util**

Category: **[Detection or installation of tools and artifacts](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-generic-sys-util/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get sys-util generic generic-sys-util" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=get,sys-util,generic,generic-sys-util`

    `cm run script --tags=get,sys-util,generic,generic-sys-util[,variations] `

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "get sys-util generic generic-sys-util"`

    `cmr "get sys-util generic generic-sys-util [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,sys-util,generic,generic-sys-util'
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

    `cm docker script "get sys-util generic generic-sys-util[variations]" `

___


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_g++-12`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `g++12`
      - Workflow:
    * `_gflags-dev`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `gflags-dev`
      - Workflow:
    * `_git-lfs`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `git-lfs`
      - Workflow:
    * `_glog-dev`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `glog-dev`
      - Workflow:
    * `_libboost-all-dev`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `libboost-all-dev`
      - Workflow:
    * `_libbz2-dev`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `libbz2_dev`
      - Workflow:
    * `_libev-dev`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `libev_dev`
      - Workflow:
    * `_libffi-dev`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `libffi_dev`
      - Workflow:
    * `_libffi7`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `libffi7`
      - Workflow:
    * `_libgdbm-dev`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `libgdbm_dev`
      - Workflow:
    * `_libgmock-dev`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `libgmock-dev`
      - Workflow:
    * `_liblzma-dev`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `liblzma_dev`
      - Workflow:
    * `_libmpfr-dev`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `libmpfr-dev`
      - Workflow:
    * `_libncurses-dev`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `libncurses_dev`
      - Workflow:
    * `_libnuma-dev`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `libnuma-dev`
      - Workflow:
    * `_libpci-dev`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `libpci-dev`
      - Workflow:
    * `_libre2-dev`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `libre2-dev`
      - Workflow:
    * `_libreadline-dev`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `libreadline_dev`
      - Workflow:
    * `_libsqlite3-dev`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `libsqlite3_dev`
      - Workflow:
    * `_libssl-dev`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `libssl_dev`
      - Workflow:
    * `_libudev-dev`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `libudev-dev`
      - Workflow:
    * `_ninja-build`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `ninja-build`
      - Workflow:
    * `_nlohmann-json3-dev`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `nlohmann_json3_dev`
      - Workflow:
    * `_ntpdate`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `ntpdate`
      - Workflow:
    * `_numactl`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `numactl`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * install,numactl,from.src
             * Enable this dependency only if all ENV vars are set:<br>
`{'CM_HOST_OS_FLAVOR': ['rhel'], 'CM_HOST_OS_VERSION': ['9.1', '9.2', '9.3']}`
             - CM script: [install-numactl-from-src](https://github.com/mlcommons/cm4mlops/tree/master/script/install-numactl-from-src)
    * `_nvidia-cuda-toolkit`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `nvidia-cuda-toolkit`
      - Workflow:
    * `_rapidjson-dev`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `rapidjson-dev`
      - Workflow:
    * `_rsync`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `rsync`
      - Workflow:
    * `_screen`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `screen`
      - Workflow:
    * `_sox`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `sox`
      - Workflow:
    * `_tk-dev`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `tk_dev`
      - Workflow:
    * `_transmission`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `transmission`
      - Workflow:
    * `_wget`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `wget`
      - Workflow:
    * `_zlib`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `zlib`
      - Workflow:
    * `_zlib1g-dev`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `zlib1g_dev`
      - Workflow:

    </details>

#### Default environment


These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_CLEAN_DIRS: `bin`
* CM_SUDO: `sudo`



##### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-generic-sys-util/run.sh)
=== "Windows"

No run file exists for Windows
___
#### Script output
`cmr "get sys-util generic generic-sys-util [,variations]"  -j`