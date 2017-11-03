#!/usr.bin/python

from scapy.all import*

dst_ip = sys.argv[1] if len(sys.argv) > 1 else '10.0.2.5'
src_port = RandShort()
dst_port = int(sys.argv[2]) if len(sys.argv) > 2 else 80

def UDP_scan(dst_ip,dst_port):
    tcp_UDP_resp = sr1(IP(dst = dst_ip)/UDP(sport=src_port,dport = dst_port),timeout = 3,verbose=0)
    if tcp_UDP_resp == None:
        retrans = []
        for count in range(0,3):
            retrans.append(sr1(IP(dst=dst_ip)/UDP(dport=dst_port),timeout=3,verbose=0))
        for item in retrans:
            if item == None:
               UDP_scan(dst_ip,dst_port)
        print('Port %d Open | Filtered' % dst_port)
    elif tcp_UDP_resp.haslayer(UDP):
      print('Port %d Open ' % dst_port)
    elif(tcp_UDP_resp.haslayer(ICMP)):
        if(int(tcp_UDP_resp.getlayer(ICMP).type)==3 and int(tcp_UDP_resp.getlayer(ICMP).code==3)):
            print('Port %d Closed' % dst_port)
        elif(int(tcp_UDP_resp.getlayer(ICMP).type)==3 and int(tcp_UDP_resp.getlayer(ICMP).code)in [1,2,3,9,10,13]):
            print('Port %d Filtered' % dst_port)



UDP_scan(dst_ip,dst_port)
