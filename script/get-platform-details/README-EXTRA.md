Please execute the following CM command in order to get the platform details of the SUT. 

```
cm run script --tags=get,platform-details --platform_details_dir=<DIRECTORY_TO_SAVE_THE_TXT_FILE>
```


The generated details are saved as a text file to the specified directory. If nothing is specified, the generated text file will be saved to cm cache.

Generated text file sample could be found [here](https://github.com/GATEOverflow/mlperf_inference_test_submissions_v5.0/blob/main/open/MLCommons/measurements/gh_action-reference-gpu-pytorch_v2.5.0-cu124/system_info.txt)
