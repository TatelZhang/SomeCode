#! /usr/bin/env python
# coding = utf-8
import pymysql


class QuerySQL(object):
    def __init__(self, db):
        self.db = db
        self.connection = pymysql.Connection(host='localhost', port=3306, user='root',
                                             password='1028395672', db=self.db, charset='utf8')
        self.cursor = self.connection.cursor()

    def create_table(self, sql):
        try:
            self.cursor.execute(sql)
        except Exception as e:
            self.connection.rollback()
            print(e)

    def uppdate_sql(self,sql):
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print(e)

    def sql_some(self, sql):
        try:
            self.cursor.execute(sql)
            some = self.cursor.fetchall()
            return some
        except Exception as e:
            print(e)
