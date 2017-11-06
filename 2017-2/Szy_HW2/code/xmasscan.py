from scapy.all import *
dst_ip = "10.0.2.7"
src_port = RandShort()
dst_port=22
 
tcp_connect_scan_resp = sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="FPU"),timeout=10,iface='eth0',verbose=0)
if tcp_connect_scan_resp==None:
	print "Filter or Open"
elif tcp_connect_scan_resp.haslayer(ICMP):
	if (int(xmas_scan_resp.getlayer(ICMP).type)==3 and int(xmas_scan_resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
		print "Filiter"
elif tcp_connect_scan_resp.haslayer(TCP):
	if tcp_connect_scan_resp.getlayer(TCP).flags == 0x14:
		print "Closed"
 
