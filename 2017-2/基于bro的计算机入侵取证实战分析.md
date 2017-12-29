### bro 取证分

- 实验目标：分析流量包中的extract file和log文件得到攻击主机的IP 
 
  - 实验环境：

    ![1](pic/1.png)

  - 设置bro
     - 编辑 /etc/bro/site/local.bro

    ![2](pic/2.png)

    - 创建并编辑文件mytuning.bro:redef ignore_checksums = T;

  - 数据包分析:bro -r attack-trace.pcap /etc/bro/site/local.bro

    ![3](pic/3.png)
    
  - 编辑mytuning.bro，增加一行变量定义：redef Site::local_nets = { 192.150.11.0/24 };
    - 解决警告信息
   
    ![6](pic/6.png) 

  - 发现的后门程序
  
    ![8](pic/8.png) 
  
  - 新增2个日志文件，会报告在当前流量（数据包文件）中发现了本地网络IP和该IP关联的已知服务信息
 
    ![4](pic/4.png)

  - 阅读/usr/share/bro/base/files/extract/main.bro的源代码

    ![7](pic/7.png)

     - 了解到该文件名的最右一个-右侧对应的字符串FHUsSu3rWdP07eRE4l是 files.log 中的文件唯一标识

  - 查看files.log，可以得到，该文件提取自FTP会话，并得到该流量的conn_uids为CCL51gleQJRL36JZIj
 
     - 根据conn.log文件中的会话表示定位到IP

    ![5](pic/5.png)



