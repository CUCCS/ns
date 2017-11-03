#! /usr/bin/python

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

dst_ip=sys.argv[1] if len(sys.argv)>1 else '10.0.2.11'
src_port =RandShort()
dst_port=int (sys.argv[2]) if len(sys.argv)>2 else 80

tcp_connect_scan_resp = sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=10)
if(str(type(tcp_connect_scan_resp))=="<type 'NoneType'>"):
    print('Port %d Filtered' % dst_port)
elif(tcp_connect_scan_resp.haslayer(TCP)):
    if(tcp_connect_scan_resp.getlayer(TCP).flags == 0x12):
        send_rst = sr(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="AR"),timeout=10)
        print('Port %d Open' % dst_port)
    elif (tcp_connect_scan_resp.getlayer(TCP).flags == 0x14):
        print('Port %d Closed' % dst_port) 
