import json
try:
    with open('member.json', 'r') as j_file:
        member = json.load(j_file) # json形式から辞書型に変換する
    
        print('number :' , member['number'])
        print('name :' , member['name'])
        print('annual salary :' , member['annual salary'])
        print('age :', member['age'])
        print('height :' , member['height'])
        print('weight :' , member['weight'])

except IOError as e:
    print('JSON file can not be loaded.')
    