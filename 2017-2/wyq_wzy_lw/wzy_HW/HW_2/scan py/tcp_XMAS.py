from scapy.all import *

dst_ip=sys.argv[1] if len(sys.argv)>1 else '192.168.56.102'
src_port=RandShort()
dst_port=int(sys.argv[2]) if len(sys.argv)>2 else 80

xmas_scan_resp=sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags='FPU'),timeout=3,verbose=0)

if xmas_scan_resp==None:
    print('Port %d Open' % dst_port)
elif xmas_scan_resp.haslayer(TCP):
    if xmas_scan_resp.getlayer(TCP)==0x14:
        print('Port %d Closed' % dst_port)
elif xmas_scan_resp.haslayer(ICMP):
    if int(xmas_scan_resp.getlayer(ICMP).type)==3 and int(xmas_scan_resp.getlayer(ICMP).code) in [1,2,3,9,10,13]:
        print('Port %d Filtered' % dst_port)
