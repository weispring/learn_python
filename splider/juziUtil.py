
import requests
import re

import socket
import time

from bs4 import BeautifulSoup
import pymysql
import mysqlpy.dbutil as mydbutil

def resolveHtml(div):
    sections = div
    dataList = []
    # 打印每部电影的详细信息
    for section in sections:
        data = {}
        div0 = section.find_all('div', attrs={'class': 'content_2hYZM'}, recursive=False)[0]
        div1 = section.find_all("div", recursive=False)[1]
        contenta = div0.find_all("a", recursive=False)[0]

        content = ''
        for sp in contenta.find_all("span", recursive=False):
            #print(sp)
            try:
                content = content + sp.find_all("span", recursive=False)[0].find_all("span", recursive=False)[0].text
            except:
                print(sp)

        try:
            if(len(div0.find_all("div", attrs={'class': 'source_18lGW'})) > 0):
                author = div0.find_all("div", attrs={'class': 'source_18lGW'})[0].find_all("span", recursive=False)[0].find_all("a", recursive=False)[0].find_all("span", recursive=False)[0].find_all("span", recursive=False)[0].text
                bookName = div0.find_all("div", recursive=False)[0].find_all("a", recursive=False)[0].find_all("span", recursive=False)[0].find_all("span", recursive=False)[0].text
            commentNum = ''
            if(len(div0.find_all("a", recursive=False)) > 0):
                commentNum = div1.find_all("a", recursive=False)[0].find_all("span", recursive=False)[0].text
            loveNum = ''
            if(len(div0.find_all("span", recursive=False)) > 0):
                loveNum = div1.find_all("span", recursive=False)[0].find_all("span", recursive=False)[0].text

            data['content'] = content.replace("\t", "").replace("\n", "")
            data['author'] = author.replace("\t", "").replace("\n", "")
            data['bookName'] = bookName.replace("\t", "").replace("\n", "")
            data['commentNum'] = commentNum.replace("\t", "").replace("\n", "")
            data['loveNum'] = loveNum.replace("\t", "").replace("\n", "")
            if(data['commentNum'] == ''):
                data['commentNum'] = 0
            if(data['loveNum'] == ''):
                data['loveNum'] = 0
            dataList.append(data)
            #print(data)
        except Exception as r:
            print('未知错误 %s' %r)
    return dataList



def convert(html):
    soup = BeautifulSoup(html,features='html.parser')
    container = soup.find_all('div', attrs={'id': '__nuxt'})[0].find_all('div', attrs={'id': '__layout'})[0].find_all('div', attrs={'class': 'container'})[0]

    main_3CNyC = container.find_all('div', attrs={'class': 'container_d4i6X'})[0].find_all('div', attrs={'class': 'main_3CNyC'})[0]
    list_1fuFI = main_3CNyC.find_all('div', attrs={'class': 'content_3VON-'})[0].find_all('div', attrs={'class': 'list_1fuFI'})[0]

    dataList = resolveHtml(list_1fuFI.find_all("section"))

    mysqlconnect = pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='learn')
    mydbutil.insert("t_love_articles", dataList, mysqlconnect)

