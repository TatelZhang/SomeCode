#! /usr/bin/env python
# coding = utf-8

"""
class Old_class1:
    def __init__(self):
        print("Old class1")

    def save(self):
        print('Old class1')


class Old_class2(Old_class1):
    def __init__(self):
        print('Old class2')


class Old_class3(Old_class1):
    def __init__(self):
        print('Old class3')

    def save(self):
        print('Old class3')


class New_class(Old_class2, Old_class3):
    def __init__(self):
        print('new class')
        # Old_class2.__init__(self)
        # Old_class3.__init__(self)
"""

class A:
    def __init__(self):
        print('This is A ')

    def save(self):
        print('From A')


class B(A):
    def __init__(self):
        print('This is B ')


class C(A):
    def __init__(self):
        print('This is C ')

    def save(self):
        print('From C')


class D(B, C):
    def __init__(self):
        print('This is D ')



if __name__ == "__main__":
    new = D()
    new.save()