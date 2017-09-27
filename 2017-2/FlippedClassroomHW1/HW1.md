#实验一实验报告#

##实验要求
* 基于VirtualBox的网络攻防基础环境搭建实例讲解
    * 节点：靶机、网关、攻击者主机
    * 连通性
        * 靶机可以直接访问攻击者主机
        * 攻击者主机无法直接访问靶机
        * 网关可以直接访问攻击者主机和靶机
        * 靶机的所有对外上下行流量必须经过网关
        * 所有节点均可以访问互联网
    * 其他要求
        * 所有节点制作成基础镜像（多重加载的虚拟硬盘）

##实验完成情况
* 实验完成度为100%
* 靶机（kaliVictim)  
靶机设置一个网卡，连接方式为内部网络，如下图所示。  
![](https://github.com/ghan3/ns/blob/master/2017-2/FlippedClassroomHW1/%E9%9D%B6%E6%9C%BA%E7%BD%91%E5%8D%A1.PNG)  
具体设置如下图所示。  
![](https://github.com/ghan3/ns/blob/master/2017-2/FlippedClassroomHW1/%E9%9D%B6%E6%9C%BAIP.PNG)


* 网关（kali）  
网关设置两张网卡，一张连接方式为内部网络，一张连接方式为NAT网络，如下图所示。  
![](https://github.com/ghan3/ns/blob/master/2017-2/FlippedClassroomHW1/%E7%BD%91%E5%85%B3%E7%BD%91%E5%8D%A11.PNG)  
![](https://github.com/ghan3/ns/blob/master/2017-2/FlippedClassroomHW1/%E7%BD%91%E5%85%B3%E7%BD%91%E5%8D%A12.PNG)  
具体设置如下图所示，其中profile1设置为自动获取。  
![](https://github.com/ghan3/ns/blob/master/2017-2/FlippedClassroomHW1/%E7%BD%91%E5%85%B3IP1.PNG)  
![](https://github.com/ghan3/ns/blob/master/2017-2/FlippedClassroomHW1/%E7%BD%91%E5%85%B3IP2.PNG)

* 攻击机（kaliAttack）  
攻击机设置一张网卡，连接方式为NAT网络，如下图所示。  
![](https://github.com/ghan3/ns/blob/master/2017-2/FlippedClassroomHW1/%E6%94%BB%E5%87%BB%E6%9C%BA%E7%BD%91%E5%8D%A1.PNG)  
攻击机IP设置为自动获取，如下图所示。  
![](https://github.com/ghan3/ns/blob/master/2017-2/FlippedClassroomHW1/%E6%94%BB%E5%87%BB%E6%9C%BAIP.PNG)

* 靶机可以访问攻击者主机  
![](https://github.com/ghan3/ns/blob/master/2017-2/FlippedClassroomHW1/%E9%9D%B6%E6%9C%BA-%E6%94%BB%E5%87%BB%E6%9C%BA.PNG)
* 攻击者主机无法直接访问靶机  
![](https://github.com/ghan3/ns/blob/master/2017-2/FlippedClassroomHW1/%E6%94%BB%E5%87%BB%E6%9C%BA-%E9%9D%B6%E6%9C%BA.PNG)
* 网关可以直接访问攻击者主机和靶机  
![](https://github.com/ghan3/ns/blob/master/2017-2/FlippedClassroomHW1/%E7%BD%91%E5%85%B3-%E9%9D%B6%E6%9C%BA%E6%94%BB%E5%87%BB%E6%9C%BA.PNG)
* 靶机的所有对外上下行流量必须经过网关  
![](https://github.com/ghan3/ns/blob/master/2017-2/FlippedClassroomHW1/%E9%9D%B6%E6%9C%BA%E9%80%9A%E8%BF%87%E7%BD%91%E5%85%B3.PNG)
* 所有节点均可以访问互联网  
![](https://github.com/ghan3/ns/blob/master/2017-2/FlippedClassroomHW1/%E5%9D%87%E8%83%BD%E4%B8%8A%E7%BD%91.PNG)
* 所有节点制作成基础镜像（多重加载的虚拟硬盘）  
![](https://github.com/ghan3/ns/blob/master/2017-2/FlippedClassroomHW1/%E6%94%BB%E5%87%BB%E6%9C%BA%E5%A4%9A%E9%87%8D%E5%8A%A0%E8%BD%BD.PNG)  
![](https://github.com/ghan3/ns/blob/master/2017-2/FlippedClassroomHW1/%E7%BD%91%E5%85%B3%E5%A4%9A%E9%87%8D%E5%8A%A0%E8%BD%BD.PNG)  
![](https://github.com/ghan3/ns/blob/master/2017-2/FlippedClassroomHW1/%E9%9D%B6%E6%9C%BA%E5%A4%9A%E9%87%8D%E5%8A%A0%E8%BD%BD.PNG)

##实验完成思路
靶机在内网，攻击机在外网。  
网关一个网卡在内网与靶机连通，一个网卡在外网与攻击机连通。  
外网可以与网络连通，靶机通过网关上网。
![](https://github.com/ghan3/ns/blob/master/2017-2/FlippedClassroomHW1/%E5%AE%9E%E9%AA%8C%E4%B8%80%E5%9B%BE.png)  


##实验完成步骤 
 
* 按照上面图片所示配置好三台虚拟机的网卡，之前采取动态分配的采用静态的方式设置之前分配的IP地址。  
此时网卡和攻击机可以相互ping通，网卡和靶机可以相互ping通。  
攻击机可以上网。网关先设置外网网卡可以上网，再设置内网网卡无法上网。靶机无法上网，但若网关可以上网，则靶机可以上网。
* 解决网关上网的问题。因为网关可以通过外网网卡上网，所以内网网卡将数据包发给外网网卡，从而解决网关的上网问题，具体操作如下所示，参考链接：https://linux.cn/article-5595-1.html 。
 -  启用IPv4转发  
执行命令 vi /etc/sysctl.conf  
将文件中 net.ipv4.ip_forward = 1 前的注释符删除  
执行命令 sysctl -p /etc/sysctl.conf
 -  配置iptables防火墙  
执行命令 iptables -A FORWARD -i eth1 -o eth0 -j ACCEPT  
上面命令中的eth1为外网网卡，即可连接网络的网卡，eth0为内网网卡  
执行命令 iptables -A FORWARD -i eth0 -o eth1 -m state --state ESTABLISHED,RELATED -j ACCEPT  
上面命令是为了防火墙能够允许已建立的连接通过 
 -  配置NAT  
执行命令 iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
* 此时三台虚拟机均可上网且均能ping通。
* 为了使攻击机无法ping通靶机，在靶机上设置一条防火墙规则。
 - 执行命令 iptables -I INPUT -s 10.0.2.5 -j DROP  
 上面的命令是阻止IP为10.0.2.5的机器访问靶机
  

