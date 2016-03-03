#!/usr/bin/env python
from __future__ import print_function
import pyeapi

def get_show_intf(connection):
    intf = connection.enable("show interfaces")[0]
    interfaces = intf['result']['interfaces']
    return(interfaces)


def parse_intf_stats(interfaces):
    for key in interfaces.keys()[1:-1]:
        print(key)
        print("-" * 9)
        print("Input Octets: %d" % (interfaces[key]['interfaceCounters']['inOctets']))
        print("Output Octets: %d" % (interfaces[key]['interfaceCounters']['outOctets']))
        print("")

def main():
    print("\n***This example uses device pynet-sw2.\n")
    device_name = raw_input("Please enter device name: ")
    print("Collecting interface statistics...\n")
    pynet_sw2 = pyeapi.connect_to(device_name)
    parse_intf_stats(get_show_intf(pynet_sw2))

if __name__ == "__main__":
    main()
