import json
import pymysql
import mysqlpy.dbutil as mydbutil

mysqlconnect = pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='learn')

with open('C:\\Users\\kingdee\\Desktop\\78\\xiecheng.json', 'r',encoding="utf-8") as f:
    data = json.load(f)
    mydbutil.insert("t_er_city", data["datas"], mysqlconnect)






