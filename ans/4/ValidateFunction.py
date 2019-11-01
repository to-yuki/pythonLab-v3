import sys

def checkInt(i):
    try:
        return int(i)
    except ValueError as e:
        print(e)
        exit(-1)
 
if len(sys.argv) == 3:
    result1 = checkInt(sys.argv[1])
    result2 = checkInt(sys.argv[2])
    print('sys.argv1 + sys.argv2 = ',(result1 + result2))
else:
    print('please input 2 number.')
