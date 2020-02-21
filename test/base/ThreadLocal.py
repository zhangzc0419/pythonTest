import threading

local_school = threading.local()

def process_student():
    std = local_school.student
    print std, threading.current_thread().name

def process_thread(name):
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread, args=('Alice',), name='thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
