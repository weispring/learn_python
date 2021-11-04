#!/usr/bin/python
# -*- coding: UTF-8 -*-

#问题原因：
# python2和python3在数据库模块支持这里存在区别，python2是mysqldb，而到了python3就变成mysqlclient，pip install mysqlclient即可。

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "123456", "learn", charset='utf8' )
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()
print ("Database version : %s " % data)
# 关闭数据库连接



db.close()