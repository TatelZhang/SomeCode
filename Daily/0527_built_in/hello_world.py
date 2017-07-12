#! /usr/bin/env python
# coding = utf-8

"""
nothing is impossible
@author: Tatel
"""

"""
def login(name):
    if name == 'Tatel':
        return 1
    else:
        return 0


def description(name):
    print(name, 'is 赛高')
    return 0


def func(name, job='砍柴', *args):
    print('''
      hello My name is %s ,and My job is %s
    ''' % (name, job))
    print(args)

if __name__ == '__main__':
    flag = 1
    while flag:
        usr = input("输入用户名：")
        res = login(usr)
        if res:
            func(usr, 'work', (1, 2, 3, 4))
            flag = description(usr)
        else:
            print("登陆失败了！")
"""

"""
d = {'name': "Tatel", 'age': 18}
l = ['tatel', 18]


def show(*args, **kwargs):
    for i in args:
        print(i)
    for k, v in kwargs.items():
        print(k, v)

show(*l)
"""

"""
def it():
    i = 0
    while i < 10:
        yield i
        i = i + 1
l = it()
for j in l:
    print(j)
"""

"""
def read_file():
    seek = 0
    while True:
        with open('account.txt', 'r') as f:
            f.seek(seek)
            data = f.readline()
            if data:
                seek = f.tell()
                yield data
            else:
                return
"""

"""
def read_file():
    with open('account.txt', 'r') as f:
        while True:
            data = f.readline()
            if data:
                yield data
            else:
                return

for i in read_file():
    print(i.strip())
"""
import random

# 定义可变参数时，传入的为列表，列表被认为是单个元素，调用时需使用 "*l " 将元素转成列表
def daluan(*args):       # daluan(l)   l = [1, 2, 3, 4, 5, 6, 7]
    print(type(args))    # 元组
    print(args)          # args = ([1, 2, 3, 4, 5, 6, 7],)
    print(type(*args))
    print(*args)         # args = [1, 2, 3, 4, 5, 6, 7]
l = [1, 2, 3, 4, 5, 6, 7]


def duoge(*args):             # duoge(1, 2, 3, 4, 5)
    print(type(args))         # 元组
    # print(type(*args))      # 异常 args 被转换成单个元素


