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

device_list = [pynet_rtr1,pynet_rtr2]

def config_mode(device):
    #Enter config mode
    device.config_mode()
    time.sleep(2)
    #Verify status
    output = device.check_config_mode()
    time.sleep(2)
    if output == True:
        print("Entered config mode.")

def send_config(device,commands):
    for command in commands:
        output = device.send_config_set(commands)
        print(output)
    device.exit_config_mode()
    time.sleep(2)

def send_config_file(device,config_file):
    output = device.send_config_from_file(config_file)
    time.sleep(2)
    print(output)

def get_run_config(device):
    output = device.send_command('show run')
    print(output)


def main():
    config_file = 'config_commands.txt'
    #Establish SSH connection
    for device in device_list:
        router_conn = ConnectHandler(**device)
        #Execute commands
        send_config_file(router_conn,config_file)


if __name__ == '__main__':
    main()
