#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Sam Quinn
# 1-29-2017

def main():
    grid = []
    for i in xrange(0,20):
        grid.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

    for i in grid: print i
    return 1
    count = 0
    all_found = False
    while not all_found:
        idx = (0,0)
        while not idx == (19,19):
            print idx
            # Go down
            if idx[1] < 19 and grid[idx[0]][idx[1] + 1] == 0:
                grid[idx[0]][idx[1] + 1] = 1
                idx = (idx[0], idx[1] + 1)
            # Go right
            elif idx[0] < 19 and grid[idx[0] + 1][idx[1]] == 0:
                grid[idx[0] + 1][idx[1]] = 1
                idx = (idx[0] + 1, idx[1])
            else:
                all_found = True
                break

            if idx == (19,19):
                grid[19][19] = 0
                count = count + 1

    print 'There are %s ways to the bottom right corner' % count



if __name__ == "__main__":
        main()
