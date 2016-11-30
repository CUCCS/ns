## 配置能实现Basic认证的apache

### 安装 Apache 实用工具软件包
* 为了创建存储密码访问受限制所需的文件，要使用一个称为 htpasswd 实用程序。它可以在在 Ubuntu 资料库内 apache2 utils包中找到。直接安装就好啦（以下操作都在root权限下）

		apt-get update
		apt-get install apache2 
		apt-get install apache2-utils

### 创建密码文件

* 使用htpasswd来创建一个密码文件.htpasswd 隐藏在路径/etc/apache2之下（创建第一个用户的时候需要加属性 -c，之后想要再填加其他用户时不加-c）

		htpasswd -c /etc/apache2/.htpasswd Abby

![image](/images/1.png)

* 输入密码：asd123

* 用cat查看文件的内容

		cat /etc/apache2/.htpasswd
![image](/images/2.png)

### 配置身份验证

* 既然已经有Apache 可以读取的用户Basic认证（用户名和密码）的文件了，现在呢，需要配置 Apache 服务使他在打开我们保护的内容之前先查看这个文件

	##### 使用.htaccess 文件配置访问控制
	* 编辑 Apache 的主配置文件允许.htaccess 文件︰
	
				cd /etc/apache2/sites-available
				vi default
	![image](/images/3.png)

	* 添加.htaccess 文件到希望限制的目录 我的是/var/www（因为时隐藏的文件，所以ls时是看不到的）
	![image](/images/4.png)



### 重启apache
			
		service apache2 restart

![image](/images/5.png)

> 配置成功啦^_^


[https://www.digitalocean.com/community/tutorials/how-to-set-up-password-authentication-with-apache-on-ubuntu-14-04](url)
...再补充


