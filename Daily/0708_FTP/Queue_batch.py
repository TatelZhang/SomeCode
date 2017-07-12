#! /usr/bin/env python
# coding = utf-8

import queue


def task(name, work_queue):
    if work_queue.empty():
        print('task {} has nothing to do'.format(name))
    else:

        while not work_queue.empty():
            n = work_queue.get()
            total = 0
            for i in range(n):
                print('Task {} was doing {}'.format(name, n))
                total += 1
            print('total %s' % total)


def main():
    q = queue.Queue()
    l = [1, 3, 5, 7]
    for i in l:
        q.put(i)

    tasks = [(task, 'one', q),
             (task, 'two', q),]

    for t, n, qq in tasks:
        t(n, qq)

if __name__ == '__main__':
    main()
