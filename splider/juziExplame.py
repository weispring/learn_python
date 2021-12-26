import requests
import re

import socket
import time
import juziUtil

url ='https://www.juzikong.com/tags/%E5%8F%A5%E5%AD%90%E8%BF%B7';

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',

    'if-none-match': '"1ad67-hAJgvpCOAmng05bNSs/HKJlJEo0"',
    'referer': 'https://www.baidu.com/link?url=r1GoMcvN-tKOwvSUbDww_47SkfzIRtm8GO1kUZ9xaFvvuQ_XFCIhMqPduzbm2UWdhYNMf2D8wLSRiuiB91EsDH_DBtvWS-RFNWH889o3zYi&wd=&eqid=bc52287d00029bf30000000661c81f78',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

# 解析html, get 请求header, try, list, dict
# 不允许爬取，改为机器人点击
# for x in range(8):
#     if(x > 0):
#         url = "https://www.juzikong.com/tags/%E5%8F%A5%E5%AD%90%E8%BF%B7?page=1" + str(x+1)
#     r = requests.get(url, headers=headers)
#     html = r.text
#     print("解析结果：\n", juziUtil.convert(html))
f = open(r"C:\Users\lixia\Desktop\jd\1.html", encoding="utf-8")
print("解析结果：\n", juziUtil.convert(f))
f.close()



