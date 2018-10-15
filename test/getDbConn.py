# encoding=utf-8
#
# Python 3.5
# 需要安装pymysql模块

import pymysql
class getDbConn:
    def __init__(self):
        self.host = '118.24.0.202'
        self.port = 3306
        self.user = 'testuser'
        self.passwd = '123456'
        self.db = 'doub'

    def doSql(self,sql):
        try:
            conn = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                passwd=self.passwd,
                db=self.db,
                charset='utf8'
            )
            cur = conn.cursor();
            result = cur.execute(sql);
            # print(result);
            conn.commit();
        except(BaseException):
            print "error:"+sql
        finally:
            conn.close();


    def doSelect(self,sql):
        try:
            conn = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                passwd=self.passwd,
                db=self.db,
                charset='utf8'
            )
            cur = conn.cursor();
            cur.execute(sql);
            result = cur.fetchone();
            print(result);
            conn.commit();
        finally:
            conn.close();
        return result;

