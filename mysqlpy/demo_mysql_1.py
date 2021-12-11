import pymysql
import dbutil as mydbutil
mysqlconnect = pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='learn')
print(mysqlconnect)
mycursor = mysqlconnect.cursor()
print(mycursor.execute("SHOW DATABASES"))

for x in mycursor:
    print(x)
mycursor.execute("CREATE DATABASE if not exists demo1")
mycursor.execute("CREATE TABLE if not exists  sites (name VARCHAR(255), url VARCHAR(255), id bigint(20) not null primary key  auto_increment)")

data = [
    {
        "name":"RUNOOB",
        "url":"https://www.runoob.com"
    }
]

mydbutil.insert("sites", data, mysqlconnect)
print(mycursor.rowcount, "记录插入成功。")

sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = [
    ('Google', 'https://www.google.com'),
    ('Github', 'https://www.github.com'),
    ('Taobao', 'https://www.taobao.com'),
    ('stackoverflow', 'https://www.stackoverflow.com/')
]

# 批量插入
# mycursor.executemany(sql, val)
mysqlconnect.commit()


mycursor.execute("SELECT * FROM sites")

myresult = mycursor.fetchall()     # fetchall() 获取所有记录

for x in myresult:
    print(x)

mycursor.execute("SELECT * FROM sites")

myresult = mycursor.fetchone()     # 只想读取一条数据，可以使用 fetchone() 方法：

for x in myresult:
    print(x)


print("我是%s" % "中国人")

mycursor.close()