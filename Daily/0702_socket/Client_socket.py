#! /usr/bin/env python
# coding = utf-8
import socket


class ClientClass(object):

    def __init__(self):
        self.__addr = ('localhost', 8080)
        self.__client = self.connect2server()

    def connect2server(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(self.__addr)
        return client

    def send_and_receive(self):
        while 1:
            data = input("输入数据：")
            self.__client.send(data.encode())
            data = self.__client.recv(1024).decode()
            if data == '0':
                break
            print(data)

if __name__ == '__main__':
    c = ClientClass()
    c.send_and_receive()
