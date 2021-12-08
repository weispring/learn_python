# os模块提供了不少与操作系统相关联的函数。

import os
print("当前目录", os.getcwd())

#print("功能集合", dir(os))
#print("帮助文档", help(os))

# 针对日常的文件和目录管理任务，:mod:shutil 模块提供了一个易于使用的高级接口
import shutil
shutil.copyfile("demo01.py", "2.txt")

import glob
print(glob.glob("*.py"))

import sys
sys.stderr.write('Warning, log file not found starting a new one\n')

import re
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))
print(re.sub(r'(\b[a-z]+) ', r'\1', 'cat in the the hat'))

# 互联
from urllib.request import urlopen


#for line in urlopen('https://blog.csdn.net/weixin_39584549/article/details/110544661'):
#    line = line.decode('utf-8')  # Decoding the binary data to text


import datetime
now = datetime.date.today()
print(now)
print(datetime.date(2003, 12, 2))
print(now.strftime("%Y-%m-%d %H:%M:%S"))


import zlib
s = b'witch which has which witches wrist watch' # b' ' 表示这是一个 bytes 对象
print(len(s))
t = zlib.compress(s)
print(len(t))
print(zlib.decompress(t))

import time
# 当前时间戳 t
time_stamp = time.time()
print("当前时间戳", time_stamp)
# 时间戳转datetime
print("时间戳转datetime", datetime.datetime.fromtimestamp(time_stamp))
# datetime转时间戳
today = datetime.date.today()
print(int(time.mktime(today.timetuple())))
# datetime转字符串
today_str = today.strftime("%Y-%m-%d")
print(today_str)
# 字符串转datetime
today = datetime.datetime.strptime(today_str, "%Y-%m-%d")
print(today)

import itertools
a = [1,2]
b = [3,4,100]
c = [a, b]

print(c)
for item in itertools.product(*c):
    print(item)

def hh():
    pass

a = [1,2,3,None,(),[],]

for a in a:
    print(a)
print(type(hh()))

# re.match与re.search的区别
# re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回 None，而 re.search 匹配整个字符串，直到找到一个匹配。
import re

line = "Cats are smarter than dogs"

matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
    print ("match --> matchObj.group() : ", matchObj.group())
else:
    print ("No match!!")

matchObj = re.search(r'dogs', line, re.M|re.I)
if matchObj:
    print ("search --> matchObj.group() : ", matchObj.group())
else:
    print ("No match!!")


import re

'''
Python 的re模块提供了re.sub用于替换字符串中的匹配项。
语法：
re.sub(pattern, repl, string, count=0, flags=0)
参数：
pattern : 正则中的模式字符串。
repl : 替换的字符串，也可为一个函数。
string : 要被查找替换的原始字符串。
count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
flags : 编译时用的匹配模式，数字形式。


'''
phone = "2004-959-559 # 这是一个电话号码"

# 删除注释
num = re.sub(r'#.*$', "", phone) #	$匹配输入字符串的结尾位置
print ("电话号码 : ", num)

# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print ("电话号码 : ", num)
print("")
# ddd
#
