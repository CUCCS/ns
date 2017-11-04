import logging 
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

dst_ip=sys.argv[1] if len(sys.argv)>1 else '10.0.2.4'
src_port=RandShort()
dst_port=int(sys.argv[2]) if len(sys.argv)>2 else 68
dst_timeout=10

def udp_scan(dst_ip,dst_port,dst_timeout):
    udp_scan_resp=sr1(IP(dst=dst_ip)/UDP(dport=dst_port),timeout=dst_timeout,verbose=0,iface='eth0')

    if udp_scan_resp==None:
        retrans = []
        for count in range(0,3):
            retrans.append(sr1(IP(dst=dst_ip)/UDP(dport=dst_port),timeout=dst_timeout,verbose=0))
        for item in retrans:
            print(str(type(item)))
            if(item!=None):
                udp_scan(dst_ip,dst_port)
        print ('Port %d Open|Filtered' % dst_port)
    elif udp_scan_resp.haslayer(UDP):
        print ('Port %d Open' % dst_port)
    elif(udp_scan_resp.haslayer(ICMP)):
        if(int(udp_scan_resp.getlayer(ICMP).type)==3 and int(udp_scan_resp.getlayer(ICMP).code)==3):
            print ('Port %d Closed' % dst_port)
        elif(int(udp_scan_resp.getlayer(ICMP).tyep)==e and int(udp_scan_resp.getlayer(ICMP).code) in [1,2,9,10,13]):
            print ('Port %d Filtered' % dst_port)

print(udp_scan(dst_ip,dst_port,dst_timeout))



