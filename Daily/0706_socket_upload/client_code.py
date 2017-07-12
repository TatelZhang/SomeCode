#! /usr/bin/env python
# coding = utf-8
import os
import socket

c = socket.socket()
ip_address = ('localhost', 10086)

c.connect(ip_address)
file_path = input('file path like:D:/Python File/New_Start/0706_socket_upload/client_code.py')
# file_name = file_path.split("/")[-1]
file_name = os.path.basename(file_path)
file_size = os.stat(file_path).st_size
send_data = file_name + '|' + str(file_size)
c.send(send_data.encode())
flag = True
with open(file_path, 'rb') as file:
    while flag:
        if file_size <= 0:
            flag = False
        elif file_size > 1024:
            data = file.read(1024)
            file_size -= len(data)
            c.send(data)
        else:
            data = file.read(file_size)
            file_size -= len(data)
            c.send(data)
    c.close()
