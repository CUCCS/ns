# 基于bro的计算机入侵取证实战分析

### 实验要求

使用bro开源流量分析器通过分析流量包中的extract file和log文件得到攻击主机的IP

### 实验过程

1. 安装bro ` apt install bro bro-aux`

2. 实验环境基本信息

   ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_4/Images/%E5%AE%9E%E9%AA%8C%E7%8E%AF%E5%A2%83%E4%BF%A1%E6%81%AF.png)

3. 编辑bro配置文件

   * 编辑 ` /etc/bro/site/local.bro` ，在文件尾部追加两行新配置代码

    `@load frameworks/files/extract-all-files`*#提取所有文件*     
    `@load mytuning.bro`

    ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_4/Images/%E6%96%87%E4%BB%B6%E5%B0%BE%E9%83%A8%E8%BF%BD%E5%8A%A0%E9%85%8D%E7%BD%AE%E4%BB%A3%E7%A0%81.png)

   * 在`/etc/bro/site/`目录下创建新文件mytuning.bro，内容为：

     `redef ignore_checksums = T;`     

4. 下载pcap包（实验目标）

   `wget  https://www.honeynet.org/files/attack-trace.pcap_.gz`

5. 解压缩后使用bro自动分析pcap包

   `bro -r attack-trace.pcap /etc/bro/site/local.bro`

   出现警告信息<br/>`WARNING: No Site::local_nets have been defined. It's usually a good idea to define your local networks.`<br/>对于本次入侵取证实验来说没有影响。

   >若要解决上述警告信息，编辑`mytuning.bro`，增加一行变量定义<br/>
   `redef Site::local_nets = { 192.150.11.0/24 };`

   >添加和不添加上述一行变量定义除了bro运行过程中是否会产生警告信息的差异，增加这行关于本地网络IP地址范围的定义对于本次实验来说会新增2个日志文件，会报告在当前流量（数据包文件）中发现了本地网络IP和该IP关联的已知服务信息:`known_services.log`和`konwn_hosts.log`。

   在attack-trace.pcap文件的当前目录下会生成一些.log文件和一个extract_files目录

   ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_4/Images/pcap%E6%96%87%E4%BB%B6%E7%9B%AE%E5%BD%95%E4%B8%8B%E6%96%B0%E5%A2%9E%E6%96%87%E4%BB%B6.png)

   在extract_files目录下发现有一个文件

   ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_4/Images/extract_files%E7%9B%AE%E5%BD%95%E4%B8%8B%E7%9A%84%E6%96%B0%E6%96%87%E4%BB%B6.png)

6. 上传发现的后门程序

   将该文件上传到[ThreatBook](https://x.threatbook.cn)发现匹配了一个历史扫描报告

   ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_4/Images/%E7%BD%91%E7%BB%9C%E6%89%AB%E6%8F%8F%E6%8A%A5%E5%91%8A1.png)

   ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_4/Images/%E7%BD%91%E7%BB%9C%E6%89%AB%E6%8F%8F%E6%8A%A5%E5%91%8A2.png)   

   该报告表明这是一个已知的后门程序！至此，基于这个发现可以进行逆向倒推，寻找入侵线索。   

7. 寻找入侵线索

   * 通过阅读`/usr/share/bro/base/files/extract/main.bro`的源代码

     ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_4/Images/main%E6%BA%90%E7%A0%81.png)

     了解到该文件名的最右一个-右侧对应的字符串`FHUsSu3rWdP07eRE4l`是`files.log`中的文件唯一标识。

   * 查看`files.log`，可以得到该文件提取自FTP会话，并得到该流量的`conn_uids`为`CNg1Xh4tSyepI7CLng`

     ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_4/Images/%E6%9F%A5%E7%9C%8Bfiles-log.png)

   * 查看`conn.log`，找到id为`CNg1Xh4tSyepI7CLng`的五元组信息，得到该PE文件来自于IPv4地址为`98.114.205.102`的主机

     ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_4/Images/%E6%9F%A5%E7%9C%8Bconn-log.png)

### 实验结果

至此得到攻击主机的IP为：`98.114.205.102`

通过这个实验可以展示出bro在计算机取证方面具有十分有效的作用。它可以通过pcap包来获取入侵者留下的痕迹。

### 实验总结

* bro可以在事件生成引擎中实现应用层协议功能。在计算机取证分析中，可以高效地分析网络流量，从而找出入侵的痕迹，帮助管理者追究责任、减少损失。

* bro是一款被动的开源流量分析器。它主要用于对链路上所有深层次的可疑行为流量进行安全监控，为网络流量分析提供了一个综合平台，特别侧重于语义安全监控。虽然经常与传统入侵检测/预防系统进行比较，但bro采用了完全不同的方法，为用户提供了一个灵活的框架，可以帮助定制，深入的监控远远超出传统系统的功能。

* bro的目标在于搜寻攻击活动并提供其背景信息与使用模式。它能够将网络中的各设备整理为可视化图形、深入网络流量当中并检查网络数据包;它还提供一套更具通用性的流量分析平台。
