#!/usr/bin/env python
from snmp_helper import snmp_get_oid_v3, snmp_extract
import pygal
import time
#from sched import scheduler


input_oct = '1.3.6.1.2.1.2.2.1.10.5'
output_oct = '1.3.6.1.2.1.2.2.1.16.5'
input_ucast = '1.3.6.1.2.1.2.2.1.11.5'
output_ucast = '1.3.6.1.2.1.2.2.1.17.5'

fa4_in_octets = []
fa4_out_octets = []
fa4_in_packets = []
fa4_out_packets = []
fa4_in_bytes = []
fa4_out_bytes = []


def main():
    a_user = 'pysnmp'
    auth_key = 'galileo1'
    encrypt_key = 'galileo1'
    rtr_ip = '50.76.53.27'
    snmp_user = (a_user, auth_key, encrypt_key)
    pynet_rtr1 = (rtr_ip, 7961)
    router = pynet_rtr1

    fa4_in_octets,fa4_out_octets,fa4_in_packets,fa4_out_packets = get_intf_stats(router,snmp_user)
    fa4_in_bytes = get_count_values(fa4_in_octets)
    fa4_out_bytes = get_count_values(fa4_out_octets)
    fa4_in_packets = get_count_values(fa4_in_packets)
    fa4_out_packets = get_count_values(fa4_out_packets)
    gen_graph(fa4_in_bytes,fa4_out_bytes,"bytes-graph")
    gen_graph(fa4_in_packets,fa4_out_packets,"packets-graph")


def get_intf_stats(device,user):
    count = 0
    global fa4_in_octets,fa4_out_octets,fa4_in_packets,fa4_out_packets
    print("Gathering statistics.  Check back in 1 hour.")
    while count <= 12:
        fa4_in_oct_count = int(snmp_extract(snmp_get_oid_v3(device,user,oid=input_oct)))
        fa4_in_octets.append(fa4_in_oct_count)
        fa4_out_oct_count = int(snmp_extract(snmp_get_oid_v3(device,user,oid=output_oct)))
        fa4_out_octets.append(fa4_out_oct_count)
        fa4_in_count = int(snmp_extract(snmp_get_oid_v3(device,user,oid=input_ucast)))
        fa4_in_packets.append(fa4_in_count)
        fa4_out_count = int(snmp_extract(snmp_get_oid_v3(device,user,oid=output_ucast)))
        fa4_out_packets.append(fa4_out_count)
        count +=1
        time.sleep(10)
    print("Done.  Generating graph.")
    return(fa4_in_octets,fa4_out_octets,fa4_in_packets,fa4_out_packets)


def get_count_values(value_list):
    newlist = []
    count = 1
    count2 = 0
    while count <= 12:
        newlist.append(value_list[count] - value_list[count2])
        count += 1
        count2 += 1
    return(newlist)


def gen_graph(input_stats,output_stats,filename):
    line_chart = pygal.Line()
    line_chart.title = 'Input/Output Packets and Bytes'
    line_chart.x_labels = ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60']
    line_chart.add('InPackets', input_stats)
    line_chart.add('OutPackets', output_stats)
    line_chart.render_to_file(filename + '.svg')
    print("Graphing complete.")



if __name__ == "__main__":
    main()
