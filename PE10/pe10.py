#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Sam Quinn
# 11-14-2016

import math

def main():
    x = 2000000
    primes = []
    for i in range(0,x):
        primes.append(i)
    primes[1] = 0

    for i in range(2,int(math.sqrt(x))):
        if primes[i] != 0:
            j = i + i
            while(j < x):
                primes[j] = 0
                j = j + i


    print "Done finding the 2M primes beginning summing."
    count = 0
    for p in primes:
        count = count + p


    print "The sum of every prime under 2M is: %s" % (count)




if __name__ == "__main__":
        main()
