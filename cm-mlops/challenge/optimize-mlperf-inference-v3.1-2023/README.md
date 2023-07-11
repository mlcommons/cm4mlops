### Challenge

Prepare, optimize and reproduce MLPerf inference v3.1 benchmarks across diverse implementations, models, software and hardware.

Join this public [Discord server](https://discord.gg/JjWNWXKxwT) to discuss with the community and organizers
how to use and enhance [CM scripts and workflows](https://github.com/mlcommons/ck/blob/master/docs/README.md) 
to run and optimize MLPerf inference benchmarks on your software/hardware stack.

#### Organizers

* [MLCommons taskforce on automation and reproducibility](https://cKnowledge.org/mlcommons-taskforce)
* [cTuning foundation](https://cTuning.org)
* [cKnowledge Ltd](https://cKnowledge.org)

### Status

For MLPerf inference 3.1 we have the following benchmark tasks
1. [Image Classification](https://github.com/mlcommons/ck/blob/master/cm-mlops/challenge/optimize-mlperf-inference-v3.1-2023/docs/generate-resnet50-submission.md) using ResNet50 model and Imagenet-2012 dataset
2. [Object Detection](https://github.com/mlcommons/ck/blob/master/cm-mlops/challenge/optimize-mlperf-inference-v3.1-2023/docs/generate-retinanet-submission.md) using Retinanet model and OpenImages dataset
3. [Language processing](https://github.com/mlcommons/ck/blob/master/cm-mlops/challenge/optimize-mlperf-inference-v3.1-2023/docs/generate-bert-submission.md) using Bert-Large model and Squadv1.1 dataset
4. [Speech Recognition](https://github.com/mlcommons/ck/blob/master/cm-mlops/challenge/optimize-mlperf-inference-v3.1-2023/docs/generate-rnnt-submission.md) using RNNT model and LibriSpeech dataset
5. [Medical Imaging](https://github.com/mlcommons/ck/blob/master/cm-mlops/challenge/optimize-mlperf-inference-v3.1-2023/docs/generate-3d-unet-submission.md)  using 3d-unet model and KiTS19 dataset
6. Recommendation using DLRM model and Criteo dataset
7. [Large Language Model](https://github.com/mlcommons/ck/tree/master/docs/mlperf/inference/gpt-j) using GPT-J model and CNN Daily Mail dataset

All seven tasks are applicable to the datacenter category while all except Recommendation are applicable to the edge category. 
Further, language processing and medical imaging models have a high accuracy variant where the achieved accuracy 
must be within `99.9%` (`99%` is the default accuracy requirement) of the fp32 reference model. 
The recommendation task only has a high-accuracy variant. Currently, we are not supporting the Recommendation task as we are not having a high-end server which is a requirement.

This challenge is integrated with [our platform](https://github.com/ctuning/mlcommons-ck/tree/master/platform)
