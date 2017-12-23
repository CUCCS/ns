#! /usr/bin/python

from scapy.all import *

if len(sys.argv)>1:
    dst_ip=sys.argv[1]
else:
    dst_ip='192.168.10.9'

src_port=RandShort()

if len(sys.argv)>2:
    dst_port=int(sys.argv[2])
else:
    dst_port=80

tcp_resp=sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags='S'),timeout=3,verbose=0)

if tcp_resp==None:
    print('Port %d Filtered'%dst_port)
elif tcp_resp.haslayer(TCP):
    if tcp_resp.getlayer(TCP).flags==0X12:
        tcp_resp_tmp=sr(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags='R'),timeout=3,verbose=0)
        print('Port %d Opened'%dst_port)
    elif tcp_resp.getlayer(TCP).flags==0x14:
        print('Port %d Closed'%dst_port)
elif tcp_resp.haslayer(ICMP):
    if int(tcp_resp.getlayer(ICMP).type)==3 and int(tcp_resp.getlayer(ICMP).code) in [1,2,3,9,10,13]:
        print('Port %d Filtered'%dst_port)
