# chap0x01 基于VirtualBox的网络攻防基础环境搭建实例讲解

## 一、功能实现

*	靶机可以直接访问攻击者主机

- 攻击者主机无法直接访问靶机
- 网关可以直接访问攻击者主机和靶机
- 靶机的所有对外上下行流量必须经过网关
- 所有节点均可以访问互联网


- 所有节点制作成基础镜像（多重加载的虚拟硬盘）

## 二、配置过程

### 1、配置IP

* 全局设置：添加host-only网络，配置开启dhcp服务器。手动配置ip


* ![Alt text](https://github.com/RachelLYY/ns/raw/master/2017-2/Lab1/21.PNG)


* 网关kali-gateway设置

  * 网卡1配置nat模式，网卡2配置host-only模式。

    * ![Alt text](https://github.com/RachelLYY/ns/raw/master/2017-2/Lab1/22.PNG)
    * ![Alt text](https://github.com/RachelLYY/ns/raw/master/2017-2/Lab1/23.PNG)

  * 编辑文件/etc/network/interfaces。设置eth0开启dhcp，动态获取ip。

    * 添加以下行

      * auto eth0 

        iface eth0 inet dhcp 

      * 重启服务：/etc/init.d/networking restart

* 攻击机kali-attacker设置

  * eth0配置静态ip
    * 编辑文件/etc/network/interfaces
      * 添加以下行
        * auto eth0 
          iface eth0 inet dhcp

* 靶机kali-victim设置

  * eth0配置静态ip。与网关及攻击机在同一网段。网关设为kali-gateway的内网网卡ip。

* 配置结果

  * 网关kali-gateway：
    * ![Alt text](https://github.com/RachelLYY/ns/raw/master/2017-2/Lab1/24.PNG)
    * 外网ip：nat模式；ip动态分配。
    * 内网ip：host-only模式；ip：192.168.151.110
  * 攻击机kali-attacker：
    * ![Alt text](https://github.com/RachelLYY/ns/raw/master/2017-2/Lab1/32.PNG)
    * nat模式；ip动态分配。
    
  * 靶机kali-victim：
    * ![Alt text](https://github.com/RachelLYY/ns/raw/master/2017-2/Lab1/26.PNG)
    * host-only模式
    * ip：192.168.151.102；网关：192.168.151.110

 ### 3、端口转发实现内网联网

   *  配置端口转发
      * 在服务器（网关）上使其能转发：echo "1" > /proc/sys/net/ipv4/ip_forward
      * 配置端口转发内网ip：iptables -t nat -A POSTROUTING -o eth0（外网网卡） -s 192.168.43.0/24（内网ip） -j MASQUERADE 
   * 效果
     *  ![Alt text](https://github.com/RachelLYY/ns/raw/master/2017-2/Lab1/27.PNG)
   * 所有的上下行流量都经过网关
     *  ![Alt text](https://github.com/RachelLYY/ns/raw/master/2017-2/Lab1/28.PNG)

 ### 4、多重加载

   * ![Alt text](https://github.com/RachelLYY/ns/raw/master/2017-2/Lab1/29.PNG)

   * ![Alt text](https://github.com/RachelLYY/ns/raw/master/2017-2/Lab1/30.PNG)

   * ![Alt text](https://github.com/RachelLYY/ns/raw/master/2017-2/Lab1/31.PNG)

      ​

## 三、问题

   配置内网连通外网时，是否只需配置虚拟机中能连接外网的网卡转发内网ip即可。

      ​

      ​
