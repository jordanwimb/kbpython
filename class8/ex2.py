#!/usr/bin/env python
from __future__ import print_function
import django
from net_system.models import NetworkDevice, Credentials

devices = NetworkDevice.objects.all()
creds = Credentials.objects.all()

def main():
    for device in devices:
        if device.device_type == 'cisco':
            device.device_vendor = 'Cisco'
            print("Device %s set to %s" % (device.device_name, device.device_vendor))

        elif device.device_type == 'arista':
            device.device_vendor = 'Arista'
            print("Device %s set to %s" % (device.device_name, device.device_vendor))

        else:
            device.device_vendor = 'Juniper'
            print("Device %s set to %s" % (device.device_name, device.device_vendor))

        device.save()

if __name__ == '__main__':
    main()