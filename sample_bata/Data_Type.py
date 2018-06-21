# リストに使えるメソッド
l = [i for i in range(3,0,-1)] * 2 # 3から逆順に1までリストを作成し、2回繰り返し
print(l)

l.pop(1) # 前から2番目の要素が除かれる
print(l)

l.remove(1) # 指定した数値1が1つ除かれる
print(l)

while 3 in l: # 全部削除したいとき
    l.remove(3)
print(l)

del l[0]
print(l)

l.clear() # 要素を全部削除
print(l)

word = ["さい", "あいすくりーむ", "かいがら", "ななし", "たんばりん"]
word.sort(reverse = True) # 50音順（逆）にする
print(word)
#word.sort()　# 50音順にする
print(word)
word.sort(key=len) # 文字数順にする
print(word)

#tuple
t = (1, "Hello")
# t[1] = 2 #'tuple' object does not support item assignment
x , y = t # アンパック(listでも出来る)
# a, b, c = tap # ValueError: not enough values to unpack

# formatメソッドはPython2.6以降でしか使うことが出来ない
print("x = {}".format(x))# format()を利用すると、文字列に違う型の変数を組み込み可能となる
print("y = {}".format(y))
print("x + y = {1} + {0}".format(y, x)) 

print("{:*^10}".format("中央")) 
print("{:*>10}".format("右寄せ"))
print("{:*<10}".format("左寄せ"))

print(f"{x}　と　{y}") #別の書き方

# slice
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in list[::-1]:
    print(i, end = " ")
print()    
for i in list[4:-1:2]:
    print(i, end = " ")
print()
print("{0} と {1}　にわける".format(list[:4], list[4:]))
string = "わたしはです"
print(string[:4] + "日本人" + string[4:])

