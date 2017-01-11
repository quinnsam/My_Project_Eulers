#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Sam Quinn
# 1-10-2017



def main():
    sum = 0

    for c in xrange(1000, 2, -1):
        for b in xrange(1, 1000 - c):
            for a in xrange(0, b):
                if a + b + c == 1000:
                    if a**2 + b**2 == c**2:
                        print 'Found Pythagorean #: %s + %s = %s' % (a**2, b**2, c**2)
                        print 'a=%s + b=%s + c=%s = %s' % (a, b, c, a+b+c)
                        print 'abc = %s' % (a*b*c)
                        return



if __name__ == "__main__":
        main()
