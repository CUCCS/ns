import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
dst_ip="10.0.2.5"
src_port=RandShort()
dst_port=80

stealth_resp=sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=10)
print (type(stealth_resp))
#print (stealth_resp.getlayer(TCP).flags)

if(str(type(stealth_resp))=="<type 'NoneType'>"):
    print ('Port %d Filtered' % dst_port)
elif(stealth_resp.haslayer(TCP)):
    if(stealth_resp.getlayer(TCP).flags==0x12):
        send_rst=sr(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="R"),timeout=10)
        print ('Port %d Open' % dst_port)
    elif(stealth_resp.getlayer(TCP).flags==0x14):
        print ('Port %d Closed' % dst_port)
    elif(stealth_resp.haslayer(ICMP)):
        if(int(stealth_resp.getlayer(ICMP).type)==3 and int(stealth_resp.getlayer(ICMP).code)in [1,2,3,9,10,13]):
            print ('Port %d Filtered' % dst_port)
