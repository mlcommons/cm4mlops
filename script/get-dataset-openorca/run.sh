cmd=${CM_RUN_CMD}
echo "${cmd}"
eval "${cmd}"
test $? -eq 0 || exit $?

echo "CM_DATASET_OPENORCA_PATH=${PWD}/open_orca/open_orca_gpt4_tokenized_llama.sampled_24576.pkl.gz" > temp_ver.out
test $? -eq 0 || exit $?