### 基于VirtualBox的网络攻防基础环境搭建



#### 一、任务完成情况清单

- [x] 靶机可以直接访问攻击者主机



- [x] 攻击者主机无法直接访问靶机



- [x] 网关可以直接访问攻击者主机和靶机



- [x] 靶机的所有对外上下行流量必须经过网关



- [x] 所有节点均可以访问互联网


- [x] 所有节点制作成基础镜像（多重加载的虚拟硬盘）

#### 二、实验过程

- 设置网卡

  将网关的网卡分别设置为Host-Only、NAT网络
  
  ![image](https://github.com/yangyisama/ns/blob/master/2017-2/yangyisama/hw1/pictures/1.png)
  ![image](https://github.com/yangyisama/ns/tree/master/2017-2/yangyisama/hw1/pictures/2.png)
  
  Host-Only网卡启用DHCP服务
  
  将靶机网卡设置为Host-Only网络，让靶机变为内网的计算机，让攻击者主机没有办法直接访问靶机
 
  将攻击者主机设置为NAT网络，相当于一个外网主机，然后利用网关来进行网络连接
  
  在此时若NAT网络界面名称找不到，需要先添加NAT网络
  
  ![image](https://github.com/yangyisama/ns/tree/master/2017-2/yangyisama/hw1/pictures/3.png)

- 设置IP
 
  网关的IP

  ![image](https://github.com/yangyisama/ns/tree/master/2017-2/yangyisama/hw1/pictures/4.png)
  
  ![image](https://github.com/yangyisama/ns/tree/master/2017-2/yangyisama/hw1/pictures/5.png)

  手动设置靶机的IP,网关设置为网关的IP地址
  ![image](https://github.com/yangyisama/ns/tree/master/2017-2/yangyisama/hw1/pictures/6.png)  
 
  
  同理设置攻击者主机的IP
  
  ![image](https://github.com/yangyisama/ns/tree/master/2017-2/yangyisama/hw1/pictures/7.png)

  
- 设置多重加载

  - 过程简记：

    先在虚拟介质管理中 将 虚拟介质  **释放**；**修改** 介质属性 为 动态分配储存
    创建虚拟机，选择现有虚拟硬盘文件，选择响应虚拟硬盘。
    
    ![image](https://github.com/yangyisama/ns/tree/master/2017-2/yangyisama/hw1/pictures/8.png)

#### 三、实验结果截图
  
靶机ping攻击者，攻击者可以接收到ping包，但是响应包不能到达靶机，而是通过网关转发到靶机

![image](https://github.com/yangyisama/ns/tree/master/2017-2/yangyisama/hw1/pictures/9.png)

![image](https://github.com/yangyisama/ns/tree/master/2017-2/yangyisama/hw1/pictures/10.png)

网关可以直接ping通 靶机和攻击者主机

![image](https://github.com/yangyisama/ns/tree/master/2017-2/yangyisama/hw1/pictures/11.png)

靶机、攻击者主机都可以访问外网

![image](https://github.com/yangyisama/ns/tree/master/2017-2/yangyisama/hw1/pictures/12.png)

通过抓包验证是否所有的上下行流量都经过网关

![image](https://github.com/yangyisama/ns/tree/master/2017-2/yangyisama/hw1/pictures/13.png)

所有节点制作成基础镜像

![image](https://github.com/yangyisama/ns/tree/master/2017-2/yangyisama/hw1/pictures/14.png)

#### 四、问题

1.Kali是不是相对于Ubuntu来说是一个较为轻量级的系统；


