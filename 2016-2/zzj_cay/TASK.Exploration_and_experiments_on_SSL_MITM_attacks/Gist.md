
#HTTPS协议中间人攻击的可能性探究与实验

##DNS查询泄漏（经由DNS解析服务器）与MITM

在某些情况下，即使连接到 VPN，操作系统仍然继续使用其默认的 DNS 服务器（比如在本地解析），导致DNS泄露。

参考链接：[DNS leak - Wikipedia](https://en.wikipedia.org/wiki/DNS_leak) 

该[漏洞](https://torrentfreak.com/huge-security-flaw-leaks-vpn-users-real-ip-addresses-150130/)允许远程网站使用[WebRTC](https://webrtc.org/)（网络实时通信）确定用户的真实IP地址，WebRTC内置于大多数Web浏览器中。据漏洞发现者Daniel Roesler([Github](https://github.com/diafygi/webrtc-ips))描述，因为WebRTC允许请求ISP的STUN服务器返回用户的公共和本地IP地址，从而能允许网站确定连接的大致位置。这一切，可以使用JavaScript实现。

此外，STUN请求不是使用常规XMLHttpRequest过程创建的，因此不能在浏览器的控制台中查看，也不能由受欢迎的隐私插件（例如Ghostery或AdBlockPlus）阻止。

参考链接：[How to See If Your VPN Is Leaking Your IP Address (and How to Stop It)](http://lifehacker.com/how-to-see-if-your-vpn-is-leaking-your-ip-address-and-1685180082)


- 域传输漏洞

存在DNS泄露漏洞的主要场景：

1. 透明DNS代理技术 - ISP 可以拦截所有 DNS 查询请求(TCP/UDP端口53)，有效地迫使你使用他们的 DNS 服务器进行所有的 DNS 查找。
2. 开启VPN，PAC模式在本地解析域名，将会暴露IP。解决问题的根本原则就是确保使用了 VPN 服务商提供的 DNS 服务器。


###以下解决方案有待考证：

Windows客户端的解决办法:

1. 在连接到 VPN 之前,设置静态IP 地址
2. 在连接之后, 禁用原先 DNS 设置 
3. 断开后, 切换回 DHCP 必要时恢复原 DNS 服务器

- 解决方案1：VPN
    - 单层VPN不被视为隐匿上网。用户可以通过[dnsleaktest](https://www.dnsleaktest.com/)提供的在线检测是否存在DNS泄漏。
 
- 解决方案2：隐匿上网
    - 若对隐匿性有一定要求，不推荐使用单层VPN。为增强隐匿性和安全性，往往使用虚拟机+多层代理的组合。
    - 更多内容可参考编程随想博客《如何隐藏你的踪迹》
- 解决方案3：使用DNSCrypt加密DNS传输   
    - DNSCrypt是OpenDNS发布的，旨在确保客户端与DNS服务器传输安全的工具，基于DNSCurve发展而来。
    - 使用该软件后，DNS通讯采用加密传输，能在相当程度上，既防止泄漏，又防止劫持，可用于保护DNS通信。
    - DNSCrypt是开源项目，已经支持Windows，Linux，iOS和Android等多个平台，是避免DNS泄漏与劫持的利器。

* 参考链接：[http://libertosher.blogspot.com](https://www.dnsleaktest.com/)

拓展：

* DNS污染

  - DNS劫持就是指用户访问一个被标记的地址时，DNS服务器故意将此地址指向一个错误的IP地址的行为。
  - 网通、电信、铁通的某些用户有时候会发现自己打算访问一个地址，却被转向了各种推送广告等网站，这就是DNS劫持。

* DNS劫持

  - DNS污染，指的是用户访问一个地址，国内的服务器(非DNS)监控到用户访问的已经被标记地址时，服务器伪装成DNS服务器向用户发回错误的地址的行为。
  - 访问Youtube、Facebook之类网站等出现的状况。


##ARP欺骗与MITM

###URL流量操作 

实际操作命令：

1. 开启端口转发，（攻击者）允许本机像路由器那样转发数据包

   *echo 1 > /proc/sys/net/ipv4/ip_forward*

2. ARP投毒，向主机XP声称自己(攻击者)就是网关Ubuntu 

    *arpspoof -i eth0 -t 10.23.2.4 10.23.2.5*

3. ARP投毒，向网关Ubuntu声称自己(攻击者)就是XP 

    *arpspoof -i eth0 -t 10.23.2.5 10.23.2.4*

Notification: 攻击者要“持续投毒”，因为一旦停止投毒，将发生“clean up and re-arping”，将发送正确的目的物理地址。  

###端口重定向攻击

端口重定向接收到一个端口数据包的过程（如80端口），并且重定向它的流量到不同的端口（如8080）。实现这类型攻击的好处就是可以无止境的，因为可以随着它重定向安全的端口到未加密端口，重定向流量到指定设备的一个特定端口上。

具体操作步骤如下：

1. 开启路由转发攻击。执行命令如下所示：

    *echo 1 > /proc/sys/net/ipv4/ip_forward*

2. 启动Arpspoof工具注入流量到默认网络。例如，默认网关地址为10.32.2.1。执行命令如下：

    *arpspoof -i eth0 10.23.2.1*


3. 添加一条端口重定向的防火墙规则。执行命令如下所示：

    *iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080*

* 执行以上命令后，没有任何输出。

以上设置成功后，当用户向网关10.23.2.1的80端口发送请求时，将会被转发为8080端口发送到攻击者主机上。


##伪造SSL证书

SSL原理:(待补充)

https握手过程的证书校验环节就是为了识别证书的有效性唯一性等等，所以严格意义上来说https下不存在中间人攻击，存在中间人攻击的前提条件是没有严格的对证书进行校验，或者人为的信任伪造证书。

- 存在中间人攻击原因：
    - 证书未校验
    - 部分校验
    - 证书链校验

* 参考链接：[浅析HTTPS中间人攻击与证书校验](www.evil0x.com/posts/26569.html)

攻击基本原理：

1. 攻击者对目标客户端和网关发送ARP投毒攻击，污染它们的ARP缓存表。
2. 客户端在浏览器中输入 "https://mail.google.com/" 的网址，浏览器会尝试和 "https://mail.google.com/" 的443端口建立SSL连接，但是因为客户端受到了ARP投毒攻击，原本发往网关的数据包被发往了攻击者的主机。
3. 攻击者在本机使用iptables将接收到的443目的端口的数据包重定向到本机的IP地址。
4. 这样，受攻击者客户端的浏览器就只会和攻击者主机进行SSL连接。
5. 攻击者在本机使用监听443端口，并且伪造一个假的SSL证书，用于和客户端的连接，同时，提取客户端发送的数据包的原始目的IP地址，用于和客户端原始请求的服务器建立另一个SSL连接。
6. 中间人攻击者在双向的SSL Socket通信都建立完成后，对两边的socket进行数据读写同步，将数据通道打通，使客户端的浏览器能够正常访问(受攻击者不会察觉到已经收到SSL中间人攻击)
7. 在数据同步的同时，记录下明文数据，达到SSL中间人攻击的目的。

* 参考链接：[中间人攻击(MITM)姿势总结](http://www.cnblogs.com/LittleHann/p/3735602.html)


针对SSL，中间人攻击只可能发生在SSL的前提条件被破坏的时候，以下是一些示例：

1. 服务器私钥被盗取 - 意味着攻击者能够冒充服务器，而客户端并不知情。
2. 客户端置信于不可靠的CA（或者主密钥被盗取）- 无论谁获取了真实、可信的CA的私钥，他都可以生成证书从而冒充服务器，骗取客户端的信任。这就意味着，当服务器证书更换为另一个合法证书，浏览器并不会告知客户这件“小”事。
3. 客户端不与可信CA确认合法证书列表，这样一来，偷盗证书就可能合法化攻击者的身份。
4. 客户端被攻击，假CA被写入客户的可信CA列表。假冒的CA可以为不可信的服务器签名。

* 参考链接：[Answer: SSL and man-in-the-middle misunderstanding - Stack Overflow](http://stackoverflow.com/questions/14907581/ssl-and-man-in-the-middle-misunderstanding)

- HSTS

##合法证书签名


偷盗证书，为恶意软件签名


##WPAD中间人劫持

网络代理自动发现协议（Web Proxy Autodiscovery Protocol），通过让浏览器自动发现代理服务器，定位代理配置文件，下载编译并运行，最终自动使用代理访问网络。

代理自动配置文件（Proxy Auto-Config），定义了浏览器和其他用户代理如何自动选择适当的代理服务器来访问一个URL。


案例（待分析）

1.针对NBNS - Metasploit利用WPAD漏洞

The penetration testing framework Metasploit includes support for WPAD via a new auxiliary module located at "auxiliary/server/wpad". This module, which is written by Efrain Torres, can be used to perform for man-in-the-middle (MITM) attacks by exploiting the features of WPAD. 

 * 参考链接：[WPAD Man in the Middle](http://www.netresec.com/?page=Blog&month=2012-07&post=WPAD-Man-in-the-Middle)

2.Badtunnel

3.针对DNS - WPAD Name Collision Flaw Allows MITM Attacks 

 * 参考链接：[WPAD Name Collision Flaw Allows MITM Attacks](http://www.securityweek.com/wpad-name-collision-flaw-allows-mitm-attacks)
