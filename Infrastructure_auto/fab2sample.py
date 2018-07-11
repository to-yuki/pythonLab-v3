from fabric2 import Config # SSHコンフィグレーション
from fabric2 import Connection # コネクション
from fabric2 import ThreadingGroup # マルチスレッド実行
from fabric2 import SerialGroup # シングルスレッド実行
from invoke import task # @task annotation
from invoke import Responder 

#con = Connection("student@192.168.19.128", connect_kwargs = { "key_filename": "id_rsa"})
hosts=('192.168.19.128','192.168.19.129')
user='student'

# SingleThread Run
print('--- SingleThread Run ---')
for host in hosts:
  con = Connection(host,user=user,connect_kwargs = {"key_filename": "id_rsa"})
  print(con.host)
  con.run("hostname")
  con.close()  

print()

# MultiThread Run
print('--- MultiThread Run ---')
Config.ssh_config_path = "ssh_config" # SSH Config File 
grop = ThreadingGroup('192.168.19.128','192.168.19.129')
results = grop.run("hostname")

for connection, result in results.items():
    print(connection)
    print(result)
    #print("{0.host}: {1.stdout}".format(connection, result))

# Auto Input Response 
# sudopass = Responder(pattern=r'\[sudo\] password:',response='mypassword\n')
# c.run('sudo whoami', pty=True, watchers=[sudopass])
