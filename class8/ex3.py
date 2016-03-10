#!/usr/bin/env python
from __future__ import print_function
import django
from net_system.models import NetworkDevice, Credentials

devices = NetworkDevice.objects.all()
creds = Credentials.objects.all()

def main():
    router1 = NetworkDevice(device_name='router1',
                            device_type='juniper',
                            ip_address='1.1.1.1',
                            port='9999')
    router1.save()

    router2 = NetworkDevice.objects.get_or_create(device_name='router2',
                            device_type='arista_eos',
                            ip_address='1.1.1.2',
                            port='9999')

if __name__ == '__main__':
    main()
