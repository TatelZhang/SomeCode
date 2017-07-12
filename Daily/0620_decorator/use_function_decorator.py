#! /usr/bin/env python
# coding = utf-8


def before():
    print('hello, world')


def after(args, func):
    if args < 10:
        print('%s is less than 10' % func.__name__)
    else:
        print('%s is bigger than 10' % func.__name__)


def compare_result(b, a):
    def outer(func):
        def wrapper(args1, args2):
            b()
            result = func(args1, args2)
            a(result, func)
            return result
        return wrapper
    return outer


@compare_result(before, after)
def add_some(a, b):
    return a+b

if __name__ == '__main__':
    add_some(1, 2)
