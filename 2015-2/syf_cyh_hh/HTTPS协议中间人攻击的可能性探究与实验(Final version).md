</br>Part 1.理论部分
</br>【SSL欺骗】
</br>我们查找了很多资料，找到使用sslstrip攻击的较为简便。sslstrip是在09年黑帽大会上由Moxie Marlinspike提出的一种针对SSL攻击的方法。
</br>HTTPS确保服务器、客户和可信任第三方之间数据通信的安全过程，通过用户访问邮箱服务举例说明：
</br>1、客户端使用HTTP连接到端口80的http://mail.google.com
</br>2、服务器试用HTTP代码302重定向客户端HTTPS版本的这个网站
</br>3、客户端连接到端口443的网站https://mail.google.com
</br>4、服务器向客户端提供包含其电子签名的证书，该证书用于验证网址
</br>5、客户端获取该证书，并根据信任证书颁发机构列表来验证该证书
</br>6、加密通信成功建立
</br>如果证书验证失败，则无法验证网址的真实度，页面显示证书验证错误。可以选择冒着危险继续访问网站。
</br>用户通过HTTP302响应代码被定位到HTTPS或者他们点击连接将其定位到一个HTTPS站点，而sslstrip攻击就是在SSL连接未建立时的中间人攻击，过程说明：
</br>1、客户端与web服务器间的流量被拦截
</br>2、当遇到HTTPS URS时，sslstrip使用HTTP链接替换它，并保存了这种变化的映射
</br>3、攻击机模拟客户端向服务器提供证书
</br>4、从安全网站收到流量提供给客户端过程中服务器会认为仍然在接收SSL流量，服务器无法辨别任何改变。用户可以感觉到唯一不同的是，浏览器中不会标记HTTPS
</br>使用sslstrip攻击过程：
</br>1、安装好sslstrip（只能使用LINUX）后首先配置IP转发echo "1" > /proc/sys/net/ipv4/ip_forward
</br>2、修改iptables防火墙配置，强制将所有被拦截的HTTP流量路由到SSLstrip将会监听的端口iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port [指定随机端口]
</br>3、运行sslstrip，并将其配置为监听sslstrip -l [指定随机端口]
</br>4、使用arpspoof工具，配置ARP欺骗来拦截目标主机的流量
</br>arpspoof -i eth0 -t [被攻击IP] [网关IP]
</br>关于arpspoof -i eth0 -t IP1 IP2命令，就是欺骗IP2，告诉IP2你的计算机IP是IP1。
</br>实验执行命令时老出错而且不能实现ARP欺骗，查找到的解决办法是下面两个命令都执行
</br>arpspoof -i eth0 -t [被攻击IP] [网关IP]
</br>arpspoof -i eth0 -t [网关IP] [被攻击IP]
</br>完成后就可以主动劫持任何建立的SSL连接,然后使用数据包器从流量来收集密码等所需信息。
</br>
</br>但是由于根本只是将HTTPS连接替换成HTTP连接，随着时间发展，现在网站大多已经无法用HTTP替换连接，只有使用HTTPS连接才能够进入。因此这个方法也就只是用于少数还未进行升级的HTTPS连接的网站了。
</br>
</br>【会话劫持】
</br>任何涉及对设备间会话的攻击就是会话劫持。会话，是指存在状态的设备间的连接。首先访问者输入用户名和密码来得到网站的身份验证，即正式建立会话，然后网站会保持某种形式的会话  追踪以确保访问者的登陆状态，并允许访问者访问网站资源，通常是通过cookie来保证。当会话要结束时，登录信息就会被清除，然后会话才会结束。
</br>从cookie盗窃角度来探讨会话劫持，截取已建立会话的某些部分数据，利用这些数据来假冒通信中所涉及的任何参加者，从而获取会话信息。即获取用于维持浏览器和登陆网站间会话状态的cookie，我们就能将cookie发给网络服务器并冒充会话连接。可以使用Hamster和Ferret为工具实验，也可以使用Burpsuite进行实验，具体实验操作在其他文档中记录。
</br>
</br>【ARP缓存中毒】
</br>这是现代中间人攻击中最早出现的攻击形式，ARP缓存中毒(有时也被称为ARP中毒路由)能够让与受害用户在相同子网的攻击者窃取用户的所有网络流量。它是最容易执行的攻击形式，但也是最有效的攻击形式。
</br>ARP协议的主要目的在于简化OSI模型数据链路层和网络层间地址的翻译。数据链路层使用MAC地址，以便硬件设备可以在小范围内直接进行通信。网络层使用IP地址(最常见的形式)来创建连通世界各地用户的大规模网络。数据链路层直接处理连接在一起的设备，而网络层处理那些直接以及间接连接的设备，每一层都有自己的地址形式，他们必须合作才能实现网络通信。
</br>ARP运作围绕ARP请求数据包和ARP回复数据包展开。请求和回复的目的在于确定与特定IP地址相关的硬件MAC地址，这样流量才能够在网络上找到目的地。收到回复后，传递设备会更新其ARP缓存表，然后设备就可以与另一台设备进行通信。ARP缓存中毒利用了ARP协议不安全的本质。ARP协议有别于其他协议，例如DNS协议可以配置为仅接受安全动态更新，而使用ARP的设备则可以接受任何时间的更新。这意味着任何机器都可以向另一台主机发送ARP回复数据包，并迫使主机更新其ARP缓存。发送ARP回复而没有生成请求时，此时被成为无效ARP。当恶意攻击者以这种方式放置一些无效ARP时，用户就会认为他们正在与另一用户通信，而实际上是与窃取信息的攻击者通信。
</br>ARP缓存中毒是中间人攻击中最有效的攻击方式，因为它非常容易执行，对于现代网络是巨大的威胁，并且这种攻击方式很难检测和防御。
</br>【DNS欺骗】
</br>DNS欺骗是攻击者冒充域名服务器的一种欺骗行为，它主要用于向主机提供错误DNS信息，当用户尝试浏览网页，例如IP地址为XXX.XX.XX.XX，网址为www.alipay.com，而实际上登录的确实IP地址YYY.YY.YY.YY上的www.alipay.com，用户上网就只能看到攻击者的主页，而不是用户想要取得的网站的主页了，这个网址是攻击者用以窃取支付宝登录证书以及帐号信息的假冒网址，DNS欺骗其实并不是真的“黑掉”了对方的网站，而是冒名顶替、招摇撞骗罢了。
</br>当我们在浏览器输入网址时(例如http://www.baidu.com)，就会向DNS服务器发送一个DNS请求以便找到与该网址相对应的IP地址。这是因为与互联网互连的路由器和设备并不知道baidu.com，它们只知道IP地址，如202.108.22.5。DNS服务器本身的工作原理是，存储IP地址到DNS名称映射的记录数据库，联系这些资源记录与客户端，并将这些资源记录与其他DNS服务器联系。
</br>DNS函数是属于查询/响应类型的格式，当客户端希望解析DNS域名为IP地址时，就会向DNS服务器发送一个查询，然后服务器会将对应的作为回复。从客户端的角度来看，看到的只有两个数据包：查询和响应。
</br>我们将使用一种称为DNS ID欺骗的技术。每个通过互联网发送的DNS请求都包含一个独特的识别码，其目的在于辨识查询和响应，并将对应的查询和响应配对在一起。这就意味着，如果我们的攻击计算机可以拦截目标设备发送的DNS查询，我们就只需要做一个包含该识别码的假数据包，这样目标计算机就会根据识别码而接受我们发送的查询结果。
</br>我们将使用一个Ettercap工具分两个步骤来完成整个操作。首先，我们对目标设备进行ARP缓存中毒攻击以重新路由通过攻击主机的目标设备的通信，这样我们就能够拦截DNS查询请求，然后我们就能够发送欺骗性的数据包。这样做的目的是为了让目标网络的用户访问我们制造的恶意网址而不是他们试图访问的网址。
</br>在操作Ettercap之前，需要进行一些配置。Ettercap的核心是数据包嗅探器，主要利用不同的插件来执行不同的攻击。dns_spoof插件是用于本文示例的工具，所以我们需要修改与该插件相关的配置文件。在windows系统中，该文件位于C:\Program Files (x86)\EttercapNG\shar\etter.dns以及/usr/share/ettercap/etter.dns，这个文件很简单并且包含我们想要欺骗的DNS记录。对于我们而言，我们希望所有试图打开yahoo.com的用户被定向到本地网络的主机上，所以我们加入了一些条目：
</br>yahoo.com A 172.16.16.100 
</br>www.yahoo.com A 172.16.16.100
</br>这些信息就是告诉dns_spoof插件当它发现针对yahoo.com 或者www.yahoo.com的DNS查询请求时，就发送IP地址172.16.16.100作为响应。在实际情况下，172.16.16.100会运行某种web服务器软件向用户展现假冒网站。
</br>一旦文件配置好并保存后，我们就可以执行命令字符串来发动攻击了，命令字符串使用以下选项：
</br>-T –指定文本界面的使用
</br>-q –以静音模式运行命令，这样捕捉的数据包不会输出到屏幕
</br>-P dns_spoof –指定dns_spoof插件的使用
</br>-M arp –发起中间人ARP中毒攻击以拦截主机间的数据包
</br>// // -指定整个网络作为攻击的目标
</br>我们需要的最终命令字符串为：
</br>Ettercap.exe –T –q –P dns_spoof –M arp // //
</br>运行此命令将启动两个阶段的攻击，首先是对网络设备的ARP缓存中毒攻击，然后是发送假的DNS查询响应信息。一旦启动，任何用户试图打开www.yahoo.com都会被重新定向到我们的恶意网站。
</br>
</br>
</br>
</br>
</br>Part 2.实验部分
</br>【DNS欺骗】
</br>这次试验是通过ettercap进行DNS欺骗攻击！
</br>（1）查看DNS：locate etter.dns
</br>（2）修改etter.dns文件并保存，以确保它执行正确的DNS欺骗攻击
</br>![](https://github.com/hua12/PIC/blob/master/%E4%BF%AE%E6%94%B9dns%E6%96%87%E4%BB%B6.PNG)
</br>10.0.2.15是攻击者的IP地址。确保Web服务器运行在攻击者的机器，一定要启用IP转发
</br>![](https://github.com/hua12/PIC/blob/master/%E5%BC%80%E5%90%AFIP%E8%BD%AC%E5%8F%91.PNG)
</br>（3）清除DNS缓存
</br>![](https://github.com/hua12/PIC/blob/master/%E6%B8%85%E9%99%A4DNS%E7%BC%93%E5%AD%98.PNG)
</br>（4）通过ettercap启用DNS欺骗攻击
</br>![](https://github.com/hua12/PIC/blob/master/%E6%89%AB%E6%8F%8F.PNG)
</br>说明：-P  使用插件，这里我们使用的是dns_spoof；-T 使用基于文本界面；-q  启动安静模式（不回显的意思）；-M 启动ARP欺骗攻击
</br>（5）启用dns_spoof插件来执行DNS欺骗中间人攻击后,当受害者浏览freebuf网站的时候就会被重定向到10.0.2.15，在终端出现：
</br>dns_spoof:[freebuf.com]spoofed to [10.0.2.15]
</br>例如metasploit 渗透工具使用ettercap进行dns欺骗。选择想要的exploit，在payload中就选择 reverse_tcp：
</br>![](https://github.com/hua12/PIC/blob/master/MSF.PNG)
</br>![](https://github.com/hua12/PIC/blob/master/msf%E8%AE%BE%E7%BD%AE.PNG)
</br>一旦受害者打开该网站，就会被重定向到10.0.2.15中，然后会话开始！
</br>【会话劫持】
</br>所遇到的问题反馈：
</br>之前做实验的时候总是会遇到网络不通的问题。最终选用了桥接的网络模式。
</br>物理主机的IP信息
</br>![](https://github.com/vsmile0601/Pictures/blob/master/主机IP信息.PNG)
</br>虚拟机的IP信息
</br>![](https://github.com/vsmile0601/Pictures/blob/master/虚拟机IP信息.PNG)
</br>选用了桥接模式：
</br>![](https://github.com/vsmile0601/Pictures/blob/master/网络模式为桥接.PNG)
</br>浏览器代理设置：
</br>![](https://github.com/vsmile0601/Pictures/blob/master/浏览器代理设置.PNG)
</br>burpsuite代理设置：
</br>![](https://github.com/vsmile0601/Pictures/blob/master/burp suite代理设置.PNG)
</br>进入到邮箱的登录界面后，开启burp suite的Intercept功能，即Intercept on，输入用户名和密码，点击“登录”
</br>![](https://github.com/vsmile0601/Pictures/blob/master/登陆页面.png)
</br>如图，可以清楚的看到截获的用户名及密码（为确保隐私，以打上马赛克）
</br>![](https://github.com/vsmile0601/Pictures/blob/master/截获密码.png)
</br>测试发送邮件截获邮件内容：
</br>![](https://github.com/vsmile0601/Pictures/blob/master/发送邮件.png)
</br>从所标识的地方就可以用肉眼看出所发信件的内容：
</br>![](https://github.com/vsmile0601/Pictures/blob/master/信件内容.png)
</br>首先用被攻击账号登录mail.163.com，然后burp suite——intercept on
</br>写好的初始状态为：
</br>![](https://github.com/vsmile0601/Pic/blob/master/第二次初始邮件.png)
</br>点击发送后可以在HTTP history中看到拦截的历史：
</br>![](https://github.com/vsmile0601/Pic/blob/master/Proxy中的HTTP%20history.PNG)
</br>将所要选择的条目右键单击send to repeater，可以找到所写邮件的标题名称：
</br>![](https://github.com/vsmile0601/Pic/blob/master/第二次被攻击前的信件名称.PNG)
</br>将标题名称进行修改：然后点击上方的“GO”
</br>![](https://github.com/vsmile0601/Pic/blob/master/第二次修改信件名称.PNG)
</br>将intercept off后即可看到邮件发送成功，在收件人邮箱里可以看到被攻击的文件：
</br>![](https://github.com/vsmile0601/Pic/blob/master/第二次收到的邮件.png)
</br>但是不知道为什么收件人信箱每次实验可以收到两封邮件，一个是被攻击的，一个是没被攻击的：
</br>![](https://github.com/vsmile0601/Pic/blob/master/每次发两封？！.png)
</br>不知是否点击repeater中的GO时就已经发送了修改的邮件，然而off后邮件的客户端又发送了一下原本的邮件？？？？
</br>（Ps.我们一共连续实验了两次，上面展示的是第二次实验的内容）
</br>
</br>
</br>
</br>
</br>
</br>
</br>Part 3.实验总结：
</br>实验初期，我们做了ARP毒化的实验，但是，我们一直困惑在虚拟机的网络模式（NAT、host-only、bridge），傻傻分不清楚。导致实验进展困难，所以只是展示了比较顺利的一部分内容。在实验过程的后半段，我们选择了使用burp suite代理，认为它比较容易实现中间人攻击，结果的确是通过代理截获了用户名和密码并且成功地篡改了邮件内容，遗憾的是，并不是在https的协议下截获的。最后，我们又尝试了一下ettercap和msfconsole工具，使用ettercap的dns插件进行dns欺骗，只是不知道如何将截获的dns_spoof解析到burp suite上（55555555555），由于理解msfconsole不够透彻，导致我们本来要攻击虚拟机但是莫名的攻击了Windows系统。
</br>总的来说，虽然我们实验开始的时间很早，但是由于对网络拓扑这方面的知识了解匮乏，所以走了很多弯路，可喜的是，我们因此对网络拓扑有了更深的了解，补足了自己的缺漏。另外，我们所查找的资料不够权威，用google用的很少。在实验走了很多的弯路之后，已经越来越背离实验的初衷。
</br>（Ps.祝老师在新的一年里工作顺利、阖家欢乐、心想事成，么么哒。）
</br>
</br>
</br>
</br>
</br>Part 4.参考文献： 
</br>【1】http://www.freebuf.com/tools/48016.html SSL中间人证书攻击测试演练 
</br>【2】http://caifu.zol.com.cn/183/1833310.html 解析中间人攻击之SSL欺骗 
</br>【3】http://caifu.zol.com.cn/174/1747067.html 解析中间人攻击之ARP缓存中毒 
</br>【4】http://www.freebuf.com/article/system/5265.html 中间人攻击-DNS欺骗 
</br>【5】http://www.ithao123.cn/content-5687474.html ms10_046_shortcut_icon_dllloader漏洞利用和ettercap dns欺骗 
</br>【6】http://security.ctocio.com.cn/499/9435999.shtml 解析中间人攻击——会话劫持 
</br>【7】http://2cto.com/Article/201208/146999.html DNS欺骗



