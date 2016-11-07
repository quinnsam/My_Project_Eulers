#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Sam Quinn
# 11-07-2016

def dec2bin(x):
    #bin = ''
    #while x != 1 or x != 0:
    #    x = x/2
    #    bin = bin + str(x % 2)
    #if len(bin) < 4:
    #    for i in range(len(bin), 4):
    #        bin = bin + '0'
    #elif len(bin) < 8 and len(bin) > 4:
    #    for i in range(len(bin), 8):
    #        bin = bin + '0'
    #if len(bin) < 16 and len(bin) > 8:
    #    for i in range(len(bin), 16):
    #        bin = bin + '0'
    #if len(bin) < 32 and len(bin) > 16:
    #    for i in range(len(bin), 32):
    #        bin = bin + '0'
    return bin(x)[2:]

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
    sum = 0
    for i in range(0, 1000000):
        if check_pal(i) and check_pal(dec2bin(i)):
            print str(i) + "\t" + dec2bin(i)
            sum = sum + i

    print "Sum Total: ", sum

if __name__ == "__main__":
        main()
