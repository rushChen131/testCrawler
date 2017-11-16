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
        self.page = 1;

    def randomNum (self):
        ranNum = random.randint(1, 200000)
        return ranNum


    def start(self):
        y=189;
        while ( y>0):
            print y
            url = "https://s.taobao.com/search?q=%E6%AF%9B%E8%A1%A3&sort=sale-desc";
            newUrl = self.saveFile(url,  self.i);
            if(newUrl ==""):
                return
            self.i = self.i+1;


    def saveFile(self,url, num):
        try:
            headers = {
                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                       'Accept-Encoding': 'gzip, deflate, br',
                       'Accept-Language': 'zh-CN,zh;q=0.9',
                       'Connection': 'keep-alive',
                       'Host': 'www.easyapi.com',
                       'Cache-Control': 'max-age=0',
                       'Cookie':'Hm_lvt_07b306be81dcbc23fd29affebc7b173e=1509096673; Hm_lpvt_07b306be81dcbc23fd29affebc7b173e=1509096673; JSESSIONID=F3ADED175D57D14EBCD443F2A6866BDC',
                       'Upgrade-Insecure-Requests': '1',
                       "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36"
            }
            html = requests.get(url, headers=headers, allow_redirects=False)
            m = html.text;
        except urllib2.URLError, e:
            print e.reason
        # myItems = re.findall('<div class="con_nofound">(.*)</div>', m,re.S)  # <a href="(.*)">(.*)</a>
        img = re.findall('<p><img src="(.*)" title="(.*)" width="600"></p>',m)
        self.ranNum = self.randomNum()
        print img[0][0]
        localPath = self.path + str(self.ranNum) + "_" + str(num) + '.jpg';
        print localPath
        urllib.urlretrieve(img[0][0], localPath)

# 调用
co = copyPic();
co.start();
