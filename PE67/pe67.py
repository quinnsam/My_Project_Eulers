#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Sam Quinn
# 1-29-2017


tri = []
rem = {}

def main():
    make_tri()
    #for i in tri: print i
    tot_sum = best(0,0)
    print "The best possible path is %s " % tot_sum

def best(y,x):
    global tri
    global rem

    # If we have computed this value before return it.
    if (y,x) in rem:
        return rem[(y,x)]

    # We have reached the bottom of the triangle
    if y == len(tri) -1:
        return tri[y][x]


    rem[(y,x)] = tri[y][x] + max(best(y+1,x),best(y+1,x+1))
    return rem[(y,x)]

def make_tri():
    global tri
    with open('./p067_triangle.txt') as f:
        for line in f:
            a = list(map(int,line.split()))
            tri.append(a)

if __name__ == "__main__":
    main()
