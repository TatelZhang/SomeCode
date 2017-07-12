#! /usr/bin/env python
# coding = utf-8

import socket
"""
c = socket.socket()
ip_address = ('www.baidu.com', 80)
c.connect(ip_address)
request_line = 'GET HTTP/1.1'
request_header = '''Host: baidu.com:80\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.8
'''
request_blank = '\r\n'
message = '\r\n'.join([request_line, request_header, request_blank])
c.send(message.encode())
data = c.recv(1024)  # 返回了个锤子哟
print(data)
"""

client = socket.socket()
client.connect(("www.seriot.ch", 80))
line = 'GET /index.php HTTP/1.1'
header = 'HOST: seriot.ch'
blank = '\r\n'

m = '\r\n'.join([line, header, blank])
client.send(m.encode())
data = client.recv(1024)
client.close()
print(data)