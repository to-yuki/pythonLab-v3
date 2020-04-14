try:
	with open('test.txt','w') as wfile: # ファイルを開く(書き込み)
		wfile.write('Hello') #ファイルに書き込み
except IOError as e:
	print('FileProcessError')

try:
	with open('test.txt','r') as rfile: # ファイルを開く(読み込み)
		line = rfile.readline() # ファイルから一行読み込み
		print(line)
except IOError as e:
	print('FileProcessError')
