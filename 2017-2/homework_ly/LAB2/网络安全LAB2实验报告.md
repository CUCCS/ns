#编程实现网络扫描

##实验要求

    TCP connect scan
    TCP stealth scan
    TCP XMAS scan
    UDP scan 

##实验环境

>服务器：GW kali-linux

>目标主机：victim kali-linux

##实验过程

1. 查看目标主机IP地址及端口开放情况
![Alt text](/lab2_1.png)

2. 扫描关闭端口
![Alt text](/lab2_2.png)

![Alt text](/lab2_3.png)

![Alt text](/lab2_4.png)

![Alt text](/lab2_5.png)

3. 开启80端口与22端口

![Alt text](/lab2_6.png)
![Alt text](/lab2_8.png)

4. 扫描80端口与22端口
![Alt text](/lab2_7.png)

![Alt text](/lab2_9.png)


5. 过滤22端口
![Alt text](/lab2_11.png)

6. 再次扫描22端口
![Alt text](/lab2_12.png)

##未完成
UDP scan
![Alt text](/lab2_10.png)

##参考资料
http://resources.infosecinstitute.com/port-scanning-using-scapy/