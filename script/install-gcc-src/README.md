Automatically generated README for this automation recipe: **install-gcc-src**

Category: **Compiler automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=install-gcc-src,faae0ebd6e1242db) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@cm4mlops](https://github.com/mlcommons/cm4mlops/tree/dev)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/cm4mlops/tree/dev/script/install-gcc-src)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *install,src,gcc,src-gcc*
* Output cached? *True*
* See [pipeline of dependencies](#dependencies-on-other-cm-scripts) on other CM scripts


---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://access.cknowledge.org/playground/?action=install)
* [CM Getting Started Guide](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "install src gcc src-gcc" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=install,src,gcc,src-gcc`

`cm run script --tags=install,src,gcc,src-gcc `

*or*

`cmr "install src gcc src-gcc"`

`cmr "install src gcc src-gcc " `


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'install,src,gcc,src-gcc'
                  'out':'con',
                  ...
                  (other input keys for this script)
                  ...
                 })

if r['return']>0:
    print (r['error'])

```

</details>


#### Run this script via GUI

```cmr "cm gui" --script="install,src,gcc,src-gcc"```

#### Run this script via Docker (beta)

`cm docker script "install src gcc src-gcc" `

___
### Customization

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

#### Versions
Default version: `12`

* `master`
___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/install-gcc-src/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/cm4mlops/tree/master/script/detect-os)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/cm4mlops/tree/dev/script/install-gcc-src/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/install-gcc-src/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/dev/script/install-gcc-src/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/install-gcc-src/_cm.json)
  1. Run "postrocess" function from customize.py
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/install-gcc-src/_cm.json)***
     * get,gcc
       * Skip this dependenecy only if all ENV vars are set:<br>
`{'CM_REQUIRE_INSTALL': ['yes']}`
       - CM script: [get-gcc](https://github.com/mlcommons/cm4mlops/tree/master/script/get-gcc)

___
### Script output
`cmr "install src gcc src-gcc "  -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
