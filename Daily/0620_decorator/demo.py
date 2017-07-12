#! /usr/bin/env python
# coding = utf-8
import functools


def decorator(func):  # 传入需装饰函数
    @functools.wraps(func)         # 用于将返回的函数名 转变成原函数函数名
    def wrapper(*args, **kwargs):
        print("call %s()" % func.__name__)
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper  # 此处为返回给原函数的函数名


def decorator2(text):  # 传入装饰器参数
    def outer(func):   # 传入需装饰函数

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(text)
            func(*args, **kwargs)
        return wrapper
    return outer   # 返回装饰器


@decorator2('some')
def func1():
    print('Executed')

if __name__ == "__main__":
    # print(func1.__name__)
    func1()
