Automatically generated README for this automation recipe: **install-github-cli**

Category: **Detection or installation of tools and artifacts**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=install-github-cli,cd948ec309344bf8) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@cm4mlops](https://github.com/mlcommons/cm4mlops/tree/dev)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/cm4mlops/tree/dev/script/install-github-cli)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *install,gh,github,cli,github-cli*
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

````cmr "install gh github cli github-cli" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=install,gh,github,cli,github-cli`

`cm run script --tags=install,gh,github,cli,github-cli `

*or*

`cmr "install gh github cli github-cli"`

`cmr "install gh github cli github-cli " `


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'install,gh,github,cli,github-cli'
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

```cmr "cm gui" --script="install,gh,github,cli,github-cli"```

#### Run this script via Docker (beta)

`cm docker script "install gh github cli github-cli" `

___
### Customization

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/install-github-cli/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/cm4mlops/tree/master/script/detect-os)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/cm4mlops/tree/dev/script/install-github-cli/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/install-github-cli/_cm.json)
  1. ***Run native script if exists***
     * [run-macos.sh](https://github.com/mlcommons/cm4mlops/tree/dev/script/install-github-cli/run-macos.sh)
     * [run-rhel.sh](https://github.com/mlcommons/cm4mlops/tree/dev/script/install-github-cli/run-rhel.sh)
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/dev/script/install-github-cli/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/install-github-cli/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/cm4mlops/tree/dev/script/install-github-cli/_cm.json)

___
### Script output
`cmr "install gh github cli github-cli "  -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
