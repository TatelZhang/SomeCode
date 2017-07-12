#! /usr/bin/env python
# coding = utf-8
"""
    装饰器的测试。
"""

import time

"""
def deco(foo):
    def wrapper(args):
        print('decorator')
        s = foo(args)
        print(s, foo.__name__)
        return s # 返回func的函数返回值，保持原有功能，在使用装饰器的同时要根据原函数的定义进行处理
    # wrapper('s') # 本质上为重定义func函数，并将func作为传入deco的参数，并使用wrapper调用func函数，无返回值
    return wrapper # 本质上为重定义func函数为wrapper函数


@deco
def func(args):
    return args

func('hello')
"""
"""
def hello3(foo):# 直接调用函数
    foo()


@hello3
def func4():
    print('hello4')
"""

"""
# 装饰后直接调用函数
def hello1(foo):
    print(time.ctime())
    foo()
    print('zhixingwancheng')


@hello1
def func2():
    print('func2')


@hello1
def func3():
    print('func3')
"""

"""
# 装饰器，在函数调用前对函数进行预处理，并返回装饰后的函数
def hello(foo, args):
    def wrapper():
        print('hello', time.ctime())
        s = foo()
        print(s)
    return wrapper  # 返回装饰后的函数


@hello
def func1(args):
    args = input('something:')
    return args
"""


def deco1(a1):
    def _deco(foo):
        print(a1)

        def __deco(args):
            foo(args)
        return __deco
    return _deco


@deco1("hello")
def func(args= 's'):
    print(args)

if __name__ == '__main__':
    func('s')
    pass
