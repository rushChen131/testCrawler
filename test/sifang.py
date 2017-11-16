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
import string
import urllib2
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
        self.ranNum = self.randomNum()
        self.path ='/home/chen/sifang/'
        # db = connDB.getDbConn();
        # self.path = str(db.doSelect("select config_value from t_system_config where config_key = 'localhost2'")[0]);
        print self.path;
        self.i = 1
        self.page = 9387

    def randomNum (self):
        ranNum = random.randint(1, 200000)
        return ranNum


    def start(self):
        while ( 1 >0):
            url = "https://www.4493.com/xingganmote/" + str(self.page) + "/" + str(self.i) + ".htm";
            print str(self.page)+".htm/"+str(self.i)
            self.saveFile(url,  self.i);



    def saveFile(self,url, num):
        print url
        try:
            headers = {
                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                       'Accept-Encoding': 'gzip, deflate, br',
                       'Accept-Language': 'zh-CN,zh;q=0.9',
                       'Connection': 'keep-alive',
                       'Host': 'www.4493.com',
                       'Cache-Control': 'max-age=0',
                       'Cookie':'UM_distinctid=15f5c8467b56d2-0e8e72f4466875-102c1709-1fa400-15f5c8467b673b; CNZZDATA30040472=cnzz_eid%3D1679380792-1509084018-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1509084018; CNZZDATA1257119591=1976078557-1509085055-https%253A%252F%252Fwww.baidu.com%252F%7C1509085055; Hm_lvt_65d17d8c0da1175e9c1d1e00ed413540=1509085703,1509091442; Hm_lpvt_65d17d8c0da1175e9c1d1e00ed413540=1509091444; CNZZDATA1257134914=2035089887-1509084345-https%253A%252F%252Fwww.4493.com%252F%7C1509084345',
                       'Upgrade-Insecure-Requests': '1',
                       "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36"
            }
            html = requests.get(url, headers=headers, allow_redirects=False)
            m = html.text;
            headTitle = re.findall('<div class="breadnav">(.*)<\/div>',m);
            htmlTitle = re.findall('<a href="(.*)">(.*)<\/a>',headTitle[0])
            print htmlTitle
            if (htmlTitle[0][1].find("性感美女") == -1 and  htmlTitle[0][1].find("唯美写真") == -1 and htmlTitle[0][1].find("丝袜美腿") == -1):
                self.ranNum = self.randomNum()
                self.i = 1
                self.page = self.page + 1
                return
            print htmlTitle[0][1]
            if (htmlTitle[0][1].find("性感美女") != -1):
                self.path = "/home/chen/sifang/xinggan/"
            else:
                if(htmlTitle[0][1].find("唯美写真") != -1):
                    self.path = "/home/chen/sifang/weimei/";
                else:
                    self.path= "/home/chen/sifang/siwa/"
            myItems = re.findall('<div class="picsbox picsboxcenter">(.*)</div>', m,re.S)  # <a href="(.*)">(.*)</a>
            img = re.findall('<img(.*?) src=\"(.*)\" onload=(.*)>',m)
            localPath = self.path + str(self.ranNum) + "_" + str(num) + '.jpg';
            print localPath
            urllib.urlretrieve(img[0][1], localPath)
            nextUrls = re.findall('<div class="page">(.*)</div>',m,re.S);
            aUrls = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", nextUrls[0], re.I|re.S|re.M);#u'javascript:gotourl(\\'12.htm\\');'
            nexUrl = ''
            for s in range(len(aUrls)):
                if (aUrls[s].find("javascript:gotourl") !=-1):
                    nexsUrl = aUrls[s]
                    print nexsUrl
                    prefix = nexsUrl.find("'");#u'javascript:gotourl(\\'12.htm\\');'
                    fix = nexsUrl.rfind("'");
                    nexUrl = nexsUrl[prefix+1:fix];
            nexUrl = nexUrl[0:nexUrl.find(".")]
            self.i = self.i + 1;
            if(int(nexUrl) == num):
                self.ranNum = self.randomNum()
                self.i =1
                self.page = self.page+1
        except BaseException, e:
            self.ranNum = self.randomNum()
            self.i = 1
            self.page = self.page + 1
            return
# 调用
co = copyPic();
co.start();
