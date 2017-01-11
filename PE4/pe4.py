#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Sam Quinn
# 11-14-2016

def check_pal(i):
    ret = 0
    for x in range(0, len(str(i)) -1):
        y = len(str(i)) -1 -x
        if str(i)[x] == str(i)[y]:
            ret = ret +1
        else:
            return False
    if ret == len(str(i))-1:
        return True

def main():
    max = 0
    for i in reversed(range(0, 1000)):
        for j in reversed(range(0,1000)):
            if check_pal(i*j):
                #print "%s x %s = %s" % (i,j,i*j)
                if i*j > max: max = i*j
    print "Max: %s" % (max)

if __name__ == "__main__":
        main()
