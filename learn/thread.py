# 线程创建
# 如果希望主线程退出后，其子线程也退出而不再执行，则需要设置子线程为后台线程。Python 提供了 setDeamon 方法。


import time
import threading

class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print("thread {}, @number: {}".format(self.name, i))

def main():
    print("start main thread")
    threads = [MyThread() for i in range(3)]
    for t in threads:
        t.start()
        t.join()
    print("end main thread")

main()

import multiprocessing
# 创建进程的类：Process([group [, target [, name [, args [, kwargs]]]]])
  #target 表示调用对象
  #args 表示调用对象的位置参数元组
  #kwargs表示调用对象的字典
  #name为别名
  #group实质上不使用

def worker(interval, name):
    print(name + "start")
    time.sleep(interval)
    print(name + "end")

p1=multiprocessing.Process(target=worker, args=(2, "两点水1"))
p2=multiprocessing.Process(target=worker, args=(3, "两点水2"))
p3=multiprocessing.Process(target=worker, args=(4, "两点水3"))
# p3.start() # 无法运行报错

print("the number of CPU is:" + str(multiprocessing.cpu_count()))
for p in multiprocessing.active_children():
    print("child   p.name:" + p.name + "\tp.id" + str(p.pid))
print("END!!!!!!!!!!!!!!!!!")

class ClockProcess(multiprocessing.Process):
    def __init__(self, interval):
        multiprocessing.Process.__init__(self)
        self.interval = interval

    def run(self):
        n = 5
        while n > 0:
            print("当前时间: {0}".format(time.ctime()))
            time.sleep(self.interval)
            n -= 1


if __name__ == '__main__':
    p = ClockProcess(3)
    p.start()