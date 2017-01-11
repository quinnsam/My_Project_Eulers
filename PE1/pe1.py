#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Sam Quinn
# 11-14-2016

def mult(y):
    ret = 0
    for i in range(1,y):
        if (i % 3 == 0 or i % 5 == 0):
            #print i
            ret = ret + i
    return ret

def main():

    print "Sum Total: ", mult(1000)

if __name__ == "__main__":
        main()
