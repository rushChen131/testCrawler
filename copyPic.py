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
class copyPic:
    def __init__(self):
        self.flag = 0
        self.dirName = ''
        self.ranNum = 1000
        self.path ='/opt/pic/'
        self.i = 0

    def randomNum (self):
        ranNum = random.randint(1, 200000)
        return ranNum


    def start(self):
        url = "http://desk.zol.com.cn/bizhi/7132_88317_2.html";
        while (url != ''):
            newUrl = self.saveFile(url,  self.i);
            self.i = self.i+1;
            url = newUrl;

    def saveFile(self,url, num):
        try:
            m = urllib2.urlopen(url).read().decode("gbk").encode("utf-8");
        except(BaseException):
            return ''
        print '图片url:'+url
        myItems = re.findall('<img id="bigImg" src="(.*)" width="960" height="600">', m)  # <a href="(.*)">(.*)</a>
        print myItems
        if (self.flag == 0):
            self.flag = 1
            self.ranNum = self.randomNum()
            dirNames = re.findall('<a id="titleName" href="(.*)">(.*)</a>', m)[0]
            print '文件名：'+dirNames[1]
            self.dirName = dirNames[1]
            hasDir = os.path.exists(self.path+self.dirName);
            if(not hasDir):
                os.mkdir(  self.path+self.dirName)
        for y in range(len(myItems)):
            img = urllib2.urlopen(myItems[y]).read();
            sName =   self.path+self.dirName+"/" + str(self.ranNum) + "_" + str(num) + '.jpg'  # 自动填充成六位的文件名
            print '正在下载第' + str(num) + '个网页，并将其存储为' + sName + '......'
            f = open(sName, 'w+')
            f.write(img)
            f.close()
        match = '<a id="pageNext" class="next" href="(.*)" title="(.*)">';
        print match
        next = re.findall(match, m)
        print next
        nextUrls = next[0]
        print "nextUrls[0]"+nextUrls[0]
        nextUrl = nextUrls[0]
        hasNext = cmp(nextUrl,"javascript:;")
        if (hasNext != -1):
            div = re.findall('<a href="(.*)" class="txt">',m)
            print div
            nextUrl = div[1]
            self.flag = 0
            self.i = 0
        return 'http://desk.zol.com.cn' + nextUrl;
        # db = connDB.getDbConn();
        # result = db.doSql("insert into douyin (douyin_id) VALUES ("+str(i)+")");


# 调用
co = copyPic();
co.start();
