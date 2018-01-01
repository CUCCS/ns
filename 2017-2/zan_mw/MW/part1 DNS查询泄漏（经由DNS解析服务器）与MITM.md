# DNS查询泄露（经由DNS解析服务器）与MITM   
## ZoneTransfer域传送漏洞  
DNS服务器分为：主服务器、备份服务器和缓存服务器。在主备服务器之间同步数据库，需要使用“DNS域传送”。域传送是指后备服务器从主服务器拷贝数据，并用得到的数据更新自身数据库。  
若DNS服务器配置不当，可能导致匿名用户获取某个域的所有记录。造成整个网络的拓扑结构泄露给潜在的攻击者，包括一些安全性较低的内部主机，如测试服务器。凭借这份网络蓝图，攻击者可以节省很少的扫描时间。  
大的互联网厂商通常将内部网络与外部互联网隔离开，一个重要的手段是使用Private DNS。如果内部DNS泄露，将造成极大的安全风险。风险控制不当甚至造成整个内部网络沦陷。

## 互联网服务提供商(ISP)给虚拟专用网络(VPN)用户挖坑

### 背景知识——透明代理
当访问一网站时，browser首先解析域名映射到某一IP，这个解析过程需要拿到某个NameServer上解析。一般情况下这个NameServer是ISP（如三大运营商）指定的，所以ISP可以完全控制此NameServer，故可以记录你的地址解析活动，所以当你做某些事情时，实际上已经被跟踪记录在案了。
使用了透明代理技术的ISP将会在我们不知情的情况下去使用他指定的NameServer（大多数情况下都是如此），即使自己指定了NameServer也没用。
### 实现原理    
当我们使用匿名VPN时，虽然指定了特定的NameServer来使得域名解析活动相对保密进行，但仍有可能因为错误的配置而使用default NameServer而不是秘密的NameServer，这时又会被ISP记录在案了。  
尽管DNS泄漏是由于几个因素造成的，但是常见的情况是恶意网站采用将网站响应延迟到用户计算机的策略，从而导致浏览器切换到不安全的DNS。 同时，较新的Windows操作系统有一些内置的功能，增加其易于DNS泄漏。     
![](pics/part1/DnsLeak.png)    
### 解决方案
如果你的计算机使用默认设置，并没有通过VPN的DNS服务器发送DNS请求，那么这个泄漏很难看出,需要做[泄漏测试](www.dnsleaktest.com) 。   
- 强制一个很好的DNS服务。在网络适配器的属性中的TCP/IPv4的选项，设置OpenDNS的或任何DNS服务，你更喜欢所有可用的网络适配器。 这确保您的互联网提供商DNS服务器永远不会使用，即使当VPN未连接。
- 禁用Teredo的服务。要防止DNS请求通过非隧道IPv6连接，请在路由器上禁用Teredo和IPv6相关选项。在Windows上，打开命令提示符（cmd.exe的运行），然后运行“netsh接口设置Teredo的状态已禁用”。   
- 将计算机网络设置更改为使用静态IP地址，以确保新的DNS设置被赋予高优先级，并且不会在没有暗示的情况下进行修改。  
- 使用带有DNS泄漏保护功能的VPN。根据BestVPNz.com，TorGuard所提供的信息，VPNArea，PureVPN，ExpressVPN，VPN.AC和LiquidVPN都提供了这种保护功能。如果你正在使用这些VPN中的一 个，请确保你的设置是否正确。打开设置，你就会看到一个检查防范DNS漏洞的选项。
- 使用VPN监控软件。某些VPN监控软件还包括修复DNS泄漏。VPNCheck Pro版本和OpenVPN Watchdog有这个功能。只有收费软件有修复泄漏这样的选项。


## 后果——基于DNS欺骗的数据重定向
泄露域名服务器的IP地址或者关联网址，为hacker实现DNS spoofing制造机会。也就是说当hacker悉知网络层的通信规则，就可以从链路层进行中间人攻击。



参考链接：  
[Transparent DNS proxies](https://www.dnsleaktest.com/what-is-transparent-dns-proxy.html)  
[What is a DNS leak and why should I care?](https://www.dnsleaktest.com/what-is-a-dns-leak.html)  
[How can I fix a DNS leak?](https://www.dnsleaktest.com/how-to-fix-a-dns-leak.html)
