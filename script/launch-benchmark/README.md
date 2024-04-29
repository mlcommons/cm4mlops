Automatically generated README for this automation recipe: **launch-benchmark**

Category: **Collective benchmarking**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=launch-benchmark,5dc7662804bc4cad) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@cm4mlops](https://github.com/mlcommons/cm4mlops/tree/dev)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/cm4mlops/tree/dev/script/launch-benchmark)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* All CM tags to find and reuse this script (see in above meta description): *launch,benchmark*
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

````cmr "launch benchmark" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=launch,benchmark`

`cm run script --tags=launch,benchmark `

*or*

`cmr "launch benchmark"`

`cmr "launch benchmark " `


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'launch,benchmark'
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

```cmr "cm gui" --script="launch,benchmark"```

#### Run this script via Docker (beta)

`cm docker script "launch benchmark" `

___
### Customization

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/launch-benchmark/_cm.yaml)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/cm4mlops/tree/dev/script/launch-benchmark/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/launch-benchmark/_cm.yaml)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/launch-benchmark/_cm.yaml)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/cm4mlops/tree/dev/script/launch-benchmark/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/launch-benchmark/_cm.yaml)

___
### Script output
`cmr "launch benchmark "  -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
