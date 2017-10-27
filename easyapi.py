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
import random
import string, urllib2
import re
import random
import os
import urllib

import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class copyPic:
    def __init__(self):
        self.flag = 0
        self.dirName = ''
        self.ranNum = 1000
        self.path ='/home/chen/easyapi/'
        # db = connDB.getDbConn();
        # self.path = str(db.doSelect("select config_value from t_system_config where config_key = 'localhost2'")[0]);
        print self.path;
        self.i = 0

    def randomNum (self):
        ranNum = random.randint(1, 200000)
        return ranNum


    def start(self):
        y=235;
        while ( y>0):
            print y
            url = "https://www.easyapi.com/s";
            newUrl = self.saveFile(url,  self.i);
            if(newUrl ==""):
                return
            self.i = self.i+1;


    def saveFile(self,url, num):
        try:
            headers = {
                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-CN,zh;q=0.9',
                       'Connection': 'keep-alive',
                       'Host': 'jandan.net',
                       'Cache-Control': 'max-age=0',
                       'Cookie':'__cfduid=d11fe2c058f1d3df38b665933cab4d3f31509087660; _ga=GA1.2.1250263778.1509087661; _gid=GA1.2.214701713.1509087662',
                       'Upgrade-Insecure-Requests': '1',
                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
                       "Referer":"http://jandan.net/ooxx/",
                       "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36"
            }
            html = requests.get(url, headers=headers, allow_redirects=False)
            m = html.text;
        except urllib2.URLError, e:
            print e.reason
        myItems = re.findall('<div class="con_nofound">(.*)</div>', m,re.S)  # <a href="(.*)">(.*)</a>
        img = re.findall('<img src="(.*)" title="欣赏美女" width="600">',myItems[0])
        self.ranNum = self.randomNum()
        for y in range(len(img)):
            picUrls = "http:"+img[y]
            print picUrls
            localPath = self.path + str(self.ranNum) + "_" + str(y) + '.jpg';
            print localPath
            urllib.urlretrieve(picUrls, localPath)
            # headers = {
            #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            #     'Accept-Encoding': 'gzip, deflate',
            #     'Accept-Language': 'zh-CN,zh;q=0.9',
            #     'Connection': 'keep-alive',
            #     'Host': 'ws1.sinaimg.cn',
            #     'Cache-Control': 'max-age=0',
            #     'Upgrade-Insecure-Requests': '1',
            #     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
            # }
            #
            # img = requests.get(picUrls, headers=headers, allow_redirects=False).text
            # print img
            # print self.path + str(self.ranNum) + "_" + str(num) + '.jpg'
            # sName = self.path + str(self.ranNum) + "_" + str(num) + '.jpg'  # 自动填充成六位的文件名
            # f = open(sName, 'w+')
            # f.write(img)
            # f.close()

        # db = connDB.getDbConn();
        # result = db.doSql("insert into douyin (douyin_id) VALUES ("+str(i)+")");


# 调用
co = copyPic();
co.start();
