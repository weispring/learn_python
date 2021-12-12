import time
ticks = time.time()
print("当前时间戳：{}".format(int(ticks)))

localtime = time.localtime(time.time())
print("本地时间为：{}".format(localtime))

localtime = time.asctime(time.localtime(time.time()))
print("本地时间为 {}".format(localtime))

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

print(time.strptime("2021-12-12 16:10:41", "%Y-%m-%d %H:%M:%S"))

import calendar

cal = calendar.month(2021, 12)
print ("以下输出2016年1月份的日历:")
print (cal)
print(time.timezone, time.tzname)

print(calendar.calendar(theyear=2021, w=2, l=1, c=6))

print(time.ctime(time.time()))