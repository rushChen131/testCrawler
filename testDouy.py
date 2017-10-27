# -*- coding: utf-8 -*-
# ---------------------------------------
#   程序：百度贴吧爬虫
#   版本：0.1
#   作者：why
#   日期：2013-05-14
#   语言：Python 2.7
#   操作：输入带分页的地址，去掉最后面的数字，设置一下起始页数和终点页数。
#   功能：下载对应页码内的所有页面并存储为html文件。
# ---------------------------------------

import string, urllib2,connDB
import re

import requests


def start():
    url = "http://www.mm131.com/qingchun/3118.html";
    i = 0 ;
    while( url !='') :
        i = i + 1;
        newUrl = saveFile(url,i);
        url = newUrl;


def saveFile(url,num):
    # try:
        # m = urllib2.urlopen(url).read().decode("gbk").encode("utf-8");
    m = yunsite(url);
    # except(BaseException):
        # return ''
    print url
    return ""+readHtml(m,num)
    # db = connDB.getDbConn();
    # result = db.doSql("insert into douyin (douyin_id) VALUES ("+str(i)+")");
def readHtml(m,num):

    myItems = re.findall('<div class="content-pic">(.*)</div>', m)  # <a href="(.*)">(.*)</a>
    print myItems
    y=0
    hrefList=re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')" ,myItems[y])
    print hrefList[0]
    picStr = re.findall(r"(?<=src=\").+?(?=\")|(?<=src=\').+?(?=\')" ,myItems[y])
    print picStr
    headers = {
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',

               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Connection': 'keep-alive',
               'Host': 'www.mm131.com',
               'Cookie':'UM_distinctid=15f573a4018138e-0919bc4fdc617f-102c1709-1fa400-15f573a401a845; bdshare_firstime=1508996956409; CNZZDATA3866066=cnzz_eid%3D1127825081-1494676185-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1494676185; Hm_lvt_9a737a8572f89206db6e9c301695b55a=1508996956,1509005425; Hm_lpvt_9a737a8572f89206db6e9c301695b55a=1509008609',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
               "If-None -Match": "59aa1d87-1d9a",
               "Referer":picStr[0],
               "User-Agent":"Mozilla/5.0(X11;Linuxx86_64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 62.0.3202.62  Safari / 537.36"
    }
    img = requests.get(picStr[0], headers=headers, allow_redirects=False,timeout=10).text
    print img
    sName = "./pic/"+str(num) + "xxxx" + str(0) + '.jpg'  # 自动填充成六位的文件名
    print '正在下载第' + str(num) + '个网页，并将其存储为' + sName + '......'
    f = open(sName, 'w+')
    f.write(img)
    f.close()
    return "http://www.mm131.com/qingchun/" + hrefList[0];
def yunsite(url):
    'url'
    headers = {
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',

               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Connection': 'keep-alive',
               'Host': 'pwww.mm131.com',
               'Cookie':'UM_distinctid=15f573a4018138e-0919bc4fdc617f-102c1709-1fa400-15f573a401a845; bdshare_firstime=1508996956409; CNZZDATA3866066=cnzz_eid%3D1127825081-1494676185-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1494676185; Hm_lvt_9a737a8572f89206db6e9c301695b55a=1508996956,1509005425; Hm_lpvt_9a737a8572f89206db6e9c301695b55a=1509008609',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
               "If-None -Match": "59aa1d87-1d9a",
               "Referer":url,
               "User-Agent":"Mozilla/5.0(X11;Linuxx86_64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 62.0.3202.62  Safari / 537.36"
    }

    html = requests.get(url, headers=None, allow_redirects=False)
    # text = html.text
    # text1 = html.content
    # print text
    # print text1
    return html.text
# 调用
start();
