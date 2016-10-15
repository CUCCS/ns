#! /usr/bin/python
 
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
 
dst_ip = "192.168.56.109"
src_port = RandShort()
dst_port=69
dst_timeout=10
 
def udp_scan(dst_ip,dst_port,dst_timeout):
	udp_scan_resp = sr1(IP(dst=dst_ip)/UDP(dport=dst_port),timeout=dst_timeout)
	if (str(type(udp_scan_resp))=="<type 'NoneType'>"):
		retrans = []
		for count in range(0,3):
			retrans.append(sr1(IP(dst=dst_ip)/UDP(dport=dst_port),timeout=dst_timeout))
		for item in retrans:
			if (str(type(item))!="<type 'NoneType'>"):	
				udp_scan(dst_ip,dst_port,dst_timeout)
				print "Open|Filtered"
			elif (udp_scan_resp.haslayer(UDP)):
				print "Open"
			elif(udp_scan_resp.haslayer(ICMP)):
				if(int(udp_scan_resp.getlayer(ICMP).type)==3 and int(udp_scan_resp.getlayer(ICMP).code)==3):
						print "Closed"
				elif(int(udp_scan_resp.getlayer(ICMP).type)==3 and int(udp_scan_resp.getlayer(ICMP).code) in [1,2,9,10,13]):
						print "Filtered"

udp_scan(dst_ip,dst_port,dst_timeout)
