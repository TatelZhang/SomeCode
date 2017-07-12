#! /usr/bin/env python
# coding = utf-8

import socket

s = socket.socket()
address = ('localhost', 10086)

s.bind(address)
s.listen(5)
while True:
    client, ip_address = s.accept()
    client.send(b'hello')
    flag = 1
    while flag:
        data = client.recv(1024)
        print(data.decode())
        client.send(b'hello')
        if data.decode() == 'exit':
            flag = 0
    client.close()
