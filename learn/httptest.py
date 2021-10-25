import urllib.request
import urllib.parse
import requests

#pip install requests
resp = urllib.request.urlopen("http://www.baidu.com/")
html = resp.read().decode("utf-8")

url = "https://www.baidu.com/"
resp=requests.get(url)
print(resp.text)

url = "https://www.baidu.com/"
postdatas={"k":"v"}
resp=requests.post(url, postdatas)
print(resp.text)
