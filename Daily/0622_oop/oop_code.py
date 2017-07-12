#! /usr/bin/env python
# coding = utf-8


class Person:
    def __init__(self, name):
        self.Name = name
        # self.bar
        self.__name = 'private'
        self.__nothing = 'default'

    @property
    def bar(self):              # 设置字段为外部为只读
        return self.Name

    @staticmethod
    def __method_private():
        print('卧槽，居然不能使用实例变量')

    @property
    def nothing(self):
        return self.__nothing

    @nothing.setter
    def nothing(self, value):  # 可以设置字段值
        self.__nothing = value
        print(self.nothing, 'ok')


if __name__ == '__main__':
    tatel = Person("Tatel")
    # tatel._Person__method_private()
    # tatel.nothing = 'hahah'
    # print(tatel.nothing)
    print(tatel.bar)
    # tatel.bar = 'some'  # 只读， Error
