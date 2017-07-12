#! /usr/bin/env python
# coding = utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 8080))
s.listen(5)
while 1:
    c, a = s.accept()
    data = c.recv(1024)
    print(data.decode())
    c.send(b'HTTP/1.1 200 OK\r\n\r\n')
    c.send(b'hello!')
    c.close()
