#! /usr/bin/env python
# coding = utf-8
import copy

'''
字典深浅拷贝
'''
__all__ = ['s1', 's2', 's3', '_s4']
s1 = 's11'
s2 = 's22'
s3 = 's33'
_s4 = 's44'

"""
a1 = 'sjajdjasdkkajfl'
a2 = 'sjajdjasdkkajfl'
a3 = copy.copy(a1)
# print(id(a1))
# print(id(a3))


d1 = dict(name='tatel', age=25)
d2 = d1
d1['name'] = 'tao'  # 赋值后d1 更改，d2同样更改
# print(d1, d2)  # {'name': 'tao', 'age': 25} {'name': 'tao', 'age': 25}


d3 = copy.copy(d1)
d3['name'] = 'tatel'  # 浅赋值后d1更改,d3不随d1更改
print('d1:%s ,d2:%s' % (id(d1), id(d3)))


dd = dict(name='tatel', age=25)
dd1 = dict(name='shine', d=dd)
dd2 = copy.copy(dd1)  # 浅复制
dd1['d']['name'] = 'tao'  # 浅复制后修改字典的元素的字典，修改其中一个，其他一个同样变化
print('1,%s;2%s' % (id(dd1), id(dd2)))


# dd3 = copy.deepcopy(dd1)
# dd3['d']['new'] = 'new'  # 深拷贝后不更改
# print('深拷贝：1，%s 2:\x1b[34m %s\x1b[0m' % (dd1, dd3))
"""


def comp(argv1, argv2):
    print('变量值：argv1:%s , argv2:%s \n内存地址: argv1:%s ，argv2：%s' % (argv1, argv2, id(argv1), id(argv2)))

dict1 = dict(name='tao', age=25)
dict2 = dict1
dict2['name'] = 'tatel'
# comp(dict1, dict2)
"""
结果：
参数值：argv1:{'name': 'tatel', 'age': 25} , argv2:{'name': 'tatel', 'age': 25} 
内存地址: argv1:58484752 ，argv2：58484752

字典赋值操作，更改变量值时操作同一内存，被赋值变量值改变，赋值变量值同样变更
"""

dict3 = dict(name='tao', age=25)
dict4 = copy.copy(dict3)  # 浅复制
dict4['name'] = 'tatel'
# comp(dict3, dict4)
'''
变量值：argv1:{'name': 'tao', 'age': 25} , argv2:{'name': 'tatel', 'age': 25} 
内存地址: argv1:49701488 ，argv2：20113040
浅复制：
'''

dict5 = dict(k1='something', k2={'name': 'something'})
dict6 = copy.copy(dict5)
dict6['k2']['name'] = 'tatel'
comp(dict5['k2'], dict6['k2'])
'''
变量值：argv1:{'k1': 'something', 'k2': {'name': 'tatel'}} , argv2:{'k1': 'something', 'k2': {'name': 'tatel'}} 
内存地址: argv1:48194016 ，argv2：46852112
字典浅复制：变量元素的字典内存相同
'''

