from fabric2 import Config # SSHコンフィグレーション
from fabric2 import Connection # コネクション
from fabric2 import ThreadingGroup # マルチスレッド実行
from fabric2 import SerialGroup # シングルスレッド実行
from invoke import task # @task annotation
import sys

# run > fab2 -H 192.168.19.128,192.168.19.129 hostnames

Config.ssh_config_path = "ssh_config"
@task
def hostnames(host):
    """ 対象ホストのホスト名を取得するサンプル """
    print(host.host)
    host.run("hostname")

@task
def ip(host):
    """ 対象ホストのIPを取得するサンプル """
    print('Run Host Name/IP : ' + str(host.host))
    host.run("ip addr")
    print()

# All Task Run 
def main():
    hosts=['192.168.19.128','192.168.19.129']
    Config.ssh_config_path = "ssh_config" # SSH Config File 

    try:
        for host in hosts:
            con = Connection(host)
            # All Rask Run
            hostnames(con)
            ip(con)

    except RuntimeError as r:
        print()
        sys.stderr.write('Runtime Error!')
        sys.stderr.write(str(r.args))
    print('Done!')

if __name__ == '__main__':
    main()