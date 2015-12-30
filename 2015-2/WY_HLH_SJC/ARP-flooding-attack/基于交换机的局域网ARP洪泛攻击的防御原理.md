# 基于交换机的局域网ARP洪泛攻击的防御原理
## ARP洪泛攻击的实现：  
由于ARP协议存在的漏洞，ARP包中所有字段都可以伪造。
ARP洪泛攻击持续把伪造的IP-MAC映射对发给受害主机，对于局域网内的所有主机和网关进行广播，抢占网络带宽和干扰正常通信。

![image](https://github.com/weiyi1024/github-tutorial/raw/master/ARP报文格式.jpg)  
图1.ARP报文格式	

ARP洪泛攻击的实质就是发生虚假ARP广播包。图1为ARP报文格式， ARP数据包就是按照这个格式来进行构造的。
虚假ARP广播包的构造如下:  
硬件类型指明发送方想知道的硬件接口类型。一般都是在以太网中，值为1;  
协议类型指明发送方提供的高层协议地址类型。对TCP/IP互联网，采用IP地址，值为十六机制的0806;  
操作指明ARP的操作类型，ARP请求为1 ,  ARP响应为2,  RARP请求为3 ,  RARP响应为4。洪泛发送ARP响应包，值为2;  
发送方硬件地址，即源MAC地址，值可以随意取，只要不是广播地址;  
发送方IP地址，即源IP地址，值为本局域网内任意一台主机的IP地址;  
目标硬件地址，即目的MAC地址，值为00-00-00-00-00-00(广播地址)，以此来实现广播;  
目标IP地址，即目的IP地址，值可以为任意IP地址。  
通过随机改变ARP数据包中源MAC地址和源IP地址，而达到洪泛攻击的目的。  
	
## 针对MAC洪泛攻击的防御
目前考虑的做法：  
对于ARP洪泛攻击，由于此种攻击会在网络中产生大量虚假的源MAC地址，因此可以采用配置交换机端口的安全策略来对其进行防御。
首先设置每个交换端口所允许通过的源MAC地址的阈值，接着把网络中所有交换机的安全策略配置成RestrictTrap模式。
当交换机某个端口产生安全违例时，将发送一个Trap包(Trap包中包含发送Trap包的交换机及其端口的信息)给管理系统。
管理系统实时监听网络数据，并捕获Trap包。由于交换机的MAC地址表是层层映射的。
所以，如果网络中有一台主机发出洪泛攻击，原则上网络中所有的交换机都将会发出Trap包。
当管理系统收到一系列Trap包后，将对这些Trap包进行分析，查找到产生安全违例的交换机端口。
通过查看该交换机端口是否连接的是一台主机，如果是一台主机，那么该台主机就是一个攻击源。
当管理系统定位攻击源后，会给用户发出警报，并关闭攻击源所连交换机的端口，使攻击源与网络进行隔离。
当攻击源主机恢复成正常主机后，再重新把它加入网络。
如图2所示，Manager为管理主机，Terminal为用户主机。
将图中所有交换机的安全策略配置成RestrictTrap模式，对交换机每个端口都进行如下配置:  
Switch(config一if)#switchport mode access  
Switch(config一if)#switchport port一security maximum 10  
Switch(config一if)#switchport port一security violation restrict  
Switch(config一if)#switchport port一security    
对于不断伪造IP-MAC地址映射对的泛洪攻击，当交换机存储的不同MAC地址数超过10个时产生安全违例，就认为发生了泛洪攻击，并发送Trap包。  
接着对交换机进行下面的配置:  
Switch(config)#snmp一server community access rw host 192.168.0.11  
Switch(config)#snmp一server host 192.168.0.11 traps version 2c access  
Switch(config)#snmp一server enable traps portsecurityviolate  
Switch(config)#end  

![image](https://github.com/weiyi1024/github-tutorial/raw/master/ARP攻击防御图1.jpg)  
图2. ARP攻击防御图

它的作用是使得交换机产生安全违例时将Trap包发送给管理主机(192.168.0.11)。当图中Terminal2发起ARP洪泛攻击时，会使得网络中产生大量虚假的MAC地址，使得图中3台交换机都产生安全违例，并向管理主机发送Trap包。当管理系统收到一系列Trap包后，将对这些Trap包进行分析，查找到产生安全违例的交换机端口。通过分析Switchl的某个端口连接的Terminal2是攻击源。管理系统定位攻击源Terminal2后，会给用户发出警报，并关闭Terminal2所连交换机的端口，使它与网络进行隔离。当Terminal2恢复成正常主机后，再重新把它加入网络。
