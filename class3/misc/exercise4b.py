#!/usr/bin/env python
from snmp_helper import snmp_extract,snmp_get_oid_v3

router_name = '1.3.6.1.2.1.1.5.0'
router_description = '1.3.6.1.2.1.1.1.0'
device_uptime = '1.3.6.1.2.1.1.3.0'
config_last_changed = '1.3.6.1.4.1.9.9.43.1.1.1.0'


def main():
    a_user = 'pysnmp'
    auth_key = 'galileo1'
    encrypt_key = 'galileo1'
    snmp_user = (a_user, auth_key, encrypt_key)

    hostname = raw_input("Please enter hostname: ")
    rtr_ip = '50.76.53.27'

    if hostname == "pynet-rtr1":
        snmp_port = 7961
    else:
        snmp_port = 8061

    router_info = (rtr_ip, snmp_port)
    device = (router_info) 
    rtr_name = snmp_get_oid_v3(device,snmp_user,oid=router_name)
    #rtr_uptime = snmp_get_oid(device,oid='1.3.6.1.2.1.1.3.0')
    name_output = snmp_extract(rtr_name)
    #desc_output = snmp_extract(rtr_desc)
    #change_out = snmp_extract(rtr_out)
    #sys_uptime = snmp_extract(rtr_uptime)
    print(name_output)

if __name__ == "__main__":
    main()
