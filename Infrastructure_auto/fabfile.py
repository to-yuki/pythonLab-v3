from fabric2 import Config # SSHコンフィグレーション
from fabric2 import Connection # コネクション
from fabric2 import ThreadingGroup # マルチスレッド実行
from fabric2 import SerialGroup # シングルスレッド実行
from invoke import task # @task annotation
import sys

# run > fab2 -H 192.168.19.128,192.168.19.129 hostnames
# run > fab2 -H 192.168.19.128,192.168.19.129 chpasswd --passwd newpasswd

Config.ssh_config_path = "ssh_config"

@task
def help(host):
    """ Helpの表示 """
    print("ツールの使い方")
    print("    fab2 -H hostname1,hostname2... taskNmae1 --taskOption1 ...")
    print("タスクリストの表示")
    print("    fab2 --list")

# ALL HOSTs RUN COMMAND
@task
def ahc(host,command,hide=False,hostNameShow=True):
    """ 指定されたコマンドを実行する fab2 Option --command 新規パスワード """
    if hostNameShow:
        print(host.host)
    return host.run(command, hide=hide).stdout.strip()

@task
def hostname(host,hide=False):
    """ 対象ホストのホスト名を取得する """
    #print(host.host)
    command = "hostname"
    return host.run(command, hide=hide).stdout.strip()

@task
def ip(host,hide=False):
    """ 対象ホストのIPを取得する """
    #print('Run Host Name/IP : ' + str(host.host))
    command = "ip addr"
    return host.run(command, hide=hide).stdout.strip()
    
@task
def disk_free(host,hide=False):
    """ 対象ホストのDisk使用率を取得する """
    result = host.run('uname -s', hide=hide)
    uname = result.stdout.strip()
    if 'Linux' in uname:
        command = "df -h"
        return host.run(command, hide=hide).stdout.strip()
    err = "No idea how to get disk space on {}!".format(uname)
    raise RuntimeError(err)

@task 
def chpasswd(host,passwd,hide=False):
    """ 対象ホストのパスワードを変更する fab2 Option --passwd 新規パスワード """
    #print(host.host)
    command = "echo 'root:" + passwd + "' | chpasswd"
    result = host.run(command, hide=hide)
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
            print()
            print('==============')
            print(ahc(con,"date",hide=True,hostNameShow=False))
            print(hostname(con,hide=True))
            print(ip(con,hide=True))
            print(disk_free(con,hide=True))
            print(chpasswd(con,"python",hide=True))
            con.close()
            
    except RuntimeError as r:
        sys.stderr.write('=== Runtime Error! ===')
        sys.stderr.write(str(r.args))
    print('ALL Done!')

if __name__ == '__main__':
    main()