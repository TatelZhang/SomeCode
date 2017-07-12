#! /usr/bin/env python
# coding = utf-8

# 魔术方法


class Func(object):
    def __int__(self):      # 构造函数
        pass

    def __del__(self):     # 析构函数
        print('Game Over')

    def __call__(self, *args, **kwargs):    # call 函数 ，可以对实例进行调用
        print(*args, kwargs)

    def __str__(self):      # 使用实例名时 调用
        return 'hehh'

    def __repr__(self):    # 返回机器可读字符串
        self.__str__()

if __name__ == '__main__':
    f1 = Func()
    # print(f1)
    f1('wowo', 'nman', name='wowoow')
