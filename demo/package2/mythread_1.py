
# 多线程
import _thread
import time
# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print ("%s: %s" % (threadName, time.ctime(time.time())))
# 创建两个线程
try:
    #_thread.start_new_thread(print_time, ("Thread-1", 2, ))
    # _thread.start_new_thread(print_time, ("Thread-2", 4, ))
    pass
except:
    print("Error: 无法启动线程")

import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开始线程：" + self.name)
        print_time(self.name, self.counter, 5)
        print ("退出线程：" + self.name)

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# 创建新线程
thread1 = myThread(3, "Thread-3", 1)
thread2 = myThread(4, "Thread-4", 2)

# 开启新线程
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print ("退出主线程")



