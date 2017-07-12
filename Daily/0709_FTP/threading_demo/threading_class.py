#! /usr/bin/env python
# coding = utf-8
from threading import Thread


class MyThread(Thread):

    def run(self):
        print('我是线程.')
        Thread.run(self)


def func():
    print('func1')

t = MyThread(target=func)
t.start()
