#!/usr/bin/env python
from __future__ import print_function
import pexpect
import getpass
import time

def show_ip_int_brief(remote_conn):
    remote_conn.sendline('show ip int brief')
    remote_conn.expect('#')
    print(remote_conn.before)

def set_logging(remote_conn):
    remote_conn.sendline('config t')
    remote_conn.expect('#')

    remote_conn.sendline('logging buffered 20011')
    remote_conn.expect('#')
    print(remote_conn.before)
    
    remote_conn.sendline('exit')
    remote_conn.expect('#')

def verify_config(remote_conn):
    remote_conn.sendline('sh run | i logging')
    time.sleep(2)
    remote_conn.expect('#')
    print(remote_conn.before)

def main():
    #Establish SSH connection
    ip_address = '50.76.53.27'
    user = 'pyclass'
    password = getpass.getpass()
    port = 8022    
    passphrase = "Enter passphrase for key"
    
    remote_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(user,ip_address,port))
    remote_conn.timeout = 6
    remote_conn.expect(":")
    remote_conn.sendline()
    time.sleep(1)
    remote_conn.sendline()
    time.sleep(1)
    remote_conn.expect('ssword:')
    remote_conn.sendline(password)
    remote_conn.expect('#')
    print(remote_conn.before)
    
    #Send and verify commands
    set_logging(remote_conn)
    verify_config(remote_conn)

if __name__ == '__main__':
    main()
