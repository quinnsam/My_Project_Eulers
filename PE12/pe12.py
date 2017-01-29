#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import sqrt

# Sam Quinn
# 1-28-2017


def factor(x):
    fact = []
    for i in xrange(1,(x/2) + 1):
        if x % i == 0:
            fact.append(i)
    fact.append(x)
    return fact

def main():
    print 'This is not the best way to solve this problem. Please consider another solution. This takes a while.'
    tri = 1
    count = 2

    while len(factor(tri)) < 500:
        tri = tri + count
        count = count + 1
        #print tri

    print 'The first Triangle number with over 500 factors is %s' % tri


if __name__ == "__main__":
        main()
