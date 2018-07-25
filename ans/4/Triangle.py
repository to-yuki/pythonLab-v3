import sys

l = 0
i = 0
roop = int(sys.argv[1])

while l < roop:
    while i <= l:
        print('*', end = '')
        i += 1
    i = 0
    l += 1
    print('')