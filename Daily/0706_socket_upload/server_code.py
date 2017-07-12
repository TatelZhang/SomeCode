#! /usr/bin/env python
# coding = utf-8

import socket
import os

s = socket.socket()
ip_address = ('localhost', 10086)
s.bind(ip_address)
s.listen(5)
base_path = 'D:/temp'
while 1:
    conn, address = s.accept()
    data = conn.recv(1024).decode()
    file_name, file_size = data.split('|')
    file_size = int(file_size)
    save_path = os.path.join(base_path, file_name)
    flag = True
    with open(save_path, 'wb') as file:
        while flag:
            data = conn.recv(1024)
            if file_size:
                file.write(data)
                file_size -= len(data)
            elif file_size <= 0:
                flag = False
            print(len(data))
        conn.close()
    print('upload complete')
