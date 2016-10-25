# snort检测SQL注入攻击 #

## 实验内容 ##
- 简单介绍snort工具的三种工作模式
- 编写自定义snort规则，以对sql注入攻击行为作出警告
- 利用snort的NIDS模式检测SQL注入攻击

##实验环境##
- 本实验攻击方与防御方均为linux Cali系统
- 服务器为

##实验过程##
- snort的嗅探模式：
该模式下，可以解码捕获到的报文后输出到标准输出到控制台上，功能与tcpdump、wireshark类似
![](image/1.PNG)
- 实际上snort并没有自己的捕包工具，它需要一个外部的捕包程序库：libpcap。它利用libpcap独立地从物理链路上进行捕包
- snort的报文记录模式：该模式下，snort可以将捕获到的报文保存下来，用wireshark等工具进行后续分析
![](image/2.PNG)![](image/3.PNG)
##实验中遇到的问题##
- 嗅探和报文记录模式下出现“No preprocessors configured for policy 0”警告”：其原因是没有加载预处理器，解决方法是应用snort规则


##相关文献##
- Linux平台Snort入侵检测系统实战指南http://www.2cto.com/Article/201208/145925.html
- https://www.snort.org/documents
