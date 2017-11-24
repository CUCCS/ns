基于VirtualBox的攻防环境搭建
 ==========================
 实验要求
----------------------------
### 1.靶机可以直接访问攻击者主机
### 2.攻击者主机无法直接访问靶机
### 3.网关可以直接访问攻击者主机和靶机
### 4.靶机的所有对外上下行流量必须经过网关
### 5.所有节点均可以访问互联网
### 6.所有节点制作成基础镜像


实验过程
------------
#### 网络拓扑图

![](https://raw.githubusercontent.com/Geraens/ns/master/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/%E5%9F%BA%E4%BA%8EVirtualBox%E7%9A%84%E6%94%BB%E9%98%B2%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA/%E5%9B%BE%E7%89%87/%E6%8B%93%E6%89%91%E5%9B%BE.JPG)


#### 三台虚拟机

![](https://raw.githubusercontent.com/Geraens/ns/master/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/%E5%9F%BA%E4%BA%8EVirtualBox%E7%9A%84%E6%94%BB%E9%98%B2%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA/%E5%9B%BE%E7%89%87/%E6%80%BB%E5%9B%BE.png)

#### 网关机和靶机采用内部网络连接
网关机网卡1

![](https://raw.githubusercontent.com/Geraens/ns/master/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/%E5%9F%BA%E4%BA%8EVirtualBox%E7%9A%84%E6%94%BB%E9%98%B2%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA/%E5%9B%BE%E7%89%87/%E7%BD%91%E5%85%B3%E6%9C%BA%E7%BD%91%E5%8D%A11.png)

#### 靶机网卡

![](https://raw.githubusercontent.com/Geraens/ns/dd256721369187b5221a3b5729d0bd196899c44a/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/%E5%9F%BA%E4%BA%8EVirtualBox%E7%9A%84%E6%94%BB%E9%98%B2%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA/%E5%9B%BE%E7%89%87/%E9%9D%B6%E6%9C%BA%E7%BD%91%E5%8D%A1.png)

### 网关机与攻击机采用NAT网络连接

#### 网关机网卡2

![](https://raw.githubusercontent.com/Geraens/ns/dd256721369187b5221a3b5729d0bd196899c44a/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/%E5%9F%BA%E4%BA%8EVirtualBox%E7%9A%84%E6%94%BB%E9%98%B2%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA/%E5%9B%BE%E7%89%87/%E7%BD%91%E5%85%B3%E6%9C%BA%E7%BD%91%E5%8D%A12.png)

### 网关，靶机和攻击机的IP设置

* 网关的外网网卡采用DHCP自动分配，为10.0.2.7

![](https://raw.githubusercontent.com/Geraens/ns/dd256721369187b5221a3b5729d0bd196899c44a/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/%E5%9F%BA%E4%BA%8EVirtualBox%E7%9A%84%E6%94%BB%E9%98%B2%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA/%E5%9B%BE%E7%89%87/%E7%BD%91%E5%85%B3%E6%9C%BA%E7%BD%91%E5%8D%A11IP.png)

* 内网网卡手动设置为192.168.1.1，网关设为外网网卡IP

![](https://raw.githubusercontent.com/Geraens/ns/dd256721369187b5221a3b5729d0bd196899c44a/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/%E5%9F%BA%E4%BA%8EVirtualBox%E7%9A%84%E6%94%BB%E9%98%B2%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA/%E5%9B%BE%E7%89%87/%E7%BD%91%E5%85%B3%E6%9C%BA%E7%BD%91%E5%8D%A12IP.png)

* 靶机IP手动设为192.168.1.2，与网关机内网IP在同一个网段

![](https://raw.githubusercontent.com/Geraens/ns/ea92412a33551fca085f166493215a310fef5d27/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/%E5%9F%BA%E4%BA%8EVirtualBox%E7%9A%84%E6%94%BB%E9%98%B2%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA/%E5%9B%BE%E7%89%87/%E9%9D%B6%E6%9C%BAIP.png)

* 攻击机IP采用DHCP自动分配

![](https://raw.githubusercontent.com/Geraens/ns/ea92412a33551fca085f166493215a310fef5d27/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/%E5%9F%BA%E4%BA%8EVirtualBox%E7%9A%84%E6%94%BB%E9%98%B2%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA/%E5%9B%BE%E7%89%87/%E6%94%BB%E5%87%BB%E6%9C%BAIP.png)


> 为了使靶机能够连接外网，在网关机上采用了IP转发，将sysctl.conf中的ip_forward更改为1，以及iptables防火墙的配置：
>>  #iptables -A FORWARD -i wlan2 -o eth2 -j ACCEPT
>> #iptables -A FORWARD -i eth2 -o wlan2 -m state --state ESTABLISHED,RELATED -j ACCEPT

> 最后进行了NAT配置：
>> #iptables -t nat -A POSTROUTING -o eth2 -j MASQUERADE

实验要求实现：
------------------
### 1.靶机可以直接访问攻击者主机

![](https://raw.githubusercontent.com/Geraens/ns/ea92412a33551fca085f166493215a310fef5d27/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/%E5%9F%BA%E4%BA%8EVirtualBox%E7%9A%84%E6%94%BB%E9%98%B2%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA/%E5%9B%BE%E7%89%87/%E9%9D%B6%E6%9C%BAping%E9%80%9A%E6%94%BB%E5%87%BB%E6%9C%BA.png)

### 2.攻击者主机无法直接访问靶机

![](https://raw.githubusercontent.com/Geraens/ns/ea92412a33551fca085f166493215a310fef5d27/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/%E5%9F%BA%E4%BA%8EVirtualBox%E7%9A%84%E6%94%BB%E9%98%B2%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA/%E5%9B%BE%E7%89%87/%E6%94%BB%E5%87%BB%E6%9C%BA%E6%97%A0%E6%B3%95ping%E9%80%9A%E9%9D%B6%E6%9C%BA.png)

### 3.网关可以直接访问攻击者主机和靶机

* 网关访问攻击机

![](https://raw.githubusercontent.com/Geraens/ns/ea92412a33551fca085f166493215a310fef5d27/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/%E5%9F%BA%E4%BA%8EVirtualBox%E7%9A%84%E6%94%BB%E9%98%B2%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA/%E5%9B%BE%E7%89%87/%E7%BD%91%E5%85%B3%E6%9C%BAping%E9%80%9A%E6%94%BB%E5%87%BB%E6%9C%BA.png)

* 网关访问靶机

![](https://raw.githubusercontent.com/Geraens/ns/ea92412a33551fca085f166493215a310fef5d27/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/%E5%9F%BA%E4%BA%8EVirtualBox%E7%9A%84%E6%94%BB%E9%98%B2%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA/%E5%9B%BE%E7%89%87/%E7%BD%91%E5%85%B3%E6%9C%BA%E5%8F%AFping%E9%80%9A%E9%9D%B6%E6%9C%BA.png)

### 4.靶机的所有对外上下行流量必须经过网关

* 图为网关机抓取的靶机的数据包

![](https://raw.githubusercontent.com/Geraens/ns/master/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/%E5%9F%BA%E4%BA%8EVirtualBox%E7%9A%84%E6%94%BB%E9%98%B2%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA/%E5%9B%BE%E7%89%87/%E9%9D%B6%E6%9C%BA%E8%AE%BF%E9%97%AE%E5%A4%96%E7%BD%91%E6%8A%93%E5%8C%85.jpg)

* 图为网关机抓取攻击机访问外网的数据包

![](https://raw.githubusercontent.com/Geraens/ns/master/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/%E5%9F%BA%E4%BA%8EVirtualBox%E7%9A%84%E6%94%BB%E9%98%B2%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA/%E5%9B%BE%E7%89%87/%E6%94%BB%E5%87%BB%E6%9C%BA%E8%AE%BF%E9%97%AE%E5%A4%96%E7%BD%91.jpg)


### 5.所有节点均可以访问互联网

* 网关机

![](https://raw.githubusercontent.com/Geraens/ns/dd256721369187b5221a3b5729d0bd196899c44a/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/%E5%9F%BA%E4%BA%8EVirtualBox%E7%9A%84%E6%94%BB%E9%98%B2%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA/%E5%9B%BE%E7%89%87/%E7%BD%91%E5%85%B3%E6%9C%BA%E5%8F%AF%E8%BF%9E%E6%8E%A5%E5%A4%96%E7%BD%91.png)

* 靶机

![](https://raw.githubusercontent.com/Geraens/ns/dd256721369187b5221a3b5729d0bd196899c44a/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/%E5%9F%BA%E4%BA%8EVirtualBox%E7%9A%84%E6%94%BB%E9%98%B2%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA/%E5%9B%BE%E7%89%87/%E9%9D%B6%E6%9C%BAping%E9%80%9A%E5%A4%96%E7%BD%91.png)

* 攻击机

![](https://raw.githubusercontent.com/Geraens/ns/dd256721369187b5221a3b5729d0bd196899c44a/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/%E5%9F%BA%E4%BA%8EVirtualBox%E7%9A%84%E6%94%BB%E9%98%B2%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA/%E5%9B%BE%E7%89%87/%E6%94%BB%E5%87%BB%E6%9C%BAping%E9%80%9A%E5%A4%96%E7%BD%91.png)
