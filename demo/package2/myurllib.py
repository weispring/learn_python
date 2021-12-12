from urllib.request import urlopen
from urllib.request import quote, unquote, Request
from  urllib.error import HTTPError
myUrl = urlopen("https://www.runoob.com/")
print(myUrl.getcode())
print(myUrl.read(1))

try:
    myURL2 = urlopen("https://www.runoob.com/no.html")
except HTTPError as e:
    if e.code == 404:
        print(404)   # 404

encode_url = quote("https://www.runoob.com/")
print(encode_url)

unencode_url = unquote(encode_url)    # 解码
print(unencode_url)


import urllib.parse

url = 'https://www.runoob.com/?s='  # 菜鸟教程搜索页面
keyword = 'Python 教程'
key_code = urllib.request.quote(keyword)  # 对请求进行编码
url_all = url+key_code
header = {
    'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}   #头部信息
request = Request(url_all,headers=header)
reponse = urlopen(request).read()
print(reponse)


import urllib.robotparser
rp = urllib.robotparser.RobotFileParser()
rp.set_url("http://www.musi-cal.com/robots.txt")
print("读取：", rp.read())
rrate = rp.request_rate("*")


rp.crawl_delay("*")
rp.can_fetch("*", "http://www.musi-cal.com/cgi-bin/search?city=San+Francisco")
rp.can_fetch("*", "http://www.musi-cal.com/")