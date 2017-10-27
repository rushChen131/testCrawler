# encoding=utf-8
#
# Python 3.5
# 需要安装pymysql模块

import pymysql
class getDbConn:

    def doSql(sql):
        try:
            conn = pymysql.connect(
                host='localhost',
                port=3306,
                user='root',
                passwd='13122441',
                db='test',
                charset='utf8'
            )
            cur = conn.cursor();
            result = cur.execute(sql);
            print(result);
            conn.commit();
        finally:
            conn.close();
        return result;



db = getDbConn();


db.doSql("insert into douyin (douyin_id) VALUES (23213)")