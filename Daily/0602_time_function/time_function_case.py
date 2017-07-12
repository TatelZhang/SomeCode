#! /usr/bin/env python
# coding = utf-8

import time, pickle, json
d = {'a': 'b'}
c = {'d': 'e'}
p1 = pickle.dumps(d)
p2 = pickle.dumps(c)
j1 = json.dumps(d)
j2 = json.dumps(c)

def write2txt():
    with open('time.txt', 'w') as f:
        f.write(j1)
        f.write('\n')
        f.write(j2)


def readftxt():
    with open ('time.txt', 'r') as f:
        line =f.readlines()
        for i in line:
            print(json.loads(i))
        
        for line in f.readlines():
            line = pickle.loads(line)
            print(line)
if __name__ == '__main__':
    # write2txt()
    readftxt()
