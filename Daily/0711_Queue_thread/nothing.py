#! /usr/bin/env python
# coding = utf-8


def fib(x):
    if x < 3:
        return 1
    else:
        return fib(x-1) + fib(x-2)


for i in range(20):
    print(fib(i))