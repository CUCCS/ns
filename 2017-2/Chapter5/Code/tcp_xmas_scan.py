from scapy.all import *

dst_ip = sys.argv[1] if len(sys.argv)>1 else '10.0.4.36'
src_port = RandShort()
dst_port= sys.argv[2] if len(sys.argv)>2 else 22


resp = sr1( IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="FPU"),timeout=10 ,verbose=0)

if resp == None:
	print('Port %d Open or Filtered' % dst_port)
elif resp.haslayer(ICMP):
        if int(resp.getlayer(ICMP).type) == 3 and int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]:
            print('Port %d Filtered' % dst_port)
elif resp.haslayer(TCP):
    if resp.getlayer(TCP).flags == 0x14:
        print('Port %d Closed' % dst_port)


