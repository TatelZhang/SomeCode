# coding = utf-8
#! /usr/bin/env python

from threading import Thread
from queue import Queue
import time


class Producer(Thread):
    def __init__(self, name, queue):
        self.__name = name
        self.__queue = queue
        super(Producer, self).__init__()

    def run(self):
        while True:
            if self.__queue.full():
                time.sleep(2)
            else:
                self.__queue.put('something')
                print('Producer %s 生产了 something' % self.__name)
                time.sleep(1)
            # Thread.run(self)


class Consumer(Thread):

    def __init__(self, name, queue):
        self.__name = name
        self.__queue = queue
        super(Consumer, self).__init__()

    def run(self):
        while True:
            if self.__queue.empty():
                time.sleep(2)
            else:
                self.__queue.get()
                time.sleep(10)
                print('Consumer %s 消费了 something' % self.__name)
                # Thread.run(self)

q = Queue(maxsize=20)

for item in range(4):
    name = '生产者：%s' % item
    p = Producer(name, q)
    p.start()


for item in range(10):
    name = '消费者：%s' % item
    c = Consumer(name, q)
    c.start()


