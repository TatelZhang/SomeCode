#! /usr/bin/env python
# coding = utf-8
import json
import os


s = "D:/Python File/New_Start/0706_socket_upload/client_code.py"
l = s.split('/')
r = os.path.basename(s)
sz = os.stat(s).st_size
t = "什么"
t1 = b'\xe4\xbb\x80\xe4\xb9\x88'
print(len(t1))

d = dict(name='tatel', age=25, gender='Male')
d = json.dumps(d)
b = d
s = {"name": "tatel", "age": 25, "gender": "Male"}
print(type(b))