from scapy.all import *

dst_ip = sys.argv[1] if len( sys.argv )>1 else '10.0.4.254'
src_port = RandShort()
dst_port = int( sys.argv[2] ) if len( sys.argv )>2 else 22
print('dst_ip = %s' % dst_ip)
print('src_port = %d' % src_port)
print('dst_port = %d' % dst_port)

resp = sr1( IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags='S'),iface='eth0',timeout=10)

if resp == None:
    print('Port %d Filtered' % dst_port)
elif resp.haslayer(TCP):
    if resp.getlayer(TCP).flags == 0x12: # ak
        sr( IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags='R'),timeout=10,verbose=0)
        print('Port %d Open' % dst_port)
    elif resp.getlayer(TCP).flags == 0x14: #rst
        print('Port %d Close' % dst_port)


