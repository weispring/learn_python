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


for line in urlopen('https://blog.csdn.net/weixin_39584549/article/details/110544661'):
    line = line.decode('utf-8')  # Decoding the binary data to text
    if 'EST' in line or 'EDT' in line:
        # look for Eastern Time
        print(line)


