# 网关设置
- 两张网卡，一张内部网络，一张nat网卡
![image](https://raw.githubusercontent.com/CUCfromHY001/ns/master/2017-2/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82/01/1.png)
- 内部网络地址：192.168.56.101
- NAT网卡地址：10.0.2.4
![image](https://raw.githubusercontent.com/CUCfromHY001/ns/master/2017-2/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82/01/2.png)
# 靶机
- 使用内部网络
- ip地址：192.168.56.103
- 默认网关：192.168.56.101
![image](https://raw.githubusercontent.com/CUCfromHY001/ns/master/2017-2/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82/01/3.png)
# 攻击者主机
- 使用NAT网络
- 地址：10.0.2.5
![image](https://raw.githubusercontent.com/CUCfromHY001/ns/master/2017-2/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82/01/4.png)
# 网关设置
- 设置过滤表，允许靶机通过网关访问外部网络
![image](https://raw.githubusercontent.com/CUCfromHY001/ns/master/2017-2/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82/01/5.png)
- 更改ip_forward：0->1 ，允许网卡间转发数据包 
# 功能实现 
- 靶机能访问攻击者主机
![image](https://raw.githubusercontent.com/CUCfromHY001/ns/master/2017-2/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82/01/7.png)
- 攻击者主机不能访问靶机
![image](https://raw.githubusercontent.com/CUCfromHY001/ns/master/2017-2/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82/01/8.png)
- 网关可以访问靶机
![image](https://raw.githubusercontent.com/CUCfromHY001/ns/master/2017-2/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82/01/9.png)
- 网关可以访问攻击机主机
![image](https://raw.githubusercontent.com/CUCfromHY001/ns/master/2017-2/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82/01/6.png)
- 靶机的所有对外上下行流量必须经过网关
![image](https://raw.githubusercontent.com/CUCfromHY001/ns/master/2017-2/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82/01/10.png)
- 所有节点均可以访问互联网
- 1.靶机

![image](https://raw.githubusercontent.com/CUCfromHY001/ns/master/2017-2/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82/01/11.png)
- 2.网关

![image](https://raw.githubusercontent.com/CUCfromHY001/ns/master/2017-2/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82/01/12.png)
- 3.攻击者主机
![image](https://raw.githubusercontent.com/CUCfromHY001/ns/master/2017-2/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82/01/13.png)