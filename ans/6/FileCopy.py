import sys

with open(sys.argv[1], 'r') as rfile:
    with open(sys.argv[2], 'w') as wfile:
        for line in rfile:
            wfile.write(line)
            print(line)