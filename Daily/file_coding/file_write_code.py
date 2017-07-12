#! /usr/bin/env python
# coding = utf-8


def write2file(content):
    with open('file.txt', 'a') as file:
        file.write('\n')
        file.write(content)


if __name__ == '__main__':
    write2file('hello world')
    write2file('dierhang')