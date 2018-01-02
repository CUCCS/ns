## conn.log

ts: time &log
This is the time of the first packet.
第一个数据包的时间  （大小 怎么计算）

---

uid: string &log
A unique identifier of the connection.
connection标识

---

id: conn_id &log
The connection’s 4-tuple of endpoint addresses/ports.
connection四元组

---

proto: transport_proto &log
The transport layer protocol of the connection.
传输层协议

---

service: string &log &optional
An identification of an application protocol being sent over the connection.
服务  应用层协议
可选项

---

duration: interval &log &optional
How long the connection lasted. For 3-way or 4-way connection tear-downs, this will not include the final ACK.
connection持续了多长时间 3次握手开始4次握手结束 分割
可选项

---

orig_bytes: count &log &optional
The number of payload bytes the originator sent. For TCP this is taken from sequence numbers and might be inaccurate (e.g., due to large connections).
originator 发送的payload的大小 对于TCP协议 是通过序列号计算出来的 可能不准确
可选项

---

resp_bytes: count &log &optional

The number of payload bytes the responder sent. See orig_bytes.
responder 发送的payload的大小 
可选项

---

conn_state: string &log &optional
conn_state	Meaning
S0	Connection attempt seen, no reply.         

尝试连接 无响应

S1	Connection established, not terminated.    

连接已经开始，没有终止

SF	Normal establishment and termination. Note that this is the same symbol as for state S1. You can tell the two apart because for S1 there will not be any byte counts in the summary, while for SF there will be.

 正常的建立连接，结束连接  它和s1状态有相同的符号（??） 但是S1在summary里没有计数 但是它有？？

REJ	Connection attempt rejected.               

尝试连接拒绝    

S2	Connection established and close attempt by originator seen (but no reply from responder).   

建立连接 但是orignatr尝试终止连接，responder没有响应

S3	Connection established and close attempt by responder seen (but no reply from originator).  

 建立连接 但是responder尝试终止连接，orignatr没有响应

RSTO	Connection established, originator aborted (sent a RST).                                 

建立连接 orignator 放弃（RST）

RSTR	Responder sent a RST.                                                                    

Responder发送RST

RSTOS0	Originator sent a SYN followed by a RST, we never saw a SYN-ACK from the responder.      Originator 

发送 SYN RST responder没有SYN-ACK 

RSTRH	Responder sent a SYN ACK followed by a RST, we never saw a SYN from the (purported) originator.     

Responder发送SYN ACK RST 但是没有收到orignator的SYN

SH	Originator sent a SYN followed by a FIN, we never saw a SYN ACK from the responder (hence the connection was “half” open).   

Originator发送FIN SYN 从来没有看到来自于responder的SYN ACK

SHR	Responder sent a SYN ACK followed by a FIN, we never saw a SYN from the originator.          Responder SYN ACK FIN 

没有看到来自于originator的SYN

OTH	No SYN seen, just midstream traffic (a “partial connection” that was not later closed).      没有SYN

连接状态
可选项

---


local_orig: bool &log &optional                       
If the connection is originated locally, this value will be T. If it was originated remotely it will be F. In the case that the Site::local_nets variable is undefined, this field will be left empty at all times.
如果这个连接是本地发起，将会是T 如果是远程发起将会是F  如果bro设置中local_net没有设置 这一项将会永远是空的
可选项

---

local_resp: bool &log &optional
If the connection is responded to locally, this value will be T. If it was responded to remotely it will be F. In the case that the Site::local_nets variable is undefined, this field will be left empty at all times.
如果连接被本地响应 将会是T 如果是远程响应连接将会是F
可选项

---

missed_bytes: count &log &default = 0 &optional
Indicates the number of bytes missed in content gaps, which is representative of packet loss. A value other than zero will normally cause protocol analysis to fail but some analysis may have been completed prior to the packet loss.
遗失的字节 代表内容间隔（分片？）中遗失的字节  如果这个值不是0可能导致 一些协议解析失败 但是有些协议解析已经完成在丢包之前 
可选项

---

history: string &log &optional
Records the state history of connections as a string of letters. The meaning of those letters is:

记录连接的历史状态

Letter	Meaning    

s	a SYN w/o the ACK bit set       

h	a SYN+ACK (“handshake”)    

 SYN+ACK

a	a pure ACK                 

 ACK  

d	packet with payload (“data”)  

有负载

f	packet with FIN bit set        

FIN位已经设置

r	packet with RST bit set       

 RST位已经设置

c	packet with a bad checksum     

数据包校验失败

t	packet with retransmitted payload    

带有重传payload的数据包

i	inconsistent packet (e.g. FIN+RST bits set)    

不一致的数据包（例如，FIN+RST位都设置了）

q	multi-flag packet (SYN+FIN or SYN+RST bits set)   

多flag数据包 (SYN+FIN或者SYN+RST)

^	connection direction was flipped by Bro’s heuristic 

 ^数据包连接方向被bro翻转

If the event comes from the originator, the letter is in upper-case; if it comes from the responder, it’s in lower-case.

如果时间来自于发起者，字母大写，如果来自于响应方，字母小写

 Multiple packets of the same type will only be noted once (e.g. we only record one “d” in each direction, regardless of how many data packets were seen.)

 多个数据包有相同的类型将会只标记一次 例如我们仅仅会记录一个d在没有个方向 而不是有多少个传输数据的数据包就记录一个d

可选项

---

orig_pkts: count &log &optional
Number of packets that the originator sent. Only set if  use_conn_size_analyzer = T.
originator发送的数据包的个数  只有在 use_conn_size_analyzer = T是才会有这一项
可选项

---

orig_ip_bytes: count &log &optional
Number of IP level bytes that the originator sent (as seen on the wire, taken from the IP total_length header field). Only set if use_conn_size_analyzer = T.
originitor发送的数据包中的IP层的字节个数   来自于IP头 只有在 use_conn_size_analyzer = T是才会有这一项
可选项

---

resp_pkts: count &log &optional
Number of packets that the responder sent. Only set if  use_conn_size_analyzer = T.
responder发送的数据包的个数  只有在 use_conn_size_analyzer = T是才会有这一项
可选项

---

resp_ip_bytes: count &log &optional
Number of IP level bytes that the responder sent (as seen on the wire, taken from the IP total_length header field). Only set if use_conn_size_analyzer = T.
responder发送的数据包中的IP层的字节个数   来自于IP头 只有在 use_conn_size_analyzer = T是才会有这一项
可选项

---

tunnel_parents: set [string] &log

If this connection was over a tunnel, indicate the uid values for any encapsulating parent connections used over the lifetime of this inner connection.
如果连接是建立在隧道上的 代表每一个封装连接的隧道连接的uid

---

orig_l2_addr: string &log &optional

(present if policy/protocols/conn/mac-logging.bro is loaded)
Link-layer address of the originator, if available.
可选项
originator链路层地址
设置 policy/protocols/conn/mac-logging.bro

---

resp_l2_addr: string &log &optional

(present if policy/protocols/conn/mac-logging.bro is loaded)
Link-layer address of the responder, if available.
可选项
responder链路层地址
设置 policy/protocols/conn/mac-logging.bro

---

vlan: int &log &optional

(present if policy/protocols/conn/vlan-logging.bro is loaded)
The outer VLAN for this connection, if applicable.
可选项
设置policy/protocols/conn/vlan-logging.bro
连接的outer VLAN

---

inner_vlan: int &log &optional

(present if policy/protocols/conn/vlan-logging.bro is loaded)
The inner VLAN for this connection, if applicable.
可选项 连接的inner VLAN