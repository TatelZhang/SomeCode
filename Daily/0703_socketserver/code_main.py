#! /usr/bin/env python
# coding = utf-8

import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def setup(self):
        pass

    def handle(self):
        while 1:
            data = self.request.recv(1024)
            if data.decode() == 'exit':
                break
            self.request.send(b'hello')
        self.request.close()

    def finish(self):
        pass

if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(('localhost', 10086), MyServer)
    server.serve_forever()
