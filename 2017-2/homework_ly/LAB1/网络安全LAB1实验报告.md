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

*全局设定
![Alt text](/1.png)

*靶机
![Alt text](/4.png)
![Alt text](/8.png)

*网关
![Alt text](/2.png)
![Alt text](/3.png)
![Alt text](/6.png)

*攻击者主机
![Alt text](/5.png)
![Alt text](/7.png)


*实验结果

    攻击者主机无法直接访问靶机
![Alt text](/9.png)

    端口转发实现内网联网，所有对外上下行流量必须经过网关
![Alt text](/10.png)
![Alt text](/11.png)

    所有节点制作成基础镜像
![Alt text](/12.png)



