# chap0x01 基于VirtualBox的网络攻防基础环境搭建

- 要求与完成情况概括  
 - 节点：靶机、网关、攻击者主机
 - 连通性  
  　　　靶机可以直接访问攻击者主机（√）  
　　　攻击者主机无法直接访问靶机（√）  
　　　网关可以直接访问攻击者主机和靶机（√）  
　　　靶机的所有对外上下行流量必须经过网关（√）    
　　　所有节点均可以访问互联网（×）  
 - 其他要求  
    　　　所有节点制作成基础镜像（多重加载的虚拟硬盘）（√）  
- 配置情况  
  kali:网关  
  kali-victim:靶机  
  kali-attacker:攻击者    

  - 网关设置转发功能  
  ![](https://i.imgur.com/qWIyD4e.png)
  -  靶机(NAT网络)：  
       ![](https://i.imgur.com/A3Dbo7r.png)
  - 攻击者(桥接)：  
    ![](https://i.imgur.com/vBzZFNx.png)  
  - 网关(对应靶机:eth0-NAT网络、对应攻击者:eth1-桥接)：   
    ![](https://i.imgur.com/H7hs3eq.png)   
- 连通情况  
  - 靶机可以访问攻击者主机  
  ![](https://i.imgur.com/eEPFjj8.png)  
  - 攻击者主机无法直接访问靶机（iptables）  
  ![](https://i.imgur.com/0ulhkXR.png)  
![](https://i.imgur.com/X0cjN3O.png)  
  - 网关可以直接访问攻击者主机和靶机  
  ![](https://i.imgur.com/hIeJxIN.png)  
  - 靶机所有上下行流量必须经过网关  
  ![](https://i.imgur.com/ha4WsBe.png)
  - 所有节点可以访问互联网（未完成：攻击者和网关可以、靶机不可以，网关route设置不成功）  
  ![](https://i.imgur.com/1NBdp1r.png)    
   ![](https://i.imgur.com/OLahWE9.png)   
添加默认路由没有显示出错，但是查看路由表并没有添加进去
![](https://i.imgur.com/tklTzol.png)  
  查看靶机网卡上抓的包，数据到达192.168.1.1（默认路由选择的网关）就转发不到10.0.2.15（靶机）了，想添加一条新的默认路由（10.0.2.16，靶机的网关），但是没有成功。  
- 所有节点制作成基础镜像（多重加载的虚拟硬盘）  
 ![](https://i.imgur.com/jntJq8K.png)



 