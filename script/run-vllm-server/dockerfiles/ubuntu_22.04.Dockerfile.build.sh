docker build  --no-cache \
 --build-arg GID=\" $(id -g $USER) \" --build-arg UID=\" $(id -u $USER) \" \
 -f "/home/anandhu/CM/repos/anandhu-eng@cm4mlops/script/run-vllm-server/dockerfiles/ubuntu_22.04.Dockerfile" \
 -t "cknowledge/cm-script-run-vllm-server:ubuntu-22.04-latest" \
 .
