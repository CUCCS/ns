网络安全LAB1实验报告

基于VirtualBox的网络攻防基础环境搭建实例讲解

    节点：靶机、网关、攻击者主机
    连通性
        靶机可以直接访问攻击者主机
        攻击者主机无法直接访问靶机
        网关可以直接访问攻击者主机和靶机
        靶机的所有对外上下行流量必须经过网关
        所有节点均可以访问互联网
    其他要求
        所有节点制作成基础镜像（多重加载的虚拟硬盘）


实验环境

靶机 target：linux 2.0
网关 kali：linux 2.0
攻击者主机 attack linux 2.0

网络配置

### 全局设定

![](https://github.com/LuYe2/ns/blob/master/2017-2/homework_ly/LAB1/1.png?raw=true)

#### 靶机

![](https://github.com/LuYe2/ns/blob/master/2017-2/homework_ly/LAB1/4.png?raw=true)
![](https://github.com/LuYe2/ns/blob/master/2017-2/homework_ly/LAB1/8.png?raw=true)

#### 网关

![](https://github.com/LuYe2/ns/blob/master/2017-2/homework_ly/LAB1/2.png?raw=true)
![](https://github.com/LuYe2/ns/blob/master/2017-2/homework_ly/LAB1/3.png?raw=true)
![](https://github.com/LuYe2/ns/blob/master/2017-2/homework_ly/LAB1/6.png?raw=true)

#### 攻击者主机

![](https://github.com/LuYe2/ns/blob/master/2017-2/homework_ly/LAB1/5.png?raw=true)
![](https://github.com/LuYe2/ns/blob/master/2017-2/homework_ly/LAB1/7.png?raw=true)

### 实验结果

#### 攻击者主机无法直接访问靶机

![](https://github.com/LuYe2/ns/blob/master/2017-2/homework_ly/LAB1/9.png?raw=true)

#### 端口转发实现内网联网，所有对外上下行流量必须经过网关

![](https://github.com/LuYe2/ns/blob/master/2017-2/homework_ly/LAB1/10.png?raw=true)
![](https://github.com/LuYe2/ns/blob/master/2017-2/homework_ly/LAB1/11.png?raw=true)

#### 所有节点制作成基础镜像

![](https://github.com/LuYe2/ns/blob/master/2017-2/homework_ly/LAB1/12.png?raw=true)


