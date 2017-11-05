from scapy.all import *

dst_ip = "10.0.3.3"
src_port = RandShort()
dst_port = 22

xmas_resp = sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="FPU"),timeout=10)
if(str(type(xmas_resp))=="<type 'NoneType'>"):
	print "Port 22 is open or filtered"
elif(xmas_resp.haslayer(TCP)):
	if(xmas_resp.getlayer(TCP).flags == 0x14):
		print "Port 22 is closed"
	elif(xmas_resp.haslayer(ICMP)):
		if(int(xmas_resp.getlayer(ICMP).type)==3 and int(xmas_resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
			print "Port 22 is filtered"
