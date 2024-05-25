# app-stable-diffusion-onnx-py
Automatically generated README for this automation recipe: **app-stable-diffusion-onnx-py**

Category: **[Modular AI/ML application pipeline](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/app-stable-diffusion-onnx-py/README-extra.md)

* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/app-stable-diffusion-onnx-py/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "modular python app stable-diffusion onnx" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI
    `cm run script --tags=modular,python,app,stable-diffusion,onnx`

    `cm run script --tags=modular,python,app,stable-diffusion,onnx[,variations] [--input_flags]`

=== "CLI Alt"
    ##### Run this script via CLI (alternative)

    `cmr "modular python app stable-diffusion onnx"`

    `cmr "modular python app stable-diffusion onnx [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*


#### Input Flags

* --**text**=Text to generate image
* --**output**=Output directory

=== "Python"

    ```python
r=cm.access({... , "text":...}
```
=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'modular,python,app,stable-diffusion,onnx'
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

    `cm docker script "modular python app stable-diffusion onnx[variations]" [--input_flags]`

___


#### Variations

  * Group "**target**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_cpu`** (default)
      - Environment variables:
        - *USE_CPU*: `True`
        - *CM_DEVICE*: `cpu`
      - Workflow:
    * `_cuda`
      - Environment variables:
        - *USE_CUDA*: `True`
        - *CM_DEVICE*: `cuda:0`
      - Workflow:

    </details>


#### Default variations

`_cpu`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--output=value`  &rarr;  `CM_APP_STABLE_DIFFUSION_ONNX_PY_OUTPUT=value`
* `--text=value`  &rarr;  `CM_APP_STABLE_DIFFUSION_ONNX_PY_TEXT=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "output":...}
```

</details>


##### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/app-stable-diffusion-onnx-py/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/app-stable-diffusion-onnx-py/run.bat)
___
#### Script output
`cmr "modular python app stable-diffusion onnx [,variations]" [--input_flags] -j`