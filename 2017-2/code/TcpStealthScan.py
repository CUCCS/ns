import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

dst_ip = "192.168.56.102"
src_port = RandShort()
dst_port = 80


resp = sr1( IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags='S'),iface='eth1',timeout=10,verbose=0)

if resp == None:
    print('Port %d Filtered' % dst_port)
elif resp.haslayer(TCP):
    if resp.getlayer(TCP).flags == 0x12: # ak
        sr( IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags='R'),timeout=10,verbose=0)
        print('Port %d Open' % dst_port)
    elif resp.getlayer(TCP).flags == 0x14: #rst
        print('Port %d Closed' % dst_port)

elif resp.haslayer(ICMP):
    if(int(resp.getlayer(ICMP).type)==3 and int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
        print ('Port %d Filtered' % dst_port)
