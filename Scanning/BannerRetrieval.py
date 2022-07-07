from platform import python_branch


#!/usr/bin/python

import socket

def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)

    except:
        return

def main():
    port = 22
    ip = "192.168.1.75"
    banner = retBanner(ip, port)
    if banner:
        print("[+] " + ip + ":" + banner)
    
main()
