#! /usr/bin/python
 
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

dst_ip = "192.168.56.109"
src_port = RandShort()  
dst_port=80

stealth_scan_resp = sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=10)
if(str(type(stealth_scan_resp))=="<type 'NoneType'>"):
    print "Filtered"
elif(stealth_scan_resp.haslayer(TCP)):
	if(stealth_scan_resp.getlayer(TCP).flags == 0x12):
    		send_rst = sr(IP(dst=dst_ip)/TCP		(sport=src_port,dport=dst_port,flags="R"),timeout=10)
		print "Open"
	elif (stealth_scan_resp.getlayer(TCP).flags == 0x14):
		print "Closed"
elif(stealth_scan_resp.haslayer(ICMP)):
	if(int(stealth_scan_resp.getlayer(ICMP).type)==3 and int(stealth_scan_resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
    		print "Filtered"
 
