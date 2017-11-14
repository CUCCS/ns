from scapy.all import *

dst_ip = sys.argv[1] if len(sys.argv) > 1 else '10.0.2.9'
src_port = RandShort()
dst_port = int(sys.argv[2]) if len(sys.argv) >2 else 68

def udp_scan(dst_ip,dst_port):
    udp_resp = sr1(IP(dst = dst_ip)/UDP(dport = dst_port),timeout = 3,verbose = 0)
    if udp_resp == None:
        retrans = []
        for count in range (0,3):
            retrans.append(sr1(IP(dst = dst_ip)/UDP(dport = dst_port),timeout = 3,verbose = 0))
        for item in retrans:
            if item != None:
                udp_scan(dst_ip,dst_port)
        print ('Port %d Open or Filter' % src_port)
    elif (udp_resp.haslayer(UDP)):
        print ('Port %d Open' % src_port)
    elif (udp_resp.haslayer(ICMP)):
        if(int(udp_resp.getlayer(ICMP).type)==3 and int(udp_resp.getlayer(ICMP).code)==3):
            print ('Port %d Closed' % src_port)
        elif(int(udp_resp.getlayer(ICMP).type)==3 and int(udp_resp.getlayer(ICMP).code)in [1,2,9,10,13]):
            print ('Port %d FIlter' % src_port)

udp_scan(dst_ip,dst_port)
