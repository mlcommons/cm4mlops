﻿"""
Testing CM debugging

# Developer(s): Grigori Fursin
"""

import os
import json

print ("Hello World 1")

env = os.environ

import json
print ('')
print (json.dumps(dict(env), indent=2))

# Import cmind to test break points
import cmind.utils
if os.environ.get('CM_TMP_DEBUG_UID', '') == '45a7c3a500d24a63':
    cmind.utils.debug_here(__file__, port=5678, text='Debugging main.py!').breakpoint()

print ('')
print ("Hello World 2")

