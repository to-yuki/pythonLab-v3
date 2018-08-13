import sys

with open(sys.argv[1], 'r') as file:
    count = 0
    for line in file:
        print(line,end='')
        count += 1
    print('行数：', end = ' ')
    print(count)