#!/bin/bash

echo "************************************************"
echo "Installing some system dependencies via sudo apt"


if [[ "$CM_TMP_QUIET" != "yes" ]]; then 
 echo "Enter skip to skip this step or press enter to continue:"
 read DUMMY

 if [[ "$DUMMY" == "skip" ]]; then exit 0; fi
fi

CM_APT_TOOL=${CM_APT_TOOL:-apt}

${CM_SUDO} ${CM_APT_TOOL} update && \
    ${CM_SUDO} ${CM_APT_TOOL} install -y --no-install-recommends \
           apt-utils \
           git \
           wget \
           curl \
           zip \
           unzip \
           bzip2 \
           libz-dev \
           libbz2-dev \
           openssh-client \
           libssl-dev \
           vim \
           mc \
           tree \
           gcc \
           g++ \
           autoconf \
           autogen \
           libtool \
           make \
           cmake \
           libc6-dev \
           build-essential \
           libbz2-dev \
           libffi-dev \
           python3 \
           python3-pip \
           python3-dev \
           libtinfo-dev \
           python-is-python3 \
           sudo
