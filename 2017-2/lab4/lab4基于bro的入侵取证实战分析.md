# 基于bro的入侵取证实战分析
## 实验要求：
使用bro开源流量分析器通过分析流量包中的extract file和log文件得到攻击主机的IP

## 实验过程
### 安装bro

```
apt install bro bro-aux
```


### 实验环境
![image](https://github.com/wq0712/ns/blob/master/2017-2/lab4/%E7%8E%AF%E5%A2%83.PNG?raw=true)

### 编辑bro配置文件
* 编辑/etx/bro/site/local.bro，在文件尾追加两行新配置代码 
```
@load frameworks/files/extract-all-files
@load mytuning.bro
```
![image](https://github.com/wq0712/ns/blob/master/2017-2/lab4/local_bro.PNG?raw=true)
* 在/etc/site/bro/目录下创建新文件mytuning.bro,内容为： 

```
redef ignore_checksums = T;
```
![image](https://github.com/wq0712/ns/blob/master/2017-2/lab4/mytuning_bro.PNG?raw=true)

### 使用bro自动化分析pacp文件
* 下载pacp文件地址：http://sec.cuc.edu.cn/huangwei/textbook/ns/chap0x12/attack-trace.pcap

```
bro -r attack-trace.pcap /etc/bro/site/local.bro
```
![image](https://github.com/wq0712/ns/blob/master/2017-2/lab4/%E8%AD%A6%E5%91%8A.PNG?raw=true)
* 出现警告信息
```
WARNING: No Site::local_nets have been defined. It's usually a good idea to define your local networks.
```
对本次实验没有影响。
* 若要解决上述警告信息，编辑mytuning.bro，增加一行变量定义。
![image](https://github.com/wq0712/ns/blob/master/2017-2/lab4/edit_mytuning.PNG?raw=true)
* 添加和不添加上述一行变量定义除了bro运行过程中是否会产生警告信息的差异，增加这行关于本地网络IP地址范围的定义对于本次实验来说会新增2个日志文件，会报告在当前流量（数据包文件）中发现了本地网络IP和该IP关联的已知服务信息。
![image](https://github.com/wq0712/ns/blob/master/2017-2/lab4/1.PNG?raw=true)
* 在attack-trace.pcap文件的当前目录下会生成一些.log文件和一个extract_files目录，在该目录下我们会发现有一个文件。 
![image](https://github.com/wq0712/ns/blob/master/2017-2/lab4/2.PNG?raw=true)
* 将该文件上传到x.threatbook.cn我们会发现匹配了一个历史扫描报告,该报告表明这是一个已知的后门程序！至此，基于这个发现可以进行逆向倒推，寻找入侵线索。 
![image](https://github.com/wq0712/ns/blob/master/2017-2/lab4/%E5%8E%86%E5%8F%B2%E6%89%AB%E6%8F%8F%E6%8A%A5%E5%91%8A.PNG?raw=true)

### 寻找入侵线索
* 通过阅读
```
/usr/share/bro/base/files/extract/main.bro
``` 
的源代码
![image](https://github.com/wq0712/ns/blob/master/2017-2/lab4/main_bro.PNG?raw=true)
了解到该文件名的最右一个-右侧对应的字符串FHUsSu3rWdP07eRE4l是files.log中的文件唯一标识。
* 查看files.log，可以得到该文件提取自FTP会话，并得到该流量的conn_uids为CNg1Xh4tSyepI7CLng
![image](https://github.com/wq0712/ns/blob/master/2017-2/lab4/files_log.PNG?raw=true)
* 该C3hfjY1u7FHHBy7sL会话标识在conn.log中可以找到对应的IP五元组信息。 通过conn.log的会话标识匹配，我们发现该PE文件来自于IPv4地址为：98.114.205.102的主机。 
* ![image](https://github.com/wq0712/ns/blob/master/2017-2/lab4/conn_log.PNG?raw=true)