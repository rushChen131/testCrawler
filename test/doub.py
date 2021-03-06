# coding=utf-8
import json
import urllib2
import re
import random
import urllib

import requests

from getDbConn import getDbConn
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)


####### tag : ['热门','最新','经典','可播放','豆瓣高分','冷门佳片','华语','欧美','韩国','日本','动作','喜剧','爱情','科幻','悬疑','恐怖','治愈']
####### tag : ['热门','美剧','英剧','韩剧','日剧','国产剧','港剧','日本动画','综艺','纪录片']


class copyPic:
    def __init__(self):
        self.db = getDbConn()
        self.startValue = 480
        self.subLen = len("https://www.douban.com/link2/?url=")


    def randomNum(self):
        ranNum = random.randint(1, 200000)
        return ranNum

    def start(self):
        tag = ['综艺','纪录片']
        for i in tag :
            while (True):
                url = "https://movie.douban.com/j/search_subjects?type=tv&tag=" + i + "&sort=recommend&page_limit=20&page_start=" + str( self.startValue)
                # url = "https://movie.douban.com/j/search_subjects?type=movie&tag=" + i + "&sort=recommend&page_limit=20&page_start=" + str( self.startValue)
                flag = self.saveFile(url,i)
                if flag :
                    self.startValue += 20
                else:
                    self.startValue = 0
                    break

    def saveFile(self, url,tag):
        dataList = self.getJson(url)['subjects']
        print "=================================================="
        if dataList:
            for i in dataList:
                id = i['id']
                sql = "select * from doub where doub_id = "+id
                list = self.db.doSelect(sql)
                if list :
                    continue
                rate = i['rate']
                title = i['title']
                playable = i['playable']
                url = i['url']
                cover = i['cover']
                data = self.getJson("https://movie.douban.com/j/subject_abstract?subject_id="+str(i['id']))['subject']
                release_year = data["release_year"]
                region = data["region"]
                duration = data["duration"]
                subtype = data["subtype"]
                types = ",".join(data["types"])
                directors = ",".join(data["directors"]).replace("'"," ").replace("•"," ")
                actors = ",".join(data["actors"]).replace("'"," ").replace("•"," ")
                sql = "INSERT INTO doub (title,rate,doub_url,playable,doub_id,cover_url,release_year,region,duration,subtype,types,directors,actors,tag )VALUES('"+title+"','"+rate+"','"+url+"','"+str(playable)+"','"+id+"','"+cover+"','"+release_year+"','"+region+"','"+duration+"','"+ subtype+"','"+types+"','"+directors+"','"+actors +"','"+tag +"')"
                print sql
                self.db.doSql(sql)
                if playable == True :
                    try:
                        headers = {
                            'Accept-Encoding': 'gzip, deflate',
                            'Accept-Language': 'zh-CN,zhq=0.9',
                            'Connection': 'keep-alive',
                            'Host': 'movie.douban.com',
                            'Cache-Control': 'max-age=0',
                            'Upgrade-Insecure-Requests': '1',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0 Win64 x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
                            'Referer': 'https://movie.douban.com/explore',
                            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
                        }

                        html = requests.get(url, headers=headers, allow_redirects=False)
                        content = html.content
                    except urllib2.URLError, e:
                        print e.reason
                    myItems = re.findall('<ul class="bs">(.*)</ul>', content,  re.S)  # <a href="(.*)">(.*)</a>
                    # print myItems[0]
                    # img = re.findall(r"""<a\b[^>]+\bhref="([^"]*)"[^>]*>([\s\S]*?)</a>""", myItems[0])
                    lis = re.findall(r"""<li>[\s\S]*?</li>""", myItems[0])
                    # print img
                    for j in lis:
                        img = re.findall(r"""<a\b[^>]+\bhref="([^"]*)"[^>]*>([\s\S]*?)</a>""", j)[0]
                        # if "https://www.douban.com/link2/?url=" in img[0]:
                        if "javascript: void 0;" in img[0]:
                            url = img[0][self.subLen:len(img[0]) - 1]
                            url = urllib.unquote(url).strip()
                            value = re.findall(r"""<span>[\s\S]*?</span>""", j)[0].replace("\n","")
                            value = re.findall(r"""<span>(.*)</span>""", value)[0].strip()
                            # print url.strip()
                            name = img[1].strip()
                            sql = "INSERT INTO dob_video (doub_id,video_name,video_url,video_type )VALUES('"+ str(id) + "','" + name + "','" + url +  "','" + value + "')"
                            print sql
                            self.db.doSql(sql )
            return True
        else:
            return False

    def getJson(self,url):
        print url
        try:
            headers = {
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zhq=0.9',
                'Connection': 'keep-alive',
                'Host': 'movie.douban.com',
                'Cache-Control': 'max-age=0',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0 Win64 x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
                'Referer': 'https://movie.douban.com/explore',
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
            }

            html = requests.get(url, headers=headers, allow_redirects=False)
            content = html.content
        except urllib2.URLError, e:
            print e.reason
        print content
        return json.loads(content)


co = copyPic()
co.start()
