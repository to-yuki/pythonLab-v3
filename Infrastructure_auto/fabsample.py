# fabric3 is Pythoin3's fabric(Ver.1) compatible library
# pip uninstall fabric;pip intall fabric3

from fabric.api import run
from fabric.api import execute
from fabric.api import env
import sys

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
    run('ip addr show')
    response = run('exit 0',warn_only=True,quiet=False)
    #response = run('exit 1',warn_only=True,quiet=False) # command return code not 0 
    if not response.succeeded:
        raise RuntimeError("Oops! Command return code not 0 ")

def main():
    env.user = 'student'
    #env.password = 'student'
    #env.port = 22
    env.key_filename = ['id_rsa']
    try:
        execute(task, hosts=['student@192.168.19.128','student@192.168.19.129'])
    except RuntimeError as r:
        print()
        sys.stderr.write('Runtime Error!')
        sys.stderr.write(str(r.args))
    print('Done!')


if __name__ == '__main__':
    main()