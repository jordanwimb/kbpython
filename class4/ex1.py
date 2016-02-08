#!/usr/bin/env python
from __future__ import print_function
import paramiko
import getpass
import time

remote_conn_pre = paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def get_version(remote_conn):
    remote_conn.send("terminal length 0\n")
    time.sleep(1)
    remote_conn.send("show version\n")
    time.sleep(2)
    output = remote_conn.recv(1000)
    if remote_conn.recv_ready():
        output += remote_conn.recv(65535)
    print(output)

def main():
    #Establish SSH connection
    ip_address = '50.76.53.27'
    user = 'pyclass'
    password = getpass.getpass()
    port = 8022    
    remote_conn_pre.connect(ip_address,username=user,password=password,look_for_keys=False,allow_agent=False,port=port)
    remote_conn = remote_conn_pre.invoke_shell()

    #Collect running config
    get_version(remote_conn)


if __name__ == "__main__":
    main()
