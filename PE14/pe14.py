#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Sam Quinn
# 1-28-2017
num = []
max_num = []
max_len = 0
def collatz(x):
    num.append(x)
    if x == 1:
        return 1
    if x % 2 == 0:
        collatz(x/2)
    else:
        collatz((3 * x) + 1)

def main():
    global num
    global max_num
    global max_len
    for i in xrange(1,1000000):
        num = []
        collatz(i)
        if len(num) > max_len:
            max_len = len(num)
            max_num = num


    print '%s' % max_num
    print 'The largest Coallatz chain under a million is %s' % max_len

if __name__ == "__main__":
        main()
