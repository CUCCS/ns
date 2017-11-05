#scapy编程实现网络扫描: 

- TCP connect scan  

- TCP stealth scan

- TCP XMAS scan

- UDP scan （未实现）

##环境：
     
     [1]Client:10.0.3.2

     [2]Server:10.0.3.3

###一、TCP connect scan

- [Code:TCP_ CONNECT_ SCAN.py](https://github.com/U2Vino/ns/blob/Chapter5/2017-2/TCP_CONNECT_SCAN.py)

- Srceen shots:

 nmap扫描自身，查看端口状态。
	
![](https://raw.githubusercontent.com/U2Vino/ns/Chapter5/2017-2/S1.PNG)

 Client运行TCP_CONNECT_SCAN.py,检测到80端口关闭状态。

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter5/2017-2/C1.PNG)

 Server开启Apache2(80端口)

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter5/2017-2/C2.PNG)

Client运行TCP_CONNECT_SCAN.py,检测到80端口开启状态。

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter5/2017-2/S2.PNG)

安装gufw

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter5/2017-2/gufw.PNG)

使用ufw设置防火墙过滤规则，禁止外部访问80端口

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter5/2017-2/S3.PNG)

Client运行TCP_CONNECT_SCAN.py

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter5/2017-2/C3.PNG)

###二、TCP stealth scan

- [Code:TCP_ stealth_ scan.py](https://github.com/U2Vino/ns/blob/Chapter5/2017-2/TCP_stealth_scan.py)

- Srceen shots:

nmap查看Server端口状态

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter5/2017-2/S4.PNG)

Client运行TCP_Stealth_scan.py,检测到22端口关闭

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter5/2017-2/C4.PNG)

开启22端口

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter5/2017-2/S5.PNG)

Client运行TCP_Stealth_scan.py,检测到22端口open

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter5/2017-2/C5.PNG)

过滤22端口

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter5/2017-2/S6.PNG)

Client运行TCP_Stealth_scan.py

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter5/2017-2/C6.PNG)

###三、TCP XMAS scan

- [Code:Xmas_scan.py](https://github.com/U2Vino/ns/blob/Chapter5/2017-2/Xmas_scan.py)

- Srceen shots:

Server关闭22端口

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter5/2017-2/S7.PNG)

Client运行TCP_XMAS_scan.py

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter5/2017-2/C7.PNG)

开启22端口

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter5/2017-2/S8.PNG)

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter5/2017-2/C8.PNG)

Server过滤22端口


![](https://raw.githubusercontent.com/U2Vino/ns/Chapter5/2017-2/S9.PNG)

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter5/2017-2/C9.PNG)

###四、UDP scan

-[Code:UDP_scan.py](https://github.com/U2Vino/ns/blob/Chapter5/2017-2/UDP_scan.py)