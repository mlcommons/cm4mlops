[ [Back to MLPerf inference benchmarks index](../README.md) ]

# MLPerf inference benchmark

## Speech recognition with RNNT

### Notes

In the edge category, ResNet50 has Offline, SingleStream and MultiStream scenarios and in the datacenter category, it has Offline and Server scenarios.

Please check [MLPerf inference GitHub](https://github.com/mlcommons/inference) for more details.

### Run using the [MLCommons CM framework](https://github.com/mlcommons/ck)

*From Feb 2024, we suggest you to use [this GUI](https://access.cknowledge.org/playground/?action=howtorun&bench_uid=39877bb63fb54725)
 to configure MLPerf inference benchmark, generate CM commands to run it across different implementations, models, data sets, software
 and hardware, and prepare your submissions.*

### A few ready-to-use CM commands

The following guides explain how to run different implementations of this benchmark via CM:

* [MLCommons Reference implementation in Python](README_reference.md)
* [NVIDIA optimized implementation (GPU)](README_nvidia.md)
