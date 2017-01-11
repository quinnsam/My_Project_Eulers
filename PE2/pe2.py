#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Sam Quinn
# 11-14-2016

def fib(x):
    if x == 1 or x == 0:
        return 1
    else:
        return fib(x-2) + fib(x-1)

def main():

    i = 1
    j = 0
    sum = 0
    while(j < 4000000):
        j = fib(i)
        if j % 2 == 0:
            sum = sum + j
        i = i + 1
    print sum
if __name__ == "__main__":
        main()
