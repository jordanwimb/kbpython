#!/usr/bin/env python
from __future__ import print_function
import django
from net_system.models import NetworkDevice, Credentials

devices = NetworkDevice.objects.all()
creds = Credentials.objects.all()

def main():
    dev_name = raw_input("Enter device to delete or 'q' to quit: ")
    
    while not dev_name == 'q':
        dev = NetworkDevice.objects.get(device_name=dev_name)
        dev.delete()
        print("%s has been deleted." % dev_name)

    else:
        print("Quitting.")

if __name__ == '__main__':
    main()
