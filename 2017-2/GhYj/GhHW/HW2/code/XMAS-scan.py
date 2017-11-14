from scapy.all import *

dst_ip = sys.argv[1] if len(sys.argv) > 1 else '10.0.2.9'
src_port = RandShort()
dst_port = int(sys.argv[2]) if len(sys.argv) >2 else 80

xmas_resp = sr1(IP(dst = dst_ip)/TCP(sport = src_port,dport = dst_port,flags='FPU'),timeout = 3,verbose = 0)
if xmas_resp == None:
    print('Port %d Open or FIlterd' % dst_port)
elif xmas_resp.haslayer(TCP):
    if xmas_resp.getlayer(TCP).flags == 0x14:
        print('Port %d Closed' % dst_port)
elif xmas_scan.haslayer(ICMP):
    if (int(xmas_resp.getlayer(ICMP).type)==3 and int(xmas_resp.getlayer(ICMP).code)in [1,2,3,9,10,13]):
        print('Port %d FIlterd' % dst_port)
