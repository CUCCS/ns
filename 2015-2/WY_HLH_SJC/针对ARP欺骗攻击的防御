
#防御终端ARP缓存投毒者#


##第一种方案##
**适用于小型的局域网**

1. 终端采用静态IP地址的方式，使网络中每一台计算机的IP地址与硬件地址一一对应，不可更改
2. 配置静态ARP地址表，用手工的方法更新缓存记录，对MAC地址和IP地址进行绑定，使终端ARP缓存投毒无法进行
   - arp -s <网关IP> <网关MAC>
3. 使用ARP服务器，通过该服务器查找自己的ARP转换表来响应其他计算机的ARP请求包。但必须确保这台服务器不被攻击
4. 敏感数据加密后再传输并使用加密通信协议
 - 应用层（负载）加密
5. 分析本机接收到的所有ARP数据包，掌握网络动态，找出潜在的攻击者或中病毒的机器
6. 发现本机有对外攻击行为时，自动定位本机感染的恶意程序、病毒程序
7. 定期使用rarp请求来检查ARP响应的真实性

##第二种方案##
**适用于中大型的局域网**

1. 除了网关外，不响应其它机器发送的ARP请求包，达到隐身效果，减少受到攻击的几率
2. 在系统内核层拦截本机对外的ARP攻击数据包，以减少感染恶意程序后对外攻击给用户带来的麻烦
3. 主动与网关保持通讯，并通告网关正确的MAC地址，以保持网络畅通及通讯安全
4. 只绑定网关IP与MAC地址
   - arp -s <网关IP> <网关MAC>
5. 敏感数据加密后再传输并使用加密通信协议
 - 应用层（负载）加密
6. 分析本机接收到的所有ARP数据包，掌握网络动态，找出潜在的攻击者或中病毒的机器
7. 发现本机有对外攻击行为时，自动定位本机感染的恶意程序、病毒程序
8. 定期使用rarp请求来检查ARP响应的真实性
#防御交换机DoS攻击
1. 限制交换机单个物理端口可以动态绑定的MAC地址数量，或者，只允许指定的MAC地址或者指定数量的MAC地址访问某个端口

 - 配置安全端口
    
            -安全MAC地址最大数量限制   
            switchport port-security maximum value
            -违反规则后的处理模式的设置 
            switchport port-security violation {restrict|shutdown} 
            -指定安全的MAC地址
            switchport port-security mac-address mac_address 
            -启动sticky learning
            switchport port-security mac_address sticky

 - 设置端口安全老化
            
            switchport port-security [aging time aging_time | type {absolute|inactivity}]
2. ARP报文限速
   
    该技术可以防止设备因为处理大量ARP数据包，因负荷过重而无法处理而变成Hub模式。通过对每秒内交换机全局、VLAN、接口或源IP接收的ARP报文数量进行统计。若每秒收到的ARP报文数量超过设定值，则认为该交换机全局、VLAN、接口或源IP接收的ARP报文处于超速状态，即收到ARP报文攻击。此时，交换机应该丢弃超出阈值部分的ARP报文，从而避免大量的ARP报文攻击设备。
3. 划分VLAN
     
    VLAN的实际目标是在超出物理网络的基础上构建逻辑网络。在一个交换式网络环境下，我们已经隔离了网络流量。这种隔离不会扩展到广播域以外。在一个VLAN中，广播的流量将被限制在VLAN中。
   
    利用交换机的端口划分VLAN，是被设定的端口都在同一个广播域内。这样划分的VLAN也称为静态VLAN技术。它按照局域网中交换机端口来定义VLAN成员。VLAN从逻辑上把局域网交换机的端口划分开来，从而把终端系统划分为不同的部分，各部分相对独立，在功能上模拟了传统的局域网。
   
    通过划分VLAN，不仅能够减小广播风暴的危害，还能够阻止对攻击者对整个物理网络的嗅探。
#防御交换机投毒者

1. 交换机物理端口和MAC地址的静态绑定
   
    通过交换机上的绑定功能，可以对端口转发的报文进行过滤控制。当端口接收到报文后查找绑定表项，如果报文中的目的MAC地址与绑定表项中MAC地址相匹配，则端口转发该报文，否则丢弃处理。
            
        -若要将交换机的fastethernet1/1端口，与某计算机的MAC地址进行绑定
        -mac_address代表被绑定的计算机的MAC地址
        -相关命令
         configure terminal
         interface fastethernet1/1
         switchport port-security
         switchport port-security mac-address mac_address
         end
         copy running-config startup-config   
            
