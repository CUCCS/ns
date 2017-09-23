### 基于VirtualBox的网络攻防基础环境搭建



#### 一、任务完成情况清单

- [x] 靶机可以直接访问攻击者主机



- [x] 攻击者主机无法直接访问靶机



- [x] 网关可以直接访问攻击者主机和靶机



- [x] 靶机的所有对外上下行流量必须经过网关



- [x] 所有节点均可以访问互联网


- [x] 所有节点制作成基础镜像（多重加载的虚拟硬盘）

#### 二、实验过程详述

- 设置网卡

  内部局域网使用了Host-Only网卡，连接外网使用的是NAT 网络。

  Host-Only网卡启用DHCP服务。

  ![Host-Only网卡设置](E:\Dcuments\CourseStudy\Junior3rd\NetworkSecurity\HW_final\ns\2017-2\Sonya_Coursework\FlippedClassroom_HW\HW_1\2.png)

  三个主机（靶机，攻击者主机，网关）都连接到了同一个Host-Only网卡

![网卡机器—网络设置1](E:\Dcuments\CourseStudy\Junior3rd\NetworkSecurity\HW_final\ns\2017-2\Sonya_Coursework\FlippedClassroom_HW\HW_1\3.png)

​    网关主机设置两个网卡，另加一个设置成NAT 网络的网卡，其余两台主机只有一个Host-Only网卡。 

![网卡机器—网络设置1](E:\Dcuments\CourseStudy\Junior3rd\NetworkSecurity\HW_final\ns\2017-2\Sonya_Coursework\FlippedClassroom_HW\HW_1\4.png)

- 设置IP

  网关的IP不需要设置，两个网卡都使用默认分配的IP。

  ![5](E:\Dcuments\CourseStudy\Junior3rd\NetworkSecurity\HW_final\ns\2017-2\Sonya_Coursework\FlippedClassroom_HW\HW_1\5.png)

  注： 两个网卡的设置会同步

  靶机的IP改为手动设置。 网关设为192.168.26.103。

  ![6](E:\Dcuments\CourseStudy\Junior3rd\NetworkSecurity\HW_final\ns\2017-2\Sonya_Coursework\FlippedClassroom_HW\HW_1\6.png)

  攻击者主机的设置也一样。（攻击者主机IP :192.168.26.5）

  注： 

  | 主机角色  | 内网IP                          |
  | ----- | ----------------------------- |
  | 靶机    | 192.168.26.2                  |
  | 网关主机  | 192.168.26.103（外网IP：10.0.2.9） |
  | 攻击者主机 | 192.168.26.5                  |

  ​

- 设置靶机防火墙规则，禁止攻击者主机IP访问，以达到单向访问的目的。

  ```shell
  iptables -I INPUT -s 192.168.26.5 -j DROP
  ```

  ​

  ![7](E:\Dcuments\CourseStudy\Junior3rd\NetworkSecurity\HW_final\ns\2017-2\Sonya_Coursework\FlippedClassroom_HW\HW_1\7.png)

  效果验证： 

  - 靶机ping攻击者，攻击者可以接收到ping包，但是响应包不能到达靶机。

  ![8](E:\Dcuments\CourseStudy\Junior3rd\NetworkSecurity\HW_final\ns\2017-2\Sonya_Coursework\FlippedClassroom_HW\HW_1\8.png)

  - 网关可以直接访问靶机和攻击者主机。

    ![10](E:\Dcuments\CourseStudy\Junior3rd\NetworkSecurity\HW_final\ns\2017-2\Sonya_Coursework\FlippedClassroom_HW\HW_1\10.png)

- 配置端口转发

  ```shell
  iptables -t nat -I PREROUTING -j DNAT --to 10.0.2.9
  ```

  效果验证：

  - 靶机、攻击者主机可以访问外网IP

    ![11](E:\Dcuments\CourseStudy\Junior3rd\NetworkSecurity\HW_final\ns\2017-2\Sonya_Coursework\FlippedClassroom_HW\HW_1\11.png)

  - 所有的上下行流量都经过网关

    ![12](E:\Dcuments\CourseStudy\Junior3rd\NetworkSecurity\HW_final\ns\2017-2\Sonya_Coursework\FlippedClassroom_HW\HW_1\12.png)

- 设置多重加载

  - 过程简记：

    ​	VBox: 管理->虚拟介质管理 **释放**虚拟介质 **修改**属性为多重加载；创建虚拟机，选择现有虚拟硬盘文件，选择响应虚拟硬盘。

  - 效果验证 ：

    ![13](E:\Dcuments\CourseStudy\Junior3rd\NetworkSecurity\HW_final\ns\2017-2\Sonya_Coursework\FlippedClassroom_HW\HW_1\13.png)

#### 三、问题

1. 不能直接访问的定义是什么？ 在个人的认识中如果A不能访问B,会导致B不能接收到A的响应包，这样在使用效果来看B也不能访问A了。但是如果设定特定的规则（比如响应时间，或者数据包的标识），是A的响应包可以被B接收，这样合理吗？
2. ping 域名 有待设置

#### 四、附

```shell
iptables -I INPUT -s 192.168.26.5 -j DROP

-I 插入规则
INPUT 数据包流入口
PREROUTING 路由前
-s 源IP
-j DROP 数据包丢弃
```



