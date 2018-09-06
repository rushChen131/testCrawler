# coding=utf-8
import json
import urllib2
import re
import random
import urllib

import requests

from getDbConn import getDbConn


####### tag : 热门  最新  经典  可播放  豆瓣高分  冷门佳片  华语  欧美  韩国  日本  动作 喜剧  爱情  科幻  悬疑  恐怖  成长


class copyPic:
    def __init__(self):

        self.db = getDbConn()

    def randomNum(self):
        ranNum = random.randint(1, 200000)
        return ranNum

    def start(self):
        start = 400
        while (True):
            url = "https://movie.douban.com/j/search_subjects?type=movie&tag=" + '经典' + "&sort=recommend&page_limit=20&page_start=" + str(
                start)
            self.saveFile(url)
            start += 20

    def saveFile(self, url):

        dataList = self.getJson(url)['subjects']
        for i in dataList:
            rate = i['rate']
            title = i['title']
            playable = i['playable']
            url = i['url']
            cover = i['cover']
            id = i['id']
            data = self.getJson("https://movie.douban.com/j/subject_abstract?subject_id="+str(i['id']))['subject']
            release_year = data["release_year"]
            region = data["region"]
            duration = data["duration"]
            subtype = data["subtype"]
            types = ",".join(data["types"])
            directors = ",".join(data["directors"])
            actors = ",".join(data["actors"])
            self.db.doSql("INSERT INTO doub (title,rate,doub_url,playable,doub_id,cover_url,release_year,region,duration,subtype,types,directors,actors )VALUES('"
                                                +title+"','"+rate+"','"+url+"','"+str(playable)+"','"+id+"','"+cover+"','"+release_year+"','"+region+"','"+duration+"','"+ subtype+"','"+types+"','"+directors+"','"+actors +"')")

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
