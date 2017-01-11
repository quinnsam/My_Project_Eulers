#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Sam Quinn
# 11-14-2016

def main():
    run = True
    x = 2
    while(run):
        count = 0
        for i in range(1,21):
            count = count + (x % i)
            if count:
                break

        if count == 0:
            run = False
            print x
        x = x + 1



if __name__ == "__main__":
        main()
