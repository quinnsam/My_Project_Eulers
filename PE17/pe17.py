#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Sam Quinn
# 1-29-2017

def num2word(x):
    if x < 10:
        if x == 0: return ''
        elif x == 1: return 'One'
        elif x == 2: return 'Two'
        elif x == 3: return 'Three'
        elif x == 4: return 'Four'
        elif x == 5: return 'Five'
        elif x == 6: return 'Six'
        elif x == 7: return 'Seven'
        elif x == 8: return 'Eight'
        elif x == 9: return 'Nine'
    if len(str(x)) == 2:
        if x == 10: return 'Ten'
        elif x == 11: return 'Eleven'
        elif x == 12: return 'Twelve'
        elif x == 13: return 'Thirteen'
        elif x == 14: return 'Fourteen'
        elif x == 15: return 'Fifteen'
        elif x == 16: return 'Sixteen'
        elif x == 17: return 'Seventeen'
        elif x == 18: return 'Eighteen'
        elif x == 19: return 'Nineteen'
        elif int(str(x)[0]) == 2: return 'Twenty %s' % num2word(int(str(x)[1]))
        elif int(str(x)[0]) == 3: return 'Thirty %s' % num2word(int(str(x)[1]))
        elif int(str(x)[0]) == 4: return 'Forty %s' % num2word(int(str(x)[1]))
        elif int(str(x)[0]) == 5: return 'Fifty %s' % num2word(int(str(x)[1]))
        elif int(str(x)[0]) == 6: return 'Sixty %s' % num2word(int(str(x)[1]))
        elif int(str(x)[0]) == 7: return 'Seventy %s' % num2word(int(str(x)[1]))
        elif int(str(x)[0]) == 8: return 'Eighty %s' % num2word(int(str(x)[1]))
        elif int(str(x)[0]) == 9: return 'Ninety %s' % num2word(int(str(x)[1]))
    if len(str(x)) == 3:
        if x % 100 == 0: return '%s Hundred' % num2word(int(str(x)[0]))
        return '%s Hundred and %s' % (num2word(int(str(x)[0])), num2word(int(str(x)[1:])))
    if x == 1000: return 'One Thousand'

def main():
    count = 0
    for i in xrange(1,1001):
        print '%s - %s' % (i, num2word(i))
        count = count + len(num2word(i).replace(' ',''))

    print 'It takes %s characters to spell 1-1000 in words.' % count
if __name__ == "__main__":
        main()
