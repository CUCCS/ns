#!/usr.bin/python

from scapy.all import*

dst_ip = sys.argv[1] if len(sys.argv) > 1 else '10.0.2.5'
src_port = RandShort()
dst_port = int(sys.argv[2]) if len(sys.argv) > 2 else 80

tcp_stealth_resp = sr1(IP(dst = dst_ip)/TCP(sport=src_port,dport = dst_port,flags='S'),timeout = 3,verbose=0)

if tcp_stealth_resp == None:
    print('Port %d Filtered' % dst_port)
elif tcp_stealth_resp.haslayer(TCP):
    if tcp_stealth_resp.getlayer(TCP).flags == 0x12:
        tcp_stealth_resp_tmp = sr(IP(dst = dst_ip)/TCP(sport=src_port,dport = dst_port,flags='R'),timeout = 3,verbose=0)
        print('Port %d Open' % dst_port)
    elif tcp_stealth_resp.getlayer(TCP).flags == 0x14:
        print('Port %d Closed' % dst_port)

