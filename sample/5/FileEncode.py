import sys,codecs

with codecs.open('JISfile.txt','w','ISO-2022-JP') as f:
    f.write('こんにちは') # ISO-2022-JP(JIS)で書き込む

with codecs.open('JISfile.txt','r','cp932') as f:
    print(f.readline()) # 文字エンコーディングが異なるため文字化け
