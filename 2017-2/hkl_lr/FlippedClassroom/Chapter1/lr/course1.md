# 基于VirtualBox的网络攻防基础环境搭建实验报告 #
---
## 一．实验目的 ##
节点：靶机、网关、攻击者主机

连通性 ：

靶机可以直接访问攻击者主机

攻击者主机无法直接访问靶机

网关可以直接访问攻击者主机和靶机

靶机的所有对外上下行流量必须经过网关

所有节点均可以访问互联网

其他要求 ：

所有节点制作成基础镜像（多重加载的虚拟硬盘）

---
## 二．实验操作 ##

（1）虚拟机搭建系统

1.虚拟机安装kali64bit

2.将虚拟机的vdi文件释放，修改为多重加载，并剪切复制到其他路径

3.新建虚拟机使用已有虚拟硬盘

（2）配置网络
靶机：kali-v 网关：kali-gateway 主机：kali-attacker

设置网卡，都为NAT网络

![](https://github.com/canyousee/ahelloworld/raw/master/1.png)

![](https://github.com/canyousee/ahelloworld/raw/master/2.png)


kali-gateway：使用两个网卡

![](https://github.com/canyousee/ahelloworld/raw/master/3.png)

Kali-v 使用Nat2 网卡
Kali-attacker 使用Nat网卡


手动修改靶机和主机的ip
![](https://github.com/canyousee/ahelloworld/raw/master/4.png)

结果：

主机
![](https://github.com/canyousee/ahelloworld/raw/master/5.png)

靶机
![](https://github.com/canyousee/ahelloworld/raw/master/6.png)

防火墙设置：
![](https://github.com/canyousee/ahelloworld/raw/master/7.png)

效果：
1.主机ping 靶机 ping不通
![](https://github.com/canyousee/ahelloworld/raw/master/8.png)

2.靶机ping 主机 成功
![](https://github.com/canyousee/ahelloworld/raw/master/9.png)

3.防火墙设置使得靶机所有对外访问都要通过网关

参考：

http://blog.csdn.net/cfw88888/article/details/7755924

http://blog.chinaunix.net/uid-26495963-id-3279216.html