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
import json
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
        self.path ='/home/chen/pic/'
        # db = connDB.getDbConn();
        # self.path = str(db.doSelect("select config_value from t_system_config where config_key = 'localhost2'")[0]);
        print self.path;
        self.i = 1
        self.page = 261

    def randomNum (self):
        ranNum = random.randint(1, 200000)
        return ranNum


    def start(self):
        # url = "http://api.9wuli.com/sdk/meitu/app/share/detail.html?nid=c7fb339f0b4fefc7";

        while ( 1 >0):
            url = "http://api.9wuli.com/v3/message/list/client?pageSize=1&recommend="+str(self.page)+"&channelId=0aa9a4ddd587259196d6c154b4dc0da8&appId=2cd2626cd63b148f13fa2e019820e971&appSecret=8c4c4358b39153e936f4a1919a5853fd&since=0";
            self.saveFile(url);



    def saveFile(self,url):
        print url
        try:
            headers = {
                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                       'Accept-Encoding': 'gzip, deflate, br',
                       'Accept-Language': 'zh-CN,zh;q=0.9',
                       'Connection': 'keep-alive',
                       'Host': 'api.9wuli.com',
                       'Cache-Control': 'max-age=0',
                       'Cookie':'USER_COOKIE_INFO=54358666201746667083; USER_COOKIE_INFO=25407159695061617683; fingerprint=l4nkpVSoMsZuIISMZVLQ1510805880024; Hm_lvt_5f77e51d151580510747b16c02209f2c=1510805880,1510805909,1510805931; Hm_lpvt_5f77e51d151580510747b16c02209f2c=1510805931; Hm_lvt_96f0086d3b483352cb3b96d36de576ae=1510805880,1510805909,1510805931; Hm_lpvt_96f0086d3b483352cb3b96d36de576ae=1510805931; Hm_lvt_4ac2d807f0e84509890c29b24dfe3255=1510803625,1510805880,1510805909,1510805931; Hm_lpvt_4ac2d807f0e84509890c29b24dfe3255=1510805931',
                       'Upgrade-Insecure-Requests': '1',
                       "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36"
            }
            html = requests.get(url, headers=headers, allow_redirects=False)
            m = html.text;
            data = json.loads(m)['data'][0];
            print data['title']
            list = data['imageDTOList']
            for s in range(len(list)):
                nexsUrl = list[s]
                print "picUrl:====="+nexsUrl['src']
                localPath = self.path + str(self.ranNum) + "_" + str(nexsUrl['key']) + '.jpg'
                print localPath
                urllib.urlretrieve(nexsUrl['src'], localPath)
            self.i = 1
            self.page = self.page+1
            self.ranNum = self.randomNum()
        except BaseException, e:
            self.ranNum = self.randomNum()
            self.i = 1
            self.page = self.page + 1
            return
# 调用
co = copyPic();
co.start();
