import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

dst_ip=sys.argv[1]if len(sys.argv)>1 else '10.0.2.4'
src_port=RandShort()
dst_port=int(sys.argv[2])if len(sys.argv)>2 else 80

tcp_scan_resp=sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=10,iface='eth0',verbose=0)

if tcp_scan_resp==None:
    print ('Port %d Filterd' % dst_port)
elif(tcp_scan_resp.haslayer(TCP)):
    if(tcp_scan_resp.getlayer(TCP).flags==0x12):
        tcp_resp_tmp=sr(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags='AR'),timeout=10,verbose=0)
        print ('Port %d Open' %dst_port)
    elif(tcp_scan_resp.getlayer(TCP).flags==0x14):
        print ('Port %d Closed' % dst_port)
