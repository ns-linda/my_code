import threading

class myThread(threading.Thread):
    def __init__(self, thread_name):
        threading.Thread.__init__(self)
        self.thread_name = thread_name

    def run(self):
        print("Thread name is :" + self.thread_name)


thread1 = myThread("First Thread")
thread1.start()

t1 = ('a', 'b', 'c', 'd', 'e', 'f')
t2 = (1, 2, 3, 4)
print(dict(zip(t1,t2)))

s = "yogeshyogkumar"
import re
ex= re.split("yog",s)
ex1=re.sub("yog", "lin",s)
# ex1=re.subn("yog", "lin",s)
print(ex)
print(ex1)