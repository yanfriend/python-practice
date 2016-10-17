# -*- coding: utf-8 -*-
# Author: 黄哥python培训 qq:1465376564


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

p = fib()
print [p.next() for i in xrange(101)]
