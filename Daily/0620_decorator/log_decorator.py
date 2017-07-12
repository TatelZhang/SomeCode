#! /usr/bin/env python
# coding = utf-8
import time

"""
def log(somewhere):
    def outer(func):
        def wrapper(*args, **kwargs):
            with open(somewhere, 'a') as file:
                file.write(time.ctime())
            func(*args, **kwargs)
        return wrapper
    return outer
"""


def log_print(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print("%s is wrong, Exception: %s" % (func.__name__, e))
    return wrapper


@log_print
def func1(a, b):
    print(a+b)

if __name__ == "__main__":
    func1(3, 's')
