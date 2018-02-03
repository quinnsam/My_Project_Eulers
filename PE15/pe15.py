#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Sam Quinn
# 1-29-2017

def main():
    # Solving with math. It is a combination problem with the formula
    #       n!/r!(n-r)! = n(n-1)(n-2)... (n-r+1) / r!
    #
    #   As you can see the amount of Downs (D) and rights (R) do not change through out.
    #
    #   DDRR
    #   DRDR
    #   RDRD
    #   RRDD
    #   RDDR
    #   DRRD

    numerator = 1
    denominator = 1

    for i in xrange(40,20,-1):
        numerator = i * numerator
    for i in xrange(20,0,-1):
        denominator = i * denominator


    count = numerator / denominator

    print 'There are %s ways to the bottom right corner of a 20 X 20 grid' % count

if __name__ == "__main__":
        main()
