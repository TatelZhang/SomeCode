#! /usr/bin/env python
# coding = utf-8
import pymysql
"""
Conn = pymysql.Connection(host='localhost', user='root', password='1028395672', db='helloworld',
                          cursorclass=pymysql.cursors.DictCursor) # cursorclass=pymysql.cursors.DictCursor 返回列名
cursor = Conn.cursor()

s1 = 'select * from user_table'
s2 = '''insert into user_table(username, account) VALUES (%s, %s)'''
para1 = [
    ('tao', 200000),
    ('zhang', 200000)
]
para2 = ('hello', 20000)
# cursor.executemany(s2, para1) # 执行多行语句,且只能执行多行语句
cursor.execute(s1)
# Conn.commit()      # 更改数据库之后要提交事务，跟rollback() 相反
res = cursor.fetchone()  # 查询数据库并返回一条数据信息
count = cursor.rowcount   # 返回事务操作影响数据条数
# print(count, res)
print(res)
"""
"""
Conn = pymysql.Connection(host='localhost', user='root', password='1028395672', db='helloworld')
sql = '''select * from user_table'''

Cur = Conn.cursor()
Cur.execute(sql)

data = Cur.fetchone()
data = Cur.fetchone()
data = Cur.fetchone()
# Cur.scroll(0, mode='absolute')  # 绝对定位，指向第0个
Cur.scroll(0)     # 默认相对定位，指向当前位置，Cur.fetchone()
# Cur.scroll(0, mode='relative')  # 相对定位，等同于scroll(0)
data = Cur.fetchone()

# data = Cur.fetchmany()  # 返回多条数据，默认返回1条
for i in range(Cur.rowcount):
    data = Cur.fetchone()
    print(data)
"""


Conn = pymysql.Connection(host='localhost', user='root', password='1028395672', db='helloworld')
Cursor = Conn.cursor()
sql = 'insert into user_table(username, account) VALUES (%s, %s)'
para = ('new', 10000)

Cursor.execute(sql, para)
Conn.commit()
pos = Cursor.lastrowid   # 返回当前事务最后一次操作所在位置
print(pos)
