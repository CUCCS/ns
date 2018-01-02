#! /usr/bin/python
from scapy.all import *

dst_ip = sys.argv[1] if len(sys.argv)>1 else "10.0.2.7"
src_port = RandShort()  #随机产生扫描机的端口号
dst_port=int(sys.argv[2]) if len(sys.argv)>2 else 80

tcs_pkt = sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=3,verbose=0)
#sr1(),在第三层发送数据包，有接收功能，但只接收第一个包。
#flag默认是SYN
tcs_resp=sr1

if resp==None:
    print('Port %d Filtered' % dst_port)
elif resp.haslayer(TCP):
    if resp.getlayer(TCP).flags == 0x12:    #SYN/ACK
        resp_tmp = sr(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="AR"),timeout=3,verbose=0) #ACK+RST
        print('Port %d Open' % dst_port)
    elif resp.getlayer(TCP).flags == 0x14:  #RST
        print('Port %d Closed' % dst_port)