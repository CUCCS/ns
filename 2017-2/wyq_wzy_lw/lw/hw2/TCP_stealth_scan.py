import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

dst_ip=sys.argv[1] if len(sys.argv)>1 else '10.0.2.4'
src_port=RandShort()
dst_port=int(sys.argv[2])if len(sys.argv)>2 else 22

stealth_scan_resp=sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="S"),iface='eth0',timeout=10,verbose=0)
#print (type(stealth_scan_resp))

if stealth_scan_resp==None:
    print ('Port %d Filtered' % dst_port)
elif(stealth_scan_resp.haslayer(TCP)):
    if(stealth_scan_resp.getlayer(TCP).flags==0x12):
        sr(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="R"),timeout=10,verbose=0)
        print ('Port %d Open' % dst_port)
    elif(stealth_scan_resp.getlayer(TCP).flags==0x14):
        print ('Port %d Closed' % dst_port)
elif(stealth_scan_resp.haslayer(ICMP)):
    if(int(stealth_scan_resp.getlayer(ICMP).type)==3 and int(stealth_scan_resp.getlayer(ICMP).code)in [1,2,3,9,10,13]):
        print('Port %d Filtered' % dst_port)


