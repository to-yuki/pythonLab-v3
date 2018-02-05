# -*- coding: UTF-8 -*-

# GMail簡易送信モジュール
import gmail
import getpass

# Gmailアカウント情報
sendUsername = None #u"from_user@gmail.com"
sendUserPassword = None #u"from_user_password"

# メール送信パラメータ
subject = u"件名"
toAddr = None #u"to_user@gmail.com"
body = u"本文"

# メールサーバに接続して、ログインとメール送信
try:
    print(u"メール送信開始")
    # ユーザ名とパスワードの入力
    print(u"MailAccount: "),
    sendUsername = raw_input()
    sendUserPassword = getpass.getpass()

    # 受信者アドレスの入力
    print(u"ToMailAddress: "),
    toAddr = raw_input()

    # Gmailへのログインとメール送信
    client = gmail.GMail(sendUsername, sendUserPassword)
    message = gmail.Message(subject=subject,to=toAddr,text=body)
    client.send(message)
    client.close()
    print(u"メール送信完了!")
except:
    # メール送信エラー時の対処
    try:
        client.close()
    except:
        pass
    print(u"メール送信エラーです。")
    