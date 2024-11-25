# Developer: Grigori Fursin

import cmind
import sys

print(sys.executable)

r = cmind.access(
    'run script "print hello-world python" --debug_uid=f52670e5f3f345a2')
print(r)
