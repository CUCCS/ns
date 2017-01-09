## Fail2Ban怎样保护Apache服务器

> 运行Apache服务器时,通过一些安全措施来保护站点和用户是很重要的。防火墙策略和限制访问某些地区使用密码身份验证可以作为保护系统的起点。然而，任何可公开访问的密码提示很可能吸引来自恶意用户甚至机器人的暴力尝试。设置fail2ban可以帮助缓解这一问题。当用户多次未能通过身份验证（或其他可疑的活动）时，fail2ban锁定ban的IP地址，动态地修改正在运行的防火墙策略


### 安装 Apache 和配置Basic身份验证
可以看文件夹下另一篇 配置能实现Basic认证的apache.md 里面有详细的解释

### 安装Fail2Ban
		apt-get install fail2ban

### 调整Fail2Ban常规设置

* 调整配置文件，fail2ban需要通过这些来确定监视哪个应用日志，以及当发现攻击时要采取什么行动fail2ban有许多jail 定位到/etc/fail2ban，里面这些文件都是很有用哒，(●'◡'●) 其中的jail.conf就是关于jail的配置文件啦

* 先将此文件复制到 /etc/fail2ban/jail.local。当系统更新提供了一个新的默认文件的时候，这可以防止我们的更改被覆盖
	
	cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
  
![Image text](https://github.com/Zhaojytt/ns/blob/master/2016-2/zjy/img_folder/6.png)


* 可以更改设置啦
	* 首先是一些默认的设置
		* ignoreip 白名单 里面的ip不会被fail2ban监视
		* bantime  被ban的ip所要禁止的时间
		* findtime maxretry如果用户在findtime设置的时间内尝试次数超过 maxretry就会被禁止 
	* 邮件通知（当被攻击的时候可以收到邮件）
		* 首先要安装一个MTA，所以先跳过，之后做
	* 监视Apache日志
		* 配置[Apache] 
		* 其他的一些监狱
			* [apache-noscript] 禁止那些寻找可执行利用的脚本的用户
			* [apache-overflows] 禁止那些用长又可疑的url的用户
			* ...
### 重启fail2ban
		service fail2ban restart

### 一些使用说明
* 如果你想快速查看打开了那些监狱，可以酱
		
		fail2ban-client status
    
    ![Image text](https://github.com/Zhaojytt/ns/blob/master/2016-2/zjy/img_folder/7.png)
    
    * 如果你想看firewall的变化，可以酱

		iptables -S
		
	* 开启之前		
    ![Image text](https://github.com/Zhaojytt/ns/blob/master/2016-2/zjy/img_folder/10.png)
 	* 开启之后
    ![Image text](https://github.com/Zhaojytt/ns/blob/master/2016-2/zjy/img_folder/8.png)
* 如果你想看某个监狱的具体信息，可以酱

		fail2ban-client status apache
    ![Image text](https://github.com/Zhaojytt/ns/blob/master/2016-2/zjy/img_folder/9.png)

### 测试example看下一篇啦
