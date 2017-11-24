
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
dst_ip="10.0.2.5"
src_port=RandShort()
dst_port=53
dst_timeout=10
def udp_scan(dst_ip,dst_port,dst_timeout):
    udp_resp=sr1(IP(dst=dst_ip)/UDP(dport=dst_port),timeout=dst_timeout)
    if(str(type(udp_resp))=="<type 'NoneType'>"):
        retrans=[]
        for count in range(0,3):
            retrans.append(sr1(IP(dst=dst_ip)/UDP(dport=dst_port),timeout=dst_timeout))
        for item in retrans:
              print(str(type(item)))
              if(str(type(item))!="<type 'NoneType'>"):
                udp_scan(dst_ip,dst_port,dst_timeout)
        print("world")     
        return "Open|Filtered"
    elif(udp_resp.haslayer(UDP)):
                return  "Open"
    elif(udp_resp.haslayer(ICMP)):
                if(int (udp_resp.getlayer(ICMP).type)==3 and int(udp_resp.getlayer(ICMP).code)==3):
                  return  "Closed"
                elif(int(udp_resp.getlayer(ICMP).type)==3 and int(udp_resp.getlayer(ICMP).code)in [1,2,9,10,13]):
                  return  "Filtered"


print(udp_scan(dst_ip,dst_port,dst_timeout))