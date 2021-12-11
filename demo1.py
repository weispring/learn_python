print ("Python!")

# 判断一个数是否是正整数
a=11
if a>=0:
    print("yes")
    print("=")
else:
    print("NO")
    print("haha")

import time  # 引入time模块
ticks = time.time()
print("当前时间戳为:", ticks)
print("当前时间戳：", int(time.time()))
localtime = time.localtime(time.time())
print("本地时间为 :", localtime)
ocaltime = time.asctime(time.localtime(time.time()))
print("本地时间为 :", localtime)
# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "2021-11-20 16:33:09"
print(time.strptime(a,"%Y-%m-%d %H:%M:%S"))
