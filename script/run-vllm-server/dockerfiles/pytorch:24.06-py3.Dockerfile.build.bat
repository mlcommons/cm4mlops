docker build  --no-cache ^
 --build-arg GID=\" $(id -g $USER) \" --build-arg UID=\" $(id -u $USER) \" ^
 -f "/home/anandhu/CM/repos/anandhu-eng@cm4mlops/script/run-vllm-server/dockerfiles/pytorch:24.06-py3.Dockerfile" ^
 -t "cknowledge/cm-script-run-vllm-server:ubuntu-22.04-latest" ^
 .
