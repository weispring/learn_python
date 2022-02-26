from urllib.request import urlopen
from urllib.request import quote, unquote, Request
from  urllib.error import HTTPError
import urllib.parse
import requests
try:
    fileName = "3std-bsc.zip"
    url = 'https://feature.kingdee.com:1026/cosmic-cd-fi/devfi/test/prepare/runtime/appstore/biz/3std-bsc.zip'  # 菜鸟教程搜索页面
    header = {
        'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }   #头部信息

    r = requests.get(url) # 发送请求
    # 保存
    with open (fileName, 'wb') as f:
        f.write(r.content)
        f.close
except HTTPError as e:
    print(e)
    if e.code == 404:
        print(404)   # 404


