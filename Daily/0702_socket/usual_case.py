#! /usr/bin/env python
# coding = utf-8
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 8080))
s.listen(5)
conn, addr = s.accept()
conn.send(b'hello')
conn.close()