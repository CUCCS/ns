# 基于交换机的局域网ARP洪泛攻击的防御实验

## 测试实验背景：
* 测试环境：  
   Windows 7下运行软件Cisco Packet Tracer进行模拟实验环境：    
   由于实验条件有限（>_<|||），利用软件Cisco Packet Tracer进行模拟实验：
   * 交换机型号：2950-24    
   * 主机：普通PC-PT  
![image](https://github.com/weiyi1024/github-tutorial/raw/master/PACKET tracer.JPG)
![image](https://github.com/weiyi1024/github-tutorial/raw/master/网络拓扑图.JPG)

## 测试概要：
   * 测试一：1个交换机，1台PC机  
      测试条件说明 : 交换机的端口10与PC机相连，攻击源为PC机。连接情况如图所示：  
      ![image](https://github.com/weiyi1024/github-tutorial/raw/master/测试一.JPG)
      
   * 测试二：2台交换机，2台PC机（四种情况）
     * 情况一：  
       测试条件说明：交换机A的端口9与交换机B的端口23连接，交换机A的端口10与PC机A连接，交换机B 的端口10与PC机B相连接。PC机A为攻击源。连接情况如图所示：  
       ![image](https://github.com/weiyi1024/github-tutorial/raw/master/测试二A.JPG)
     * 情况二： 
       测试条件说明：交换机A的端口9与交换机B的端口23相连接，交换机A的端口10与PC机A相连接，交换机B的端口10与PC机B相连接。PC机B为攻击源。连接情况如图所示：
       ![image](https://github.com/weiyi1024/github-tutorial/raw/master/测试二B.JPG)
     * 情况三：  
       测试条件说明：交换机A的端口9与交换机B的端口23相连接，交换机A的端口10与PC机A相连接，交换机B的端口10与PC机B相连接。PC机A和PC机B同为攻击源。连接情况如图所示：
       ![image](https://github.com/weiyi1024/github-tutorial/raw/master/测试二C.JPG)
     * 情况四：
       测试条件说明：交换机A的端口9与交换机B的端口23相连接，交换机B的端口10与PC机A相连接，交换机B的端口11与PC机B相连接。PC机A和PC机B同为攻击源。连接情况如图所示：
       ![image](https://github.com/weiyi1024/github-tutorial/raw/master/测试二D.JPG)
   * 测试三：  
      测试条件说明：交换机A的端口10与交换机B的端口23相连接，交换机A的端口11与PC机A相连接，交换机B的端口10与交换机C的端口23相连接，交换机C的端口10与PC机B相连接。PC机B为攻击源。连接情况如图所示：
       ![image](https://github.com/weiyi1024/github-tutorial/raw/master/测试三.JPG)

   * 初始化安全交换机测试  
    初始化安全交换机的工作就是设置交换机的安全端口模式为RestrictTrap模式，设定交换机端口安全违例的阈值，并指定管理主机，使得系统能够接收到交换机发出的安全违例Trap包。使用到的技术主要就是telnet与socket发送数据包。这个模块的功能单一，方法确定。对于不同的交换机，其配置过程是完全相同的，不同的是交换机的指令集。由于不同厂家生产的交换机具有不同的指令集，当我们需要把一种新的交换机列入系统范围的时候，就需要抽取其进行相应的指令集，以完成配置需要。
     
     ![image](https://github.com/weiyi1024/github-tutorial/raw/master/交换机配置.JPG)
     * [ ] 一种交换机的配置命令集如下:
        * Switch# configure terminal
        * Switch(config)# interface f0/15
        * Switch(config-if)# switchport mode access
        * Switch(config-if)# switchport port-security maximum 10
        * Switch(config-if)# switchport port-security violation restrict
        * Switch(config-if)# switchport port-security
        * Switch(config-if)# exit
        * Switch(config)# snmp-server community access rw host 192.168.0.11
        * Switch(config)# snmp-server host 192.168.0.11 traps version 2c access
        * Switch(config)# snmp-server enable traps portsecurityviolate
        * Switch(config)# end  
        其中192.168.0.11是管理主机的IP地址。  
    在这一部分中，目的就是要获取全部正确的指令集，从而正确配置交换机。
        
## 实验概述：
* 对于ARP洪泛攻击，攻击源定位算法主要查找的是交换机发出的Trap包。由于交换机的MAC地址表是层层映射的，所以，如果网络中有一台主机发起ARP洪泛攻击，原则上网络中所有的交换机都将会发出Trap包。攻击源定位算法从中找到攻击源的方法，就是在交换机中找到这样一种Trap包:该包中记录的交换机的端口连接的是一台主机。那么该主机就是一个ARP攻击源。网络拓扑图如下：

  ![image](https://github.com/weiyi1024/github-tutorial/raw/master/网络拓扑图示.JPG)

  在图所示的网络拓扑图中，Terminal2向网络发出随机地址攻击，当发包数量超过预先设置的阈值时，就会触发交换机的安全违例，随之发出Trap包。在网络中，所有的交换机都会发出Trap包，报出安全违例的端口情况如下:  
  * Switch1报出本交换机链接到Terminal2的端口出现安全违例(图中红色标出);
  * Switch2报出本交换机连接到Switch1的端口出现安全违例(图中绿色标出);
  * Switch3报出本交换机连接到Switch2的端口出现安全违例(图中蓝色标出)。  
  所有的Trap包会送到Manager管理主机。管理主机通过分析这些Trap包知，Switch1发出的Trap包报告的安全违例端口连接的是主机终端，满足上述攻击源定位算法判定攻击源条件，于是对该端口进行处理。在此过程中，Switch2,  Switch3所发出的Trap包都不符合要求，于是放弃处理。
  
### 关闭和开启交换机端口实验：  
* 当攻击源不断的发出攻击的时候，我们可以对其做出处理使其立即停止攻击。处理的方式就是关闭其相应的交换机的端口，在攻击源停止攻击之后，可以再开启相应的设备端口。当然这个功能是可选的，不必一定要关闭交换机的端口。这个模块同样功能单一，方法确定。对于不同的交换机，其配置过程是完全相同的，不同的是交换机的指令集。
     * [ ]  一种关闭交换机的配置命令集如下:
       * Switch# configure terminal
       * Switch(config)# interface FastEthernet0/2
       * Switch(config-if)# shutdown
       * Switch(config-if)# end
       * Switch# exit

* 系统尝试关闭Terminal5所连接的交换机端口，然后用Terminal1-Terminal4同时Ping Terminal5，发现无法Ping通。当再次开启Terminal5所连接的交换机端口，用Terminal1-Terminal4同时Ping Terminal5，这时就能Ping通了。
    * 利用Cisco Packet Tracer,创建网络拓扑图如下：  
      ![image](https://github.com/weiyi1024/github-tutorial/raw/master/交换机开关实验一.JPG)
    * 配置Terminal1-Terminal5的IP、掩码和网关。  
      ![image](https://github.com/weiyi1024/github-tutorial/raw/master/1-4介绍.JPG)
      ![image](https://github.com/weiyi1024/github-tutorial/raw/master/5介绍.JPG)
    * 配置完成后，关闭Terminal5所连接的交换机端口   
      ![image](https://github.com/weiyi1024/github-tutorial/raw/master/关闭交换机端口.JPG)
    * 然后用Terminal1-Terminal4同时Ping Terminal5，发现无法Ping通    
      ![image](https://github.com/weiyi1024/github-tutorial/raw/master/1-4ping5不通.JPG)
    * 再次开启Terminal5所连接的交换机端口     
      ![image](https://github.com/weiyi1024/github-tutorial/raw/master/打开交换机端口.JPG)
    * Terminal1-Terminal4同时Ping Terminal5      
      ![image](https://github.com/weiyi1024/github-tutorial/raw/master/1-4再次ping5.JPG)

* 实验成功，根据[实验原理](https://github.com/weiyi1024/ns/blob/master/2015-2/WY_HLH_SJC/ARP-flooding-attack/%E5%9F%BA%E4%BA%8E%E4%BA%A4%E6%8D%A2%E6%9C%BA%E7%9A%84%E5%B1%80%E5%9F%9F%E7%BD%91ARP%E6%B4%AA%E6%B3%9B%E6%94%BB%E5%87%BB%E7%9A%84%E9%98%B2%E5%BE%A1%E5%8E%9F%E7%90%86.md)，通过初始化交换机配置，正确运行攻击源定位算法，如果网络中有一台主机发起ARP洪泛攻击，网络中所有的交换机都将会发出Trap包。攻击源定位算法从中找到攻击源的方法，就是在交换机中找到这样一种Trap包:该包中记录的交换机的端口连接的是一台主机。那么该主机就是一个ARP攻击源。然后通过关闭和开启交换机端口来实现防御攻击的目的，同时也向管理主机报告了攻击源主机。




