from scapy.all import *
dst_ip = '10.0.2.7'
src_port = RandShort()
dst_port = 68

resp = sr1( IP(dst=dst_ip)/UDP(sport=src_port,dport=dst_port),timeout=10,verbose=0)

if resp == None:
    print('Port %d Filtered or Open' % dst_port)
elif resp.haslayer(UDP):
    print('Port %d Open' % dst_port)
elif resp.haslayer(ICMP):
	if int(resp.getlayer(ICMP).type)==3 and int(resp.getlayer(ICMP).code)==3:
		print('Port %d Closed' % dst_port)
	if int(resp.getlayer(ICMP).type)==3 and int(resp.getlayer(ICMP).code) in [1,2,9,10,13]:
		print('Port %d Filtered' % dst_port)
