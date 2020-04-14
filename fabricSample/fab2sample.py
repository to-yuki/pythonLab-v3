from fabric2 import Config # SSHコンフィグレーション
from fabric2 import Connection # コネクション
from fabric2 import ThreadingGroup # マルチスレッド実行
from fabric2 import SerialGroup # シングルスレッド実行
from invoke import task # @task annotation
from invoke import Responder 

#con = Connection('student@192.168.19.128', connect_kwargs = { 'key_filename': 'id_rsa'})
# SSH の設定ファイル指定
#
Config.ssh_config_path = 'ssh_config'

hosts=('192.168.19.128','192.168.19.129')

# SingleThread Run
print('--- SingleThread Run ---')
for host in hosts:
  con = Connection(host)
  print(con.host)
  con.run('hostname') 

# SingleThread Group Run
print('--- SingleThread Group Run ---')
result = SerialGroup('192.168.19.128','192.168.19.129').run('hostname')

# MultiThread Group Run
print('--- MultiThread Group Run ---')
result = ThreadingGroup('192.168.19.128','192.168.19.129').run('hostname')
