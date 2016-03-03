#!/usr/bin/env python
from __future__ import print_function
import pyeapi

#interfaces.keys()
#[u'Management1', u'Ethernet2', u'Ethernet3', u'Ethernet1', u'Ethernet6', u'Ethernet7', u'Ethernet4', u'Ethernet5', u'Vlan1']

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
    print("This example uses device pynet-sw2.")
    print("")
    device_name = raw_input("Please enter device name: ")
    print("Collecting interface statistics...")
    pynet_sw2 = pyeapi.connect_to(device_name)
    parse_intf_stats(get_show_intf(pynet_sw2))

if __name__ == "__main__":
    main()