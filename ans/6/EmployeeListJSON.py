import json, sys
import pprint

# numberを入力させるメソッドを定義する
def number_input():
    print('>>背番号を入力してください。終了するには stop と入力してください')
    no = input() # 標準入力を利用して、データを入力する
    return no

try:
    j_file = open('members.json', 'r')
    j_dict = json.load(j_file) # json形式から辞書型に変換する
    members = j_dict['members']
    #pprint.pprint(members) # pprint()を使用すると、辞書型データを整形して出力できる

    no = None
    while True: # stopと入力されるまで、同じ処理を繰り返す
        try:
            no = number_input()

            if no == 'stop':
                break
            else:
                no = int(no)

            for menber in members:
                if no == menber['number']: # 入力された数値と一致する背番号のメンバーを探す
                    #pprint.pprint(menber)
                    print('matched!')
                    print('----------------------------')
                    print('number :' , menber['number'])
                    print('name :' , menber['name'])
                    print('annual salary :' , menber['annual salary'])
                    print('age :', menber['age'])
                    print('height :' , menber['height'])
                    print('weight :' , menber['weight'])
                    print('')
                    break
            else:
                print('該当の番号はありません')
                print('')    
        except Exception as e:
            #print(e)
            print('該当の番号はありません')
            print('')
    print('検索を終了しました。')
except:
    print('JSON file can not be loaded.')