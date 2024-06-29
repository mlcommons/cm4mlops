"""
Testing CM debugging

# Developer(s): Grigori Fursin
"""
import logging
import os
import json

logging.info ("Hello World 1")

env = os.environ

import json
logging.info ('')
logging.info (json.dumps(dict(env), indent=2))

# Import cmind to test break points
import cmind.utils
if os.environ.get('CM_TMP_DEBUG_UID', '') == '45a7c3a500d24a63':
    cmind.utils.debug_here(__file__, port=5678, text='Debugging main.py!').breakpoint()

logging.info ('')
logging.info ("Hello World 2")

