import sys

def checkInt(i):
    try:
        return int(i)
    except ValueError as e:
        print(e)
        exit(-1)
 
try:
    result1 = checkInt(sys.argv[1])
    result2 = checkInt(sys.argv[2])
except IndexError as e:
        print(e)
        exit(-1)

print('sys.argv1 + sys.argv2 = ',(result1 + result2))
