#! /usr/bin/env python
# coding = utf-8
import socket


def handle(client):
    buff = client.recv(1024)
    print(buff)
    client.send("HTTP/1.0 200 OK\r\n\r\n".encode())
    client.send('hello'.encode())


def main():
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind(('localhost', 8080))
    serv.listen(5)
    while True:
        conn, addr = serv.accept()
        handle(conn)
        conn.close()


if __name__ == '__main__':
    main()
    """
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(('localhost', 8080))
    data = c.recv(1024)
    print(data)
    """