# 实战Bro网络入侵取证

## 实验目的
本次实战的例子是pcap attack trace，通过分析流量包中的extract file和log文件得到攻击主机的IP。

## 实验过程

### 安装bro

`apt-get install bro bro-aux`   

### 实验环境基本信息
![img](./实验环境.PNG)   

### 编辑bro配置文件

* 编辑`etc/bro/site/local.bro`,在文件尾部两行配置代码。
![image](./配置bro.PNG)   

* 在`/etc/bro/site/`目录下创建文件mytuning.bro,并添加内容`redef ignore_checksums = T;`,忽略校验和验证。
![image](./touch mytuning.PNG)
![image](./show mytuning.PNG)

### 使用bro自动化分析pcap文件

执行命令`bro -r attack-trace.pcap /etc/bro/site/local.bro`

```
Usage:bro [options] [file ...]
-r|--readfile <readfile>   |read from given tcpdump file
```

![image](./bro -r.PNG)

执行上述命令后出现警告信息`WARNING: No Site::local_nets have been defined. It's usually a good idea to define your local networks.`对于本次入侵取证实验来说没有影响。       

如果要解决上述警告信息，编辑mytuning.bro,增加一行变量定义`redef Site::local_nets = { 192.150.11.0/24 };`增加后再次实验结果如下。

![image](./bro-r-no error.PNG)

添加一行变量定义前，执行bro -r命令在pcap文件所在的目录下会出现八个日志文件和extract_files文件夹。   
添加一行变量定义前，执行bro -r命令在pcap文件所在的目录下会出现十个日志文件和extract_files文件夹。   
增加的两个日志文件为know_hosts.log/know_services.log，会报告在当前流量（数据包文件）中发现了本地网络IP和该IP关联的已知服务信息。

![image](./cat known.PNG)   

### 分析结果上传virustotal

* 进入extract_files文件夹。
![image](./extract_files.PNG)

* 将该文件上传至virustotal网站获得分析结果,确认这是一个已知的后门程序，基于这个发现进行逆向倒推，寻找入侵线索。
![image](./virus.PNG)

### 获取攻击者IP

通过阅读`usr/share/bro/base/files/extract/main.bro`的源代码
