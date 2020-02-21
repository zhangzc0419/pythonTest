import time, threading


def loop():
    print("Thread %sis running ..." % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print("thread %s >>> %s " % (threading.current_thread().name, n))
        time.sleep(1)
    print ("Thread %s is running " % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t  =  threading.Thread(target=loop, name='loop thread')
t.start()
t.join()
print ("Thread %s is running " % threading.current_thread().name)
