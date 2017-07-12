#! /usr/bin/env python
# coding = utf-8
import pymysql


class MySQLHelper(object):

    def __init__(self, host='localhost', db='tatel'):
        self.__host = host
        self.__db = db
        # self.__cursor_class = cursor_class
        self.__Conn = pymysql.Connection(host=self.__host, user='root',password='1234', db=self.__db,)

    def get_one(self, sql, params):
        try:
            cursor = self.__Conn.cursor()
            cursor.execute(sql, params)
            data = cursor.fetchone()
            cursor.close()
            return data
        except Exception as e:
            print('get_one() ,Error:', e)

    def get_all(self, sql, params):
        try:
            cursor = self.__Conn.cursor()
            cursor.execute(sql, params)
            data = cursor.fetchall()
            cursor.close()
            return data
        except Exception as e:
            print('get_all() Error', e)

    def insert_into(self, sql, params):
        try:
            cursor = self.__Conn.cursor()
            cursor.execute(sql, params)
            self.__Conn.commit()
            cursor.close()
        except Exception as e:
            self.__Conn.rollback()
            print(e)
        else:
            return 1

    def original_execute(self, sql):
        try:
            cursor = self.__Conn.cursor()
            cursor.execute(sql)
            self.__Conn.commit()
            cursor.close()
            return 1
        except Exception as e:
            self.__Conn.rollback()
            print(e)

    def __del__(self):
        self.__Conn.close()

if __name__ == '__main__':
    helper = MySQLHelper()
    # sql = '''create table user(id INT , username VARCHAR (20));'''
    # helper.original_execute(sql)
    sql = '''select * from user'''
    helper.original_execute(sql)
