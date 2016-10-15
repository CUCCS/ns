

* dns tld synchronization：
ICANN有关同步tld(gTLDs 与ccTLDs)的问答：
https://www.icann.org/resources/pages/synchronized-idn-cctlds-faqs-2012-02-25-en#what-does-mean

* dns anycast：
Anycast is one source that can "talk" to a service that is advertised or hosted on multiple nodes configured with the same IP Address.  Layer 3 routing will route the packets to the "nearest" target based upon topology.
简单来讲，大部分DNS服务器采用了任播技术，同一ip地址的DNS服务器可以分布在好几台物理主机。有关anycast技术在DNS上的应用，找到了如下一篇很棒的介绍：
http://ddiguru.com/blog/118-introduction-to-anycast-dns

* dns root zone synchronization：
 有关 dns zone transfer:  https://en.wikipedia.org/wiki/DNS_zone_transfer

*关于TLDs：
在整个 DNS 系统的最上方一定是 . (小数点) 这个 DNS 服务器 (称为 root)，最早以前它底下管理的就只有 (1)com, edu, gov, mil, org, .net 这种特殊领域以及 (2)以国家为分类的第二层的主机名了！这两者称为 Top Level Domains (TLDs) 喔！

    一般最上层领域名 (Generic TLDs, gTLD)：例如 .com, .org, .gov 等等
    国码最上层领域名 (Country code TLDs, ccTLD)：例如 .tw, .uk, .jp, .cn 等

先来谈谈一般最上层领域 (gTLD) 好了，最早 root 仅管理六大领域名，分别如下：
名称 	代表意义
com 	公司、行号、企业
org 	组织、机构
edu 	教育单位
gov 	政府单位
net 	网络、通讯
mil 	军事单位

但是因特网成长的速度太快了，因此后来除了上述的六大类别之外，还有诸如 .asia, .info, .jobs (注1) 等领域名的开放。此外，为了让某些国家也能够有自己的最上层领域名，因此， 就有所谓的 ccTLD 了。
(from: http://blog.csdn.net/garfielder007/article/details/50748819)


有关bind配置；主从服务器搭建实验的参考：

*多环境下主从服务器搭建实验：
https://www.garron.me/en/go2linux/how-setup-dns-server-master-slave-bind.html
http://www.devtrends.com/index.php/setting-up-a-simple-dns-server-with-bind9/

*debian中bind9配置介绍：
https://wiki.debian.org/Bind9

*bind中文简介及简单教程
http://www.linuxprobe.com/chapter-13.html?jimmo2574#131
