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


* ![Alt text](C:\Users\RachelLyy\Pictures\大三下\数字安全\1.png)


* 网关kali-gateway设置

  * 网卡1配置nat模式，网卡2配置host-only模式。

    * ![Alt text](C:\Users\RachelLyy\Pictures\大三下\数字安全\2.png)
    * ![Alt text](C:\Users\RachelLyy\Pictures\大三下\数字安全\3.png)

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
          iface eth0 inet static 
          address 192.168.3.90 
          gateway 192.168.3.1 
          netmask 255.255.255.0 

* 靶机kali-viictim设置

  * eth0配置静态ip。与网关及攻击机在同一网段。网关设为kali-gateway的内网网卡ip。

* 配置结果

  * 网关kali-gateway：
    * 外网ip：net模式；ip动态分配。
    * 内网ip：host-only模式；ip：192.168.43.110
  * 攻击机kali-attacker：
    * host-only模式
    * ip：192.168.43.102；网关：192.168.43.110
  * 靶机kali-victim：
    * host-only模式
    * ip：192.168.43.103；网关：192.168.43.110

  ### 2、设置访问规则

  * 攻击者主机无法直接访问靶机

    * 设置过滤规则

      ![Alt text](C:\Users\RachelLyy\Pictures\大三下\数字安全\4.png)

    * 效果

      * 攻击者主机使用**tcpdump -n -i eth0 dst 192.168.43.102**抓包
      * ![Alt text](C:\Users\RachelLyy\Pictures\大三下\数字安全\5.png)
      * 可以看到靶机ping攻击者ping不通。

    ### 3、端口转发实现内网联网

    *  配置端口转发
      * 在服务器（网关）上使其能转发：echo "1" > /proc/sys/net/ipv4/ip_forward
      * 配置端口转发内网ip：iptables -t nat -A POSTROUTING -o eth0（外网网卡） -s 192.168.43.0/24（内网ip） -j MASQUERADE 
      * 效果
        * ![Alt text](C:\Users\RachelLyy\Pictures\大三下\数字安全\9.png)
    * 所有的上下行流量都经过网关
      * ![Alt text](C:\Users\RachelLyy\Pictures\大三下\数字安全\10.png)

    ### 4、多重加载

    * ![Alt text](C:\Users\RachelLyy\Pictures\大三下\数字安全\6.png)

    * ![Alt text](C:\Users\RachelLyy\Pictures\大三下\数字安全\7.png)

    * ![Alt text](C:\Users\RachelLyy\Pictures\大三下\数字安全\8.png)

      ​

      ## 三、问题

      配置内网连通外网时，是否只需配置虚拟机中能连接外网的网卡转发内网ip即可。

      ​

      ​