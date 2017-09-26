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
  
  ![image](http://note.youdao.com/favicon.ico)
  ![image](http://note.youdao.com/favicon.ico)
  
  Host-Only网卡启用DHCP服务
  
  将靶机网卡设置为NAT网络，让靶机变为内网的计算机，让攻击者主机没有办法直接访问靶机
 
  将攻击者主机设置为Host-Only，相当于一个外网主机，然后利用网关来进行网络连接
  
  在此时若NAT网络界面名称找不到，需要先添加Nat网络
  
  ![image](http://note.youdao.com/favicon.ico)

- 设置IP
 
  网关的IP

  ![image](http://note.youdao.com/favicon.ico)

  手动设置靶机的IP,网关设置为网关的IP地址
  
  ![image](http://note.youdao.com/favicon.ico)
  
  同理设置攻击者主机的IP
  
  ![image](http://note.youdao.com/favicon.ico)

  
- 设置多重加载

  - 过程简记：

    先在虚拟介质管理中 将 虚拟介质  **释放**；**修改** 介质属性 为 动态分配储存
    创建虚拟机，选择现有虚拟硬盘文件，选择响应虚拟硬盘。
    
    ![image](http://note.youdao.com/favicon.ico)

#### 三、实验结果截图
  
靶机ping攻击者，攻击者可以接收到ping包，但是响应包不能到达靶机，而是通过网关转发到靶机

![image](http://note.youdao.com/favicon.ico)

网关可以直接ping通 靶机和攻击者主机

![image](http://note.youdao.com/favicon.ico)

靶机、攻击者主机都可以访问外网

![image](http://note.youdao.com/favicon.ico)

通过抓包验证是否所有的上下行流量都经过网关

![image](http://note.youdao.com/favicon.ico)

所有节点制作成基础镜像

![image](http://note.youdao.com/favicon.ico)

#### 四、问题

1.Kali是不是相对于Ubuntu来说是一个较为轻量级的系统；


