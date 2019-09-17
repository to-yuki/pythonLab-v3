import re

# 検査対象文字列
string = 'https://www.python.org/community/irc/'
# 正規表現文字列
reString = r'https://(.*)/(.*)/(.*)/'

# 正規表現文字列のコンパイル
pattern = re.compile(reString)

# 正規表現を使いマッチング
matched = pattern.match(string)

print(matched.group())
print(matched.group(0))
print(matched.group(1))
print(matched.group(2))
print(matched.group(3))



