#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Sam Quinn
# 11-14-2016

def sq_sum(x):
    ret = 0
    for i in range(0,x+1):
        ret = ret + i * i
    return ret

def sum_sq(x):
    ret = 0
    for i in range(0,x+1):
        ret = ret + i
    return (ret * ret)
def main():
    x = 100
    print "Difference: %s" % (sum_sq(x) - sq_sum(x))


if __name__ == "__main__":
        main()
