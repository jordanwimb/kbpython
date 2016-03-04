#!/usr/bin/env python
from __future__ import print_function
import pyeapi
import argparse
import re


def get_config(connection):
    config = connection.get_config(as_string=True)
    return(config)

def check_vlan(config,vlan_id):
    pattern = 'vlan ' + vlan_id
    vlan_conf = re.search(r'\b%s\b' % pattern, config)
    if vlan_conf:
        status = True
    else:
        status = False
    return(status)

def create_vlan(connection,vlan_id,vlan_name):
    cmds = ["vlan %s" % vlan_id, "name %s" % vlan_name]
    connection.config(cmds)

def remove_vlan(connection,vlan_id,vlan_name):
    connection.config("no vlan %s" % vlan_id)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", type=str, default="")
    parser.add_argument("vlan", type=str)
    parser.add_argument("--remove", action="store_true", default=False)
    args = parser.parse_args()
    print("Checking for VLAN...")

    #print(args.name)
    #print(args.vlan)
    #print(args.remove)

    vlan_id = args.vlan
    vlan_name = args.name
    pynet_sw2 = pyeapi.connect_to('pynet-sw2')
    config = get_config(pynet_sw2)

    vlan_status = check_vlan(config,vlan_id)
    if args.remove == False:
        if vlan_status == False:
            print("VLAN does not exist...")
            create_vlan(pynet_sw2,vlan_id,vlan_name)
            print("\nVLAN has been created.")
        else:
            print("This VLAN is currently in use.")

    else:
        if vlan_status == False:
            print("No VLAN to remove.")
        else:
            remove_vlan(pynet_sw2,vlan_id,vlan_name)
            print("\nVLAN has been removed.")            

if __name__ == "__main__":
    main()


