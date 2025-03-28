# This test covers version, variation, compilation from src, add_deps,
# add_deps_recursive, deps, post_deps

import check as checks
import cmind as cm

from pathlib import Path
import sys
import os

sys.path.insert(
    1,
    os.path.join(
        Path(__file__).parent.parent.resolve(),
        "script"))

r = cm.access({'action': 'run', 'automation': 'script', 'tags': 'run,mlperf,inference,generate-run-cmds', 'adr':
               {'python': {'name': 'mlperf', 'version_min': '3.8'}}, 'submitter': 'Community',
               'implementation': 'python', 'hw_name': 'default', 'model': 'resnet50', 'backend': 'tvm-onnx', 'device': 'cpu', 'scenario': 'Offline',
               'mode': 'accuracy', 'test_query_count': '5', 'clean': 'true', 'quiet': 'yes'})
checks.check_return(r)


r = cm.access({'action': 'run', 'automation': 'script', 'tags': 'run,mlperf,inference,generate-run-cmds,_submission', 'adr':
               {'python': {'name': 'mlperf', 'version_min': '3.8'}}, 'submitter': 'Community',
               'implementation': 'python', 'hw_name': 'default', 'model': 'resnet50', 'backend': 'tvm-onnx', 'device': 'cpu', 'scenario': 'Offline',
               'test_query_count': '500', 'clean': 'true', 'quiet': 'yes'})
checks.check_return(r)
