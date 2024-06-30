docker build  ^
 --build-arg GID=\" $(id -g $USER) \" --build-arg UID=\" $(id -u $USER) \" ^
 -f "/home/anandhu/CM/repos/anandhu-eng@cm4mlops/script/app-mlperf-inference/dockerfiles/mlperf-inference:mlpinf-v4.0-cuda12.2-cudnn8.9-x86_64-ubuntu20.04-public.Dockerfile" ^
 -t "cknowledge/cm-script-app-mlperf-inference:ubuntu-20.04-latest" ^
 .
