with open('hello.txt') as f: # ファイルを開く(読み込み)
    for line in f: # ファイルから1行読み込み(行が無くなるまで)
        print(line,end='')
