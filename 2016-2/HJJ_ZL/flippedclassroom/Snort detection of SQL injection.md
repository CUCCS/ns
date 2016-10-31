# snort检测SQL注入攻击 #

## 实验内容 ##
- 简单介绍snort工具的三种工作模式
- 编写自定义snort规则，以对sql注入攻击行为作出警告
- 利用snort的NIDS模式检测SQL注入攻击

##实验环境##
- 本实验攻击方为linux Cali系统pc1
- 服务器采用的是Pentesterlab封装好的镜像来进行搭建，采用的是debian的系统，设置默认网关为PC2
- 所有访问服务器的流量都会经过一台cali主机pc2，snort和iptables均在pc2上设置
- 在/proc/sys/net/ipv4路径下执行echo 1 > ip_forward，将默认值0改为1，开启IP转发，使得网关PC2可以对pc的访问流量进行监控和检测


##实验过程##
- snort的嗅探模式：
该模式下，可以解码捕获到的报文后输出到标准输出到控制台上，功能与tcpdump、wireshark类似
![](image/1.PNG)
- 实际上snort并没有自己的捕包工具，它需要一个外部的捕包程序库：libpcap。它利用libpcap独立地从物理链路上进行捕包
- snort的报文记录模式：该模式下，snort可以将捕获到的报文保存下来，用wireshark等工具进行后续分析
![](image/2.PNG)
![](image/3.PNG)

- snort的NIDS模式：这个模式为本次试验的主要工作模式，其探测入侵的方式是通过对嗅探到的数据包与规则链表进行查询匹配，如果有匹配的规则，则进行丢包或者报警
![](image/6.PNG)
- 进入snort默认的规则目录 /etc/snort/rules,这个目录下可以看到snort自带的规则
![](image/5.PNG)
- 先应用snort自带规则进行试验（因为只是单纯的ping所以不会有警告）
![](image/7.PNG)
- 为了检测sql注入需要新建一个自定义规则 vim myrule.rules 
- 建立好自定义的规则后，还需要在/etc/snort/snort.conf文件中加入myrule.rules
![](image/10.PNG)
- 本次试验的自定义规则有:
- alert tcp any any -> any 80 (msg:"SQL Injection 1";flow:to_server,established;uricontent:".php";pcre:"/(\%27)|(\')|(\-\-)|(%23)|(#)/i";classtype:Web-application-attack;sid:9099;rev:5;)
- alert tcp any any -> any 80 (msg:"SQL attack";content:"union"; nocase; sid:1000002; rev:1;)
- 接下来输入指令snort -vd -l /log -c /etc/snort/snort.conf 打开snort的检测模式
- 打开攻击机器PC1，在网站界面中输入Sql注入语句http://localhost/cat.php?id=1%20union%20select%201,2,3,4
![](image/9.PNG)
- 回到PC2查看snort监控窗口

##实验中遇到的问题##
- 嗅探和报文记录模式下出现“No preprocessors configured for policy 0”警告”：其原因是没有加载预处理器，解决方法是应用snort规则
![](image/4.PNG)
- 开始编写的snort语法规则有些错误
![](image/11.PNG)

##相关文献##
- Linux平台Snort入侵检测系统实战指南http://www.2cto.com/Article/201208/145925.html
- https://www.snort.org/documents
