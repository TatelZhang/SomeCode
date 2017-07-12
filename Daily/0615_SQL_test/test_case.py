#! /usr/bin/env python
# coding = utf-8

from SQL_Oprate_Class import QuerySQL


class Person(object):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def change_account(self, account):
        sql = """UPDATE user_table SET account = %s WHERE username = '%s '""" % (account, self.name)
        return sql

    def insert_user(self, userid, username, account):
        sql = "INSERT INTO user_table VALUES(%d, '%s', %d)" % (userid, username, account)
        return sql

person = Person('tim', 2000)
operate = QuerySQL('helloworld')
# change = person.change_account(100000)
for i in range(10):
    change = person.insert_user(i+5, 'hahah', 2000*i)
    print(change)
    operate.uppdate_sql(change)
    operate.connection.commit()
