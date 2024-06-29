import cmind as cm
import time
import logging
times = []

steps = 10

logging.info ('Running search with tags {} times ...'.format(steps))

for step in range(steps):

    start = time.time()
    r = cm.access({'action':'search',
                   'automation':'script',
                   'tags':'detect,os'})
    timer = time.time() - start

    if r['return']>0: cm.error(r)

    times.append(timer)

step = 0
for t in times:
    step += 1
    logging.info ("{}) {:0.3f} sec.".format(step, t))
