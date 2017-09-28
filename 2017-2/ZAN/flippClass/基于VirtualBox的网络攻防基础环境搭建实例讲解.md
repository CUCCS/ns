#基于VirtualBox的网络攻防基础环境搭建实例讲解#
<br/>
## 要求 ##
* [ ] 节点：靶机、网关、攻击者主机
    * 连通性
        * 靶机可以直接访问攻击者主机
        * 攻击者主机无法直接访问靶机
        * 网关可以直接访问攻击者主机和靶机
        * 靶机的所有对外上下行流量必须经过网关
        * 所有节点均可以访问互联网
    * 其他要求
        * 所有节点制作成基础镜像（多重加载的虚拟硬盘）

## 已实现功能 ##
- 攻击者主机无法直接访问靶机：攻击机和靶机相互不能ping

- 网关可以直接访问攻击者主机和靶机
![](https://github.com/kjAnny/ns/blob/master/2017-2/ZAN/pictures/ping%E7%BD%91%E5%85%B3.jpg)

- 所有节点制作成基础镜像（多重加载的虚拟硬盘）
![](https://github.com/kjAnny/ns/blob/master/2017-2/ZAN/pictures/%E5%A4%9A%E9%87%8D%E5%8A%A0%E8%BD%BD.JPG)


## 网络配置 ##
- 靶机：kali-1，NAT网络，ip:10.0.2.2
- 攻击机：kali-2，桥接网卡,ip:192.168.10.9
- 网关：配置NAT网络和桥接网卡,ip:10.0.2.1,192.168.10.1

![](https://github.com/kjAnny/ns/blob/master/2017-2/ZAN/pictures/1net.JPG)
![](https://github.com/kjAnny/ns/blob/master/2017-2/ZAN/pictures/2net.JPG)
![](https://github.com/kjAnny/ns/blob/master/2017-2/ZAN/pictures/gw-net1.JPG)
![](https://github.com/kjAnny/ns/blob/master/2017-2/ZAN/pictures/gw-net2.JPG)

----------

![](https://github.com/kjAnny/ns/blob/master/2017-2/ZAN/pictures/gw-bridge-network.JPG)
![](https://github.com/kjAnny/ns/blob/master/2017-2/ZAN/pictures/gw-network.JPG)
![](https://github.com/kjAnny/ns/blob/master/2017-2/ZAN/pictures/kali-1ip.JPG)
![](https://github.com/kjAnny/ns/blob/master/2017-2/ZAN/pictures/kali-2network.JPG)

----------
网关上的iptables：
![](https://github.com/kjAnny/ns/blob/master/2017-2/ZAN/pictures/gw-iptables.JPG)
## 问题 ##
- 桥接网卡连的是物理网卡，为什么不能连上外网？
- 靶机kali-1可以ping通网关的另一个接口，为什么不能再把icmp包再转发到攻击机上？
