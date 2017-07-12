#! /usr/bin/env python
# coding = utf-8

import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def setup(self):
        pass

    def handle(self):
        print(self.request, self.client_address, self.server)

    def finish(self):
        pass

if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(('localhost', 10086), MyServer)
    server.serve_forever()
