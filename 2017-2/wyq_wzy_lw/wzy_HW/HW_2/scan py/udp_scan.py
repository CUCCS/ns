from scapy.all import *

dst_ip=sys.argv[1] if len(sys.argv)>1 else '192.168.56.102'
src_port=RandShort()
dst_port=int(sys.argv[2]) if len(sys.argv)>2 else 80

udp_resp=sr1(IP(dst=dst_ip)/UDP(sport=src_port,dport=dst_port),timeout=3,verbose=0)

if udp_resp==None:
    retrans=[]
    for count in range(0,3):
        retrans.append(sr1=(IP(dst=dst_ip)/UDP(sport=src_port,dport=dst_port),timeout=3,verbose=0))
    for item in retrans:
        if(item!=None):
              udp_scan(dst_ip,dst_port)
    print('Port %d Open or Filtered' % dst_port)
elif udp_resp.haslayer(UDP):
    print('Port %d Open' % dst_port)
elif udp_resp.haslayer(ICMP):
    if int(udp_resp.getlayer(ICMP).type)==3 and int(udp_resp.getlayer(ICMP).code)==3:
        print('Port %d Closed' % dst_port)
    elif int(udp_resp.getlayer(ICMP).type)==3 and int(udp_resp.getlayer(ICMP).code)in[1,2,9,10,13]:
        print('Port %d Filtered'% dst_port)

