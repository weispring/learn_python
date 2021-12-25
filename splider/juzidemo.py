
import requests
import re

import socket
import time

true_socket = socket.socket

ipbind='219.133.170.'

def bound_socket(i, *a, **k):
    sock = true_socket(*a, **k)
    sock.bind((ipbind + str(78 + i), 0))
    return sock



url ='https://www.juzine.com/juzi/aiqing/'

headers = {':authority': 'www.juzikong.com',
           ':method': 'GET', 
           ':path': '/tags/%E5%8F%A5%E5%AD%90%E8%BF%B7', 
           ':scheme': 'https', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
           'accept-encoding': 'gzip, deflate, br', 
           'accept-language': 'zh-CN,zh;q=0.9', 
           'cache-control': 'no-cache', 
           'cookie': 'UM_distinctid=17df0254c7a617-01e436bfd7f962-4303066-1fa400-17df0254c7bbbc; CNZZDATA1279835904=615083684-1640404286-https%253A%252F%252Fwww.baidu.com%252F%7C1640415147; __gads=ID=254b760e4e148f8d-227dc9d886cf00df:T=1640417879:RT=1640417879:S=ALNI_MbnB0zbWDgpmHxPzcoCD2TxJezTQw; refer=https://www.juzikong.com/tags/%25E5%258F%25A5%25E5%25AD%2590%25E8%25BF%25B7; token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLmp1emlrb25nLmNvbVwvYXBpXC9xcVwvbG9naW4iLCJpYXQiOjE2NDA0MjE5MDksImV4cCI6MTY3MTk1NzkwOSwibmJmIjoxNjQwNDIxOTA5LCJqdGkiOiJTTE9XZkg1Z0ZCUFlMeVlrIiwic3ViIjozNzA1Njg0LCJwcnYiOiIyYmM1YTVlNzJjNWI0ZjQ5MTY3YTMzMmJhNWJmMzU4NzE4YjM2ZTk3IiwidXVpZCI6ImIwZDJlYzc0LTU2MjYtNDlkNy05OGI1LTM4ZDk3MDQ3ZTA5MCIsInVzZXJuYW1lIjoiOTBXVHpRWGsifQ.GEGnEaEJlx4ZMCfgCpr_jP-HRptgeTfSNqYNiic0kMA; Hm_lvt_bdf284068ceac91d2241963e43550528=1640418271,1640419125,1640421912,1640421922; Hm_lpvt_bdf284068ceac91d2241963e43550528=1640421922',
           'pragma': 'no-cache', 
           'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"', 
           'sec-ch-ua-mobile': '?0', 
           'sec-ch-ua-platform': '"Windows"', 
           'sec-fetch-dest': 'document', 
           'sec-fetch-mode': 'navigate', 
           'sec-fetch-site': 'same-origin', 
           'sec-fetch-user': '?1', 
           'upgrade-insecure-requests': '1', 
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

for x in range(10):
    #socket.socket = bound_socket(x+1)
    r = requests.get(url, verify=False)
    so_url = r.request.url
    html = r.text
    print(html)
    time.sleep(3)