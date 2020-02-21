from multiprocessing import Process;
from multiprocessing import Pool;

import os, time, random


def long_time_task(name):
    print('run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print ('task %s runs %0.2f sec' % (name, (end - start)))


if __name__ == '__main__':
    print('parent process %s.' % os.getpid())
    p = Pool(5)
    for i in range(4):
        p.apply_async(long_time_task, args=(i,))

    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
