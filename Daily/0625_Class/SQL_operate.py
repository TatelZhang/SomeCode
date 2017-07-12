#! /usr/bin/env python
# coding = utf-8
import pymysql


class MainOperate(object):
    def __init__(self, db):
        self.db = db
        self.Conn = MainOperate.connection(self.db)
        self.cursor = self.Conn.cursor()

    def execute_select(self, sql):
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return res

    def execute_insert(self, sql):
        try:
            self.cursor.execute(sql)
            self.Conn.commit()
        except Exception as e:
            print(e)
        else:
            print('Insert Success')

    def execute_del(self, sql):
        try:
            self.cursor.execute(sql)
            self.Conn.commit()
        except Exception as e:
            print(e)
        else:
            print("Delete Success")

    def execute_update(self, sql):
        try:
            res = self.cursor.execute(sql)
            self.Conn.commit()
        except Exception as e:
            print(e)
        else:
            print('update Success')
            return res

    def __del__(self):
        self.cursor.close()
        self.Conn.close()

    @staticmethod
    def connection(database):
        Conn = pymysql.Connection(host='localhost', port=3306, user='root', password='1028395672', db=database,
                                  charset='utf8')
        return Conn

if __name__ == "__main__":
    s1 = """select * from user"""
    s2 = """insert into user(FIRST_NAME, LAST_NAME, AGE, SEX) 
             VALUES ("tao", "zhang", 25, "Male")"""
    s3 = """delete from user where FIRST_NAME = 'tao'
    """
    s4 = """ update user set SEX = 'Male', AGE = 25 WHERE FIRST_NAME = 'Tatel'
    """
    s5 = """
    update user set HOBBY = 'Coding' WHERE  FIRST_name = 'Tatel'"""
    Conn = MainOperate('helloworld')
    # Conn.execute_insert(s2)
    # Conn.execute_del(s3)
    # res = Conn.execute_update(s4)
    Conn.execute_insert(s2)
