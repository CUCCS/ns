#HTTPS协议中间人攻击的可能性探究与实验

回顾[2003年黑帽大会](https://www.blackhat.com/presentations/bh-europe-03/bh-europe-03-valleri.pdf)相关演讲内容，先来看看经典的中间人攻击(MITM):

- MITM - Different attacks in different scenarios: 

  - LOCAL AREA NETWORK: 

    - ARP poisoning 
    - DNS spoofing 
    - STP mangling 
    - Port stealing

  - FROM LOCAL TO REMOTE (through a gateway): 

    - ARP poisoning 
    - DNS spoofing 
    - DHCP spoofing 
    - ICMP redirection 
    - IRDP spoofing 
    - route mangling 

  - REMOTE: 

    - DNS poisoning 
    - traffic tunneling
    - route mangling


SSL/TLS机制的出现，使得上述中间人攻击得到有效的遏制。
但安全对抗从未停止，MITM已经演化出针对SSL的中间人攻击。
DNS泄露和ARP欺骗则是实现此类攻击的前提，即获知请求发送者的IP地址。
此外，还提供了其他获取IP的方法，供参考。

详情描述如下：


###DNS查询泄漏（经由DNS解析服务器）与MITM

在某些情况下，即使连接到 VPN，操作系统仍然继续使用其默认的 DNS 服务器（比如在本地解析），导致DNS泄露。

Click it. -> [DNS泄露在线测试](https://www.dnsleaktest.com/) 

DNS查询泄露漏洞存在的主要场景及其解决方案：

1. ZoneTransfer域传送漏洞 - DNS服务器的主备数据同所使用的功能

    详见tjy组翻转课堂。

2. 互联网服务提供商(ISP)给虚拟专用网络(VPN)用户挖坑

    通常情况下，DNS服务器由ISP提供。与此同时，ISP使用透明DNS代理技术，拦截所有DNS查询请求(TCP/UDP端口53)，有效地迫使用户使用他们的 DNS 服务器进行所有的 DNS 查找。这意味着他们可以监控、记录任何该用户发送到服务器的请求。
    
    为了躲避这种监控，用户使用VPN，DNS请求本应该通过VPN被定向到一个匿名的DNS服务器，防止ISP监视此次网络连接。不幸的是，有时用户的浏览器会忽视打开的VPN，并会直接发送DNS请求到ISP。这就是一个DNS泄漏。这会导致用户认为自己实现了匿名通信，但事实上通信数据并不会得到保护。
    
    另外一种类似的情况是，VPN用户开启PAC模式，而非全局模式。这种情况下，浏览器需要先发送DNS请求到本地DNS服务器，即ISP提供的DNS服务器，然后再判断是否通过VPN进行通信。
    
    * 针对VPN的解决方案：
    
      *  使用 VPN 服务商提供的 DNS 服务器，包括使用DNSCrypt加密DNS传输。防止原生ISP或者hacker截获DNS查询请求。
     * 更改默认的DNS服务器。
     * 使用带有DNS泄漏保护功能的VPN。
     * 使用VPN监控软件，某些VPN监控软件还可以修复DNS泄漏。 
     * 禁用Teredo，IPv4和IPv6之间的转换可能会引起DNS泄漏。

* 参考链接：[当DNS泄漏让VPN不再安全，我们该怎么办？](http://www.freebuf.com/articles/network/67591.html) 

__DNS查询泄露造成的后果__
泄露域名服务器的IP地址或者关联网址，为hacker实现DNS spoofing制造机会。也就是说当hacker悉知网络层的通信规则，就可以从链路层进行中间人攻击。

相关知识拓展：

* DNS污染

  - DNS劫持就是指用户访问一个被标记的地址时，DNS服务器故意将此地址指向一个错误的IP地址的行为。
  - 网通、电信、铁通的某些用户有时候会发现自己打算访问一个地址，却被转向了各种推送广告等网站，这就是DNS劫持。

* DNS劫持

  - DNS污染，指的是用户访问一个地址，国内的服务器(非DNS)监控到用户访问的已经被标记地址时，服务器伪装成DNS服务器向用户发回错误的地址的行为。
  - 访问Youtube、Facebook之类网站等出现的状况。


More>> [Crippling HTTPS with unholy PAC](https://www.blackhat.com/docs/us-16/materials/us-16-Kotler-Crippling-HTTPS-With-Unholy-PAC.pdf)

###ARP欺骗与MITM

最初，攻击者只要将网卡设为混杂模式，伪装成代理服务器监听特定的流量就可以实现攻击，这是因为很多通信协议都是以明文来进行传输的，如HTTP、FTP、Telnet等。后来，随着交换机代替集线器，简单的嗅探攻击已经不能成功，必须先进行ARP欺骗才行。

__URL流量操作__ 

实际操作命令：

1. 开启端口转发，（攻击者）允许本机像路由器那样转发数据包

   > echo 1 > /proc/sys/net/ipv4/ip_forward

2. ARP投毒，向主机XP声称自己(攻击者)就是网关Ubuntu 

    > arpspoof -i eth0 -t 10.23.2.4 10.23.2.5

3. ARP投毒，向网关Ubuntu声称自己(攻击者)就是XP 

    > arpspoof -i eth0 -t 10.23.2.5 10.23.2.4

* 注意: 当hacker停止投毒时，arpspoof将进行“clean up and re-arping”，发送正确的目的物理地址。  

__端口重定向攻击__

端口重定向接收到一个端口数据包的过程（如80端口），并且重定向它的流量到不同的端口（如8080）。实现这类型攻击的好处就是可以无止境的，因为可以随着它重定向安全的端口到未加密端口，重定向流量到指定设备的一个特定端口上。

具体操作步骤如下：

1. 开启路由转发攻击。执行命令如下所示：

    > echo 1 > /proc/sys/net/ipv4/ip_forward


2. 启动Arpspoof工具注入流量到默认网络。例如，默认网关地址为10.32.2.1。执行命令如下：

    > arpspoof -i eth0 10.23.2.1


3. 添加一条端口重定向的防火墙规则。执行命令如下所示：
 
    > iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080

* 执行以上命令后，没有任何输出。

以上设置成功后，当用户向网关10.23.2.1的80端口发送请求时，将会被转发为8080端口发送到攻击者主机上。


##针对SSL协议的中间人攻击

SSL原理:(待补充)

https握手过程的证书校验环节就是为了识别证书的有效性唯一性等等，所以严格意义上来说https下不存在中间人攻击，存在中间人攻击的前提条件是没有严格的对证书进行校验，或者人为的信任伪造证书。

- 存在中间人攻击原因：
    - 证书未校验
    - 部分校验
    - 证书链校验

* 参考链接：[浅析HTTPS中间人攻击与证书校验](www.evil0x.com/posts/26569.html)      

针对SSL，中间人攻击只可能发生在SSL的前提条件被破坏的时候，以下是一些示例：

1. 服务器私钥被盗取 - 意味着攻击者能够冒充服务器，而客户端并不知情。
2. 客户端置信于不可靠的CA（或者主密钥被盗取）- 无论谁获取了真实、可信的CA的私钥，他都可以生成证书从而冒充服务器，骗取客户端的信任。这就意味着，当服务器证书更换为另一个合法证书，浏览器并不会告知客户这件“小”事。
3. 客户端不与可信CA确认合法证书列表，这样一来，偷盗证书就可能合法化攻击者的身份。
4. 客户端被攻击，假CA被写入客户的可信CA列表。假冒的CA可以为不可信的服务器签名。

* 参考链接：[Answer: SSL and man-in-the-middle misunderstanding - Stack Overflow](http://stackoverflow.com/questions/14907581/ssl-and-man-in-the-middle-misunderstanding)



###伪造SSL证书


攻击基本原理：

1. 攻击者对目标客户端和网关发送ARP投毒攻击，污染它们的ARP缓存表。
2. 客户端在浏览器中输入 "https://mail.google.com/" 的网址，浏览器会尝试和 "https://mail.google.com/" 的443端口建立SSL连接，但是因为客户端受到了ARP投毒攻击，原本发往网关的数据包被发往了攻击者的主机。
3. 攻击者在本机使用iptables将接收到的443目的端口的数据包重定向到本机的IP地址。
4. 这样，受攻击者客户端的浏览器就只会和攻击者主机进行SSL连接。
5. 攻击者在本机使用监听443端口，并且伪造一个假的SSL证书，用于和客户端的连接，同时，提取客户端发送的数据包的原始目的IP地址，用于和客户端原始请求的服务器建立另一个SSL连接。
6. 中间人攻击者在双向的SSL Socket通信都建立完成后，对两边的socket进行数据读写同步，将数据通道打通，使客户端的浏览器能够正常访问(受攻击者不会察觉到已经收到SSL中间人攻击)
7. 在数据同步的同时，记录下明文数据，达到SSL中间人攻击的目的。

参考链接：

* [中间人攻击(MITM)姿势总结](http://www.cnblogs.com/LittleHann/p/3735602.html)
* [通过伪造CA证书，实现SSL中间人攻击](http://blog.sina.com.cn/s/blog_4a898cfb0100t8j7.html)

__实验过程__
参考链接：[Burp Suite抓HTTPS数据包](http://blog.csdn.net/zyw_anquan/article/details/47904495)

1. 设置firefox，手动配置代理
Preferences -> Advanced -> Settings -> Manual proxy configuration

2. 运行BurpSuite,用firefox浏览器访问http://burp,点击CA Certificate下载burp的内置证书。

3. 将证书导入Firefox，Burp Suite被视为可信任的根，成为用户浏览器访问HTTPS网站的代理，达到监视双方（客户端与服务器端）通信过程的目的。

4. [How To: Use mitmproxy to read and modify HTTPS traffic](https://blog.heckel.xyz/2013/07/01/how-to-use-mitmproxy-to-read-and-modify-https-traffic-of-your-phone/#How-it-works)


###SSLstrip

[New Tricks For Defeating SSL In Practice](https://www.blackhat.com/presentations/bh-dc-09/Marlinspike/BlackHat-DC-09-Marlinspike-Defeating-SSL.pdf) by Moxie Marlinspike (2009) 


    Something must be wrong, but...

        All the signatures are valid. 
        Nothing has expired. 
        The chain is in tact. 
        The root CA is embedded in the browser and trusted.

SSL剥离的实施方法是阻止浏览器与服务器建立HTTPS连接。

它的前提是用户很少直接在地址栏输入https://，用户总是通过点击链接或3xx重定向，从HTTP页面进入HTTPS页面。所以攻击者可以在用户访问HTTP页面时替换所有https://开头的链接为http://，达到阻止HTTPS的目的。

SSL卸载攻击的效果优于证书伪造的攻击方法，因为服务器端看不出任何分别，客户端也不会接收到弹框警告。


HSTS很大程度上解决了上述两种针对SSL的中间人攻击。

HSTS的作用是强制客户端（如浏览器）使用HTTPS与服务器建立连接。服务器开启HSTS的方法是，当客户端通过HTTPS发出请求时，在服务器返回的超文本传输协议响应头中包含Strict-Transport-Security字段。非加密传输时设置的HSTS字段无效。

如果中间人hacker使用自己的自签名证书来进行攻击，浏览器会给出警告，但是许多用户会忽略警告。HSTS也解决了这一问题，一旦服务器发送了HSTS字段，用户将不再允许忽略警告。只要浏览器曾经与服务器建立过一次安全连接，之后浏览器会强制使用HTTPS，即使链接被换成了HTTP。

__Reserved for code__

### MITMf带你绕过HSTS

[Bypassing HSTS (HTTP Strict Transport Security) with MITMf](https://sathisharthars.wordpress.com/2015/02/27/bypassing-hsts-http-strict-transport-security-with-mitmf/)

__Reserved for code__

###SSLsniff

Using a tool maded by [Moxie Marlinspike](https://moxie.org/). <-The man hacked the world! ( • ̀ω ⁃᷄)✧

It supports many kinds of attacks, such as the [Null Prefix Attacks](https://moxie.org/papers/null-prefix-attacks.pdf), the [OCSP attacks](https://moxie.org/papers/ocsp-attack.pdf) and something else.

###SSLsplit - transparent SSL/TLS interception 
[工具](https://github.com/droe/sslsplit)



###合法证书签名


偷盗证书，为恶意软件签名

__Reserved for code__

###WPAD中间人劫持

网络代理自动发现协议（Web Proxy Autodiscovery Protocol），通过让浏览器自动发现代理服务器，定位代理配置文件，下载编译并运行，最终自动使用代理访问网络。

代理自动配置文件（Proxy Auto-Config），定义了浏览器和其他用户代理如何自动选择适当的代理服务器来访问一个URL。


案例（待分析）

1.针对NBNS - Metasploit利用WPAD漏洞

The penetration testing framework Metasploit includes support for WPAD via a new auxiliary module located at "auxiliary/server/wpad". This module, which is written by Efrain Torres, can be used to perform for man-in-the-middle (MITM) attacks by exploiting the features of WPAD. 

 * 参考链接：[WPAD Man in the Middle](http://www.netresec.com/?page=Blog&month=2012-07&post=WPAD-Man-in-the-Middle)

2.Badtunnel

3.针对DNS - WPAD Name Collision Flaw Allows MITM Attacks 

 * 参考链接：[WPAD Name Collision Flaw Allows MITM Attacks](http://www.securityweek.com/wpad-name-collision-flaw-allows-mitm-attacks)



