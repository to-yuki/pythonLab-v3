import json

try:
    # 読み込む JSON ファイル
    with open('python.json','r') as json_file:
        # JSON ファイルのロードと辞書型へ変換
        json_dict = json.load(json_file)
        print('python.json(辞書型) :' + str(json_dict))

        # name Key の値を取得
        objects = json_dict['list']
        for object in objects:
            print(object['name'])

        # 新しい要素の追加
        abc = {'kind': 'Language' ,'name': 'ABC','birthday': 1980}
        objects.append(abc)

        # 新規出力用の JSON ファイル
        with open('python2.json','w') as new_json_file:
            # 新しく追加された要素を新し JSON ファイルへダンプ
            json.dump(json_dict,new_json_file)
except IOError as e:
    print('JSONファイル処理エラー')
