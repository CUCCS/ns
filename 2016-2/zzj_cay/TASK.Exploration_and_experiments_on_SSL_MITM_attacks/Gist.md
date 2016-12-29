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
（然而IE用户仍然暴露在简单中间人攻击的威胁下，因为IE浏览器从Windows10起支持HSTS）

但安全对抗从未停止，MITM已经演化出针对SSL的中间人攻击。
ARP欺骗和DNS泄露是实现此类攻击的前提，即获知请求发送者的IP地址。
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

__DNS查询泄露造成的后果 --> 基于DNS欺骗的数据重定向__  
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

__基于ARP欺骗的数据重定向__ 

实际操作命令：

1. 开启端口转发，（攻击者）允许本机像路由器那样转发数据包

    > echo 1 > /proc/sys/net/ipv4/ip_forward

2. ARP投毒，向主机XP（10.23.0.4）声称自己(攻击者)就是网关Ubuntu（10.23.0.5） 

    > arpspoof -i eth0 -t 10.23.2.4 10.23.2.5

3. ARP投毒，向网关Ubuntu声称自己(攻击者)就是XP 

    > arpspoof -i eth0 -t 10.23.2.5 10.23.2.4

* 注意: 当hacker停止投毒时，arpspoof将进行“clean up and re-arping”，发送正确的目的物理地址。  

__端口重定向__

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

# SSL协议回顾

* [https连接的前几毫秒发生了什么?](http://yincheng.site/https)

# 针对SSL协议的中间人攻击

https握手过程的证书校验环节就是为了识别证书的有效性唯一性等等，所以严格意义上来说https下不存在中间人攻击，存在中间人攻击的前提条件是没有严格的对证书进行校验，或者人为的信任伪造证书。

- 存在中间人攻击原因：
    - 证书未校验（客户端没有做任何的证书校验 对应3）
    - 部分校验（例如在证书校验过程中只做了证书域名是否匹配的校验，可以使用burp的如下模块生成任意域名的伪造证书进行中间人攻击）
    - 证书链校验（人为的信任伪造的证书或者安装伪造的CA公钥证书从而间接信任伪造的证书 对应1、2、4）  

* 参考链接：[浅析HTTPS中间人攻击与证书校验](www.evil0x.com/posts/26569.html)  


针对SSL，中间人攻击只可能发生在SSL的前提条件被破坏的时候，以下是一些示例：

1. 服务器私钥被盗取 - 意味着攻击者能够冒充服务器，而客户端并不知情。  
2. 客户端置信于不可靠的CA（或者主密钥被盗取）- 无论谁获取了真实、可信的CA的私钥，他都可以生成证书从而冒充服务器，骗取客户端的信任。这就意味着，当服务器证书更换为另一个合法证书，浏览器并不会告知客户这件“小”事。  
3. 客户端不与可信CA确认合法证书列表。  
4. 客户端被攻击，假CA被写入客户的可信CA列表。假冒的CA可以为不可信的服务器签名。

参考链接：[Answer: SSL and man-in-the-middle misunderstanding - Stack Overflow](http://stackoverflow.com/questions/14907581/ssl-and-man-in-the-middle-misunderstanding)

## 利用伪造的X.509证书（SSL劫持）

这种类型的SSL会话劫持成功的必要条件如下：
  
  * 能够通过ARP欺骗、DNS欺骗或者浏览器数据重定向等欺骗技术，使得SSL客户端C和服务端之间的数据都流向中间人监测主机；
  * SSL客户端在接收到伪造的X.509证书后，用户选择信任该证书，并继续SSL连接；
  * SSL服务端未要求对SSL客户端进行认证。


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

### 利用代理服务器Burpsuite进行SSL劫持    
  
参考链接：[Burp Suite抓HTTPS数据包](http://blog.csdn.net/zyw_anquan/article/details/47904495)

1. 设置firefox，手动配置代理
Preferences -> Advanced -> Settings -> Manual proxy configuration

2. 运行BurpSuite,用firefox浏览器访问http://burp,点击CA Certificate下载burp的内置证书。

3. 将证书导入Firefox，Burp Suite被视为可信任的根，成为用户浏览器访问HTTPS网站的代理，达到监视双方（客户端与服务器端）通信过程的目的。

### mitmproxy (Transparent Proxying)
[How To: Use mitmproxy to read and modify HTTPS traffic](https://blog.heckel.xyz/2013/07/01/how-to-use-mitmproxy-to-read-and-modify-https-traffic-of-your-phone/#How-it-works)

* 局限：不能理解其他基于TLS/SSL的流量，比如FTPS, SMTP over SSL, IMAP over SSL等。

* 前期准备：受害者信任攻击者伪造的CA证书，受害者的网关IP被篡改为攻击者IP(为了方便连接Internet，DNS服务器也是攻击者)。


### SSLsplit  
[工具](https://github.com/droe/sslsplit)
[English](https://blog.heckel.xyz/2013/08/04/use-sslsplit-to-transparently-sniff-tls-ssl-connections/#Sniffing-HTTPS-google-de-and-facebook-com)  
[中文](http://zhiwei.li/text/2015/08/16/%e7%94%a8sslsplit%e5%88%86%e6%9e%90ssl%e8%bf%9e%e6%8e%a5-%e5%8c%85%e6%8b%ac%e9%9d%9ehttps%e5%8d%8f%e8%ae%ae/)

如同上述方法。


###  SSLsniff

Using a tool maded by [Moxie Marlinspike](https://moxie.org/). <-The man hacked the world! ( • ω ⁃᷄)✧

It supports many kinds of attacks, such as the [Null Prefix Attacks](https://moxie.org/papers/null-prefix-attacks.pdf), the [OCSP attacks](https://moxie.org/papers/ocsp-attack.pdf) and something else.


## 利用HTTP与HTTPS之间跳转的验证漏洞 （SSL卸载）

这种类型的SSL会话劫持成功的必要条件如下：
  
  * 能够通过ARP欺骗、DNS欺骗或者浏览器数据重定向等欺骗技术，使得SSL客户端和服务端之间的数据都流向中间人监测主机； 
  * 客户端访问的Web页面存在http页面至https页面的跳转；
  * SSL服务端未要求对SSL客户端进行认证。


### SSLStrip与HSTS的编年史

Moxie Marlinspike 在Black Hat DC在2009年发布了他的工具SSLStrip。SSLStrip通过拦截受害者和路由器之间的请求（ARP欺骗)，用HTTP替换HTTPS请求，以便攻击者能够嗅闻到用户认为是加密的流量。

[New Tricks For Defeating SSL In Practice](https://www.blackhat.com/presentations/bh-dc-09/Marlinspike/BlackHat-DC-09-Marlinspike-Defeating-SSL.pdf) by Moxie Marlinspike


    Something must be wrong, but...

        All the signatures are valid. 
        Nothing has expired. 
        The chain is in tact. 
        The root CA is embedded in the browser and trusted.

SSLstrip使用了社会工程学的原理：为了图方便省事，用户很少直接在地址栏输入https://，用户总是通过点击链接或3xx重定向，从HTTP页面进入HTTPS页面。所以攻击者可以在用户访问HTTP页面时替换所有https://开头的链接为http://，达到阻止HTTPS的目的。

SSL卸载攻击的效果优于证书伪造的攻击方法，因为服务器端看不出任何分别，客户端也不会接收到弹框警告（BetterCap实验可见攻击效果）。

为了对抗上述攻击方法，大多数浏览器引入了“HTTP严格传输安全”（HSTS）安全策略机制。用户曾经访问过的页面将在浏览器注册登记为安全页面，并强制使用HTTPS协议。因此用户未曾访问过的页面或网站，才会面临SSL卸载攻击的威胁。

  > HTTP严格传输安全（HSTS）是一种Web安全策略机制，有助于保护网站免受协议降级攻击和Cookie劫持。 它允许Web服务器声明Web浏览器（或其他合规用户代理）应该只使用安全的HTTPS连接，而不是通过不安全的HTTP协议与它交互。

2014年，Leonardo Nve	Egea发布了SSLStrip2，用降级攻击绕开HSTS。原始的攻击性工具SSLStrip2和dns2proxy的源码不再公开，其功能集成到MITMf框架下。

  > 通常情况下，HSTS规则在是基于每个主机名应用的，攻击的诀窍是将HTTPS链接降级为HTTP，并在其前面添加一些自定义子域名。 每个生成的链接将不会对任何DNS服务器有效，但攻击者可以解析这些主机名。  

[OFFENSIVE:Exploiting changes on DNS server conﬁguration](https://www.blackhat.com/docs/asia-14/materials/Nve/Asia-14-Nve-Offensive-Exploiting-DNS-Servers-Changes.pdf) by Leonardo Nve	Egea

### 绕过HSTS

* MITMf框架

* BetterCap

* cachEraser

* 其他工具

  * ettercap
  * Wifi-Pumpkin
  * Pythem
  * BURP + Tor Browser


### SSLStrip的防御方法 

1. 对于网站来说，在配置HTTPS服务的时候加上“HTTP Strict Transport Security”配置项；或者是在代码中将所有HTTP的请求强制转移到HTTPS上，使用URL REWRITE也可以达到同样的效果。   

    HSTS很大程度上解决了上述两种针对SSL的中间人攻击。HSTS的作用是强制客户端（如浏览器）使用HTTPS与服务器建立连接。服务器开启HSTS的方法是，当客户端通过HTTPS发出请求时，在服务器返回的超文本传输协议响应头中包含Strict-Transport-Security字段。非加密传输时设置的HSTS字段无效。

    如果中间人hacker使用自己的自签名证书来进行攻击，浏览器会给出警告，但是许多用户会忽略警告。HSTS也解决了这一问题，一旦服务器发送了HSTS字段，用户将不再允许忽略警告。只要浏览器曾经与服务器建立过一次安全连接，之后浏览器会强制使用HTTPS，即使链接被换成了HTTP。

2. 对于关键的信息，例如用户登录网站的ID和密码，在发送之前先用JavaScript进行一次加密处理，这种方法不但是对SSLStrip有效，对SSL劫持攻击也有效，甚至是即便使用HTTP协议来传输用户登录的ID和密码都是安全的。  

3. 对于用户来说，在访问支持HTTPS的网站时，输入URL加上“https://”。大多数用户平时并不会注意这点，比如访问gmail，我们一般就输入“gmail.com”，如果是输入“https://gmail.com”就可以避免SSLStrip的攻击。对于使用脚本实现地址跳转也需要注意这个问题，location.href之后的URL，一定要强制加上“https://”。

防御SSLStrip攻击比较简单，大多数的网站都已经做好了安全方面的配置，但也有少数的网站仍然没有重视这个问题。


## MITMore

### HTTPS向下降级攻击

SSL/TLS协议通过握手来确定通信信息，其中握手双方要统一加密协议版本。  

在握手过程中这样确认加密协议版本：  

1. 由客户端（如浏览器）发送第一个数据包 ClientHello，这个数据包中保存着客户端支持的加密协议版本。
2. 服务器收到这个ClientHello数据包，查看里面客户端支持的加密协议版本，然后匹配服务器自己支持的加密协议版本，从而确认双方应该用的加密协议版本。
3. 服务器发送ServerHello数据包给客户端，告诉客户端要使用什么加密协议版本。  


在上述过程中，如果客户端发送给服务器的ClientHello数据包中说自己仅支持某个有漏洞的旧版本加密协议（比如仅支持SSLv3.0）,服务器有两种可能：  

* 服务器支持很多版本，其中包括有漏洞的旧版本和新版本（包括了SSLv3.0协议），那么服务器会认可使用有漏洞的旧版本协议，从而告诉客户端使用有漏洞的旧版本（可以使用SSLv3.0）。
* 服务器不支持有漏洞的旧版本，拒绝客户端的这次请求，握手失败。  

对于攻击者，作为中间人只能监听到加密过的数据，如果这些数据通过没有漏洞的加密版本加密，攻击者并不能做什么。但是，如果服务器提供有漏洞的旧版本加密协议的支持，而同时攻击者又能作为中间人控制被攻击者的浏览器发起漏洞版本的HTTPS请求，那虽然攻击者监听到的也是加密过的数据，但因为加密协议有漏洞，可以解密这些数据，所以数据就和明文传输没有什么差别了。
  
这就是HTTPS协议降级。

案例：

* [CBC模式加密的Padding Oracle攻击](https://pentesterlab.com/exercises/padding_oracle)
* [对称加密ECB模式的漏洞利用](https://pentesterlab.com/exercises/ecb)


### HTTPS前端劫持 

[参考链接](http://div.io/topic/747)

* 浏览器的安全策略

### 第三类攻击

所谓第三类攻击，完全就是软件厂商在软件的设计过程中忽略的了安全的问题。这是一种普遍存在的情况，程序的bug、漏洞，设计缺陷，都会打破一些安全模型。

### Beast、Crime...

