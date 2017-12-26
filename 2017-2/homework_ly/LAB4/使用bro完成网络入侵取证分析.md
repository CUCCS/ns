# Bro网络入侵取证

## 实验要求

使用bro开源流量分析器通过分析流量包中的extract file和log文件得到攻击主机的IP

## 实验步骤

1. 安装bro

> apt-get install bro bro-aux

2. 实验环境基本信息

![](https://github.com/LuYe2/ns/blob/master/2017-2/homework_ly/LAB4/%E5%AE%9E%E9%AA%8C%E7%8E%AF%E5%A2%83.png?raw=true)

3. 编辑bro配置文件

编辑 /etc/bro/site/local.bro 插入如下代码

> @load frameworks/files/extract-all-files
> 
> @load mytuning.bro

![](https://github.com/LuYe2/ns/blob/master/2017-2/homework_ly/LAB4/%E7%BC%96%E8%BE%91bro%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6.png?raw=true)

在/etc/bro/site/目录下创建并编辑文件mytuning.bro，代码如下:

> redef ignore_checksums = T;

![](https://github.com/LuYe2/ns/blob/master/2017-2/homework_ly/LAB4/%E7%BC%96%E8%BE%91mytuning.png?raw=true)

4. 下载pcap包

下载网址
> http://sec.cuc.edu.cn/huangwei/textbook/ns/chap0x12/attack-trace.pcap

5. 使用bro自动分析pcap包

> bro -r attack-trace.pcap /etc/bro/site/local.bro

出现警告信息

![](https://github.com/LuYe2/ns/blob/master/2017-2/homework_ly/LAB4/warning.png?raw=true)

此警告信息对于本次入侵取证实验来说没有影响。若要解决上述警告信息，编辑mytuning.bro，增加一行变量定义：

redef Site::local_nets = { 192.150.11.0/24 };

![](https://github.com/LuYe2/ns/blob/master/2017-2/homework_ly/LAB4/redef%20site.png?raw=true)

增加这行关于本地网络IP地址范围的定义会新增2个日志文件，会报告在当前流量（数据包文件）中发现了本地网络IP和该IP关联的已知服务信息。 

![](https://github.com/LuYe2/ns/blob/master/2017-2/homework_ly/LAB4/%E6%96%B0%E5%A2%9E%E6%97%A5%E5%BF%97%E6%96%87%E4%BB%B6.png?raw=true)

6. 上传发现的后门程序

将该文件上传到x.ThreatBook.cn发现匹配了一个历史扫描报告

![](https://github.com/LuYe2/ns/blob/master/2017-2/homework_ly/LAB4/report.png?raw=true)

该报告表明这是一个已知的后门程序！至此，基于这个发现可以进行逆向倒推，寻找入侵线索。

7. 寻找入侵线索

阅读/usr/share/bro/base/files/extract/main.bro的源代码

![](https://github.com/LuYe2/ns/blob/master/2017-2/homework_ly/LAB4/main_bro.png?raw=true)

了解到该文件名的最右一个-右侧对应的字符串FHUsSu3rWdP07eRE4l是files.log中的文件唯一标识。

通过查看files.log，发现该文件提取自网络会话标识为CDV2iYlwB8CvVIxdk2的FTP会话。 

![](https://github.com/LuYe2/ns/blob/master/2017-2/homework_ly/LAB4/FTP%E4%BC%9A%E8%AF%9D.png?raw=true)

查看conn.log，找到id为CDV2iYlwB8CvVIxdk2的五元组信息，得到该PE文件来自于IPv4地址为98.114.205.102的主机

![](https://github.com/LuYe2/ns/blob/master/2017-2/homework_ly/LAB4/%E6%94%BB%E5%87%BB%E8%80%85IP.png?raw=true)

