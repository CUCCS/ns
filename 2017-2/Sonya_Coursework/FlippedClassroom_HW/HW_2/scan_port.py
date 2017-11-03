#! /usr/bin/python
 
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
 

 #udp_scan
def udp_scan(dst_ip,dst_port,flag):
	dst_timeout =3
	udp_scan_resp = sr1(IP(dst=dst_ip)/UDP(dport=dst_port),timeout=dst_timeout,verbose=0)
	if (str(type(udp_scan_resp))=="<type 'NoneType'>"):
		retrans = []
		for count in range(0,3):
			retrans.append(sr1(IP(dst=dst_ip)/UDP(dport=dst_port),timeout=dst_timeout,verbose=0))
		for item in retrans:
			if (str(type(item)) != "<type 'NoneType'>"):
				udp_scan(dst_ip,dst_port,dst_timeout)
				return 
		print "Port %d Open|Filtered"%dst_port
	elif(udp_scan_resp.haslayer(UDP)):
		print "Port %d Open"%dst_port
	elif(udp_scan_resp.haslayer(ICMP)):
		if(int(udp_scan_resp.getlayer(ICMP).type)==3 and int(udp_scan_resp.getlayer(ICMP).code)==3):
			if flag == 2:
				print "Port %d Closed"%dst_port
		elif(int(udp_scan_resp.getlayer(ICMP).type)==3 and int(udp_scan_resp.getlayer(ICMP).code) in [1,2,9,10,13]):
				print "Port %d Filtered"%dst_port
 
#tcp connect scan
def  tcp_con_scan(dst_ip,dst_port,flag):
	tcp_connect_scan_resp = sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=10,verbose=0)
	if(str(type(tcp_connect_scan_resp))=="<type 'NoneType'>"):
		if flag == 2:
			print "port %d Filter"%dst_port
	elif(tcp_connect_scan_resp.haslayer(TCP)):
		if(tcp_connect_scan_resp.getlayer(TCP).flags == 0x12):
			send_rst = sr(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="AR"),timeout=10,verbose=0)
			print "port %d Open"%dst_port
		elif (tcp_connect_scan_resp.getlayer(TCP).flags == 0x14):
			if flag == 2:
				print "port %d Closed"%dst_port

#tcp stealh scan
def tcp_stea_scan(dst_ip,dst_port,flag):
	stealth_scan_resp = sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=10,verbose =0)
	if(str(type(stealth_scan_resp))=="<type 'NoneType'>"):
		if flag == 2:
			print "port %d Filter"%dst_port
	elif(stealth_scan_resp.haslayer(TCP)):
		if(stealth_scan_resp.getlayer(TCP).flags == 0x12):
			send_rst = sr(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="R"),timeout=10,verbose=0)
			print "port %d Open"%dst_port
		elif (stealth_scan_resp.getlayer(TCP).flags == 0x14):
			if flag == 2:
				print "port %d Close"%dst_port
		elif(stealth_scan_resp.haslayer(ICMP)):
			if(int(stealth_scan_resp.getlayer(ICMP).type)==3 and int(stealth_scan_resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
				print "port %d Filtered"%dst_port	
# TCP Xmas scan
def tcp_xmas_scan(dst_ip,dst_port,flag):

	xmas_scan_resp = sr1(IP(dst=dst_ip)/TCP(dport=dst_port,flags="FPU"),timeout=10,verbose=0)
	if (str(type(xmas_scan_resp))=="<type 'NoneType'>"):
		print "Port %d Open or Filtered"%dst_port
	elif(xmas_scan_resp.haslayer(TCP)):
		if(xmas_scan_resp.getlayer(TCP).flags == 0x14):
			if flag == 2:
				print "Port %d Closed"%dst_port
		elif(xmas_scan_resp.haslayer(ICMP)):
			if(int(xmas_scan_resp.getlayer(ICMP).type)==3 and int(xmas_scan_resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
				print "Port %d Filtered"%dst_port	

def select_scan_type(dst_ip,i,flag,scan_type):
	if scan_type == 1:
		tcp_con_scan(dst_ip,i,flag)
	elif scan_type == 2:
		tcp_stea_scan(dst_ip,i,flag)
	elif scan_type == 3:
		tcp_xmas_scan(dst_ip,i,flag)
	elif scan_type == 4:
		udp_scan(dst_ip,i,flag)

def help():
	print '''
		three params:
		scan type  [Required]  
				'1' : TCP connect scan
				'2' : TCP stealth scan
				'3' : TCP XMAS scan
				'4' : UDP scan
		destination ip [Required]   eg: 10.0.0.1
		destination port [Optional]   default:scan all ports 
	'''
if __name__ == '__main__':
	if sys.argv[1]=='--help':
		help()
	else:
		flag_all = 0
		scan_type = int(sys.argv[1])
		dst_ip = sys.argv[2]
		src_port = RandShort()
		dst_port = 'all'
		if len(sys.argv) == 4:
			dst_port=int(sys.argv[3])
		if dst_port == 'all':
			print "This is a test case, so we just test port 20-88 (output only filtered or open)"
			flag = 1
			for i in range(20,89):
				select_scan_type(dst_ip,i,1,scan_type)
		else:
			select_scan_type(dst_ip,dst_port,2,scan_type)
