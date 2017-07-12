#! /usr/bin/env python
# coding = utf-8

import socketserver
"""
a = b'GET / HTTP/1.1\r\nHost: localhost:8080\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.8\r\n\r\n'
a = a.decode()
b = a.split('\r\n')
for i in b:
    print(i)
"""

with open('nothing.txt', "r") as file:
    print(file)   # <_io.TextIOWrapper name='nothing.txt' mode='r' encoding='cp936'>  文件句柄

