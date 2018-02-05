try:
	wfile = open('test.txt','w')
	wfile.write('Hello')
	wfile.flush()
except:
	print('FileProcessError')	
finally:
	wfile.close()


try:
	rfile = open('test.txt','r')
	line = rfile.readline()
	print(line)
except:
	
	print('FileProcessError')
finally:
	rfile.close()

