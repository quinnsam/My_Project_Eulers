#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Sam Quinn
# 11-14-2016

import math

def main():
    x = 1000001
    primes = []
    for i in range(0,x):
        primes.append(i)
    primes[1] = 0

    for i in range(2,int(math.sqrt(x))):
        if primes[i] != 0:
            j = i + i
            while(j < 999999):
                primes[j] = 0
                j = j + i


    print "Done finding the 10001th now"
    count = 0
    i = -1
    while(count != 10001):
        i = i + 1
        if i > 1000000:
            print "Not found count: %s" % (count)
            return -1
        if primes[i]:
            count = count + 1


    print "The %s is %s" % (count,primes[i])




if __name__ == "__main__":
        main()
