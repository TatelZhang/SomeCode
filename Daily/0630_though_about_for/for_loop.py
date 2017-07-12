#! /usr/bin/env python
# coding = utf-8


class MyLoop(object):
    def __init__(self, num):
        self.num = num
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.num:
            self.i += 1
            return self.i-1
        else:
            raise StopIteration


l = MyLoop(3)

for i in MyLoop(3):
    print(i)
