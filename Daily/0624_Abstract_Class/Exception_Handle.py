#! /usr/bin/env python
# coding = utf-8


class MyException(Exception):
    def __init__(self, msg):
        self.error = msg

    def __str__(self):
        return self.error


try:
    s = int(input('something:'))
    if s == 1:
        raise MyException('cuowu')
except ValueError as e:
    print(e)