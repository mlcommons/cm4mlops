Automatically generated README for this automation recipe: **download-torrent**

Category: **DevOps automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=download-torrent,69b752c5618e45bb) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/download-torrent)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *download,torrent,download-torrent*
* Output cached? *True*
* See [pipeline of dependencies](#dependencies-on-other-cm-scripts) on other CM scripts


---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://access.cknowledge.org/playground/?action=install)
* [CM Getting Started Guide](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@ck```

#### Print CM help from the command line

````cmr "download torrent download-torrent" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=download,torrent,download-torrent`

`cm run script --tags=download,torrent,download-torrent[,variations] [--input_flags]`

*or*

`cmr "download torrent download-torrent"`

`cmr "download torrent download-torrent [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'download,torrent,download-torrent'
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

```cmr "cm gui" --script="download,torrent,download-torrent"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=download,torrent,download-torrent) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "download torrent download-torrent[variations]" [--input_flags]`

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_torrent.#`
      - Environment variables:
        - *CM_TORRENT_FILE*: `#`
      - Workflow:

    </details>


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--wait=value`  &rarr;  `CM_TORRENT_WAIT_UNTIL_COMPLETED=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "wait":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_TORRENT_WAIT_UNTIL_COMPLETED: `no`

</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/download-torrent/_cm.json)***
     * get,generic-sys-util,_transmission
       - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/download-torrent/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/download-torrent/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/download-torrent/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/download-torrent/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/download-torrent/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/download-torrent/_cm.json)

___
### Script output
`cmr "download torrent download-torrent [,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `<<<CM_TORRENT_DOWNLOADED_PATH_ENV_KEY>>>`
* `CM_TORRENT_DOWNLOADED_PATH`
#### New environment keys auto-detected from customize

* `CM_TORRENT_DOWNLOADED_PATH`