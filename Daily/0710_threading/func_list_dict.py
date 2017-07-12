#! /usr/bin/env python
# coding = utf-8

dict1 = {'name': 'tatel', 'd1': {'var1': 'something', 'var2': {'1': '1111', '2': 2222}}}

l = []


def func(args):
    for value1 in args.values():
        if isinstance(value1, dict):
            func(value1)
        else:
            l.append(value1)

func(dict1)
print(l)
