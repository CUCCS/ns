# FAIL2BAN 学习总结

> 浏览了许多文档，以下是我学习之后自己总结整理的一些points，如在之后的实验中有新的发现、新的知识，定再做补充；如整理内容有误，望批评指出，定及时改正。
        
		
## Fail2Ban 工作原理
Servers do not exist in isolation, and those servers with only the most basic SSH configuration can be vulnerable to brute force attacks. Fail2Ban is an intrusion prevention framework written in the Python programming language ，which provides a way to automatically protect the server from malicious signs. The program works by scanning through log files and reacting to offending actions such as repeated failed login attempts.It acts like:
- scans SSH, ProFTP, Apache logs etc
- bans IPs that show the malicious signs -- too many password failures, seeking for exploits, etc.
- update firewall rules | uses iptables profiles to block brute-force attempts.

服务器的存在不是孤立的。当面对暴力破解攻击时，那些只有SSH basic认证的服务器会非常的脆弱。Fail2Ban是一个用python编写的防止非法入侵的框架，它提供了一个方法，去自动地保护这些服务器远离恶意入侵信号。它通过扫描日志文件，对入侵行为作为反击（比如说多次尝试登陆失败就可以看作一个入侵行为）

- 扫描日志文件(SSH,ProFTP, Apache等等的日志文件)，

- 禁止有恶意迹象的IP (密码多次失败，寻找漏洞等等)通过

- 更新防火墙规则，调用iptables来阻挡暴力破解的尝试。_




## Fail2Ban支持服务解析
它的功能非常强大，我查阅了一下，它支持的服务主要有sshd,apache,qmail,proftpd,sasl等等

### **sshd**
OpenSSH服务，是一个典型的独立守护进程(standalone daemon)，但也可以根据需要通过网络守护进程(Internet Daemon)-inetd或Ineternet Daemon's more modern-xinte加载。OpenSSH服务可以通过/etc/ssh/sshd_config文件进行配置。

_守护进程：在linux或者unix操作系统中，守护进程（Daemon）是一种运行在后台的特殊进程，它独立于控制终端并且周期性的执行某种任务或等待处理某些发生的事件。由于在linux中，每个系统与用户进行交流的界面称为终端，每一个从此终端开始运行的进程都会依附于这个终端，这个终端被称为这些进程的控制终端，当控制终端被关闭的时候，相应的进程都会自动关闭。但是守护进程却能突破这种限制，它脱离于终端并且在后台运行，并且它脱离终端的目的是为了避免进程在运行的过程中的信息在任何终端中显示并且进程也不会被任何终端所产生的终端信息所打断。它从被执行的时候开始运转，直到整个系统关闭才退出。_


### **Apache**
Apache HTTP Server（简称Apache）是一个开放源码的网页服务器，可以在大多数计算机操作系统中运行，由于其多平台和安全性被广泛使用，是最流行的Web服务器端软件之一。它快速、可靠并且可通过简单的API扩展，将Perl/Python等解释器编译到服务器中。[2]  

### **qmail**
作为Linux下面主流的邮件系统内核，大量著名的商业邮件系统都是在Qmail内核下开发，比如Hotmail等。Qmail具有安装方便、安全性高、邮件结构合理、支持SMTP服务、队列管理、邮件反弹、基于域名的邮件路由、SMTP传输、转发和邮件列表、本地(邮件)传送、POP3 服务等强大的功能。它已经逐渐替代传统的Sendmail成为linux下邮件系统内核的主流选择

### **proftpd**
FTP服务器软件

###  **sasl**
SASL全称Simple Authentication and Security Layer，是一种用来扩充C/S模式验证能力的机制。在Postfix可以利用SASL来判断用户是否有权使用转发服务，或是辨认谁在使用你的服务器。SASL提供了一个通用的方法为基于连接的协议增加验证支持




## Fail2Ban功能评价
Fail2Ban is able to reduce the rate of incorrect authentications attempts however it cannot eliminate the risk that weak authentication presents. Configure services to use only two factor or public/private authentication mechanisms if you really want to protect services.

Fail2Ban 是能够减少不正确的身份验证尝试的速率，但它不能消除弱身份验证的风险。如果想要真正地保护，还是要配置双重验证或者公私钥身份验证机制。


## Fail2Ban查阅文档
> [http://www.fail2ban.org/wiki/index.php/Main_Page](url)

> [https://help.ubuntu.com/community/Fail2ban](url)

> [https://www.digitalocean.com/community/tutorials/how-to-protect-ssh-with-fail2ban-on-centos-6](url)

...
