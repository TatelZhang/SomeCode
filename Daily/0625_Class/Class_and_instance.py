#! /usr/bin/env python
# coding = utf-8


class Person(object):
    a = 1

    def __init__(self, name, weight, age):
        self.Name = name
        self.Weight = weight
        self.__Age = age
        self.Hobby = None

    def speak(self):
        print('my name is {0}'.format(self.Name))

    def fight(self, value):
        if self.Weight > value:
            print('打')
        else:
            print("跑")

    def use_other(self, func, args):
        func(args)


def fun(args):
    print(args)
if __name__ == "__main__":
    some = Person('SomeOne', 80, 18)
    # print(some.__dict__)
    # some.lover = None
    # print(some.__dict__)
    # print(Person.__dict__)
    # s = dir(Person)  # 返回对象的属性与方法
    # s = vars(some)
    # print(s)
    # print(some.__dict__)
    # some.a = 2
    # print(some.__dict__)
