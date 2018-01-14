#! /usr/bin/python

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

dst_ip = sys.argv[1] if len(sys.argv)>1 else '10.0.2.5'
src_port = RandShort()
dst_port=int(sys.argv[2]) if len(sys.argv)>2 else 80

xmas_scan_resp = sr1(IP(dst=dst_ip)/TCP(dport=dst_port,flags="FPU"),timeout=10)
if (str(type(xmas_scan_resp))=="<type 'NoneType'>"):
	print "Port %d Open or Filter"%dst_port
elif(xmas_scan_resp.haslayer(TCP)):
	if(xmas_scan_resp.getlayer(TCP).flags == 0x14):
		print "Port %d Closed"%dst_port
elif(xmas_scan_resp.haslayer(ICMP)):
	if(int(xmas_scan_resp.getlayer(ICMP).type)==3 and int(xmas_scan_resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
		print "Port %d Filter"%dst_port
