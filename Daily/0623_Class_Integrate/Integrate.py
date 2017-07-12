#! /usr/bin/env python
# coding = utf-8


class Some:
    pass


class Other(object):
    pass


class Father(object):
    f_attr = 'something'

    def __init__(self):
        self.Name = 'Father'

    def func(self):
        print('Father.func')

    def __call__(self, *args, **kwargs):
        print(self.Name)


class Son(Father):
    __slots__ = ('Name', 'age')

    def __init__(self):
        # Father.__init__(self)
        super(Son, self).__init__()
        # super().__init__()
        self.Name = 'Son'
        self.hobby = 'Game'

    def func2(self):
        print('Son.func2')

    def func(self):
        Father.func(self)
        print('son')

if __name__ == '__main__':
    f1 = Father()
    s1 = Son()
    s2 = Son()
    # s1.func()
    # s2.f_attr = 'other'
    # print(s1.f_attr)
    # print(Some.__dir__)
    # print(Other.__dir__)
    # print(s1.Name)
    # print(isinstance(Some, object))
    # s2.name = 1
    # print(s2.hobby)
    # print(isinstance(s2, type))  # False

    Bar = type('Bar', (object,), {'name': 'tatel'})

    print()
