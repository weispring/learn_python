#!/usr/bin/env python

# -*- coding: utf-8 -*-

import requests

import re

from bs4 import BeautifulSoup

url ="https://www.csdn.net/?spm=1018.2226.1000.2115"

p =2

# s = input()

s ='python'


kv = {'p':'%d' % p, 'q':'%s' % s}

r = requests.get(url, params=kv)


r.encoding ='utf-8'

so_url = r.request.url

html = r.text

# print(requests.get(so_url).text)

soup = BeautifulSoup(html, "html.parser")

# print(soup.find_all('dl'))
for dl in soup.find_all('dl'):
    text = dl.prettify()

    #print(text)
    for dd in dl.find_all("dd"):
        content = re.findall(r'"dest":"(.*?)"', str(dd))[0]

        # print(content)

        tittle = re.findall(r'target="_blank">(.*?)</a>', str(dd), re.S)[0]

        tittle = tittle.replace('\n', '')

        fb =open('%s.html' % tittle, 'w', encoding='utf-8')

        fb.write(content)
        print(tittle)
        print(tittle, content)

#exit()

# print(search)
