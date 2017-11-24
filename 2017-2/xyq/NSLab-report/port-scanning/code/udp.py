#! /usr/bin/python

from scapy.all import *

dst_ip = sys.argv[1] if len(sys.argv)>1 else '10.0.2.15'
src_port = RandShort()
dst_port = int(sys.argv[2]) if len(sys.argv)>2 else 53
dst_timeout=10

udp_resp = sr1(IP(dst = dst_ip)/UDP(dport = dst_port),timeout =dst_timeout)
if udp_resp==None:
   retrans=[]
   for count in range(0,3):
       retrans.append(sr1(IP(dst=dst_ip)/UDP(dport=dst_port),timeout=dst_timeout))
   for i in retrans:
       if i !=None:
          UDP_resp(dst_ip,dst_port)
          print('Port %d Open | Filtered' % dst_port)
    
elif udp_resp.haslayer(UDP):
    print('Port %d Open' % dst_port)
elif (udp_resp.haslayer(ICMP)):
    if(int(udp_resp.getlayer(ICMP).type)==3 and int(udp_resp.getlayer(ICMP).code==3)):
        print('Port %d Closed' % dst_port)
    elif(int(udp_resp.getlayer(ICMP).type)==3 and int(udp_resp.getlayer(ICMP).code) in [1,2,9,10,13]):
        print('Port %d Filtered' % dst_port)







