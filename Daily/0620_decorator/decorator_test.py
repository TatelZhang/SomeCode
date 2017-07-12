#! /usr/bin/env python
# coding = utf-8

"""
def func():
    print('func')

    def func1():
        print('func1')

        def func2():
            print('func2')
        return func2
    return func1

if __name__ == '__main__':
    f = func()
    f1 = f()
    f2 = f1()
"""

"""
def func1():
    print('func1')

    def func2():
        print('func2')
    return func2
"""


def func(fun):
    print('hello')
    fun()


@func
def func1():
    print('world')
