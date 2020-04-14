import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formatdate
import getpass

# メール送信パラメータ
date = formatdate()
encoding = 'utf-8'
subject = '件名:TestMail'
body = 'TestMail'
from_addr = None # 'from_user@gmail.com'
to_addrs =  None # 'to_user@gmail.com'

# メールサーバ設定情報
username = None # 'from_user@gmail.com'
passwd = None # 'from_user_password'
# Gmai SMTP
smtphost = 'smtp.gmail.com'
smtpport = 587 

# SMTPコネクションオブジェクトの変数
smtpcon = None

# メールサーバに接続して、ログインとメール送信
try:
    print('メール送信開始')

    # ユーザ名とパスワードの入力
    print('MailAccount: ',end=' ')
    username = input()
    passwd = getpass.getpass()

    # 送信者アドレスと受信者アドレスの入力
    from_addr = username
    print('宛先アドレス: ',end=' ')
    to_addrs = input()
    
    # 件名と本文の入力
    print('件名: ',end=' ')
    subject = input()
    print('メール本文: ',end=' ')
    body = input()

    # メールメッセージの組み立て
    msg = MIMEText(body, 'plain', encoding)
    msg['Subject'] = Header(subject, encoding)
    msg['From'] = from_addr
    msg['To'] = to_addrs
    msg['Date'] = date

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

    print('メール送信完了!')
except:
    # メール送信エラー時の対処
    try:
        smtpcon.close()
    except:
        pass
    print('メール送信エラー!?')
    