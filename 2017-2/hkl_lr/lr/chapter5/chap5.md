# SCAN 实验#

---
实验环境

客户端 10.0.2.5

![](c/client)

服务器 10.0.2.7

![](c/s)

---
服务器中：

通过开启apache2服务开启80端口

![](c/80.png)

没有开启dns服务所以53端口没有开启


服务器中端口开启状态：

80：开启

53：没开启

![](c/port.png)

---
实验代码中

dst_ip设置均为：10.0.2.7

dst_port在1,2,3种方式扫描中代码内设置为80，在4方式扫描代码中设置为53



1.tcp_connect_scan

![](c/1.png)

[tcp_connect_scan.py](c/1.py)

2.tcp_stealth_scan

![](c/2.png)

[tcp_stealth_scan.py](c/2.py)

3.tcp_xmas_scan

![](c/3.png)

[tcp_xmas_scan.py](c/3.py)

4.udp_scan

![](c/4.png)

[udp_scan.py](c/4.py)



