from __future__ import with_statement
import sys, codecs

try:
    with codecs.open(sys.argv[1], "r", sys.argv[2]) as rfile:
        with codecs.open(sys.argv[3], "w", sys.argv[4]) as wfile:
            for line in rfile:
                wfile.write(line)
                print(line,end='')
except:
    print('File Convert Copy Failed!')
