#! /usr/bin/env python
# coding = utf-8

import socket

client = socket.socket()
address = ('127.0.0.1', 10086)
client.connect(address)
while True:
    data = input('我说：')
    client.send(data.encode())
    if data == 'exit':
        break
    data = client.recv(1024)
    print(data.decode())
