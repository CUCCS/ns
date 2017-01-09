# DNS域传送漏洞及DNS信息收集实例讲解
***
## 1. DNS域传送漏洞原理
* 恶意用户可以通过dns域传送获取被攻击域下所有的子域名。会导致一些非公开域名（测试域名、内部域名）泄露。而泄露的类似内部域名，其安全性相对较低，更容易遭受攻击者的攻击，比较典型的譬如内部的测试机往往就会缺乏必要的安全设置。<sup>[1]</sup>
	
	[参考链接：[1]https://help.aliyun.com/knowledge_detail/37529.html](https://help.aliyun.com/knowledge_detail/37529.html) 
* DNS服务器分为：主服务器、备份服务器和缓存服务器。在主备服务器之间同步数据库，需要使用“DNS域传送”。域传送是指后备服务器从主服务器拷贝数据，并用得到的数据更新自身数据库。若DNS服务器配置不当，可能导致匿名用户获取某个域的所有记录。造成整个网络的拓扑结构泄露给潜在的攻击者，包括一些安全性较低的内部主机，如测试服务器。凭借这份网络蓝图，攻击者可以节省很少的扫描时间。<sup>[2]</sup>
	
	[参考链接：[2]http://www.lijiejie.com/dns-zone-transfer-1/](http://www.lijiejie.com/dns-zone-transfer-1/) 

## 2. 实验：演示学校DNS域传送漏洞
* dig command
	* dig是一个用于查询DNS名称服务器的灵活工具。 它执行DNS查找并显示从查询的名称服务器返回的答案。 <sup>[3]</sup>
	
		[参考链接：[3]https://linux.die.net/man/1/dig](https://linux.die.net/man/1/dig) 
	* 实验：
		1. 	获取解析其域名的DNS域名服务器
		
			> dig example.com 
		2. 查看域数据传输
		
			> dig @ns1.example.com example.com axfr
* host command
	*  host命令相对dig提供的一些不必要的信息来说更简洁快速<sup>[4]</sup>
	
		[参考链接：[4]http://kumu-linux.github.io/blog/2013/06/19/nslookup-dig-host/](http://kumu-linux.github.io/blog/2013/06/19/nslookup-dig-host/) 
	*  实验：
		1. 获取解析其域名的DNS域名服务器
		
			> host -t ns example.com
		2. 查看域数据传输

			> host -l example.com ns1.example.com

## 3. 实验：搭建DNS解析服务器，演示导致DNS域传送漏洞的配置，修复错误配置
* 搭建DNS服务器<sup>[5]</sup>
	
	 [参考链接：[5]https://www.digitalocean.com/community/tutorials/how-to-configure-bind-as-a-caching-or-forwarding-dns-server-on-ubuntu-14-04](https://www.digitalocean.com/community/tutorials/how-to-configure-bind-as-a-caching-or-forwarding-dns-server-on-ubuntu-14-04) 
* 添加自定义DNS域信息<sup>[6]</sup>
	
	 [参考链接：[6]https://www.digitalocean.com/community/tutorials/how-to-configure-bind-as-an-authoritative-only-dns-server-on-ubuntu-14-04](https://www.digitalocean.com/community/tutorials/how-to-configure-bind-as-an-authoritative-only-dns-server-on-ubuntu-14-04) 
* 导致DNS域传送漏洞的配置
	>  e.g. allow-transfer { any; };
* 修复错误配置
	> e.g. allow-transfer { 192.168.0.10; };

## 4. 其他可能获得的DNS信息的渠道
* 一个在线DNS信息收集工具：http://www.sitedossier.com/
* DNS字典爆破：dnsmap dnsenum fierce
	1. dnsenum：利用dnsenum自带的字典爆破
		> dnsenum -f /usr/share/dnsenum/dns.txt -dnsserver 8.8.8.8 cuc.edu.cn -a cuc.txt
	2. dnsmap
		> dnsmap cuc.edu.cn -w /usr/share/dnsenum/dns.txt
	3. fierce：利用fierce自带的字典爆破
		> fierce -dnsserver 8.8.8.8 -dns cuc.edu.cn -wordlist /usr/share/fierce/hosts.txt
* 搜索引擎查询
	> site:163.com
* 爬虫爬取页面提取子域名
* 通过 HTTPS 证书搜集
	 
	参考链接：[7]FreeBuf公众号 《子域名搜集思路与技巧梳理》