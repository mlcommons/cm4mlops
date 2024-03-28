Automatically generated README for this automation recipe: **print-hello-world**

Category: **Tests**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=print-hello-world,b9f0acba4aca4baa) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/print-hello-world)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *print,hello-world,hello world,hello,world,native-script,native,script*
* Output cached? *False*
* See [pipeline of dependencies](#dependencies-on-other-cm-scripts) on other CM scripts


---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://access.cknowledge.org/playground/?action=install)
* [CM Getting Started Guide](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@ck```

#### Print CM help from the command line

````cmr "print hello-world hello world hello world native-script native script" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=print,hello-world,hello world,hello,world,native-script,native,script`

`cm run script --tags=print,hello-world,hello world,hello,world,native-script,native,script [--input_flags]`

*or*

`cmr "print hello-world hello world hello world native-script native script"`

`cmr "print hello-world hello world hello world native-script native script " [--input_flags]`


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'print,hello-world,hello world,hello,world,native-script,native,script'
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

```cmr "cm gui" --script="print,hello-world,hello world,hello,world,native-script,native,script"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=print,hello-world,hello world,hello,world,native-script,native,script) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "print hello-world hello world hello world native-script native script" [--input_flags]`

___
### Customization


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--test1=value`  &rarr;  `CM_ENV_TEST1=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "test1":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_ENV_TEST1: `TEST1`

</details>

___
### Dependencies on other CM scripts


  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/print-hello-world/_cm.json)
  1. Run "preprocess" function from customize.py
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/print-hello-world/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/print-hello-world/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/print-hello-world/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/print-hello-world/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/print-hello-world/_cm.json)

___
### Script output
`cmr "print hello-world hello world hello world native-script native script " [--input_flags] -j`
#### New environment keys (filter)

* `CM_ENV_TEST*`
#### New environment keys auto-detected from customize
