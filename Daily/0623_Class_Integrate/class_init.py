#! /usr/bin/env python
# coding = utf-8


class Other(object):
    __slots__ = ('name', 'age', 'sex')


class Some(Other):
    __slots__ = ('name', 'age')

    def __init__(self, name, age, sex):
        super(Some, self).__init__()
        self.name = name
        self.age = age
        # self.sex = sex

if __name__ == '__main__':
    person = Some('Tatel', 25, 'Male')
    person.sex = 'Male'
