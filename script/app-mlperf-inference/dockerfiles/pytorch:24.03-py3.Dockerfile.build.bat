docker build  ^
 --build-arg GID=\" $(id -g $USER) \" --build-arg UID=\" $(id -u $USER) \" ^
 -f "/home/anandhu/CM/repos/anandhu-eng@cm4mlops/script/app-mlperf-inference/dockerfiles/pytorch:24.03-py3.Dockerfile" ^
 -t "cknowledge/cm-script-app-mlperf-inference:ubuntu-22.04-latest" ^
 .
