#! /usr/bin/python
from scapy.all import *

dst_ip = sys.argv[1] if len(sys.argv)>1 else "10.0.2.7"
src_port = RandShort()
dst_port=int(sys.argv[2]) if len(sys.argv)>2 else 80

stealth_scan_resp = sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=3,verbose=0)

if stealth_scan_resp==None:
    print('Port %d Filtered' % dst_port)
elif(stealth_scan_resp.haslayer(TCP)):
    if(stealth_scan_resp.getlayer(TCP).flags == 0x12):  #SYN/ACK
        send_rst = sr(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="R"),timeout=3,verbose=0)
        print('Port %d Open' % dst_port)
    elif (stealth_scan_resp.getlayer(TCP).flags == 0x14):   #RST
        print('Port %d Closed' % dst_port)