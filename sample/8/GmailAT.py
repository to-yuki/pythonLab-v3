# GMail簡易送信モジュール
import gmail
import getpass

# Gmailアカウント情報
sendUsername = None #'from_user@gmail.com'
sendUserPassword = None #'from_user_password'

# メール送信パラメータ
subject = '件名'
toAddr = None #'to_user@gmail.com'
body = '本文'

# メールサーバに接続して、ログインとメール送信
try:
    print('メール送信開始')
    # ユーザ名とパスワードの入力
    print('MailAccount: ',end=' ')
    sendUsername = input()
    sendUserPassword = getpass.getpass()

    # 受信者アドレスの入力
    print('宛先アドレス: ',end=' ')
    toAddr = input()

    # 件名と本文の入力
    print('件名: ',end=' ')
    subject = input()
    print('メール本文: ',end=' ')
    body = input()

    # Gmailへのログインとメール送信
    client = gmail.GMail(sendUsername, sendUserPassword)
    message = gmail.Message(subject=subject,to=toAddr,text=body)
    client.send(message)
    client.close()
    print('メール送信完了!')
except:
    # メール送信エラー時の対処
    try:
        client.close()
    except:
        pass
    print('メール送信エラーです。')
    