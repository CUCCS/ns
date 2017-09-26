# **Chap1 基于VirtualBox的网络攻防基础环境搭建实例** #

----------
##**实验设备：**##
- 物理主机
- 虚拟机（靶机**KaliTarget**、网关**KaliRolling**、攻击者主机**KaliAttack**）
## **实验要求：** ##
- 靶机可以直接访问攻击者主机
- 攻击者主机无法直接访问靶机
- 网关可以直接访问攻击者主机和靶机
- 靶机的所有对外上下行流量必须经过网关
- 所有节点均可以访问互联网
- *所有节点制作成基础镜像（多重加载的虚拟硬盘）*
## **实验过程：** ##
- 设置基础镜像
> 将基础镜像设为多重加载
- *​	VBox: 管理->虚拟介质管理 释放虚拟介质 修改属性为多重加载；创建虚拟机，选择现有虚拟硬盘文件，选择响应虚拟硬盘。*

![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/lw_wyq_wzy/wzy_HW/HW_1/%E5%A4%9A%E9%87%8D%E5%8A%A0%E8%BD%BD.png)

- 配置网卡
> 网关**KaliRolling**设置两个网卡，分别为NAT网络和桥接网络（eth0为桥接网络，eth1为nat网络）；
![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/lw_wyq_wzy/wzy_HW/HW_1/%E7%BD%91%E5%85%B3%E7%BD%91%E5%8D%A11.png)
![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/lw_wyq_wzy/wzy_HW/HW_1/%E7%BD%91%E5%85%B3%E7%BD%91%E5%8D%A12.png)

> 靶机**KaliTarget**和攻击者主机**KaliAttack**只设置一块NAT网络网卡
![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/lw_wyq_wzy/wzy_HW/HW_1/%E9%9D%B6%E6%9C%BA%E7%BD%91%E5%8D%A1.png)
![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/lw_wyq_wzy/wzy_HW/HW_1/%E6%94%BB%E5%87%BB%E8%80%85%E4%B8%BB%E6%9C%BA%E7%BD%91%E5%8D%A1.png)

- *NAT网络：类同VMware的NAT模式，除主机不能主动访问虚拟机。需要在全局网络配置中针对该NAT网络设置端口转发，主机与虚拟机才能有限度的互访。同一NAT网络中的虚拟机间能无限制互访。*

> 桥接网络连接外网，NAT网络为内部局域网，启用DHCP服务

![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/lw_wyq_wzy/wzy_HW/HW_1/NAT%E7%BD%91%E7%BB%9C%E8%AE%BE%E7%BD%AE.png)

- 设置IP
> 网关的网卡1启用默认IP，靶机和攻击者主机IP需手动配置，且二者网关均设为网关主机网卡1的IP即10.0.2.4，网关网卡2的IP手动设为192.168.1.9
 
-局域网内单向访问
>  在靶机终端设置防火墙规则，以使攻击者主机无法直接访问靶机。
![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/lw_wyq_wzy/wzy_HW/HW_1/%E9%9D%B6%E6%9C%BA%E8%AE%BE%E7%BD%AE%E9%98%B2%E7%81%AB%E5%A2%99.png)

- 访问外网
> 在靶机和攻击者主机配置端口转发，使可以访问互联网
    `iptables -t nat -I PREROUTING -j DNAT --to 192.168.1.9`

## **实验结果** ##
- 靶机可以ping通攻击者主机
![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/lw_wyq_wzy/wzy_HW/HW_1/%E9%9D%B6%E6%9C%BA%E7%9B%B4%E6%8E%A5%E8%AE%BF%E9%97%AE%E6%94%BB%E5%87%BB%E8%80%85%E4%B8%BB%E6%9C%BA.png)

- 攻击者主机不可以ping通靶机
![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/lw_wyq_wzy/wzy_HW/HW_1/%E6%94%BB%E5%87%BB%E8%80%85%E4%B8%BB%E6%9C%BA%E4%B8%8D%E8%83%BD%E7%9B%B4%E6%8E%A5%E8%AE%BF%E9%97%AE%E9%9D%B6%E6%9C%BA.png)

- 网关可以ping通攻击者主机和靶机
![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/lw_wyq_wzy/wzy_HW/HW_1/%E7%BD%91%E5%85%B3%E8%AE%BF%E9%97%AE%E9%9D%B6%E6%9C%BA%E5%92%8C%E4%B8%BB%E6%9C%BA.png)

- 靶机流量经过网关（网关终端设置抓包命令）
    `tcpdump -i eth1 -n （开启抓包  -n表示不反向解析）`
![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/lw_wyq_wzy/wzy_HW/HW_1/%E9%9D%B6%E6%9C%BA%E6%B5%81%E9%87%8F%E7%BB%8F%E8%BF%87%E7%BD%91%E5%85%B3.png)

- 访问外网

![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/lw_wyq_wzy/wzy_HW/HW_1/%E8%AE%BF%E9%97%AE%E4%BA%92%E8%81%94%E7%BD%91.png)
## **实验问题** ##
- 虽然配置了端口转发，但靶机和攻击者主机仍然不能访问外网，查阅了资料也做了相应更改均无效，不知在NAT网络下如何配置才可以访问外网？
- 希望老师在下次课程中能对此次实验有所讲解和示范，以纠正实验中的错误思路和做法。




