import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
 
dst_ip = "10.0.0.1"
src_port = RandShort()
dst_port=68
dst_timeout=10
  
def udp_scan(dst_ip,dst_port,dst_timeout):
    resp = sr1(IP(dst=dst_ip)/UDP(dport=dst_port),timeout=dst_timeout,iface='eth1',verbose=0)
    if resp == None:
        retrans = []
        for count in range(0,3):
            retrans.append(sr1(IP(dst=dst_ip)/UDP(dport=dst_port),timeout=dst_timeout,verbose=0))
        for item in retrans:
            if item != None:
                udp_scan(dst_ip,dst_port,dst_timeout)
        print ('Port %d Open or Filtered' % dst_port)
    elif resp.haslayer(UDP):
        print ('Port %d Open' % dst_port)
    elif resp.haslayer(ICMP):
        if int(resp.getlayer(ICMP).type)==3 and int(resp.getlayer(ICMP).code)==3:
            print ('Port %d Closed' % dst_port)
        elif int(resp.getlayer(ICMP).type)==3 and int(resp.getlayer(ICMP).code) in [1,2,9,10,13]:
            print ('Port %d Filtered' % dst_port)

udp_scan(dst_ip,dst_port,dst_timeout)
