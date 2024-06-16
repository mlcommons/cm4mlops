# For more information see: https://help.github.com/actions/language-and-framework-guides/using-python-with-github-actions

name: MLPerf inference ABTF POC Test

on:
  pull_request_target:
    branches: [ "main", "poc" ]
    paths:
      - '.github/workflows/test-mlperf-inference-abtf-poc.yml'
      - '**'
      - '!**.md'

jobs:
  build:
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: false
      matrix:
        os: [ubuntu-latest, ubuntu-20.04, ubuntu-24.04]
        python-version: [ "3.8", "3.12" ]
        backend: [ "pytorch" ]
        implementation: [ "python" ]
        exclude:
        - os: ubuntu-24.04
          python-version: "3.8"

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v3
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        pip install cm4mlops
        cm pull repo --url=${{ github.event.pull_request.head.repo.html_url }} --checkout=${{ github.event.pull_request.head.ref }}
        cm run script --quiet --tags=get,sys-utils-cm
    - name: Test MLPerf Inference ABTF POC using ${{ matrix.backend }} on docker
      run: |
        cm run script --tags=run-abtf,inference,_poc-demo --test_query_count=5 --adr.compiler.tags=gcc --quiet --docker --docker_it=no  -v --gh_token=${{ secrets.ABTF_ACCESS_TOKEN }}

  build2:
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: false
      matrix:
        os: [macos-latest, macos-13]
        python-version: [ "3.8", "3.12" ]
        backend: [ "pytorch" ]
        implementation: [ "python" ]
        exclude:
        - os: ubuntu-24.04
          python-version: "3.8"

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v3
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python3 -m pip install cmind
        cm pull repo --url=${{ github.event.pull_request.head.repo.html_url }} --checkout=${{ github.event.pull_request.head.ref }}
        cm pull repo mlcommons@cm4abtf --branch=poc
        cm run script --quiet --tags=get,sys-utils-cm
    - name: Test MLPerf Inference ABTF POC using ${{ matrix.backend }} natively
      run: |
        cm run script --tags=run-abtf,inference,_poc-demo --adr.compiler.tags=gcc --quiet  -v --gh_token=${{ secrets.ABTF_ACCESS_TOKEN }}
    
