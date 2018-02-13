from __future__ import with_statement
import sys

def main():

	lineCount=0
	wordCount=0

	with open(sys.argv[1]) as f:
		for line in f:
			lineCount += 1
			wordCount += len(line.split())
			#print line.split()

	print('LineCount:',end=' ')
	print(lineCount)
	print('WordCount:',end=' ')
	print(wordCount)

# -- Main function Define--#
if __name__ == '__main__':
	main()
