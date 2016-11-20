# fail2ban 基础搭建与防止ssh暴力破解

* **实验环境**
	* 虚拟机：
		* Victim : 
			* Ubuntu16.04 
			*  ***IP:192.168.0.1***
			*  user: **masker** ; **root**
			*  password: **123**
		* Attacker : 
			* Kali-rolling 
			*  ***IP:192.168.0.2***
	* 网络模式：
		* 内部网络（intnet）
* **实验原理**
	* fail2ban会自动根据远程ssh连接输入密码错误次数来修改本地iptables的防火墙规则，进而实现防止暴力破解ssh攻击。
* **实验过程**
	* Victim :
		* fail2ban的搭建与配置
		* ssh配置
		* iptables配置
	* Attacker :
		* 使用kali自带工具hydra进行暴力破解
	* 观察实验结果

* **配置操作**

	* 首先确保两台虚拟机开启了ssh服务，尝试使用Attacker通过ssh连接到Victim，成功连接后如下：

		<pre>ssh masker@192.168.0.1</pre>
		![]("image\1.JPG")
	* 在Victim上安装fail2ban：
		<pre>
		sudo apt-get update
    	sudo apt-get install fail2ban
		</pre>
	* fail2ban配置文件为/etc/fail2ban/jail.conf，为了防止误操作，fail2ban支持在该目录下引用jail.local，并以优先检查jail.local+默认检查jail.conf的方式进行配置，生成jail.local文件并附加#作为注释：
		<pre>awk '{ printf "# "; print; }' /etc/fail2ban/jail.conf | sudo tee /etc/fail2ban/jail.local</pre>
	* 打开jail.local配置文件，可以对[DEFAULT]下几个常用参数做自定义控制：
		* <pre>bantime = 600  ; 设定了禁止访问的时间，单位是s</pre>
		* <pre>
			findtime = 600 ; 限定了重新尝试的时间
			maxretry = 3 ; 在findtime限定的时间内重新尝试的次数
		  	</pre>
		  	<pre>
			#发送提醒邮件服务
			destemail = root@localhost ;邮件目的地址
			sendername = Fail2Ban	;邮件原地址
			mta = sendmail ;动作设定
			</pre>
			<pre>
			action = $(action_)s ;动作参数：如action_mw为发送邮件；action_mwl为发送带logs的邮件。
			</pre>
	* fail2ban还支持对更多的服务提供保护功能，在jail.conf文件中可以找到，对每一个服务的保护开启控制可以使用enabled = true/false来控制。

	* 配置完成后重新启动fail2ban来更新配置：
		<pre>service fail2ban restart</pre>
	* 配置防火前：在配置之前ubuntu的防火墙默认不做拦截，对于所有的INPUT/FORWARD/OUTPUT全部接受，因此在做实验之前需要做自定义配置：
		* <pre>sudo iptables -A INPUT -i lo -j ACCEPT ;允许本地回环地址操作</pre>
		* <pre>sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT; 允许建立连接</pre>
		* <pre>sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT;允许接受通过22端口的INPUT流量</pre>
		* <pre>sudo iptables -A INPUT -p tcp -m multiport --dports 80,443 -j ACCEPT;允许接受80,443端口的INPUT流量</pre>
		* <pre>sudo iptables -A INPUT -j DROP;丢弃其他的INPUT流量</pre>
		* 查看防火墙配置：
		* <pre>iptables -S</pre>
		* fail2ban关闭时：
			![]("image\2.JPG")
		* fail2ban开启时：
			![]("image\3.JPG")
		* 可见上图中，iptables已经成功将fail2ban配置的防火墙规则添加了进来。
	* 可以通过以下命令对防火墙进行保存操作：
	* <pre>sudo dpkg-reconfigure iptables-persistent</pre>
* **fail2ban配置前后攻击效果**
	* fail2ban配置前:
		* Attacker使用hydra工具进行暴力破解攻击：
		* <pre>hydra -l masker -P /usr/share/wordlists/fasttrack.txt 192.168.0.1 ssh </pre>
			* 效果如下： 
			* ![]("image\4.JPG")
			* Victim的防火墙规则无变化：
			* ![]("image\5.JPG")
	* fail2ban配置后：
		* Attacker再次进行暴力破解发现已经无法成功：
		* ![]("image\6.JPG")
		* Victim防火墙规则，增添了对攻击者ip的限制：
		* ![]("image\7.JPG")
		* Attacker尝试普通的ssh连接也会失败：
		* ![]("image\8.JPG")
* 参考：
	* [How To Protect SSH with Fail2Ban on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-protect-ssh-with-fail2ban-on-ubuntu-14-04)
	* [How To Set Up a Firewall Using Iptables on Ubuntu 14.04 ](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-using-iptables-on-ubuntu-14-04)
	* [How To Use SSH to Connect to a Remote Server in Ubuntu ](https://www.digitalocean.com/community/tutorials/how-to-use-ssh-to-connect-to-a-remote-server-in-ubuntu)
	* [fail2ban](http://www.fail2ban.org/wiki/index.php/Main_Page)
	* [ssh-brute-force-the-10-year-old-attack-that-still-persists](https://blog.sucuri.net/2013/07/ssh-brute-force-the-10-year-old-attack-that-still-persists.html)