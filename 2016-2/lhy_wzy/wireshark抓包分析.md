##第一题，分析附件提供的pcap中有多少可用AP？将不重复的SSID提交到以下网址，获取通关flag。
	利用python可以转换为字符串
	
	
	找到有eacons广播包的，一共11个ap，写下他们的ssid
	桃花岛训练专用WIFI
	ChinaNet
	CMCC-WEB
	CMCC
	CMCC-EDU
	CUC
	and-Business
	A101E
	CUC-AC-001
	lczhap
	a101e-guest



##第二题，找到WIFI Hacking 1题目附件中所有尝试连接过ssid为a101e-guest的无线客户端MAC地址，并将结果填入到以下网址并提交，获得通关flag。
设置过滤器，查看连接客户端的mac地址

	e2:08:bd:58:1e:3b
	70:14:a6:39:f8:2f
	00:1a:a9:c1:fc:35
	56:75:f1:3c:4c:08
	38:bc:1a:64:2c:08
	6c:25:b9:1f:cb:94
	78:9f:70:03:44:3a
	64:9a:be:82:9f:c5
	60:f8:1d:87:0e:19
	08:70:45:dd:20:a0
	34:23:ba:8b:97:b7




##第三题，找到WIFI Hacking 1题目附件中无线客户端尝试连接过但抓包期间信号覆盖范围内不存在的AP的SSID集合，将结果填入到以下网址并提交，获得通关flag。

	寻找广播请求连接，发送probe请求的，同时后面没有eacons广播包（证明不在范围内）
	筛选出如下四个（sharkAP我这个过滤不到，只找到三个不能通过，问了同学发现有个sharkAP这个包我过滤不到）
	sharkAP
	GGBWG-G
	Chu-Sushi
	Apple Setup





##第四题，找到附件中唯一的一个“乱入”的手机，这部手机没有连接上任何一个热点，但暴漏了它曾经连过很多热点。请将这些热点的SSID集合填入到以下网址并提交，获得通关flag。
	
	从发出请求没有响应的广播中，找到相同mac地址的一台手机，设置为搜索
	
	之后在搜索出来的包中可以找到连接的ssid
	
	利用python转换为字符串
	
	得到答案为
	KL4
	SQBG8701
	LieBaoWiFi744
	XUE
	Feixun_AFE4B3
	gg
	linan
	sxbl
	神州专车
	sft4-1
	ganluyuan5
	Sxblz


##第六题，找到WIFI Hacking 4题目附件中哪些AP支持WPA/WPA2企业级认证方式？请将这些热点的MAC地址集合填入到以下网址并提交，获得通关flag
	筛选出ap，查看mac地址
	52:1a:a9:c1:fc:37
	d8:fe:e3:e5:31:18

##第七题，找到WIFI Hacking 4题目附件中哪些AP可能是设置了禁止SSID广播？试列举所有的BSSID？请将这些热点的MAC地址集合填入到以下网址并提交，获得通关flag。

	找出不会广播自己存在，没有eacons包，同时会对请求做出响应的bssid
	ec:88:8f:95:ff:12
	6c:70:9f:e8:57:90

##第五题，找到WIFI Hacking 4题目附件中哪些AP仅支持使用WPA2 CCMP/AES认证加密模式？请将这些热点的MAC地址集合填入到以下网址并提交，获得通关flag。
筛选出AES*（CCM）和WPA选中包

	得出结果地址
	52:1a:a9:c1:fc:37
	ac:f1:df:78:c7:67
	6c:70:9f:e8:57:90
	ec:88:8f:95:ff:12
