### 基于VirtualBox的网络攻防基础环境搭建

#### 一、实验环境准备

- 设置网卡

  -   内部局域网使用了Host-Only网卡，连接外网使用的是NAT 网络。

  -   Host-Only网卡启用DHCP服务。

![image](https://github.com/icoy/ns/raw/master/2017-2/lyp-personal-hw1/1/1-1.PNG)


-   靶机，网关都连接到了同一个Host-Only网卡

![image](https://github.com/icoy/ns/raw/master/2017-2/lyp-personal-hw1/1/1-2.PNG)

- 攻击者使用NAT网络
 
![image](https://github.com/icoy/ns/raw/master/2017-2/lyp-personal-hw1/1/1.2-1.PNG)

-  网关主机设置两个网卡，另外一个设置成NAT 网络的网卡 
  
![image](https://github.com/icoy/ns/raw/master/2017-2/lyp-personal-hw1/1/1-3.PNG)

- 设置IP

  -   网关使用默认分配的IP。

![image](https://github.com/icoy/ns/raw/master/2017-2/lyp-personal-hw1/1/1-4.PNG)

-   靶机的IP改为手动设置（192.168.56.102）和网关在同网段，网关设为192.168.56.101。

-  攻击者主机使用默认设置。（攻击者主机IP :10.0.2.5） （为了域名解析 需要将DNS设置为网关主机的DNS地址202.205.16.4）

![image](https://github.com/icoy/ns/raw/master/2017-2/lyp-personal-hw1/1/1.2-2.PNG)
   

---


  | 主机角色  | 内网IP                          |
  | ----- | ----------------------------- |
  | 靶机    | 192.168.56.102                  |
  | 网关主机  | 192.168.56.101（外网IP：10.0.2.9） |
  | 攻击者主机 | 10.0.2.5                  |

  

---


- 设置靶机防火墙规则，禁止攻击者主机IP访问，以达到单向访问的目的。

  ```shell
  iptables -I INPUT -s 10.0.2.5 -j DROP
  ```
  
- 配置端口转发，使靶机可访问外网

   -   更改网关主机ip-forword文件值为1
   -   网关配置iptables
 
  ```shell
  iptables -t nat -A POSTROUTING -s 192.168.56.0/24 -j MASQUERADE
  ```
 

#### 二、实验目标实现

- [x] 靶机可以直接访问攻击者主机
- [x] 攻击者主机无法直接访问靶机

  - 靶机ping攻击者，攻击者可以接收到ping包，但是响应包不能到达靶机。（上为攻击主机10.0.2.5使用tcpdump命令抓包，下为靶机192.168.102）

![image](https://github.com/icoy/ns/raw/master/2017-2/lyp-personal-hw1/1/1.2-4.PNG)

- [x] 网关可以直接访问攻击者主机10.0.2.5和靶机192.168.56.102
- 
![image](https://github.com/icoy/ns/raw/master/2017-2/lyp-personal-hw1/1/1.2-5.PNG)



- [x] 所有节点均可以访问互联网

  - 靶机、攻击者主机可以访问外网IP 8.8.8.8（上为攻击者，下为靶机）

![image](https://github.com/icoy/ns/raw/master/2017-2/lyp-personal-hw1/1/1.2-6.PNG)
  
  - 网关可以访问外网
  
![image](https://github.com/icoy/ns/raw/master/2017-2/lyp-personal-hw1/1/1.2-8.PNG)

- [x] 靶机的所有对外上下行流量必须经过网关

  - 靶机机访问外网的同时，网关主机192.168.56.101使用wireshark抓包，可以抓取数据
    
![image](https://github.com/icoy/ns/raw/master/2017-2/lyp-personal-hw1/1/1.2-7.PNG)




















   



