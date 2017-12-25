## 一.使用bro来完成取证分析 ##

1.安装bro

`apt-get install bro bro-aux`

2.实验环境基本信息


![](https://github.com/canyousee/ahelloworld/raw/master/bro_image/1.png)


3.编辑bro配置文件
  
  
- 编辑/etc/bro/site/local.bro,在文件尾部追加两行新配置代码

 ` @load frameworks/files/extract-all-files`

  `@load mytuning.bro`

![](https://github.com/canyousee/ahelloworld/raw/master/bro_image/2.png)

- 在/etc/bro/site/目录下创建新文件mytuning.bro,``内容为

  `redef ignore_checksums=T;`

![](https://github.com/canyousee/ahelloworld/raw/master/bro_image/1.2.png)

4.使用bro自动化分析pcap文件

  `bro -r attack-trace.pcap /etc/bro/site/local.bro`
 
> 出现警告信息
> `WARNING: No Site::local_nets have been defined. It's usually a good idea to define your local networks.`
> 
> 对于本次入侵取证实验来说没有影响
> 
> 如果要解决上述警告信息，也很简单，同样是编辑mytuning.bro,增加一行变量定义 
> 
`redef Site::local_nets={192.150.11.0/24};`

5.在attack-trace.pcap文件的当前目录下会生成一些.log文件和一个extract_files目录。在目录下发现一个文件extract-1240198114.648099-FTP_DATA_FHUsSu3rWdP07eRE41。

![](https://github.com/canyousee/ahelloworld/raw/master/bro_image/6.png)

将文件上传到virustotal，发现是一个已知的后门程序。

![](https://github.com/canyousee/ahelloworld/raw/master/bro_image/4.png)

6.阅读/usr/share/bro/base/files/extract/main.bro 源代码

![](https://github.com/canyousee/ahelloworld/raw/master/bro_image/8.png)


发现files.log的文件唯一标识，查看files.log，发现该文件提取自网络会话标识（bro根据IP五元组计算出的一个会话唯一性散列值）的FTP会话


![](https://github.com/canyousee/ahelloworld/raw/master/bro_image/3.png)

该会话标识在conn.log中可以找到对应的IP五元组信息

![](https://github.com/canyousee/ahelloworld/raw/master/bro_image/5.png)


---
## 二.bro的一些其他技巧 ##

-使用正确的分隔符进行过滤显示的重要性
  
![](https://github.com/canyousee/ahelloworld/raw/master/bro_image/10.png)


-查看bro的超长行日志时的横向滚动技巧

![](https://github.com/canyousee/ahelloworld/raw/master/bro_image/11.png)


-使用bro-cut 查看日志中关注的数据列


![](https://github.com/canyousee/ahelloworld/raw/master/bro_image/12.png)



