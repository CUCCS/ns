##基于bro的计算机入侵取证实战分析


####1. 使用bro来完成取证分析

####1.1. 安装bro

- 执行 apt-get install bro bro-aux ，报错，apt-get update一下即可
####1.2. 实验环境基本信息

![](https://github.com/Anna-YJ/Picture/blob/master/1.png?raw=true) 


####1.3. 编辑bro配置文件

- 编辑 /etc/bro/site/local.bro，在文件尾部追加两行新配置代码
@load frameworks/files/extract-all-files
@load mytuning.bro

![](https://github.com/Anna-YJ/Picture/blob/master/2.png?raw=true)


- 在/etc/bro/site/目录下创建新文件mytuning.bro，内容为：
redef ignore_checksums = T;

![](https://github.com/Anna-YJ/Picture/blob/master/3.png?raw=true)


####1.4. 使用bro自动化分析pcap文件

bro -r attack-trace.pcap_/data /etc/bro/site/local.bro

Warning对于本次入侵取证实验来说没有影响。

如果要解决上述警告信息，也很简单，同样是编辑mytuning.bro，增加一行变量定义即可
redef Site::local_nets = { 192.150.11.0/24 };

注意添加和不添加上述一行变量定义除了bro运行过程中是否会产生警告信息的差异，增加这行关于本地网络IP地址范围的定义对于本次实验来说会新增2个日志文件，会报告在当前流量（数据包文件）中发现了本地网络IP和该IP关联的已知服务信息。

![](https://github.com/Anna-YJ/Picture/blob/master/4.png?raw=true)

![](https://github.com/Anna-YJ/Picture/blob/master/5.png?raw=true)

在attack-trace.pcap文件的当前目录下会生成一些.log文件和一个extract_files目录，在该目录下我们会发现有一个文件。

![](https://github.com/Anna-YJ/Picture/blob/master/6.png?raw=true)


将该文件上传到virustotal我们会发现匹配了一个历史扫描报告，该报告表明这是一个已知的后门程序！

![](https://github.com/Anna-YJ/Picture/blob/master/7.png?raw=true)


至此，基于这个发现就可以进行逆向倒推，寻找入侵线索了。


通过阅读/usr/share/bro/base/files/extract/main.bro的源代码

![](https://github.com/Anna-YJ/Picture/blob/master/8.png?raw=true)


我们了解到该文件名的最右一个-右侧对应的字符串FHUsSu3rWdP07eRE4l是files.log中的文件唯一标识(id)。

通过查看files.log，发现该文件提取自网络会话标识（bro根据IP五元组计算出的一个会话唯一性散列值）为CP0WpmULcjBpkDTQf的FTP会话。

- 使用bro-cut（在bro-aux软件包中）更清爽的查看日志中关注的数据列

![](https://github.com/Anna-YJ/Picture/blob/master/9.png?raw=true)
![](https://github.com/Anna-YJ/Picture/blob/master/10.png?raw=true)


该CP0WpmULcjBpkDTQf会话标识在conn.log中可以找到对应的IP五元组信息。


- （查看Bro的超长行日志时的横向滚动技巧:less -S conn.log）

- 通过conn.log的会话标识匹配，我们发现该PE文件来自于IPv4地址为：98.114.205.102的主机。

![](https://github.com/Anna-YJ/Picture/blob/master/12.png?raw=true)
![](https://github.com/Anna-YJ/Picture/blob/master/11.png?raw=true)




####1.6. 小结
在计算机取证方面，bro可以通过pcap包分析网络流量，从而找出入侵的痕迹，帮助管理者追究责任和减少损失。

####2. 参考文献

- [Frequently Asked Questions from Official Bro WebSite](https://www.bro.org/documentation/faq.html)

- [bro官方辅助工具](https://www.bro.org/community/software.html)

- [基于bro的计算机入侵取证实战分析](http://www.freebuf.com/articles/system/135843.html)





