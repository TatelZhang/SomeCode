#! /usr/bin/env python
# coding = utf-8


class FunctionMethod(object):
    def __init__(self, name):
        self.name = name

    @classmethod
    def class_method(cls):
        print('classmethod')

    @staticmethod
    def static_method():
        print('staticmethod')

    def instance_method(self):
        print('instancemethod', self.name)


if __name__ == '__main__':
    """
    func = FunctionMethod('tatel')
    func.class_method()
    func.instance_method()
    func.static_method()
    """
    FunctionMethod.static_method()  # 静态方法
    FunctionMethod('tatel').class_method()
    FunctionMethod('tatel').instance_method()
