# -*- encoding: UTF-8 -*-
# coding: UTF-8
from __future__ import with_statement
import sys,codecs

with codecs.open('cp932file.txt','w','Shift-JIS') as f:
    f.write('こんにちは')

print('こんにちは')
print(u'こんにちは') # Python2.x 系での出力方法

