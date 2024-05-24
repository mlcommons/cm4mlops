Automatically generated README for this automation recipe: **test-deps-conditions**

Category: **Tests**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=test-deps-conditions,5cb82aee472640df) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@cm4mlops](https://github.com/mlcommons/cm4mlops/tree/dev)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/cm4mlops/tree/dev/script/test-deps-conditions)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* All CM tags to find and reuse this script (see in above meta description): *test,deps,conditions*
* Output cached? *False*
* See [pipeline of dependencies](#dependencies-on-other-cm-scripts) on other CM scripts


---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://access.cknowledge.org/playground/?action=install)
* [CM Getting Started Guide](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "test deps conditions" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=test,deps,conditions`

`cm run script --tags=test,deps,conditions [--input_flags]`

*or*

`cmr "test deps conditions"`

`cmr "test deps conditions " [--input_flags]`


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'test,deps,conditions'
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

```cmr "cm gui" --script="test,deps,conditions"```

#### Run this script via Docker (beta)

`cm docker script "test deps conditions" [--input_flags]`

___
### Customization


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--test1=value`  &rarr;  `CM_ENV1=value`
* `--test2=value`  &rarr;  `CM_ENV2=value`
* `--test3=value`  &rarr;  `CM_ENV3=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "test1":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/test-deps-conditions/_cm.yaml)***
     * print,native,hello-world,_skip_print_env
       - CM script: [print-hello-world](https://github.com/mlcommons/cm4mlops/tree/master/script/print-hello-world)
     * print,native,hello-world,_skip_print_env,_text.SKIP_IF_ALL_ENV
       * Skip this dependenecy only if all ENV vars are set:<br>
`{'CM_ENV1': [True], 'CM_ENV2': [True], 'CM_ENV3': [True]}`
       - CM script: [print-hello-world](https://github.com/mlcommons/cm4mlops/tree/master/script/print-hello-world)
     * print,native,hello-world,_skip_print_env,_text.SKIP_IF_ANY_ENV
       * Skip this dependenecy only if any of ENV vars are set:<br>
`{'CM_ENV1': [True], 'CM_ENV2': [True], 'CM_ENV3': [True]}`
       - CM script: [print-hello-world](https://github.com/mlcommons/cm4mlops/tree/master/script/print-hello-world)
     * print,native,hello-world,_skip_print_env,_text.ENABLE_IF_ALL_ENV
       * Enable this dependency only if all ENV vars are set:<br>
`{'CM_ENV1': [True], 'CM_ENV2': [True], 'CM_ENV3': [True]}`
       - CM script: [print-hello-world](https://github.com/mlcommons/cm4mlops/tree/master/script/print-hello-world)
     * print,native,hello-world,_skip_print_env,_text.ENABLE_IF_ANY_ENV
       * Enable this dependency only if any of ENV vars are set:<br>
`{'CM_ENV1': [True], 'CM_ENV2': [True], 'CM_ENV3': [True]}`
       - CM script: [print-hello-world](https://github.com/mlcommons/cm4mlops/tree/master/script/print-hello-world)
  1. Run "preprocess" function from customize.py
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/test-deps-conditions/_cm.yaml)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/test-deps-conditions/_cm.yaml)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/test-deps-conditions/_cm.yaml)

___
### Script output
`cmr "test deps conditions " [--input_flags] -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
