#! /usr/bin/env python
# coding = utf-8


class MainClass(object):

    def __init__(self, some):
        self.Some = some

    def self_func(self):
        print(self.func)
        MainClass.func()

    @staticmethod
    def func():
        print('static method func')

if __name__ == '__main__':
    m = MainClass('name')
    # assert (1!=1)  # 条件判断语句，用于判断条件是否满足，若不满足会抛出AssertionError
    assert (isinstance(m, MainClass))
    m.self_func()
