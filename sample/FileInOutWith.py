#from __future__ import with_statement # Python 2.x

with open('hello.txt') as f:
    for line in f:
        print(line,end='')

