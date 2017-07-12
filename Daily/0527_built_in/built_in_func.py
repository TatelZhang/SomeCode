#! /usr/bin/env python
# coding = utf-8

"""
内置函数
"""
"""
a = []
b = {'action': 'laugh'}


class class_method(object):
    def __init__(self, name):
        self.name = name
        super(class_method, self).__init__()
# print(help(a)) # 提示a的使用方法

# print(dir(a)) # 列出a的属性及方法


c = class_method("name")
# print(vars(c))   # {'name': 'name'}  返回对象的属性键值对 （应该）等同于c.__dict__
i = vars(c)
j = c.__dict__
"""
# print(dir()) # 返回当前文件的包含的属性、方法  ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'b', 'c', 'class_method', 'i', 'j']
# print(vars()) # 返回键值对
# t = ()
# print(type(t))
# print(id(c))

"""
# 枚举
a = [x for x in range(10)]
for k, v in enumerate(a):
    print(k, v)

b = ['苹果', '香蕉', '梨']

for i in enumerate(b):
    print(i)

# 字符串格式化
s = "hello, my name's {0}{0}"
print(s.format("Tatel")) # hello, my name's Tatel
"""

"""
# Python3 不再支持 apply 函数
def apply(func, *args):
    return func(*args)


def print_my_name(args):
    print(args)

apply(print_my_name,("Tatel"))


l = [1, 2, 3, 4, 5]

m = map(lambda x: x*x, l)  # 生成一个迭代器 为函数传入l的每个参数
# print(list(m))          # 显示m中的元素

from functools import reduce
r = reduce(lambda x, y: x+y, l)
print(r)

f = filter(lambda x: x < 10, l)
print(list(f))


a = [1, 2, 3]
b = [3, None, 5]
c = [6, 7]

e = zip(a, b, c)
print(list(e))   # [(1, 3, 6), (2, 4, 7)]
"""

# 字符串解析
# s = '8*8'
# print(eval(s))
"""
m = 'sys'
# module = __import__(m)  # 通过字符串导入模块
import sys
print(sys.argv)
"""

"""
# 反射
temp = "test_hello_world"
func = 'print_hello_world'
mo = __import__(temp)
function_print = getattr(mo, func)
function_print()
"""
print(__file__)  # 文件路径
print(__name__)  # 文件执行
