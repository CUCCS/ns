from scapy.all import *

dst_ip = "10.0.3.3"
src_port = RandShort()
dst_port = 22

stealth_resp = sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=10)
if(str(type(stealth_resp))=="<type 'NoneType'>"):
	print "Port 22 is filtered"
elif(stealth_resp.haslayer(TCP)):
	if(stealth_resp.getlayer(TCP).flags == 0x12):#ack
		sr(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="R"),timeout=10)
		print "Port 22 is open"
	elif(stealth_resp.getlayer(TCP).flags == 0x14):#rst
		print "Port 22 is closed"
