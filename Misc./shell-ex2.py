from snmp_helper import snmp_get_oid_v3, snmp_extract
import pygal
import time
from sched import scheduler


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


a_user = 'pysnmp'
auth_key = 'galileo1'
encrypt_key = 'galileo1'
rtr_ip = '50.76.53.27'
snmp_user = (a_user, auth_key, encrypt_key)
pynet_rtr1 = (rtr_ip, 7961)
router = pynet_rtr1

def get_intf_stats():
    count = 0
    global fa4_in_octets,fa4_out_octets,fa4_in_packets,fa4_out_packets
    print("Gathering statistics.  Check back in 1 hour.")
    while count < 6:
        fa4_in_oct_count = int(snmp_extract(snmp_get_oid_v3(router,snmp_user,oid=input_oct)))
        fa4_in_octets.append(fa4_in_oct_count)
        fa4_out_oct_count = int(snmp_extract(snmp_get_oid_v3(router,snmp_user,oid=output_oct)))
        fa4_out_octets.append(fa4_out_oct_count)
        fa4_in_count = int(snmp_extract(snmp_get_oid_v3(router,snmp_user,oid=input_ucast)))
        fa4_in_packets.append(fa4_in_count)
        fa4_out_count = int(snmp_extract(snmp_get_oid_v3(router,snmp_user,oid=output_ucast)))
        fa4_out_packets.append(fa4_out_count)
        count +=1
        time.sleep(10)
    print("Done.  Generating graph.")
    return(fa4_in_octets,fa4_out_octets,fa4_in_packets,fa4_out_packets)

def get_inout_bytes():
    global fa4_in_bytes, fa4_out_bytes
    fa4_in_bytes =  [fa4_in_octets[1]-fa4_in_octets[0],
                    fa4_in_octets[2]-fa4_in_octets[1],
                    fa4_in_octets[3]-fa4_in_octets[2],
                    fa4_in_octets[4]-fa4_in_octets[3],
                    fa4_in_octets[5]-fa4_in_octets[4]]
    fa4_out_bytes = [fa4_out_octets[1]-fa4_out_octets[0],
                    fa4_out_octets[2]-fa4_out_octets[1],
                    fa4_out_octets[3]-fa4_out_octets[2],
                    fa4_out_octets[4]-fa4_out_octets[3],
                    fa4_out_octets[5]-fa4_out_octets[4]]
    return(fa4_in_bytes,fa4_out_bytes)


def get_inout_packets():
    global fa4_in_packets, fa4_out_packets
    fa4_in_packets =  [fa4_in_packets[1]-fa4_in_packets[0],
                    fa4_in_packets[2]-fa4_in_packets[1],
                    fa4_in_packets[3]-fa4_in_packets[2],
                    fa4_in_packets[4]-fa4_in_packets[3],
                    fa4_in_packets[5]-fa4_in_packets[4]]
    fa4_out_packets = [fa4_out_packets[1]-fa4_out_packets[0],
                    fa4_out_packets[2]-fa4_out_packets[1],
                    fa4_out_packets[3]-fa4_out_packets[2],
                    fa4_out_packets[4]-fa4_out_packets[3],
                    fa4_out_packets[5]-fa4_out_packets[4]]
    return(fa4_in_packets,fa4_out_packets)


def gen_graph(input_stats,output_stats,filename):
    line_chart = pygal.Line()
    line_chart.title = 'Input/Output Packets and Bytes'
    line_chart.x_labels = ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60']
    line_chart.add('InPackets', input_stats)
    line_chart.add('OutPackets', output_stats)
    line_chart.render_to_file(filename + '.svg')


----------------
#Pulled from old program.

def get_inout_bytes():
    global fa4_in_bytes, fa4_out_bytes
    fa4_in_bytes =  [fa4_in_octets[1]-fa4_in_octets[0],
                    fa4_in_octets[2]-fa4_in_octets[1],
                    fa4_in_octets[3]-fa4_in_octets[2],
                    fa4_in_octets[4]-fa4_in_octets[3],
                    fa4_in_octets[5]-fa4_in_octets[4]]
    fa4_out_bytes = [fa4_out_octets[1]-fa4_out_octets[0],
                    fa4_out_octets[2]-fa4_out_octets[1],
                    fa4_out_octets[3]-fa4_out_octets[2],
                    fa4_out_octets[4]-fa4_out_octets[3],
                    fa4_out_octets[5]-fa4_out_octets[4]]
    print("Graphing bytes...")
    return(fa4_in_bytes,fa4_out_bytes)


def get_inout_packets():
    global fa4_in_packets, fa4_out_packets
    fa4_in_packets =  [fa4_in_packets[1]-fa4_in_packets[0],
                    fa4_in_packets[2]-fa4_in_packets[1],
                    fa4_in_packets[3]-fa4_in_packets[2],
                    fa4_in_packets[4]-fa4_in_packets[3],
                    fa4_in_packets[5]-fa4_in_packets[4]]
    fa4_out_packets = [fa4_out_packets[1]-fa4_out_packets[0],
                    fa4_out_packets[2]-fa4_out_packets[1],
                    fa4_out_packets[3]-fa4_out_packets[2],
                    fa4_out_packets[4]-fa4_out_packets[3],
                    fa4_out_packets[5]-fa4_out_packets[4]]
    print("Graphing packets...")
    return(fa4_in_packets,fa4_out_packets)


--------------------







get_intf_stats()
get_intf_bytes()

gen_graph(fa4_in_bytes,fa4_out_bytes,"bytes-graph")
gen_graph(fa4_in_packets,fa4_out_packets,"packets-graph")


fa4_in_octets
fa4_out_octets
fa4_in_packets
fa4_out_packets

fa4_in_bytes
fa4_out_bytes