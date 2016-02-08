#!/usr/bin/env python
from __future__ import print_function
from netmiko import ConnectHandler
import getpass
import time

pynet_rtr1 = {
    'device_type':'cisco_ios',
    'ip':'50.76.53.27',
    'username':'pyclass',
    'password':'88newclass',
    'port':22
}

pynet_rtr2 = {
    'device_type':'cisco_ios',
    'ip':'50.76.53.27',
    'username':'pyclass',
    'password':'88newclass',
    'port':8022
}

srx = {
    'device_type':'juniper',
    'ip':'50.76.53.27',
    'username':'pyclass',
    'password':'88newclass',
    'port':9822
}

device_list = [pynet_rtr1, pynet_rtr2, srx]

def show_arp(connect,ip,port):
    #show arp on device
    output = connect.send_command('show arp')
    time.sleep(2)
    print("%s : %s - show ARP" % (ip,port))
    print(output)
    print('')

def main():
    #Establish SSH connection
    for device in device_list:
        router_conn = ConnectHandler(**device)
        show_arp(router_conn,device['ip'],device['port'])


if __name__ == '__main__':
    main()
