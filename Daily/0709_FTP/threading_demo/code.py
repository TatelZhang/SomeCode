#! /usr/bin/env python
# coding = utf-8
from threading import Thread
import time


def fun(*args):
    for i in args:
        time.sleep(1)
        print(i, time.ctime())


def func():
    for i in range(100):
        print(i)
        time.sleep(1)

print('start')

t1 = Thread(target=fun, args=('t11', 't12', 't13'))

# t2 = Thread(target=func)
# t2.setDaemon(True)   # 设置守护线程
t1.start()  # 执行线程
t1.join()   # t1加入主线程，时间为None，待线程执行完毕再执行主线程
# t2.start()
# print(t1.isDaemon())

print('end')
