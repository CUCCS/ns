# 编程实现网络扫描

## 实验要求

    TCP connect scan
    TCP stealth scan
    TCP XMAS scan
    UDP scan 

## 实验环境

> 服务器：GW kali-linux

> 目标主机：victim kali-linux

## 实验过程

1. 查看目标主机IP地址及端口开放情况
![](https://github.com/LuYe2/ns/blob/master/2017-2/homework_ly/LAB2/lab2_1.png?raw=true)

2. 扫描关闭端口

![](https://github.com/LuYe2/ns/blob/master/2017-2/homework_ly/LAB2/lab2_2.png?raw=true)

![](https://github.com/LuYe2/ns/blob/master/2017-2/homework_ly/LAB2/lab2_3.png?raw=true)

![](https://github.com/LuYe2/ns/blob/master/2017-2/homework_ly/LAB2/lab2_14png?raw=true)

![](https://github.com/LuYe2/ns/blob/master/2017-2/homework_ly/LAB2/lab2_5.png?raw=true)

3. 开启80端口与22端口

![](https://github.com/LuYe2/ns/blob/master/2017-2/homework_ly/LAB2/lab2_6.png?raw=true)
![](https://github.com/LuYe2/ns/blob/master/2017-2/homework_ly/LAB2/lab2_8.png?raw=true)

4. 扫描80端口与22端口

![](https://github.com/LuYe2/ns/blob/master/2017-2/homework_ly/LAB2/lab2_7.png?raw=true)

![](https://github.com/LuYe2/ns/blob/master/2017-2/homework_ly/LAB2/lab2_9.png?raw=true)

5. 过滤22端口

![](https://github.com/LuYe2/ns/blob/master/2017-2/homework_ly/LAB2/lab2_11.png?raw=true)

6. 再次扫描22端口

![](https://github.com/LuYe2/ns/blob/master/2017-2/homework_ly/LAB2/lab2_12.png?raw=true)

## 未完成
UDP scan

![](https://github.com/LuYe2/ns/blob/master/2017-2/homework_ly/LAB2/lab2_10.png?raw=true)

## 参考资料
http://resources.infosecinstitute.com/port-scanning-using-scapy/
