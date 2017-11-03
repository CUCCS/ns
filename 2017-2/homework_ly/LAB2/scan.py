#scan.py
# -- coding: utf-8 --

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

dst_ip = sys.argv[1] if len( sys.argv )>1 else '10.0.2.4'
src_port = RandShort()
dst_port = int( sys.argv[2] ) if len( sys.argv )>2 else 80

def TCP_connect_scan(dst_ip,src_port,dst_port):
    tcp_resp=sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags='S'),timeout=3,iface='eth0',verbose=0)
    if tcp_resp==None:
        print('Port %d Filtered' % dst_port)
    elif tcp_resp.haslayer(TCP):
        if tcp_resp.getlayer(TCP).flags==0x12:
            tcp_resp_tmp = sr(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags='AR'),timeout=3,verbose=0)
            print('Port %d Open' % dst_port)
        elif tcp_resp.getlayer(TCP).flags==0x14:
            print('Port %d Closed' % dst_port)


def TCP_stealth_scan(dst_ip,src_port,dst_port):
    resp = sr1( IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags='S'),iface='eth0',timeout=3)
    if resp == None:
        print('Port %d Filtered' % dst_port)
    elif resp.haslayer(TCP):
        if resp.getlayer(TCP).flags == 0x12: # ak
            sr( IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags='R'),timeout=3,verbose=0)
            print('Port %d Open' % dst_port)
        elif resp.getlayer(TCP).flags == 0x14: #rst
            print('Port %d Close' % dst_port)
			
def TCP_XMAS_scan(dst_ip,src_port,dst_port):
    resp = sr1( IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="FPU"),timeout=3 ,iface='eth0',verbose=0)
    if resp == None:
        print('Port %d Open or Filtered' % dst_port)
    elif resp.haslayer(TCP):
        if resp.getlayer(TCP).flags == 0x14:
            print('Port %d Closed' % dst_port)
    elif resp.haslayer(ICMP):
        if int(resp.getlayer(ICMP).type) == 3 and int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]:
            print('Port %d Filtered' % dst_port)


def UDP_scan(dst_ip,src_port,dst_port):
    udp_resp=sr1(IP(dst=dst_ip)/UDP(dport=dst_port),timeout=3,verbose=0)
    if udp_resp==None:
        retrans=[]
        for count in range(0,3):
            retrans.append(sr1(IP(dst=dst_ip)/UDP(dport=dst_port),timeout=3,verbose=0))
        for item in retrans:
            if item!=None:
                udp_scan(dst_port,dst_ip)
        print('Port %d Opened or Filtered'%dst_port)
        return 'Opened or Filtered'
    elif udp_resp.haslayer(UDP):
        print('Port %d Opened'%dst_port)
        return 'Opened'
    elif udp_resp.haslayer(ICMP):
        if int(udp_resp.getlayer(ICMP).type)==3 and int(udp_resp.getlayer(ICMP).code) in [1,2,9,10,13]:
            print('Port %d Filtered'%dst_port)
            return 'Filtered'
        elif int(udp_resp.getlayer(ICMP).type)==3 and int(udp_resp.getlayer(ICMP).code)==3:
            print('Port %d Closed'%dst_port)


if __name__ == '__main__':

	
	print ("请输入扫描类型、IP地址及端口号")
	input=raw_input()
	while input!='exit':
		if input == '':
			print ("未输入任何信息")
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
				print ("请输入正确的扫描类型、IP地址及端口号")
				input=raw_input()
