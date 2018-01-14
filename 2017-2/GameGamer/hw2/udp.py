#! /usr/bin/python
 
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
 
dst_ip = sys.argv[1] if len(sys.argv)>1 else '10.0.2.5'
src_port = RandShort()
dst_port=dst_port=int(sys.argv[2]) if len(sys.argv)>2 else 80
dst_timeout=10
 
udp_scan_resp = sr1(IP(dst=dst_ip)/UDP(dport=dst_port),timeout=dst_timeout)

if udp_scan_resp==None:
	print "Port %d Open or Filter"%dst_port
elif(udp_scan_resp.haslayer(UDP)):
	print "Port %d Open"%dst_port
elif(udp_scan_resp.haslayer(ICMP)):
	if(int(udp_scan_resp.getlayer(ICMP).type)==3 and int(udp_scan_resp.getlayer(ICMP).code)==3):
		print "Port %d Closed"%dst_port
	elif(int(udp_scan_resp.getlayer(ICMP).type)==3 and int(udp_scan_resp.getlayer(ICMP).code) in [1,2,9,10,13]):
			print "Port %d Filter"%dst_port
