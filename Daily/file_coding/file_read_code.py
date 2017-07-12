#! /usr/bin/env python
# coding = utf-8


def read_and_write():
    with open('file.txt', 'r+') as rfile:
        l = rfile.readlines()
        for i in range(len(l)):
            l[i] = l[i].replace('world', 'new')
        rfile.seek(0)
        rfile.writelines(l)

if __name__ == '__main__':
    read_and_write()
