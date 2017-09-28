chap0x01 基于VirtualBox的网络攻防基础环境搭建
-
小结：网关使用两块网卡，一块模式选择为NAT网络（与攻击机在同一网段，IP为10.0.2.2），第二块网卡选择内部网络模式（与靶机在同一网段，IP为192.168.76.2）;攻击机IP为10.0.2.15；靶机IP为192.168.76.3


- 网关NAT网络：

![](https://raw.githubusercontent.com/U2Vino/photo/master/eth0.PNG)

- 网关内部网络：

![](https://raw.githubusercontent.com/U2Vino/photo/master/eth1.PNG)

- 攻击机网络：

![](https://raw.githubusercontent.com/U2Vino/photo/master/主机网络uo.PNG)

- 靶机网络

![](https://raw.githubusercontent.com/U2Vino/photo/master/靶机网络.PNG)

1. 连通性
-
- [1] 靶机可以直接访问攻击者主机
![](https://raw.githubusercontent.com/U2Vino/photo/master/1.PNG)

- [2] 攻击者主机无法直接访问靶机
![](https://raw.githubusercontent.com/U2Vino/photo/master/2.PNG)

- [3] 网关可以直接访问攻击者主机和靶机
![](https://raw.githubusercontent.com/U2Vino/photo/master/3.PNG)

- [4] 靶机的所有对外上下行流量必须经过网关
![](https://raw.githubusercontent.com/U2Vino/photo/master/41.PNG)
![](https://raw.githubusercontent.com/U2Vino/photo/master/42.PNG)

- [5] 所有节点均可以访问互联网

网关访问互联网
![](https://raw.githubusercontent.com/U2Vino/photo/master/51.PNG)
靶机访问互联网
![](https://raw.githubusercontent.com/U2Vino/photo/master/41.PNG)
攻击机访问互联网
![](https://raw.githubusercontent.com/U2Vino/photo/master/53.PNG)
2. 其他要求 
所有节点制作成基础镜像（多重加载的虚拟硬盘）
![](https://raw.githubusercontent.com/U2Vino/photo/master/71.PNG)
![](https://raw.githubusercontent.com/U2Vino/photo/master/72.PNG)
![](https://raw.githubusercontent.com/U2Vino/photo/master/73.PNG)