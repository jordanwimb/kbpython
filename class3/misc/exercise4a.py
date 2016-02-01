#!/usr/bin/env python
from snmp_helper import snmp_extract,snmp_get_oid

comm = "galileo"
router = raw_input("Which device?  rtr1 or rtr2? ")

def getSnmpInfo(router,comm):
    rtr_ip = '50.76.53.27'
    if router == "rtr1":
        snmp_port = 7961
    else:
        snmp_port = 8061

    device = (rtr_ip,comm,snmp_port) 
    rtr_name = snmp_get_oid(device,oid='.1.3.6.1.2.1.1.5.0',display_errors=True)
    rtr_desc = snmp_get_oid(device,oid='.1.3.6.1.2.1.1.1.0',display_errors=True)
    rtr_out = snmp_get_oid(device,oid='1.3.6.1.4.1.9.9.43.1.1.1.0',display_errors=True)
    rtr_uptime = snmp_get_oid(device,oid='1.3.6.1.2.1.1.3.0')
    name_output = snmp_extract(rtr_name)
    desc_output = snmp_extract(rtr_desc)
    change_out = snmp_extract(rtr_out)
    sys_uptime = snmp_extract(rtr_uptime)
    return(name_output,desc_output,change_out,sys_uptime)


snmp_info = getSnmpInfo(router,comm)
print("%s's name is: \n%s" % (router,snmp_info[0]))
print("")
print("%s's description: \n%s \n" % (router,snmp_info[1]))
print("Time since last change: " + snmp_info[2])
print("Device uptime: " + snmp_info[3])



