#!/usr/bin/env python

from telnetlib import Telnet
import getpass
import time

username = 'pyclass'
password = getpass.getpass()
host = '50.76.53.27'

def getIpInterfaces(host,user,password):
    timeout = 6
    port = 23
    remote_conn = Telnet(host,port,timeout)
    remote_conn.read_until(b"sername:")
    remote_conn.write(username.encode('ascii') + b"\n")
    remote_conn.read_until(b"assword:")
    remote_conn.write(password.encode('ascii') + b"\n")
    remote_conn.write(b"show ip int brief" + b"\n")
    time.sleep(2)
    output = remote_conn.read_very_eager()
    remote_conn.close()
    print(output.decode() + "\n")

getIpInterfaces(host,username,password)

