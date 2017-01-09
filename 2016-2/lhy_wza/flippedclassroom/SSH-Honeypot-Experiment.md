#三种或三种以上不同SSH蜜罐应用实验对比分析报告

###SSH蜜罐 实验原理
-  模拟为SSH网络服务进程, 记录每次SSH口令暴力破解所尝试使用的用户名与口令
-   并在口令猜测成功之后为攻击者提供模拟的shell 执行环境
-   对攻击源IP 地址、使用的SSH 客户端类型、输入的控制命令以及下载的攻击工具文件进行捕获与记录.

###实验环境
- virtualbox
- kali-honeypot用于设置SSH蜜罐系统引诱黑客进行入侵
- kali-attacker作为攻击主机用于测试
- 安装蜜罐

###实验过程
##Kippo

      1，rehl5下下载准备环境的RPM包
      
      2，安装这些准备环境包

      3，准备Kippo的日志记录环境(Kippo需要把数据存放在数据库中，所以单独存放在一个Kippo的库，然后生成Kippo需要的数据表)

      4，安装kippo，以非root用户运行     ./start.sh

      5，安装完毕，在客户机上进行远程登录

      6，通过日志或数据库查看记录

###分析数据信息
1. data: 存放ssh key,lastlog.txt和userdb.txt lastlog.txt:last命令的输出,即存储了登陆蜜罐的信息,也可以伪造 userdb.txt:可以登陆的用户,可以给一个用户设置多个密码,一个用户一行 格式为username:uid:password

2. honeyfs: etc目录中存在group hostname hosts issue passwd resolv.conf shadow这些 文件,cat /etc/filename目录中对应的文件时会显示这些文本文件中的内容. proc目录中存在cpuinfo meminfo version这些文件,cat /proc/filename目录中对应的文件时会显示这些文本文件中的内容.

3. log: 存放日志文件的地方,该目录包含一个kippo.log文件和tty目录 kippo.log:是存放启动记录,那些IP连接等信息 tty目录是每一个ssh过来后操作的记录,可以使用strings filename直接看到里面的内容

4. txtcmds: 存放命令的地方,这些命令都是文本文件,执行相关命令的时候直接显示文件内容

5. kippo: 核心文件,模拟一些交互式的命令等等

6. dl: wget等等下载的文件存放的地方



###参考链接
关于Kippo的安装、配置参考以下文章

[http://code.google.com/p/kippo/](http://code.google.com/p/kippo/)
[http://www.haiyun.me/archives/centos-install-kippo.html](http://www.haiyun.me/archives/centos-install-kippo.html)
[http://297020555.blog.51cto.com/1396304/553382/](http://297020555.blog.51cto.com/1396304/553382/)
[http://drops.wooyun.org/papers/4578](http://drops.wooyun.org/papers/4578)
[https://github.com/desaster/kippo](https://github.com/desaster/kippo)







###实验结果分析对比