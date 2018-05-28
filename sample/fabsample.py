# -*- coding: utf-8 -*-

from fabric.api import run
from fabric.api import execute
from fabric.api import env

def task():

    # HostCheck SSH-key Configuration
    #if env.host == '192.168.19.128':
    #    env.user = 'student'
    #    env.password = 'student'
    #    env.port = 22
    #    env.key_filename = 'id_rsa_192.168.19.128'

    print('---------------------------------------')
    print('Start SSH Session : ' + str(env.host))
    run('hostname')
    run('ip addr show ens33')
    run('exit 0')

def main():
    env.user = 'student'
    #env.password = 'student'
    #env.port = 22
    env.key_filename = ['id_rsa']
    execute(task, hosts=['student@192.168.19.128','student@192.168.19.129'])
    print('Done!')


if __name__ == '__main__':
    main()