import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
dst_ip="10.0.2.4"
src_port=RandShort()
dst_port=80
tcp_resp=sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=10)
#print type(tcp_resp)
#print tcp_resp.getlayer(TCP).flags

if(str(type(tcp_resp))=="<type 'NoneType'>"):
  #  print "w"
    print "Closed"
elif(tcp_resp.haslayer(TCP)):
    if(tcp_resp.getlayer(TCP).flags==0x12):
        send_rst=sr(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="AR"),timeout=10)
    #    print "q"
        print "Open"

    elif(tcp_resp.getlayer(TCP).flags==0x14):
  #   print "r"
     print "Closed"

