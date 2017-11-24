# Scapy编程实现网络扫描

## 实验要求

- TCP connect scan  
- TCP stealth scan
- TCP XMAS scan
- UDP scan

## 实验环境

- RX-4869(KALI) 10.0.2.12
- Lion(KALI) 10.0.2.11

## 实验过程


### TCP connect scan

- 关闭服务器80端口
	- 使用nmap指令扫描自身，可以看到前1000个端口全部关闭
	- LION 调用tcp_ connect_ scan后，检测到80端口关闭 

![image](https://github.com/yangyisama/ns/raw/master/2017-2/icoy_U2Vino_yangyisama/hw2_yangyisama/picture/1.jpg)


- 开启服务器80端口
	- 开启80端口。


![image](https://github.com/yangyisama/ns/raw/master/2017-2/icoy_U2Vino_yangyisama/hw2_yangyisama/picture/2.jpg)


- [Code:Tcp_ Connect_ Scan](Code_Test/tcp_connect_scan.py)

### TCP stealth scan

- 关闭服务器22端口
	- 扫描自身看到22端口没有打开

![image](https://github.com/yangyisama/ns/raw/master/2017-2/icoy_U2Vino_yangyisama/hw2_yangyisama/picture/3.jpg)


- 开启服务器22端口

![image](https://github.com/yangyisama/ns/raw/master/2017-2/icoy_U2Vino_yangyisama/hw2_yangyisama/picture/3.jpg)




- [Code :Tcp_ Stealth Scan](Code_Test/tcp_stealth_scan.py)

### TCP XMAS scan

- 关闭服务器22端口

![image](https://github.com/yangyisama/ns/raw/master/2017-2/icoy_U2Vino_yangyisama/hw2_yangyisama/picture/5.jpg)


- 开启服务器22端口

![image](https://github.com/yangyisama/ns/raw/master/2017-2/icoy_U2Vino_yangyisama/hw2_yangyisama/picture/6.jpg)



- [Code :Tcp_ XMAS_ Scan](Code_Test/tcp_xmas_scan.py)

### UDP scan

- 服务器53端口关闭（DNS服务），开启68端口（DHCP服务）

![image](https://github.com/yangyisama/ns/raw/master/2017-2/icoy_U2Vino_yangyisama/hw2_yangyisama/picture/7.jpg)


- [Code :Udp_ Scan](Code_Test/udp_scan.py)