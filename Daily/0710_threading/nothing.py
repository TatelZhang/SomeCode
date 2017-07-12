#! /usr/bin/env python
# coding = utf-8

from threading import Thread


def func(args):
    print(args)

l = list(range(10))

t = Thread(target=func, args=(l,))
t.start()
t.join()
print('execute ended')
