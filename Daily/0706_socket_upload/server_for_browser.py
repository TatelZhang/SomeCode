#! /usr/bin/env python
# coding = utf-8

import socketserver


class MyHandler(socketserver.BaseRequestHandler):
    def setup(self):
        pass

    def handle(self):
        line = 'HTTP/1.1 200 OK\r\n\r\n'
        self.request.send(line.encode())
        self.request.send(b'GoodBye!')
        self.request.send(b'nihao')

    def finish(self):
        print(self.request, 'finished')
if __name__ == "__main__":
    s = socketserver.ThreadingTCPServer(('127.0.0.1', 8080), MyHandler)
    s.serve_forever()
