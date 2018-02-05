# -*- coding: UTF-8 -*-
import json

try:
    # 読み込む JSON ファイル
    json_file = open("python.json","r")
    # JSON ファイルのロードと辞書型へ変換
    json_dict = json.load(json_file)
    print(u"python.json(辞書型) :" + str(json_dict))

    # name Key の値を取得
    objects = json_dict["list"]
    for object in objects:
        print(object["name"])

    # 新しい要素の追加
    abc = {"kind": "Language" ,"name": "ABC","birthday": 1980}
    objects.append(abc)

    # 新規出力用の JSON ファイル
    new_json_file = open("python2.json","w")
    # 新しく追加された要素を新し JSON ファイルへダンプ
    json.dump(json_dict,new_json_file)

    # ファイルオブジェクトのクローズ処理
    json_file.close()
    new_json_file.close()
except:
    print("JSONファイル処理エラー")

