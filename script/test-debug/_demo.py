# Developer: Grigori Fursin

import cmind
import sys
import logging
logging.info(sys.executable)

r = cmind.access('run "cm-debug"')
logging.info(r)
