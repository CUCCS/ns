# IP地址管理机制
---
***
* IANA的三大职能之一，是协调全球IP和AS（自治系统）号并将它们提供给各区域Internet注册机构。

	![](http://i.imgur.com/BUHoDPg.jpg)[1]

# IP地址简介
____
### IP地址
* IP地址即__互联网协议地址（Internet Protocol Address）__[2]，或者网际协议地址。
 * IP协议是TCP/IP协议族中网络层的协议，目前大多数地区采用的是第4个版本，简称IPv4，其地址长度为32位。
* IP地址具有IP协议提供的一种统一的地址格式， 它为因特网上的每一台主机（或者路由器，或者网络）的每一个接口，都分配一个在全世界范围内唯一的标识符UI（Unique Identifiers），也就是逻辑地址，以此屏蔽下层的物理地址。
* 随着互联网的迅速发展，IPv4定义的有限地址空间必将不足。
	>2011年ICANN宣布可用的IPv4地址已耗尽，而IPv4地址空间最为富足的ARIN也于2015年宣布北美的IPv4地址耗尽）。

* 由此，人们提出了IPv4的下一个版本IPv6，其地址长度为128位，几乎可以不受限制地为全球提供IP地址。
[3][4][5][6]



### IPv4地址
* __IPv4地址__由长32bit的二进制数组成，通常以点分十进制法表示为十进制数，总共有2^32-1个地址。如：
	* 10000000.00001010.00000010.00000001
	* 即128.10.2.1

### IPv6地址
* 目前人们使用的IPv4分址方法为无分类编址CIDR，可惜即便CIDR的使用延迟了IPv4地址用完的日期，但目前的IPv4地址的确已耗尽，人们为解决此问题而开始采用具有更大地址空间的新版本IP，即IPv6。
* IPv6地址相比起IPv4，其主要变化如下——
 * 更大的地址空间：IPv6地址为128位二进制数，地址位数是IPv4的4倍，在可预见的将来完全足够全球使用；
 * 扩展的地址层次结构：地址空间大，所以有更多的层次可以划分；
 * 灵活的首部格式：有许多可选的扩展首部；
 * 增强的选项：可以包含新的选项，可提供新的设施；
 * 允许协议继续扩充，适应底层网络硬件或新的应用；
 * 支持即插即用，即自动配置；
 * 支持资源预分配。
* IPv6使用冒号十六进制记法，将每个16位的值用十六进制表示，其间以冒号分隔。
 * 零压缩：将一串连续的零用一对冒号取代，一个地址中只可用一次；
 * 如：FF05:0:0:8C64:0:0:0:B3，缩写为：FF05::8C64:0:0:0:B3或FF05:0:0:8C64::B3；
[4][7]

# IP地址分配管理
---
## 1、总述
___
- __IANA__三大职能之一，便是协调全球IP和自治系统号（Autonomous System Numbers，即AS号），并将它们分配到各大**地区性互联网注册管理机构（Regional Internet Registries，即RIRs）**；
	>（互联网中，一个自治系统(AS)是一个有权自主地决定在本系统中应采用何种路由协议的小型单位，将会分配到一个全局的唯一的16位号码，即自治系统号（AS号），也可说是边界网关协议所具有的属性之一）；
 - 这是一个分层的结构，Internet地址资源首先由IANA分配到RIRs，再由RIRs提供给各个国家的域名系统管理机构或者地区性组织、或者Internet服务提供商（ISP）、或者直接提供给用户；而ISP或者管理机构、地区性组织又将其所获得的IP地址提供给用户，或者再提供给下一层的ISP。
 - 一般来说，用户只能从一个机构得到IP地址、AS号等互联网资源。
 - 分配机构在分配地址的同时也进行空闲地址的回收，以达到地址使用效率最大化。

[1][8][9][10]

* **最初**，IANA将地址交由NIC（Network Information Center）统一负责全球地址的规划、管理，同时由Inter NIC、APNIC、RIPE等网络信息中心具体负责美国及全球其它地区的IP地址分配。

	![](http://i.imgur.com/9lpjRar.gif)[11]

 * 此时在IANA下，有3个分支机构分别负责欧洲、亚太地区、美国与其他地区的IP地址资源分配与管理：

		①RIPE（设在比利时的Réseaux IP Européens)，负责整个欧洲地区的IP地址资源分配与管理；

		②APNIC（设在澳大利亚的Asia Pacific Network Information Center），负责亚洲与太平洋地区的IP地址资源分配与管理；

		③ARIN（设在美国的American Registry for Internet Numbers) ，负责美国与其他地区的IP地址资源分配与管理。


* 而后，随着互联网在全球的飞速发展，IANA被负责协调IANA责任范围的非营利机构ICANN(Internet Corporation for Assigned Names and Numbers，互联网名称与数字地址分配机构)掌管。
	>The Internet Assigned Numbers Authority (IANA) is the entity that oversees global IP address allocation, DNSroot zone management, and other Internet protocol assignments. It is operated by ICANN. [12]

* **目前**，在ICANN下的IANA，将IPv4/IPv6地址以及AS号码分配给__五大地区性互联网注册管理机构(RIRs)__，而分配互联网号码资源(IPv4、IPv6以及AS号码资源)，注册数据的存储和维护，提供一个开放的、公开的、可访问的数据库是RIRs所共同的责任。

	![](http://i.imgur.com/IMoAMw6.jpg)[10]

 * **AFRINIC（The African Network Information Center）**

		![](http://i.imgur.com/8mJPq3u.png)[13]

		AFRINIC（非洲网络信息中心）是非洲的区域互联网注册机构（RIR），负责非洲地区的互联网号码资源如IP地址、ASN（自治系统号）的分配和管理。

		2005四月，ICANN根据其icp-2文档定义的标准（对于区域互联网注册管理机构设置标准），认可afrinic作为第五个世界性区域互联网注册机构。

		AFRINIC的使命是提供专业、高效的互联网号码资源分布于非洲的互联网社区，支持整个非洲大陆的互联网技术的应用和发展，通过鼓励参与政策制定加强非洲的互联网自我治理。

		[AFRINIC官方网站](http://afrinic.net/)

 * **APNIC（Asia Pacific Network Information Centre)）**

		![](http://i.imgur.com/PTzJm5z.jpg)[14]

		APNIC（亚太网络信息中心）是一个开放的、会员制的、不以营利为目的的组织，是五个区域互联网注册管理机构（RIR）之一，负责亚洲/太平洋地区IP地址的分配公平和负责任的管理相关资源。

		APNIC控股有限公司是于2001在澳大利亚成立，其愿景为“全球，开放，稳定和安全的互联网，服务于整个亚太共同体”（"A global, open, stable, and secure Internet that serves the entire Asia Pacific community"）。

		APNIC的使命是在会员国和其他国家的服务中提供互联网注册服务的信任，提供中立性和准确性的最高可能的标准，提供信息、培训和支持服务，同时协助社区建设和管理互联网、支持关键的互联网基础设施，以帮助社区创建和维护一个强大的互联网环境，为其愿景和社区提供领导和支持，促进APNIC区域互联网发展需要。

		APNIC不参与管理域名系统（DNS）和不负责域名注册，而是与社区合作。与此同时，APNIC积极参与互联网基础设施的整个区域的发展，包括提供培训和教育服务，支持诸如根服务器部署等技术活动，以及参与其他区域和国际组织的合作等。

		[APNIC官方网站](https://www.apnic.net/)

 * **ARIN（American Registry for Internet Numbers）**
 
		![](http://i.imgur.com/xT8hCCZ.jpg)[15]

		ARIN（美国互联网号注册机构）提供加拿大，美国、北大西洋群岛和一些加勒比岛屿地区的互联网号码资源的技术协调和管理相关的服务，是一个非营利组织成员为基础的组织。

		ARIN成立于1997十二月，设立于美国维吉尼亚州，是5个RIRs之一。

		ARIN的任务是提供与各服务区内的互联网号码资源的技术协调和管理服务。参与全球互联网社群；促进其成员和各利益相关者在其区域内制定的政策决策；支持通过在其服务区域网络数字资源管理互联网的运行，协调发展的政策，通过社区网络数字资源管理，提出通过互联网信息服务。这些服务分为四个方面：注册、组织、政策开发和技术。

		[ARIN官方网站](https://www.arin.net/)

 * **LACNIC（the Latin American and Caribbean Internet Addresses Registry）** 

		![](http://i.imgur.com/U28Y5L0.jpg)[16]

		LACNIC（拉丁美洲和加勒比互联网地址注册机构）是一个国际非政府组织，负责分配和管理拉丁美洲和一些加勒比群岛的互联网号码资源（IPv4，IPv6）、自治系统号码，同时为其反向解析和其他资源。

		LACNIC成立于2002年，设立于乌拉圭，是全球范围内存在的五个区域互联网注册机构RIRs之一。

		LACNIC致力于地区的互联网发展，通过积极合作的政策，促进和维护地方社区的利益，将使互联网创建有利于所有拉美和加勒比的国家与公民利益的环境，促使社会和谐与经济发展。其管理和运行的董事会由管理机构成员选举产生，超过4500个网络运营商在33个拉丁美洲和加勒比地区提供服务。

		[LACNIC官方网站](http://www.lacnic.net/web/lacnic/ipv6)

 * **RIPE NCC(Reseaux IP Europeens Network Coordination Center)**
 
		![](http://i.imgur.com/gIIpExJ.jpg)[17]

		RIPE NCC（RIPE网络协调中心）是欧洲、中东和中亚地区的区域互联网注册管理机构，分配和注册互联网号码资源块的互联网服务提供商（ISP）和其他组织。

		RIPE NCC成立于2002年，是非盈利性的组织，致力于支持社区和更广泛的网络社区建设。它的成员包括主要的互联网服务提供商(ISP) 、电信组织、以及位于欧洲、中东和中亚部分地区的大型企业。

		[RIPE官方网站](https://www.ripe.net/)

 * **NRO（The Nnmber Resource Oganization）**

		![](http://i.imgur.com/k8oyHKz.jpg)[18]

		NRO（号码资源组织）是一个协调机构，五个区域互联网注册管理机构（RIR）管理互联网号码资源包括IP地址和自治系统号码的分布。每个项目由其所在区域的网络社区。

		2003十月24，现有的四个RIRs——APNIC，ARIN，RIPE NCC进行互联，并订立了MOU（Memorandum of Understanding）组成NRO。afrinic成立于2005四月，之后它也签署了MOU，加入NRO。

		NRO的任务是积极贡献一个开放、稳定、安全的互联网，提供和促进一个协调的网络号码登记系统、多利益相关者模型与自底向上的政策过程、在网络治理中的权威性，从而协调和支持RIR的关节活动。

		[NRO官方网站](https://www.nro.net/)

* 除此之外，许多国家和地区都成立了**自己的域名系统管理机构**。
 * 各国或各地区自己的域名系统管理机构从RIRs获取IP地址资源后，负责在本国或本地区的分配与管理事务。
 * 这些国家和地区的域名系统管理机构大多属于半官方或准官方机构。但在实际运作过程中，相关国家或地区的政府至少在业务上对其不加干预，使其成为RIRs在各该国家或地区的附属机构，如日本的JPNIC和中国的CNNIC均属此类机构。[12]
* IANA用一定的方式来对分配给RIRs的数字资源进行控制，同时由工作人员通过日常统计报告来确认RIRs是否有违反已公布规则的内容，即自相矛盾的行为。
 * IPv4地址的分配按照规定的计划执行，不能通过申请获取。IANA每年进行两次分配（3月&9月），检查，再分配给RIRs和运营社区，IANA同时更新分配情况；
 * IPv6地址和AS号，RIRs和运营社区可以通过向IANA提出申请来获得，申请需要合理以及满足一定的要求；
 * 此外IANA还会将非单播地址分配到IETF。[1]

example-IPv6：

![](http://i.imgur.com/Zfz0tAV.jpg)[1]



## 2、具体地址分配
***
### 1、IPv4地址
* IANA中IPv4地址分配内容，包括IPv4地址空间分配、IPv4组播地址分配、IPv4专用地址注册、IPv4地址空间的注册表恢复，具体可在[IANA-Number Resources](https://www.iana.org/numbers)中查询，如[IPv4地址空间](http://www.iana.org/assignments/ipv4-address-space/ipv4-address-space.xhtml)。
[19]
#### （1）编址
* __最基本的编址方法——分类IP__
 * IP地址::={<网络号>，<主机号>}
		* 网络号：用于识别主机所在的网络；
		* 主机号：用于识别该网络中的主机；
 * 寻址时，先寻网络号，再寻主机；
 * 分类的IP地址：

	![](http://i.imgur.com/nz51R6r.jpg)[20]

 * 各类地址的地址范围、指派范围和最大主机数：

		![](http://i.imgur.com/Q3UB1KW.jpg)
		![](http://i.imgur.com/qtT2QdB.png)

 * IP地址管理机构在分配IP地址时，只分配网络号，而得到该网络号的单位可自行分配范围内的主机号。


* __改进后的编址方法——划分子网__
 * IP地址::={<网络号>，<子网号>，<主机号>}
 * 寻址时，先寻网络号，再寻子网号，再寻主机号；
 * 子网掩码：将IP地址划分为网络地址和主机地址
	 * 格式：32bit二进制数，与IP地址对应，网络号与子网号全为1，主机号全为0，如255.255.255.0；
 * IP地址的网络地址 = 子网掩码“与”IP地址（逐位相与） = {<网络号>，<子网号>，0}

		![](http://i.imgur.com/QHo2BUq.jpg)[21]

 * 未划分子网的网络将使用默认子网掩码。

		![](http://i.imgur.com/NHHz4Oz.jpg)[22]


* __目前使用的编址方法——构成超网__
 * IP地址::={<网络前缀>，<主机号>}
 * 消除ABC类地址，不再划分子网，而是自由划分网络前缀（即网络号）和主机号；
 * IP地址的网络地址 = 子网掩码“与”IP地址
	 * 斜线记法："IP地址/前缀所占位数"，如128.14.35.7/20，表示此IP地址的前20位为网络前缀，后12位为主机号；
 * 无分类编址CIDR（Classless Inter-Domain Routing）：即无类别域间路由选择，构成超网。将网络前缀相同的、连续的IP地址组成一个“CIDR”地址块，即将一组较小的网络地址聚合，使其成为一个较大的单一路由表项，从而减少网络中路由表项的数量。

		![](http://i.imgur.com/T5iyBOs.gif)[23]
[4][24]

***

### （2）保留地址
__保留地址__是IANA在IP地址范围内，保留了一部分地址专门用于内部局域网或测试等有特殊需要之处。

* __特殊IP地址__
 * 0.0.0.0：表示在本网络上的本主机，所有不清楚的主机和目的网络。可以是源地址，不可以是目的地址。

 * 255.255.255.255：表示限制广播地址，只在本网络（同一广播域）上进行广播，各路由器均不转发。不可以是源地址，可以是目的地址。

 * 127.0.0.1：表示本地软件回环测试地址。可以是源地址，可以是目的地址。

 * D类地址（224.0.0.0~239.255.255.255）：表示组播地址，224.0.0.1特指所有主机，224.0.0.2特指所有路由器，用于组播。

 * 169.254.x.x：表示DHCP服务器发生故障或响应超时后，系统分配给主机的地址，此时网络大多不能正常运行。

 * 网络号全为0，主机号为host-id：表示本网段上的某个主机host-id。

 * 网络号全为1，主机号为host-id：表示所有网络。

 * 网络号为net-id，主机号全为1：对网络net-id上的所有主机进行广播。

 * 网络号为net-id，主机号全为0：网络net-id。

* __私有地址__
 * 私有地址是指在IP地址范围内，划分出一部分地址专门用于内部局域网使用。这部分地址不能出现在公共网络IP中，而是被大量用于如企业等有需要的内部网络中。因为私有地址与外网不能直接连通，所以内部网络中可以随意分配所需IP地址。

 * 当使用私有地址的内部网络在接入外部公网时，需要使用网络地址转换(NAT)，将内部的私有地址翻译成公用合法地址，才能实现内网主机和外网通信。

 * 目前IPv4私有地址为以下四段：
		* A类：10.0.0.0－10.255.255.255
		* A类：100.64.0.0－100.127.255.255（2012年加入）
		* B类：172.16.0.0－172.31.255.255
		* C类：192.168.0.0－192.168.255.255

[4][19][25]

### 2、IPv6地址
* IANA中IPv6地址分配内容，包括IPv6的地址空间、IPv6全球单播配置、IPv6参数（参数描述了IPv6，包括头类型，操作码，等）、IPv6任播地址分配、IPv6组播地址分配、IPv6子TLA作业（不推荐使用）、IANA IPv6特殊注册表、IPv6的全球部署的公告（七月1999 14）、RIR比较政策概述，具体可在[IANA-Number Resources](https://www.iana.org/numbers)中查询，如[IPv6地址空间](http://www.iana.org/assignments/ipv6-address-space/ipv6-address-space.xhtml)。[26]

####（1）编址
* IPv6的地址类型分单播、多播、任播；

* __单播__
 * 传统的点对点通信，单一接口的地址，发送到单播地址的数据包被送到由该地址标识的接口，总地址空间占所有IPv6地址的1/8（头三位固定为001）；
 * IPv6单播地址的划分方式和CIDR相似，通常，一个128位的IPv6地址可以分为一个64位的网络前缀和一个64位的主机地址，主机地址通常根据物理地址自动生成；
 * IP地址::={<网络前缀>，<主机号>}，也使用斜线记法，表示为：地址/前缀长度；

	![](http://i.imgur.com/gKsspJe.png)

 * 网络前缀::={<全球路由选择前缀>，<子网标识符>}；
 * 全球路由选择前缀前3位固定为001，后45位可进行分配，而子网标识符则用于各公司和机构创建自己的子网，接口标识符即主机号；


* __多播（组播）__
 * 一点对多点的通信，一组接口的地址（通常分属不同节点），发送到多播地址的数据报被送到由该地址表示的每个接口；

	![](http://i.imgur.com/qbC3rRg.png)

 * 标志字段目前只指定了第4位，用于表示该地址是临时组播地址（该位为1）还是永久组播地址（该位为0）；
 * 范围字段表示组播包括的节点的范围，取值0~15；
 * 广播是多播的特例。


* **任播（任意播送）**
 * IPv6增加的类型，一组接口的地址（通常分属不同节点），发送到任意播送地址的数据报被送到由该地址标识的其中一个接口（通常为距离最近的一个）。

	![](http://i.imgur.com/eEXM4Jp.png)

 * 泛播地址不能作为源地址，不可非陪给IPv6主机，只可分配给IPv6路由器。
[4][7]


#### （2）特殊地址
* 未指明地址
 * 全0地址0:0:0:0:0:0:0:0，缩写为"::"或"::/128"，只可由主机当作源地址使用，不可作为目的地址；
* 环回地址
 * 地址0:0:0:0:0:0:0:1，缩写为"::1"或"::1/128"，作用等同IPv4环回地址；
* 基于IPv4的地址（IPv4映射的IPv6地址）
 * 地址前80位为全0，中间16位为全1，最后32位对应IPv4地址，可记为"::FFFF:0:0/96"，表示把IPv4地址嵌入到IPv6地址中；
* 本地链路单播地址
 * 地址FE80::/10，用于使用TCP/IP协议却没有连接到互联网上的主机之间的互相通信。

[26]

[全球IP分配表](http://www.iana.org/assignments/as-numbers/as-numbers.xml)


## 3、国内申请IP地址流程
---
- APNIC负责亚太地区，我国申请IP地址要通过APNIC，申请时要考虑申请哪一类的IP地址，然后向国内的代理机构提出。[29]

	![](http://i.imgur.com/PfdlVJW.jpg)[27]

- 国内IP地址申请步骤：

	![](http://i.imgur.com/pMk3kX8.jpg)[28]


##参考文献和资料

[1] [icann - Number Resources - 《iana101-numbers》](https://icann.adobeconnect.com/p7d74qdis3o/?launcher=false&fcsContent=true&pbMode=normal)

[2] [iana - 《Glossary of terms》（术语汇编）](http://www.iana.org/glossary)

[3] [RFC791 - 《INTERNET PROTOCOL&DARPA INTERNET PROGRAM&PROTOCOL SPECIFICATION》](http://datatracker.ietf.org/doc/rfc791/)

[4] 谢希仁，《计算机网络》（第六版），电子工业出版社，2013年6月

[5] [《ICANN将宣布IPv4地址耗尽 全球进入IPv6时代》 来源：搜狐IT 2011年02月02日](http://it.sohu.com/20110202/n279200756.shtml)

[6] [《IPv4地址耗尽对我们意味着什么》 来源：网界网 2015年12月24日](http://news.cnw.com.cn/news-international/htm2015/20151224_323905_2.shtml)

[7] [《第5章：IPv6报文结构》，百度文库](http://wenku.baidu.com/link?url=aGJ4FMsnbMeS2cgXkeZ9p3_xwO0uqDQWQbJmrJrW6Y3_wVuUIoFje-x5wQaeOaMNR0z5nPlAtrW2brgzLE5d4UOVaFBwYrhsYriRt3XaTwS)

[8] [wikipedia - 《Autonomous system (Internet)》](https://en.wikipedia.org/wiki/Autonomous_system_(Internet))

[9] [iana - 《Introducing IANA》](http://www.iana.org/about)

[10] [iana - 《Number Resources》](http://www.iana.org/numbers)

[11] [《IP地址及其管理》教学设计](http://courses.teacher.com.cn/DisplayInfo.aspx?ID=60484&subject=43&item=7)

[12] [《互联网数字分配机构IANA介绍》](http://www.dnshow.cn/help/zhuanjia/1330311151179.html)

[13] [AFRINIC官方网站](http://afrinic.net/)

[14] [APNIC官方网站](https://www.apnic.net/)

[15] [ARIN官方网站](https://www.arin.net/)

[16] [LACNIC官方网站](http://www.lacnic.net/web/lacnic/ipv6)

[17] [RIPE官方网站](https://www.ripe.net/)

[18] [NRO官方网站](https://www.nro.net/)

[19] [IPv4地址空间](http://www.iana.org/assignments/ipv4-address-space/ipv4-address-space.xhtml)

[20] [《IP地址和子网掩码》](http://imoocmooc.dlut.edu.cn/nodedetailcontroller/visitnodedetail?knowledgeId=2909652)

[21] [《IP协议详解之子网寻址、子网掩码、构造超网》](http://www.cnblogs.com/way_testlife/archive/2010/10/05/1844399.html)

[22] [《【CCNA教材】2.4.4 IP地址与默认子网掩码》](http://ccna.edufly.cn/CCNAziliao/5862.html)

[23] [RFC4632 - 《Classless Inter-domain Routing (CIDR):The Internet Address Assignment and Aggregation Plan》](http://tools.ietf.org/html/rfc4632)

[24] [《路由汇聚、路由协议》](http://lyj.fj61.net/show.aspx?id=536&cid=87)

[25] [RFC6598 - 《IANA-Reserved IPv4 Prefix for Shared Address Space》](http://tools.ietf.org/html/rfc6598)

[26] [IPv6地址空间](http://www.iana.org/assignments/ipv6-address-space/ipv6-address-space.xhtml)

[26] [RFC5156 - 《 Special-Use IPv6 Addresses》](https://datatracker.ietf.org/doc/rfc5156/)

[27] [《CNNIC全程助力中国向下一代互联网过渡》](http://www.cnnic.cn/cnnicztxl/IPV6zt/)

[28] [《IP/AS申请步骤》](http://www.cnnic.cn/jczyfw/ipas/IPv4dzsq/201406/t20140630_47343.htm)

[29] [中国互联网络信息中心CNNIC](http://www.cnnic.cn/)
