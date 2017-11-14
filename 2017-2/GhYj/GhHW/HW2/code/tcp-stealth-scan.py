from scapy.all import *

dst_ip = sys.argv[1] if len(sys.argv) > 1 else '10.0.2.9'
src_port = RandShort()
dst_port = int(sys.argv[2]) if len(sys.argv) >2 else 80

tcp_resp = sr1(IP(dst = dst_ip)/TCP(sport = src_port,dport = dst_port,flags='S'),timeout=3,verbose=0)

if tcp_resp == None:
    print('Port %d Filterd' % dst_port)
elif tcp_resp.haslayer(TCP):
    if tcp_resp.getlayer(TCP).flags == 0x12:
        tcp_resp_tmp=sr(IP(dst = dst_ip)/TCP(sport = src_port,dport = dst_port,flags = 'R'),timeout = 3)
        print('Port %d Open' % dst_port)
    elif tcp_resp.getlayer(TCP).flags == 0x14:
        print('Port %d Closed' % dst_port)
elif tcp_resp.haslayer(ICMP):
    if (int(tcp_resp.getlayer(ICMP).type) == 3 and int (tcp_resp.getlayer(ICMP).code)in [1,2,3,9,10,13]):
        print('Port %d Filter' % dst_port)
