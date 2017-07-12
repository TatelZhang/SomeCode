#! /usr/bin/env python
# coding = utf-8

import pymysql

conn = pymysql.connect(host='localhost', port=3306, user="root", password='1028395672', db='helloworld', charset='utf8')

SQL = """SELECT * FROM user_table"""
create = """CREATE TABLE User(
            FIRST_NAME CHAR(20) NOT NULL ,
            LAST_NAME CHAR(20),
            AGE INT,
            SEX CHAR(1)
)
"""
insert = """INSERT INTO User(
FIRST_NAME,LAST_NAME,AGE)
VALUES ('Tatel', 'zhang',20)"""
cursor = conn.cursor()
try:
    cursor.execute(SQL)
    # conn.commit()  # 用于提交事务
    c1 = cursor.fetchall()
    for row in c1:
        print('id=%s,name=%s,account=%s' % row)
except Exception as e:
    print(e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()
