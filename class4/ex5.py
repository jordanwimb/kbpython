#!/usr/bin/env python
from __future__ import print_function
from netmiko import ConnectHandler
import getpass
import time

pynet_rtr2 = {
    'device_type':'cisco_ios',
    'ip':'50.76.53.27',
    'username':'pyclass',
    'password':getpass.getpass(),
    'port':8022
}

def config_mode(device):
    #Enter config mode
    device.config_mode()
    time.sleep(2)
    #Verify status
    output = device.check_config_mode()
    time.sleep(2)
    if output == True:
        print("Entered config mode.")

def main():
    #Establish SSH connection
    rtr2 = ConnectHandler(**pynet_rtr2)
    #Enter config mode
    config_mode(rtr2)

if __name__ == '__main__':
    main()
