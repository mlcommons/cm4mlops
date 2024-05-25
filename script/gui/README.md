# gui
Automatically generated README for this automation recipe: **gui**

Category: **[GUI](..)**

License: **Apache 2.0**

Developers: [Grigori Fursin](https://cKnowledge.org/gfursin)


---

This CM script provides a unified GUI to run CM scripts using [Streamlit library](https://streamlit.io).

If you want to run it in a cloud (Azure, AWS, GCP), you need to open some port and test that you can reach it from outside.

By default, streamlit uses port 8501 but you can change it as follows:

```bash
cm run script "cm gui" --port 80
```

If you have troubles accessing this port, use this simple python module to test if your port is open:
```bash
python3 -m http.server 80
```


* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/gui/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "cm gui cm-gui script-gui cm-script-gui streamlit" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=cm,gui,cm-gui,script-gui,cm-script-gui,streamlit`

    `cm run script --tags=cm,gui,cm-gui,script-gui,cm-script-gui,streamlit[,variations] [--input_flags]`

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "cm gui cm-gui script-gui cm-script-gui streamlit"`

    `cmr "cm gui cm-gui script-gui cm-script-gui streamlit [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*


#### Input Flags

* --**script**=script tags
* --**app**=gui app

=== "Python"

    ```python
r=cm.access({... , "script":...}
```
=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'cm,gui,cm-gui,script-gui,cm-script-gui,streamlit'
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

    `cm docker script "cm gui cm-gui script-gui cm-script-gui streamlit[variations]" [--input_flags]`

___


#### Variations

  * Group "**app**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_chatgpt`
      - Environment variables:
        - *CM_GUI_APP*: `chatgpt`
      - Workflow:
    * `_graph`
      - Environment variables:
        - *CM_GUI_APP*: `graph`
      - Workflow:
        1. ***Read "prehook_deps" on other CM scripts***
           * get,generic-python-lib,_matplotlib
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/cm4mlops/tree/master/script/get-generic-python-lib)
           * get,generic-python-lib,_mpld3
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/cm4mlops/tree/master/script/get-generic-python-lib)
    * `_main`
      - Environment variables:
        - *CM_GUI_APP*: `app`
      - Workflow:
    * `_playground`
      - Environment variables:
        - *CM_GUI_APP*: `playground`
      - Workflow:
        1. ***Read "prehook_deps" on other CM scripts***
           * get,generic-python-lib,_matplotlib
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/cm4mlops/tree/master/script/get-generic-python-lib)
           * get,generic-python-lib,_mpld3
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/cm4mlops/tree/master/script/get-generic-python-lib)
           * get,generic-python-lib,_streamlit_option_menu
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/cm4mlops/tree/master/script/get-generic-python-lib)
           * get,generic-python-lib,_numpy
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/cm4mlops/tree/master/script/get-generic-python-lib)
           * get,generic-python-lib,_pandas
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/cm4mlops/tree/master/script/get-generic-python-lib)
           * get,generic-python-lib,_package.plotly
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/cm4mlops/tree/master/script/get-generic-python-lib)
           * get,generic-python-lib,_package.streamlit-aggrid
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/cm4mlops/tree/master/script/get-generic-python-lib)

    </details>


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--address=value`  &rarr;  `CM_GUI_ADDRESS=value`
* `--app=value`  &rarr;  `CM_GUI_APP=value`
* `--exp_key_c=value`  &rarr;  `CM_GUI_GRAPH_EXPERIMENT_AXIS_KEY_C=value`
* `--exp_key_s=value`  &rarr;  `CM_GUI_GRAPH_EXPERIMENT_AXIS_KEY_S=value`
* `--exp_key_x=value`  &rarr;  `CM_GUI_GRAPH_EXPERIMENT_AXIS_KEY_X=value`
* `--exp_key_y=value`  &rarr;  `CM_GUI_GRAPH_EXPERIMENT_AXIS_KEY_Y=value`
* `--exp_max_results=value`  &rarr;  `CM_GUI_GRAPH_EXPERIMENT_MAX_RESULTS=value`
* `--exp_name=value`  &rarr;  `CM_GUI_GRAPH_EXPERIMENT_NAME=value`
* `--exp_tags=value`  &rarr;  `CM_GUI_GRAPH_EXPERIMENT_TAGS=value`
* `--exp_title=value`  &rarr;  `CM_GUI_GRAPH_EXPERIMENT_TITLE=value`
* `--exp_uid=value`  &rarr;  `CM_GUI_GRAPH_EXPERIMENT_RESULT_UID=value`
* `--no_browser=value`  &rarr;  `CM_GUI_NO_BROWSER=value`
* `--no_run=value`  &rarr;  `CM_GUI_NO_RUN=value`
* `--port=value`  &rarr;  `CM_GUI_PORT=value`
* `--prefix=value`  &rarr;  `CM_GUI_SCRIPT_PREFIX_LINUX=value`
* `--script=value`  &rarr;  `CM_GUI_SCRIPT_TAGS=value`
* `--title=value`  &rarr;  `CM_GUI_TITLE=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "address":...}
```

</details>

#### Default environment


These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_GUI_EXTRA_CMD: ``
* CM_GUI_SCRIPT_PREFIX_LINUX: `gnome-terminal --`
* CM_GUI_APP: `app`



##### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/gui/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/gui/run.bat)
___
#### Script output
`cmr "cm gui cm-gui script-gui cm-script-gui streamlit [,variations]" [--input_flags] -j`