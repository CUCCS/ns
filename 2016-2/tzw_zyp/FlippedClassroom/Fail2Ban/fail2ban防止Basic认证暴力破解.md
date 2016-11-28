# fail2ban 防止Basic暴力破解

* **实验环境**
	* 虚拟机：
		* Victim : 
			* Ubuntu14.04.3 
			*  ***IP:192.168.0.1***
			*  user: **mz** ; **root**
			*  password: **123456**
		* Attacker : 
			* Kali-rolling 
			*  ***IP:192.168.0.2***
	* 网络模式：
		* 内部网络（intnet）
* **实验原理**
	* fail2ban会自动根据basic认证中密码账号的输入错误次数来修改本地iptables的防火墙规则，进而实现防止basic暴力破解。
* **实验过程**
	* Victim :
		* basic认证的搭建配置
		* fail2ban的搭建与配置
		* iptables配置
	* Attacker :
		* 使用kali自带工具hydra进行暴力破解
	* 观察实验结果

* **配置操作**

	* 首先在Victim中进行Nginx Web服务器上basic认证的设置，然后搭建配置fail2ban：
	* 在Victim上安装Nginx服务器：
 	  <pre>
		 apt-get update
    	 apt-get install nginx
		</pre>
     * 在Victim上创建一个密码文件，包含着认证所需的用户名和密码组合，这里使用OpenSSL来创建此文件，在/ etc / nginx配置目录中创建一个名为.htpasswd的隐藏文件，以存储我们的用户名和密码组合：
		<pre>
		sh -c "echo -n 'mzzy:' >> /etc/nginx/.htpasswd"
    	sh -c "openssl passwd -apr1 >> /etc/nginx/.htpasswd"  //通过键入以下内容为用户名添加加密的密码条目
		</pre>
        * 设置完毕后我们也可以查看一下我们设置的密码文件内容：
	 * ![]("image\1.PNG")
    * 在Victim上进行Nginx服务器的密码验证配置，之前我们已经创建了一个Nginx可以读取的用户密码文件，需要配置Nginx使访问我们受保护的内容之前需要检查此文件：
		<pre>
		leafpad /etc/nginx/sites-enabled/default  //打开Ubuntu中Nginx的默认服务块文件
		</pre>
      * 在文件中添加图上黄色部分的代码，设置对特定位置内的限制，这里我们限制了整个文档根目录的位置块：
         * ![]("image\2.PNG")
            *在此位置块中，使用auth_basic指令打开身份验证且在用户认证成功后选择向用户显示的领名。 用auth_basic_user_file指令，将Nginx指向我们创建的密码文件：
       * 保存此文件，并且重启Nginx使操作生效。
       * 完成以上操作，打开Attacker，内部网络PING通，访问Victim，设置结果展示如下：
        * ![]("image\3.PNG")
	* 在Victim上安装fail2ban（以下操作与组员之前所在SSH中fail2ban配置基本一致，小部分操作习惯的差别）：
		<pre>
		apt-get update
    	apt-get install fail2ban 
		</pre>
	  * 调整fail2ban使用的配置文件，以确定要监视的应用程序日志以及在发现违规条目时应采取的操作。fail2ban配置文件为/etc/fail2ban/jail.conf，将此文件复制到/etc/fail2ban/jail.local。 如果程序包更新提供了一个新的默认文件，这将防止我们的更改被覆盖：
		<pre>
        cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
        </pre>
	  * 打开jail.local配置文件，可以对[DEFAULT]下几个常用参数做自定义控制：
	    <pre>
		leafpad /etc/fail2ban/jail.local
		</pre>
		* <pre>bantime = 360  ; 设定了禁止访问的时间，单位是s</pre>
		* <pre>
			findtime = 600 ; 限定了重新尝试的时间
			maxretry = 3 ; 在findtime限定的时间内重新尝试的次数
		  	</pre>
		  
	  * fail2ban还支持邮件服务以及对更多的服务提供保护功能，在jail.conf文件中可以找到，对每一个服务的保护开启控制可以使用enabled = true/false来控制。

	  * 配置完成后重新启动fail2ban来更新配置：
		<pre>service fail2ban restart</pre>
	
	  * 查看防火墙配置：
		* <pre>iptables -S</pre>
		* 配置完fail2ban开启时：
		 * ![]("image\4.PNG")
		关闭的图忘记截了，跟组员实验中关闭时截图基本一致，可见上图中，iptables已经成功将fail2ban配置的防火墙规则添加了进来。
       * 如果想看到由jail详细操作信息，使用如下命令
	      <pre>fail2ban-client status nginx-http-auth</pre>
          *效果如图：
              * ![]("image\5.PNG")
               现在可以看出没有任何操作。
* **fail2ban配置前后攻击效果**
  * 这里采用一个命令来查看那些尝试的操作。
    <pre>tail -f /var/log/nginx/error.log</pre>
    * ![]("image\6.PNG")
	* fail2ban配置前:
		* Attacker使用hydra工具进行暴力破解攻击：
		* <pre>hydra -l mzzy -P /usr/share/wordlists/fasttrack.txt http-get://192.168.0.1
		 </pre>
			* 效果如下： 
			* ![]("image\9.PNG")
			* Victim的防火墙规则无变化
	* fail2ban配置后：
		* Attacker再次进行暴力破解发现已经无法成功：
		* ![]("image\11.PNG")
		* Victim防火墙规则，增添了对攻击者ip的限制：
		* ![]("image\12.PNG")
		* tail命令后的截图：
		* ![]("image\10.PNG")
		再进行访问操作就连接不上了。

* * 参考：
	* [How To Set Up Password Authentication with Nginx on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-password-authentication-with-nginx-on-ubuntu-14-04)
	* [How To Protect an Nginx Server with Fail2Ban on Ubuntu 14.04 ](https://www.digitalocean.com/community/tutorials/how-to-protect-an-nginx-server-with-fail2ban-on-ubuntu-14-04)
	
