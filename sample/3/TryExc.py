import sys
try:
	print(sys.argv[1])
	print('ok!')
except:
	print('Error : args is Zero!')
finally:
	print('Post process')
print('Program-END')
