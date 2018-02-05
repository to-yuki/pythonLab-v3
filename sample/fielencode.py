# -*- encoding: UTF-8 -*-
# coding: utf-8
from __future__ import with_statement
import sys,codecs

with codecs.open('cp932file.txt','w','cp932') as f:
    f.write(u'こんにちは')

print 'こんにちは '
print u'こんにちは '

print u'こんにちは '.encode('cp932')
