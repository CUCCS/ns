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

def udp_scan(dst_port,dst_ip):
    udp_resp=sr1(IP(dst=dst_ip)/UDP(dport=dst_port),timeout=3,verbose=0)
    if udp_resp==None:
        retrans=[]
        for count in range(0,3):
            retrans.append(sr1(IP(dst=dst_ip)/UDP(dport=dst_port),timeout=3,verbose=0))
        for item in retrans:
            if item!=None:
                udp_scan(dst_port,dst_ip)
        print('Port %d Opened or Filtered'%dst_port)
        return 'Opened or Filtered'
    elif udp_resp.haslayer(UDP):
        print('Port %d Opened'%dst_port)
        return 'Opened'
    elif udp_resp.haslayer(ICMP):
        if int(udp_resp.getlayer(ICMP).type)==3 and int(udp_resp.getlayer(ICMP).code) in [1,2,9,10,13]:
            print('Port %d Filtered'%dst_port)
            return 'Filtered'
        elif int(udp_resp.getlayer(ICMP).type)==3 and int(udp_resp.getlayer(ICMP).code)==3:
            print('Port %d Closed'%dst_port)
            return 'Closed'

ret=udp_scan(dst_port,dst_ip)
                                                                 
