[ [Back to MLPerf inference benchmarks index](../README.md) ]

# MLPerf inference benchmark

## Medical imaging with 3D U-Net

### Notes

3d-unet has two variants - `3d-unet-99` and `3d-unet-99.9` where the `99` and `99.9` specifies the required accuracy constraint 
with respect to the reference floating point model. Both models can be submitter under edge as well as datacenter category.

Please check [MLPerf inference GitHub](https://github.com/mlcommons/inference) for more details.

### Run using the [MLCommons CM framework](https://github.com/mlcommons/ck)

*From Feb 2024, we suggest you to use [this GUI](https://access.cknowledge.org/playground/?action=howtorun&bench_uid=39877bb63fb54725)
 to configure MLPerf inference benchmark, generate CM commands to run it across different implementations, models, data sets, software
 and hardware, and prepare your submissions.*

### A few ready-to-use CM commands

The following guides explain how to run different implementations of this benchmark via CM:

* [MLCommons Reference implementation in Python](README_reference.md)
* [NVIDIA optimized implementation (GPU)](README_nvidia.md)
