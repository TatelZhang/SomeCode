#! /usr/bin/env python
# coding = utf-8

import socket,time
host, port = "localhost", 8080
addr = (host, port)


class ServerClass(object):
    def __init__(self):
        self.__addr = addr
        self.__server = self.__start_server()

    def __start_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(self.__addr)
        server.listen(5)
        return server

    @staticmethod
    def handle_request(client):
        buff = client.recv(1024).decode()
        print(buff)
        if buff == '110':
            return 0
        else:
            client.send(("server:%s,time:%s" % (buff, time.ctime())).encode())
            return 1

    def respond(self):
        conn, addr = self.__server.accept()
        while 1:
            res = ServerClass.handle_request(conn)
            if not res:
                conn.send(b'0')
                conn.close()
                return 0

if __name__ == "__main__":
    s = ServerClass()
    s.respond()
