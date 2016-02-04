#!/usr/bin/env python
from snmp_helper import snmp_extract,snmp_get_oid_v3
import pickle

router_name = '1.3.6.1.2.1.1.5.0'
router_description = '1.3.6.1.2.1.1.1.0'
router_uptime = '1.3.6.1.2.1.1.3.0'
config_last_changed = '1.3.6.1.4.1.9.9.43.1.1.1.0'

device_file = 'device_info.pkl'

def main():
    a_user = 'pysnmp'
    auth_key = 'galileo1'
    encrypt_key = 'galileo1'
    rtr_ip = '50.76.53.27'
    snmp_user = (a_user, auth_key, encrypt_key)
    f = open(device_file, "rb")

    prev_rtr1_info = pickle.load(f)
    prev_rtr2_info = pickle.load(f)
    f.close()

    pynet_rtr1 = (rtr_ip, 7961)
    pynet_rtr2 = (rtr_ip, 8061)

    hostname = raw_input("Please enter the hostname: ")

    if hostname == "pynet-rtr1":
        router = pynet_rtr1
    elif hostname == "pynet-rtr2":
        router = pynet_rtr2

    rtr_name = snmp_get_oid_v3(router,snmp_user,oid=router_name)
    rtr_description = snmp_get_oid_v3(router,snmp_user,oid=router_description)
    rtr_uptime = snmp_get_oid_v3(router,snmp_user,oid=router_uptime)
    last_changed = snmp_get_oid_v3(router,snmp_user,oid=config_last_changed)

    name_output = snmp_extract(rtr_name)
    desc_output = snmp_extract(rtr_description)
    uptime_output = snmp_extract(rtr_uptime)
    changed_output = snmp_extract(last_changed)
    
    device_info = (name_output,desc_output,uptime_output,changed_output)
    
    if hostname == "pynet-rtr1":
        print(device_info[3], prev_rtr1_info[3])
        if device_info[3] > prev_rtr1_info[3]:
            f = open(device_file, "wb")
            pickle.dump(device_info,f)
            pickle.dump(prev_rtr2_info,f)
            f.close()
        else:
            print("No changes have been made to this device.")

    elif hostname == "pynet-rtr2":
        if device_info[3] > prev_rtr2_info[3]:
            print("Device configuration has been changed.")
            f = open(device_file, "wb")
            pickle.dump(prev_rtr1_info,f)
            pickle.dump(device_info,f)
            f.close()
        else:
            print("No changes have been made to this device.")

    f = open("device_info.pkl", "rb")

    prev_rtr1_info = pickle.load(f)
    prev_rtr2_info = pickle.load(f)
    f.close()

if __name__ == "__main__":
    main()

