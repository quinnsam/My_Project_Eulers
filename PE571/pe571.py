#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Sam Quinn
# 11-07-2016
from multiprocessing import Process, Queue
import time
sum = 0
count = 0

def dec2base(x, b):
    bin = ''
    ret = 0
    while x >= 1:
        #print "x ", x
        #print "mod ", (x % b)
        bin = str(x % b) + bin
        if x == x/b:
            ret = ret + 1
        else:
            x = x/b
        if ret == 2:
            x = 0
    return str(bin)

def check_pan(x):
    global tcount
    global tsum
    #for i in range(2, 12):
    for i in reversed(range(2, 13)):
        num = dec2base(x,i)
        #print num
        for j in reversed(range(0, i)):
            if not str(j) in num:
                return False
    return True

def worker(q, pid):
    global count
    global sum
    while True:
        i = q.get()
        if i == 'END':
            return True
        else:
            if check_pan(i):
                print "Twelve Yes: %s count: %s sum: %s" % (i,count,sum)
                count = count + 1
                sum = sum + i


def main():
    _start = time.time()
    #i = 1000000000
    i = 100000000000
    #p = 1001000000
    p = 100001000000
    procs = 8
    ql = []
    pl = []
    for t in range(0,procs):
        ql.append(Queue())
        pl.append(Process(target=worker, args=((ql[t]),t,)))
        pl[t].start()



    while count < 10:
        ql[i % procs].put(i)
        i = i + 1
        if i > p:
            print p
            p = i + 10000000


    for t in range(0,procs):
        ql[t].put('END')

    for t in range(0,procs):
        pl[t].join()

    print "Checking %s numbers with %s processes took %s time" % (i,procs, (time.time() - _start))



if __name__ == "__main__":
        main()
