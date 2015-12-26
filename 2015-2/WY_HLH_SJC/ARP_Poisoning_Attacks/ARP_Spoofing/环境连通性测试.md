一、测试连通性以及虚拟机能否与互联网中的其他主机通信
   
需修改XP系统的主机中防火墙的设置

虚拟机之间的连通性：

- host1 ping host2

![](http://i.imgur.com/gNl1QWi.png)


- host1 ping attacker

![](http://i.imgur.com/vPAoR9c.png)


- host2 ping attacker

![](http://i.imgur.com/GdjHIOS.png)

虚拟机和互联网中的其他主机通信：

- host1 ping www.baidu.com

![](http://i.imgur.com/YtUaynl.png)


-  host2 ping www.baidu.com

![](http://i.imgur.com/yPIpbyh.png)


-  attacker ping www.baidu.com

![](http://i.imgur.com/EFG10qe.png)
