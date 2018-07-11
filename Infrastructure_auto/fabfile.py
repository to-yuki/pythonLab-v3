from fabric2 import Config # SSHコンフィグレーション
from fabric2 import Connection # コネクション
from fabric2 import ThreadingGroup # マルチスレッド実行
from fabric2 import SerialGroup # シングルスレッド実行
from invoke import task # @task annotation
import sys

# run > fab2 -H 192.168.19.128,192.168.19.129 hostnames

Config.ssh_config_path = "ssh_config"
@task
def hostname(host):
    """ 対象ホストのホスト名を取得するサンプル """
    #print(host.host)
    command = "hostname"
    return host.run(command, hide=True).stdout.strip()

@task
def ip(host):
    """ 対象ホストのIPを取得するサンプル """
    #print('Run Host Name/IP : ' + str(host.host))
    command = "ip addr"
    return host.run(command, hide=True).stdout.strip()
    
@task
def disk_free(host):
    """ 対象ホストのDisk使用率を取得するサンプル """
    result = host.run('uname -s', hide=True)
    uname = result.stdout.strip()
    if 'Linux' in uname:
        #command = "df -h / | tail -n1 | awk '{print $5}'"
        command = "df -h"
        return host.run(command, hide=True).stdout.strip()
    err = "No idea how to get disk space on {}!".format(uname)
    raise RuntimeError(err)

@task 
def chpasswd(host,passwd):
    """ 対象ホストのパスワードを変更する """
    #print(host.host)
    command = "echo 'root:" + passwd + "' | chpasswd"
    result = host.run(command, hide=True)
    if result.exited != 0:
        err = "Password could not be changed!"
        raise RuntimeError(err)
    return "Password Changed!"

# All Task Run 
def main():
    hosts=['192.168.19.128','192.168.19.129']
    Config.ssh_config_path = "ssh_config" # SSH Config File 

    try:
        for host in hosts:
            con = Connection(host)
            # All Rask Run
            print('==============')
            print(hostname(con))
            print(ip(con))
            print(disk_free(con))
            print(chpasswd(con,"python"))
            
    except RuntimeError as r:
        sys.stderr.write('=== Runtime Error! ===')
        sys.stderr.write(str(r.args))
    print('ALL Done!')

if __name__ == '__main__':
    main()