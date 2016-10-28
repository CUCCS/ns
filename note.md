
#《三种或三种以上不同SSH蜜罐应用实验对比分析报告》
 


##实验原理以及基本工具认识

###SSH基本认识
Secure Shell（[https://zh.wikipedia.org/wiki/Secure_Shell](https://zh.wikipedia.org/wiki/Secure_Shell)）为一项创建在应用层和传输层基础上的安全协议，为计算机上的Shell（壳层）提供安全的传输和使用环境。SSH是目前较可靠，专为远程登录会话和其他网络服务提供安全性的协议。利用SSH协议可以有效防止远程管理过程中的信息泄露问题。通过SSH可以对所有传输的数据进行加密，也能够防止DNS欺骗和IP欺骗。

但是安全级别低的SSH服务也会造成威胁 ，例如：


1. 针对SSH弱口令爆破攻击 &%对Linux服务器的控制利用
2.  SSH弱口令爆破。比如2010年SANS互联网安全监控中心又对分布式SSH口令爆破威胁发出警报
-  Linux服务器的控制与利用。 比如利用受控Linux服务器进行进一步攻击：扫描探测、渗透攻击、架设代理、部署僵尸网络


###蜜罐（honeypot）
([https://en.wikipedia.org/wiki/Honeypot_(computing](https://en.wikipedia.org/wiki/Honeypot_(computing))
蜜罐通常伪装成看似有利用价值的电脑系统，并提供一定的漏洞，是网络管理员设下的“ 黑匣子”，用来吸引黑客攻击。蜜罐中还装有监控软件，用以收集入侵数据，并且监视黑客入侵后的举动。

### SSH蜜罐实验工具

----------


 

* Kojoney （[http://kojoney.sourceforge.net/](http://kojoney.sourceforge.net/)）
是一款非常棒的低交互式 SSH 蜜罐，以 Python 语言编写。安装 Kojoney 之后，它会在机器上模拟出一 个 SSH 服务，当互联网上的攻击者尝试连接该服务端口，就会被欺骗到蜜罐中，攻击者的口令 猜测记录和攻击源 IP 地址都会被记录下来，而一旦攻击者猜测成功预先设定的用户名口令之后，他们就可以进一步地向 Kojoney 发出一些 shell 命令，Kojoney 对这些命令都会返回预先定义的响应消息，来愚弄攻击者
 
 

1. Kippo（[http://code.google.com/p/kippo/](http://code.google.com/p/kippo/)）则是受 Kojoney 的启发，它在 Kojoney 基础上能够进一步提供更加真实的 shell 交互环境，比如支持对 一个文件系统目录的完全伪装，允许攻击者能够增加或者删除其中的文件；包含一些伪装的文件 内容，如/etc/passwd 和/etc/shadow 等攻击者感兴趣的文件；以 UML（User Mode Linux）兼容格式来记录 shell 会话日志，并提供了辅助工具能够逼真地还原攻击过程；引入很多欺骗和愚弄攻 击者的智能响应机制，往往会让攻击者对自己的智商产生怀疑，故而是一种中等交互级别的SSH蜜罐软件
 


1. Cowrie([http://www.kitploit.com/2015/07/cowrie-ssh-honeypot.html](http://www.kitploit.com/2015/07/cowrie-ssh-honeypot.html)) Cowrie是在kippo基础上开发的中型交互式SSH蜜罐，可以对暴力攻击、入侵等黑客行为进行记录，增加了SFPT支持，SSH协议更新等新功能



1. HonSSH([http://www.freebuf.com/sectool/11777.html](http://www.freebuf.com/sectool/11777.html)) HonSSH是一个高交互蜜罐解决方案,在攻击者与蜜罐之间，可以创建两个独立的SSH链接
  
  
 


