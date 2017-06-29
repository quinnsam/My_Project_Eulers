#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Sam Quinn
# 1-29-2017

def main():
    sum = 0
    for i in str(2**1000):
        sum = sum + int(i)

    print 'The sum of digits of 2^1000 is: %s' % sum

if __name__ == "__main__":
        main()
