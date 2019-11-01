import json


# numberを入力させるメソッドを定義する
def number_input():
    print('背番号を入力してください。終了するには stop と入力してください > ',end='')
    no = input() # 標準入力を利用して、データを入力する
    return no

try:
    with open('memberlist.json', 'r') as j_file:
        j_dict = json.load(j_file) # json形式から辞書型に変換する
        members = j_dict['members']

        no = None
        while True: # stopと入力されるまで、同じ処理を繰り返す
            isFound = False
            no = number_input()
            if no == 'stop':
                break
            else:
                try:
                    no = int(no)
                except ValueError as e:
                    print('数値以外の値が入力されました。')
                    continue

            for member in members:
                if no == member['number']: # 入力された数値と一致する背番号のメンバーを探す
                    print('matched!')
                    print('----------------------------')
                    print('number :' , member['number'])
                    print('name :' , member['name'])
                    print('annual salary :' , member['annual salary'])
                    print('age :', member['age'])
                    print('height :' , member['height'])
                    print('weight :' , member['weight'])
                    print()
                    isFound = True
                    break

            if not isFound:
                print('該当する選手はいません。')
    print('検索を終了しました。')
except IOError as e:
    print('JSON file can not be loaded.')