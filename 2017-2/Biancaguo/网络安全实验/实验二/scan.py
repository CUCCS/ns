#scan.py
# -- coding: utf-8 --

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
 
def TCP_connect_scan(dst_ip,src_port,dst_port):
	tcp_pkt=IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags='S')#'S':SYN,发送方请求建立连接
	tcp_resp = sr1(tcp_pkt,iface='eth1',timeout=3,verbose=0)#verbose=0:不打印反馈信息

	if tcp_resp==None:#无回应
		print('Port %d Filtered' % dst_port)
	elif tcp_resp.haslayer(TCP):#有回应
		if tcp_resp.getlayer(TCP).flags==0x12:#接收方回应为SYN/ACK
			tcp_pkt_tmp=IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags='AR')#'AR'：发送方将ACK和RST同时发送给接收方
			tcp_resp_tmp=sr(tcp_pkt_tmp,iface='eth1',timeout=3,verbose=0)
			print('Port %d Open' % dst_port)
		elif (tcp_resp.getlayer(TCP).flags == 0x14):#回应为RST
			print('Port %d Closed' % dst_port)
		
def TCP_stealth_scan(dst_ip,src_port,dst_port):
	steal_pkt=IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags='S')#'S':SYN,发送方请求建立连接
	steal_resp = sr1(steal_pkt,iface='eth1',timeout=3,verbose=0)

	if steal_resp==None:#无回应
		print('Port %d Filtered' % dst_port)
	elif steal_resp.haslayer(TCP):#有回应
		if steal_resp.getlayer(TCP).flags==0x12:#接收方回应为SYN/ACK
			steal_pkt_tmp=IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags='R')#'R'：发送方将RST发送给接收方
			steal_resp_tmp=sr(steal_pkt_tmp,timeout=3,verbose=0)
			print('Port %d Open' % dst_port)
		elif (steal_resp.getlayer(TCP).flags == 0x14):#接收方回应为RST
			print('Port %d Closed' % dst_port)
	elif steal_resp.haslayer(ICMP):
		if int(steal_resp.getlayer(ICMP).type)==3 and int(steal_resp.getlayer(ICMP).code) in [1,2,3,9,10,13]:#目的结点不可达
			print('Port %d Filtered' % dst_port)
			
def TCP_XMAS_scan(dst_ip,src_port,dst_port):
	xmas_pkt = IP(dst=dst_ip)/TCP(dport=dst_port,flags="FPU")#FIN - 结束; 结束会话；P : PUSH - 推送; 数据包立即发送；U : URG - 紧急
	xmas_resp = sr1(xmas_pkt,timeout=3,verbose=0)
	if xmas_resp==None:#无回应
		print('Port %d Filtered or Open' % dst_port)
	elif xmas_resp.haslayer(TCP):#有回应
		if (xmas_resp.getlayer(TCP).flags == 0x14):#RST
			print('Port %d Closed' % dst_port)
	elif xmas_resp.haslayer(ICMP):
		if(int(xmas_resp.getlayer(ICMP).type)==3 and int(xmas_resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):#目的结点不可达
			print('Port %d Filtered' % dst_port)
	
def UDP_scan(dst_ip,src_port,dst_port):
	udp_resp = sr1(IP(dst=dst_ip)/UDP(dport=dst_port),timeout=3,verbose=0,iface='eth1')
	print str(type(udp_resp))
	if udp_resp==None:
		retrans = []
		for count in range(0,3):
		   retrans.append(sr1(IP(dst=dst_ip)/UDP(dport=dst_port),timeout=3,verbose=0))
		for item in retrans:
		   if (item!=None):
			   UDP_scan(dst_ip,dst_port)
		print ('Port %d Filtered or Open' % dst_port)
	elif udp_resp.haslayer(UDP):
		print ('Port %d Open' % dst_port)
	elif udp_resp.haslayer(ICMP):
		if int(udp_resp.getlayer(ICMP).type)==3 and int(udp_resp.getlayer(ICMP).code)==3:
		    print ('Port %d Closed' % dst_port)
		elif int(udp_resp.getlayer(ICMP).type)==3 and int(udp_resp.getlayer(ICMP).code) in [1,2,9,10,13]:
			print ('Port %d Filtered' % dst_port)
			
def Help():
	print '''
		PORT SCAN 1.0
		Usage:[Scan Type][Destination Ip][Destination Port]
		Scan Type:
			Choose the scan type.
			tcs : TCP connect scan
			tss : TCP stealth scan
			txs : TCP XMAS scan
			us  : UDP scan
		Default:
			The default destination IP address is 127.0.0.1
			The default port is 80
		'''
		
if __name__ == '__main__':

	print '''
	-------------------------------------------------
	|                                               |
	|                                               |
	| 欢迎使用扫描工具PORT SCAN，需要帮助请输入help |
	|                                               |
	|                                               |
	-------------------------------------------------
	'''
	print ">> ",
	input=raw_input()
	while input!='exit':
		if input == 'help':
			Help()
		else:
			s2=['','','']
			s=input.split(' ')
			for i in range(len(s)):
				s2[i]=s[i]
			scan_type=s2[0]
			dst_ip=s2[1]
			dst_port=s2[2]
			
			dst_ip = dst_ip if dst_ip !='' else '127.0.0.1'
			src_port = RandShort()
			dst_port=int(dst_port) if dst_port!='' else 80
			
			if scan_type=='tcs':
				TCP_connect_scan(dst_ip,src_port,dst_port)
			elif scan_type=='tss':
				TCP_stealth_scan(dst_ip,src_port,dst_port)
			elif scan_type=='txs':
				TCP_XMAS_scan(dst_ip,src_port,dst_port)
			elif scan_type=='us':
				UDP_scan(dst_ip,src_port,dst_port)
			else:
				print "Please input the correct scan type.More information please input 'help'."
			
		print ">> ",
		input=raw_input()
