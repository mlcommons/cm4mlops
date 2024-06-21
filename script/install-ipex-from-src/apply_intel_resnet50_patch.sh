cd $IPEX_DIR
wget -nc https://github.com/mlcommons/inference_results_v3.1/blob/main/closed/Intel/code/resnet50/pytorch-cpu/input_output_aligned_scales.patch
test $? -eq 0 || exit $?
git apply input_output_aligned_scales.patch
test $? -eq 0 || exit $?
cd -
