#!/usr/bin/python
#  -*- coding: latin-1 -*-

import doctest

'''
Calculo do fibonacci
>>>f.fib(5)
5
>>>f.fib(10)
55
'''


class Fibonacci:
    def fib(self, n):
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a


if __name__ == '__main__':
    doctest.testmod(extraglobs={'f':Fibonacci()})
