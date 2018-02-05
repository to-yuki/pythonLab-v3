# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.Utils import formatdate
import getpass

# メール送信パラメータ
date = formatdate()
encoding = u"utf-8"
subject = u"件名"
body = u"本文"
from_addr = None #u"from_user@gmail.com"
to_addrs =  None #u"to_user@gmail.com"

# メールサーバ設定情報
username = None #u"from_user@gmail.com"
passwd = None #u"from_user_password"
# Gmai SMTP
smtphost = u"smtp.gmail.com"
smtpport = 587 

# メールメッセージの組み立て
msg = MIMEText(body, u"plain", encoding)
msg[u"Subject"] = Header(subject, encoding)
msg[u"From"] = from_addr
msg[u"To"] = to_addrs
msg[u"Date"] = date

# SMTPコネクションオブジェクトの変数
smtpcon = None

# メールサーバに接続して、ログインとメール送信
try:
    print(u"メール送信開始")

    # ユーザ名とパスワードの入力
    print(u"MailAccount: "),
    username = raw_input()
    passwd = getpass.getpass()

    # 送信者アドレスと受信者アドレスの入力
    print(u"FromMailAddress: "),
    from_addr = raw_input()
    print(u"ToMailAddress: "),
    to_addrs = raw_input()

    # メールサーバと接続
    smtpcon = smtplib.SMTP(smtphost, smtpport)
    # HELOコマンド送信 
    smtpcon.ehlo()
    # TLSセッションに切り替え
    smtpcon.starttls()
    # HELOコマンド送信
    smtpcon.ehlo()
    # メールサーバへ認証情報の送信
    smtpcon.login(username,passwd)
    # メールデータの送信
    smtpcon.sendmail(from_addr,to_addrs,msg.as_string())
    # QUITコマンドの送信(接続の切断)
    smtpcon.close()

    print(u"メール送信完了!")
except:
    # メール送信エラー時の対処
    try:
        smtpcon.close()
    except:
        pass
    print(u"メール送信エラー!?")