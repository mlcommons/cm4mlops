# Getting Started

## Simple script automation execution in cm

A simple script automation execution in CM is as follows:

```
cm run script --tags=detect,os -j
```

This would capture the OS details of the system which it is run. Example details could be found here:
```
    "CM_HOST_OS_TYPE": "linux",
    "CM_HOST_OS_BITS": "64",
    "CM_HOST_OS_FLAVOR": "ubuntu",
    "CM_HOST_OS_FLAVOR_LIKE": "debian",
    "CM_HOST_OS_VERSION": "24.04",
    "CM_HOST_OS_KERNEL_VERSION": "6.8.0-45-generic",
    "CM_HOST_OS_GLIBC_VERSION": "2.39",
    "CM_HOST_OS_MACHINE": "x86_64",
    "CM_HOST_OS_PACKAGE_MANAGER": "apt",
    "CM_HOST_OS_PACKAGE_MANAGER_INSTALL_CMD": "DEBIAN_FRONTEND=noninteractive apt-get install -y",
    "CM_HOST_OS_PACKAGE_MANAGER_UPDATE_CMD": "apt-get update -y",
    "+CM_HOST_OS_DEFAULT_LIBRARY_PATH": [
      "/usr/local/lib/x86_64-linux-gnu",
      "/lib/x86_64-linux-gnu",
      "/usr/lib/x86_64-linux-gnu",
      "/usr/lib/x86_64-linux-gnu64",
      "/usr/local/lib64",
      "/lib64",
      "/usr/lib64",
      "/usr/local/lib",
      "/lib",
      "/usr/lib",
      "/usr/x86_64-linux-gnu/lib64",
      "/usr/x86_64-linux-gnu/lib"
    ],
    "CM_HOST_PLATFORM_FLAVOR": "x86_64",
    "CM_HOST_PYTHON_BITS": "64",
    "CM_HOST_SYSTEM_NAME": "intel-spr-i9"
```



### How to add new CM scripts?

One of the main requirement for CM was to provide a very light-weight connectors 
between existing automation scripts and tools rather than substituting them.

You can add your own scripts and tools to CM using the following command
that will create a ready-to-use dummy CM script named `hello-world`:

```bash
cm add script hello-world --tags=hello-world,display,test
```

This creates a bare cm script inside the local repo. The new folder structure would look something like this:
```
└── CM
    ├── index.json
    ├── repos
    │   ├── local
    │   │   ├── cfg
    │   │   ├── cache
    │   │   ├── cmr.yaml
    │   │   └── script
    │   │   	└── hello-world
    │   │       	├── _cm.yaml
    │   │       	├── customize.py
    │   │       	├── README-extra.md
    │   │       	├── run.bat
    │   │       	└── run.sh
    │   └── mlcommons@cm4mlops
    └── repos.json
```

You can also run it from python as follows:
```bash
import cmind
output=cmind.access({'action':'run', 
                     'automation':'script', 
                     'tags':'hello-world,display,test`})
if output['return']==0: print (output)
```

If you find that the script you are newly creating is similar to any existing scripts in any cm repository, 
you could create a new script by copying another script entirely using the following command:

```
cm copy script <source_script> .:<target_script>
```

The `source_script` contains the name of the script that you want to make a copy and `target_script` contains the name of the new script that will be created as a copy of the `source_script`.
The existing script names in `cm4mlops` repo could be found [here](https://github.com/mlcommons/cm4mlops/tree/mlperf-inference/script).


## How to cache and reuse CM scripts' output?

By default, CM scripts run in the current directory and record all new files there.

For example, the following universal download script will download 
computer mouse image to the current directory:

<sup>

```bash
cm run script --tags=download,file,_wget --url=https://cKnowledge.org/ai/data/computer_mouse.jpg --verify=no --env.CM_DOWNLOAD_CHECKSUM=45ae5c940233892c2f860efdf0b66e7e
```

</sup>

In some cases, we want to cache and reuse the output of automation recipes (such as downloading models, preprocessing data sets or building some applications)
rather than just downloading it to the current directory.

Following the feedback from our users, we implemented a `cache` automation in CM similar to `script`.
Whenever CM encounters `"cache":true` in a meta description of a given script, it will create
a `cache` directory in `$HOME/CM/repos/local` with some unique ID and the same tags as `script`,
and will execute that script there to record all the data in cache. 

Whenever the same CM script is executed and CM finds an associated cache entry, 
it will skip execution and will reuse files from that entry.

Furthermore, it is possible to reuse large cached files in other projects that call the same CM scripts!

You can see cache entries and find a specific one as follows:

```bash
cmr "get ml-model resnet50 _onnx" -j

cm show cache
cm show cache "get ml-model resnet50 _onnx" 
cm find cache "download file ml-model resnet50 _onnx" 
cm info cache "download file ml-model resnet50 _onnx" 
```

You can clean some cache entries as follows:
```bash
cm rm cache --tags=ml-model,resnet50
```

You can also clean all CM `cache` entries and start from scratch as follows:
```bash
cm rm cache -f
```

In fact, you can remove `$HOME/CM` to reset CM framework completely
and remove all downloaded repositories and cached entries.


## How to use CM with Python virtual environments?


Using CM `cache` makes it possible to run CM automations for multiple virtual environments
installed inside CM `cache` entries. It is possible to run CM automations with different Python
virtual environments transparently to users while avoiding messing up native user environment.

We created the following CM automation recipe to create virtual environments:

```bash
cm run script --tags=install,python-venv --name=mlperf
cm show cache --tags=python-venv,name-mlperf
export CM_SCRIPT_EXTRA_CMD="--adr.python.name=mlperf"
```

If you now run our image classification automation recipe, 
it will reuse model and dataset from the cache, but will
use the newly created virtual environment `mlperf` for running the script.


## How to debug CM scripts?

One of the requirements from CM users was to avoid new and/or complex ways to debug CM automations.
Using native scripts and Python code makes it possible to apply standard techniques and tools to debug CM automations.

We were also asked to add `--debug` flag to open a shell after the last native script is executed - 
this allows users to rerun the last command line with all environment variables and paths assembled by CM
while having a full and native access to change environment and run the final command 
(such as pinning threads, changing batch sizes, modifying files, etc).

You can try it as follows on Linux, MacOS, Windows or other operating system as follows:

```bash
cm run script --tags=python,app,image-classification,onnx,_cpu --input=computer_mouse.jpg --debug

```

You can also use GDB via environment variable `--env.CM_RUN_PREFIX="gdb --args "`
to run the final command via GDB.

## How to use CM with containers?

One of the key requirements for CM was to run automation natively or inside containers in the same way.

We want CM scripts to adapt to the current/latest environment natively or run in the
container automatically generated on the fly when requested by user for more stability and determinism.

In such case, we can get rid of separate development of native scripts/workflows and Dockerfile 
and use the same CM commands instead.

To run a given script in an automatically-generated container, you can simply substitute `cm run script` 
with `cm docker script` or `cmr` with `cmrd`:

```bash
cm docker script --tags=python,app,image-classification,onnx,_cpu"
```

CM will automatically generate a Dockerfile with Ubuntu 22.04 in the `dockerfiles` 
directory of a given script, will build container with the same CM command
and will run it inside container.

* If you want to stay in the container, you can add flag `--docker_it`.
* You can change OS inside container using `--docker_base_image`, `--docker_os` and `--docker_os_version`.

The tricky part is when we want to use host files and directories with a given CM script inside container. 
To make it easier for users, we have implemented automatic detection and mounting of files and directories 
in CM script.

Developers of a CM script just need to specify which flags and environment variables are local files or directories
using `input_paths` in `docker` dictionary of the meta-description of this script:

```yaml
docker:
  skip_run_cmd: 'no'
  all_gpus: 'yes'
  input_paths:
    - input
    - env.CM_IMAGE
    - output
  skip_input_for_fake_run:
    - input
    - env.CM_IMAGE
    - output
    - j
  pre_run_cmds:
    - echo \"CM pre run commands\"
```

When you run the same script via container with the local computer_mouse.jpg file as an input,
CM will automatically mount current directory and will update the input to the CM script
inside container with the internal path:

<sup>

```bash
cm docker script --tags=python,app,image-classification,onnx,_cpu --input=computer_mouse.jpg

...

docker build  -f D:\Work1\CM\ck\cm-mlops\script\app-image-classification-onnx-py\dockerfiles\ubuntu_22.04.Dockerfile \
              -t cknowledge/cm-script-app-image-classification-onnx-py:ubuntu-22.04-latest .

...

Container launch command:
docker run  --entrypoint ""  --gpus=all -v D:\Work1\CM\ck\docs\computer_mouse.jpg:/cm-mount/Work1/CM/ck/docs/computer_mouse.jpg 
                            cknowledge/cm-script-app-image-classification-onnx-py:ubuntu-22.04-latest 
                            bash -c "echo \"CM pre run commands\" && 
                            cm run script --tags=python,app,image-classification,onnx,_cpu 
                            --input=/cm-mount/Work1/CM/ck/docs/computer_mouse.jpg "

CM pre run commands


```

</sup>

It is now possible to download large data sets and models to the host from CM containers
or pass host scratch pads and data to CM containers transparently to a user!

## How to run MLPerf benchmarks via CM?

Please check this [documentation](https://docs.mlcommons.org/inference/) for more details.


