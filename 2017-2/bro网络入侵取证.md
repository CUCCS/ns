# Chapter 12： Bro 网络入侵取证

## 1.安装bro

apt-get install bro bro-aux

## 2.实验环境

- ![](https://raw.githubusercontent.com/U2Vino/photo/Chapter-12/environment.PNG)

## 3.编辑bro配置文件

##### 编辑 /etc/bro/site/ 目录下的 local.bro，在该文件末尾添加以下代码：

- @load frameworks/files/extract-all-files

- @load mytuning.bro

- ![](https://raw.githubusercontent.com/U2Vino/photo/Chapter-12/local_bro_conf.PNG)

##### 在/etc/bro/site/目录下创建新文件mytuning.bro，内容为：

- redef ignore_checksums = T;

- ![](https://raw.githubusercontent.com/U2Vino/photo/Chapter-12/mytuning_bro1.PNG)

## 4.使用bro分析pcap文件

##### 使用下面的命令，利用bro自动化分析pcap:

- bro -r attack-trace.pcap /etc/bro/site/local.bro

##### 将会出现警告信息：

- ![](https://raw.githubusercontent.com/U2Vino/photo/Chapter-12/bro-one.PNG)

##### 此警告对于本次入侵取证实验来说没有影响。如果要解决上述警告信息，编辑mytuning.bro，增加一行变量定义：

- redef Site::local_nets = { 192.150.11.0/24 };

- ![](https://raw.githubusercontent.com/U2Vino/photo/Chapter-12/mytuning_bro2.PNG)

##### 添加了上面一行代码后，bro运行没有警告信息

- ![](https://raw.githubusercontent.com/U2Vino/photo/Chapter-12/bro-two.PNG)

##### 新增2个日志文件，会报告在当前流量（数据包文件）中发现了本地网络IP和该IP关联的已知服务信息

- ![](https://raw.githubusercontent.com/U2Vino/photo/Chapter-12/cat_services_and_hosts.PNG)

##### 在attack-trace.pcap文件的当前目录下会生成一些.log文件和一个extract_files目录，在该目录下我们会发现有一个文件:

- extract-1240198114.648099-FTP_DATA-FHUsSu3rWdP07eRE4l

- ![](https://raw.githubusercontent.com/U2Vino/photo/Chapter-12/extract.PNG)

##### 将该文件上传到[virustotal](https://www.virustotal.com/)我们会发现匹配了一个历史扫描报告，该报告表明这是一个已知的后门程序:

- ![](https://raw.githubusercontent.com/U2Vino/photo/Chapter-12/exe.PNG)

##### 通过阅读/usr/share/bro/base/files/extract/main.bro的源代码 ， 可以了解到该文件名的最右一个-右侧对应的字符串FHUsSu3rWdP07eRE4l是 files.log 中的文件唯一标识

- ![](https://raw.githubusercontent.com/U2Vino/photo/Chapter-12/main_bro.PNG)

##### 查看files.log，可以得到，该文件提取自FTP会话，并得到该流量的conn_uids为CbPIE03nLi8TywKtm3

- ![](https://raw.githubusercontent.com/U2Vino/photo/Chapter-12/file_log.PNG)

##### 查看conn.log，找到id为CbPIE03nLi8TywKtm3的五元组信息，得到该PE文件来自于IPv4地址为98.114.205.102的主机

- ![](https://raw.githubusercontent.com/U2Vino/photo/Chapter-12/conn_log.PNG)

## 5.log文件显示小技巧

###### 按照“列名”输出conn.log中我们关注的一些“列”

- bro-cut ts uid id.orig_h id.resp_h proto < conn.log

- ![](https://raw.githubusercontent.com/U2Vino/photo/Chapter-12/bro-cut-one.PNG)

###### 将UNIX时间戳格式转换成人类可读的时间

- bro-cut -d < conn.log

- ![](https://raw.githubusercontent.com/U2Vino/photo/Chapter-12/bro-cut-two.PNG)
