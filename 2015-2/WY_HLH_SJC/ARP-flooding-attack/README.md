# 概述
## ARP洪泛攻击
攻击者伪造IP-MAC映射对，广播给局域网内的所有主机和网关，在网络中产生大量的ARP通信量使网络阻塞。

这种攻击方式的主要特征包括:

   ① 交换机频于处理ARP广播包，出现洪泛现象，从而耗尽网络带宽。
   
   ② 局域网内的主机频繁出现IP冲突。
   
   ③ 用虚假的地址信息占满主机的ARP高速缓存空间，使其无法正常通信。
   
## 防御方案：
先对交换机进行相应的初始化配置。配置交换机的端口安全级别为RestrictTrap，用户设置端口上允许通过的MAC地址阈值。当出现ARP洪泛攻击时会产生大量虚假的MAC地址，致使交换机端口产生安全违例，通过网络通信状况分析出某个或某几个交换机端口连接的是ARP攻击源。

# 文档目录：
* 1.[ARP缓存的查看方法和工作原理](https://github.com/weiyi1024/ns/blob/bc33f8bbe161f6a7002ee318fd4855758ed5d668/2015-2/WY_HLH_SJC/ARP-flooding-attack/ARP%E7%BC%93%E5%AD%98%E7%9A%84%E6%9F%A5%E7%9C%8B%E5%92%8C%E5%B7%A5%E4%BD%9C%E5%8E%9F%E7%90%86%E7%9A%84%E7%A0%94%E7%A9%B6.md)
* 2.[对现行的ARP攻击防御方法——ARP防火墙的缺陷分析](https://github.com/weiyi1024/ns/blob/bc33f8bbe161f6a7002ee318fd4855758ed5d668/2015-2/WY_HLH_SJC/ARP-flooding-attack/%E7%8E%B0%E8%A1%8C%E7%9A%84ARP%E6%94%BB%E5%87%BB%E9%98%B2%E5%BE%A1%E6%96%B9%E6%B3%95.md)
* 3.[交换机端口安全策略的配置命令](https://github.com/weiyi1024/ns/blob/bc33f8bbe161f6a7002ee318fd4855758ed5d668/2015-2/WY_HLH_SJC/ARP-flooding-attack/%E4%BA%A4%E6%8D%A2%E6%9C%BA%E7%AB%AF%E5%8F%A3%E5%AE%89%E5%85%A8%E7%AD%96%E7%95%A5%E7%9A%84%E9%85%8D%E7%BD%AE%E5%91%BD%E4%BB%A4.md)
* 4.[基于交换机的局域网ARP洪泛攻击的防御原理](https://github.com/weiyi1024/ns/blob/bc33f8bbe161f6a7002ee318fd4855758ed5d668/2015-2/WY_HLH_SJC/ARP-flooding-attack/%E5%9F%BA%E4%BA%8E%E4%BA%A4%E6%8D%A2%E6%9C%BA%E7%9A%84%E5%B1%80%E5%9F%9F%E7%BD%91ARP%E6%B4%AA%E6%B3%9B%E6%94%BB%E5%87%BB%E7%9A%84%E9%98%B2%E5%BE%A1%E5%8E%9F%E7%90%86.md)
* 5.[基于交换机的局域网ARP洪泛攻击的防御实验](https://github.com/weiyi1024/ns/blob/bc33f8bbe161f6a7002ee318fd4855758ed5d668/2015-2/WY_HLH_SJC/ARP-flooding-attack/%E5%9F%BA%E4%BA%8E%E4%BA%A4%E6%8D%A2%E6%9C%BA%E7%9A%84%E5%B1%80%E5%9F%9F%E7%BD%91ARP%E6%B4%AA%E6%B3%9B%E6%94%BB%E5%87%BB%E7%9A%84%E9%98%B2%E5%BE%A1%E5%AE%9E%E9%AA%8C.md)




