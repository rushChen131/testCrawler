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
import re
import urllib2

from com.chen import connDB


class copyPic:
    def __init__(self):
        self.flag = 0
        self.dirName = ''
        self.ranNum = 1000
        # self.path ='/home/chen/pic/'
        db = connDB.getDbConn();
        self.path = str(db.doSelect("select config_value from t_system_config where config_key = 'localhost1'")[0]);
        print self.path;
        self.i = 0

    def randomNum (self):
        ranNum = random.randint(1, 200000)
        return ranNum


    def start(self):
        url = "http://desk.zol.com.cn/bizhi/2879_36872_2.html";
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
        if (self.flag == 0):
            self.flag = 1
            self.ranNum = self.randomNum()
            dirNames = re.findall('<a id="titleName" href="(.*)">(.*)</a>', m)[0]
            self.dirName = dirNames[1]
            # hasDir = os.path.exists(self.path+self.dirName);
            # if(not hasDir):
            #     os.mkdir(  self.path+self.dirName)
        for y in range(len(myItems)):
            img = urllib2.urlopen(myItems[y]).read();
            sName =   self.path + str(self.ranNum) + "_" + str(num) + '.jpg'  # 自动填充成六位的文件名
            f = open(sName, 'w+')
            f.write(img)
            f.close()
            connDB.getDbConn().doSql("insert into t_bizhi (user_name,path,html_url,pic_url) "
                                     + "VALUES ('""" + str(self.dirName) +
                                     """','""" + str(self.ranNum) + "_" + str(num) + '.jpg' + """','""" + url + """','""" + myItems[y] + """')""")
        match = '<a id="pageNext" class="next" href="(.*)" title="(.*)">';
        next = re.findall(match, m)
        nextUrls = next[0]
        nextUrl = nextUrls[0]
        hasNext = cmp(nextUrl,"javascript:;")
        if (hasNext != -1):
            div = re.findall('<a href="(.*)" class="txt">',m)
            nextUrl = div[1]
            self.flag = 0
            self.i = 0
        return 'http://desk.zol.com.cn' + nextUrl;
        # db = connDB.getDbConn();
        # result = db.doSql("insert into douyin (douyin_id) VALUES ("+str(i)+")");


# 调用
co = copyPic();
co.start();
