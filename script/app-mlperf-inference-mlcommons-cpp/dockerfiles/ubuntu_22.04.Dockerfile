FROM ubuntu:22.04

# Maintained by the MLCommons taskforce on automation and reproducibility
LABEL github="https://github.com/mlcommons/ck"
LABEL maintainer="https://cKnowledge.org/mlcommons-taskforce"

SHELL ["/bin/bash", "-c"]
ARG CM_GH_TOKEN

# Notes: https://runnable.com/blog/9-common-dockerfile-mistakes
# Install system dependencies
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip git sudo wget

# Install python packages
RUN python3 -m pip install cmind requests giturlparse  

# Setup docker environment
ENTRYPOINT ["/bin/bash", "-c"]
ENV TZ="US/Pacific"
ENV PATH="${PATH}:/home/cmuser/.local/bin"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ >/etc/timezone

# Setup docker user
RUN groupadd cm
RUN useradd  -g cm --create-home --shell /bin/bash cmuser
RUN echo "cmuser ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
USER cmuser:cm
WORKDIR /home/cmuser

# Download CM repo for scripts
RUN cm pull repo ctuning@mlcommons-ck

# Install all system dependencies
RUN cm run script --tags=get,sys-utils-cm --quiet

# Run commands
RUN cm run script --tags=app,mlperf,inference,_intel-original,_gptj-99 --quiet --fake_run --env.CM_RUN_STATE_DOCKER=True  
