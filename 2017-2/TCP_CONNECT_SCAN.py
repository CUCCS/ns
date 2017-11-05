from scapy.all import *

dst_ip = "10.0.3.3"
src_port = RandShort()
dst_port = 80

tcp_resp = sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=10)
if(str(type(tcp_resp))=="<type 'NoneType'>"):
    print "Port 80 is filtered"

elif(tcp_resp.haslayer(TCP)):
    if(tcp_resp.getlayer(TCP).flags == 0x12):
        send_rst = sr(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="AR"),timeout=10)
        print "Port 80 is open"
    elif(tcp_resp.getlayer(TCP).flags == 0x14):
        print "Port 80 is closed"
