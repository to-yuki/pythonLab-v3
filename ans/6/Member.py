import json, sys
import pprint

try:
    j_file = open('member.json', 'r')
    member = json.load(j_file) # json形式から辞書型に変換する
    
    print('number :' , member['number'])
    print('name :' , member['name'])
    print('annual salary :' , member['annual salary'])
    print('age :', member['age'])
    print('height :' , member['height'])
    print('weight :' , member['weight'])

except:
    print('JSON file can not be loaded.')
    