import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

dst_ip = '192.168.56.102'
src_port = RandShort()
dst_port = 80

resp = sr1( IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="FPU"),timeout=10 ,iface='eth1',verbose=0)

if resp == None:
    print('Port %d Open or Filtered' % dst_port)
elif resp.haslayer(TCP):
    if resp.getlayer(TCP).flags == 0x14:
        print('Port %d Closed' % dst_port)
elif resp.haslayer(ICMP):
    if int(resp.getlayer(ICMP).type) == 3 and int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]:
        print('Port %d Filtered' % dst_port)

