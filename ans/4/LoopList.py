import sys

# 
# 解答例は複数あります。
# 全て、リスト要素をループ処理で出力する方法です。
# 

# 解答例１ for構文１
print("for_1：")
for s in sys.argv:
    print(s)

# 解答例２ for構文2
print("")
print("for_2：")
for s in sys.argv:
    for t in s:
        print(t, end = "")
    print("")

# 解答例３ for構文3(補足)
print("")
print("for_3：")
for s in sys.argv:
    print(s, end = "")
print("")

# 解答例４ while構文1
print("")
print("while_1：")
i = 0
while i < len(sys.argv) :
    print(sys.argv[i])
    i += 1

# 解答例５ while構文2
print("")
print("while_2：")
i = 0
r = 0
while i < len(sys.argv) :
    while r < len(sys.argv[i]):
        print(sys.argv[i][r], end = "")
        r += 1
    i += 1
    r = 0
    print("")
