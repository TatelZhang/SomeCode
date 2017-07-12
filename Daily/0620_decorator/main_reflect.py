#! /usr/bin/env python
# coding = utf-8

main_name = input('xxx/xxx')   # 输入模块以及方法保存为str
usr = main_name.split('/')      # 分割str，并保存为列表

mo = __import__(usr[0])         # 以字符串的形式导入模块
func = getattr(mo, usr[1])      # 以字符串的形式获取方法
func()                          # 执行方法
