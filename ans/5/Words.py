import sys

def main():

	lineCount=0
	wordCount=0

	with open(sys.argv[1]) as f:
		for line in f:
			lineCount += 1
			wordCount += len(line.split())

	print('LineCount:',end=' ')
	print(lineCount)
	print('WordCount:',end=' ')
	print(wordCount)

if __name__ == '__main__':
	main()
