### 基于virtualbox的网络攻防基础环境搭建
#### 一、实现功能：

  -  靶机可以直接访问攻击者主机
  - 攻击者主机无法直接访问靶机
  - 网关可以直接访问攻击者主机和靶机
  - 靶机的所有对外上下行流量必须经过网关
  - 所有节点均可以访问互联网

#### 二、实验过程：

##### 1、网络设置：

网卡1连接外网：NAT

![](https://github.com/leemataduo/ns/blob/master/2017-2/wyq_wzy_lw/lw/hw1/%E5%9B%BE%E7%89%871.png)



网卡2连接内部网络：Host-Only

![](https://github.com/leemataduo/ns/blob/master/2017-2/wyq_wzy_lw/lw/hw1/%E5%9B%BE%E7%89%872.png)


Host-Only启用DHCP服务器:


![](https://github.com/leemataduo/ns/blob/master/2017-2/wyq_wzy_lw/lw/hw1/%E5%9B%BE%E7%89%873.png)

![](https://github.com/leemataduo/ns/blob/master/2017-2/wyq_wzy_lw/lw/hw1/%E5%9B%BE%E7%89%874.png)

（DHCP服务器负责局域网内各个计算机IP地址的申请和分配管理）

##### 2、IP设置：

  网关主机：


![](https://github.com/leemataduo/ns/blob/master/2017-2/wyq_wzy_lw/lw/hw1/%E5%9B%BE%E7%89%875.png)


（dhclient：直接控制eth来进行网络操作获取IP（获取eth0外网地址，不用修改）)



在HOST-ONLY下手动配置靶机和攻击者主机的IP，网关设置为网关主机IP：

靶机：




![](https://github.com/leemataduo/ns/blob/master/2017-2/wyq_wzy_lw/lw/hw1/%E5%9B%BE%E7%89%876.png)


攻击者主机：


![](https://github.com/leemataduo/ns/blob/master/2017-2/wyq_wzy_lw/lw/hw1/%E5%9B%BE%E7%89%877.png)


##### 3、功能实现：

（1）、靶机访问攻击者主机：


![](https://github.com/leemataduo/ns/blob/master/2017-2/wyq_wzy_lw/lw/hw1/%E5%9B%BE%E7%89%878.png)

（2）、攻击者原来可以直接访问靶机，靶机设置防火墙之后攻击者主机无法访问


![](https://github.com/leemataduo/ns/blob/master/2017-2/wyq_wzy_lw/lw/hw1/%E5%9B%BE%E7%89%879.png)


如果在靶机监听，攻击者发送的访问请求可以到达靶机，但响应无法回到攻击者主机：


![](https://github.com/leemataduo/ns/blob/master/2017-2/wyq_wzy_lw/lw/hw1/%E5%9B%BE%E7%89%8710.png)




（3）、网关主机访问靶机：


![](https://github.com/leemataduo/ns/blob/master/2017-2/wyq_wzy_lw/lw/hw1/%E5%9B%BE%E7%89%8711.png)


网关主机访问攻击者主机：


![](https://github.com/leemataduo/ns/blob/master/2017-2/wyq_wzy_lw/lw/hw1/%E5%9B%BE%E7%89%8712.png)








（4）、网关主机对靶机进行监听，靶机流量经过网关主机：


![](https://github.com/leemataduo/ns/blob/master/2017-2/wyq_wzy_lw/lw/hw1/%E5%9B%BE%E7%89%8713.png)






（5）、启用网卡1NAT访问外网：


![](https://github.com/leemataduo/ns/blob/master/2017-2/wyq_wzy_lw/lw/hw1/%E5%9B%BE%E7%89%8714.png)

![](https://github.com/leemataduo/ns/blob/master/2017-2/wyq_wzy_lw/lw/hw1/%E5%9B%BE%E7%89%8715.png)
