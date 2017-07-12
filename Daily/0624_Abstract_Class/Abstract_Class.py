#! /usr/bin/env python
# coding = utf-8

"""
貌似Python3 与 Python2并不一样
Python定义的抽象类方法在子类中不实现，并没有报错
"""

from abc import ABCMeta, abstractmethod


class InterfaceMethod:
    __metaclass__ = ABCMeta

    @abstractmethod
    def func(self): pass


class Foo(InterfaceMethod):
    def __init__(self):
        print('this is Foo')

if __name__ == '__main__':
    f1 = Foo()
    f1.func()

