#搭建支持DNSSec协议的DNS服务器，安全机理详解#

##实验任务##
1. 解释DNSSec的存在意义
2. 搭建支持DNSSec协议的DNS服务器
3. 对服务器工作的安全机理进行详细解释

##实验说明

###具体实验
1. 搭建DNS服务器
2. 进行DNS劫持实验
3. 进行DNS投毒实验
4. 在DNS服务器上成功配置DNSSec

##实验过程及结果

###一、搭建DNS服务器

  首先安装dns服务器软件：BIND

  执行安装指令：

    apt-get install bind9 dnsutils

结果如下：

![image](images/pic01.png?raw=true)

在文件位置cd /etc/bind在里面创建文件db.example.com，文件内容：

    ;
    ; BIND data file for example.com
    ;
    $TTL    604800
    @       IN      SOA     ns.example.com. root.example.com. (
                                1               ; Serial
                                604800          ; Refresh
                                86400           ; Retry
                                2419200         ; Expire
                                604800 )        ; Negative Cache TTL
    ;
    @       IN      NS      ns.example.com.
    ns      IN      A       10.0.2.15

    ;also list other computers
    box     IN      A       10.0.2.15

以及db.10文件，文件内容：

    ;
    ; BIND reverse data file for a test domain (in local)
    ;
    $TTL    604800
    @       IN      SOA     ns.example.com. root.example.com. (
                                2               ; Serial
                                604800          ; Refresh
                                86400           ; Retry
                                2419200         ; Expire
                                604800 )        ; Negative Cache TTL
    ;
    @       IN      NS      ns.
    10      IN      PTR     ns.example.com.

    ; also list other computers
    21      IN      PTR     box.example.com.


修改named.conf.local文件内容，将：

    zone "example.com" {
             type master;
             file "/etc/bind/db.example.com";
        };
替换为：

    zone "2.0.10.in-addr.arpa" {
             type master;
             notify no;
             file "/etc/bind/db.10";
        };

检验配置情况，命令：

    named-checkconf
    named-checkzone example.com /etc/bind/db.example.com
    named-checkzone 2.0.10.in-addr.arpa. /etc/bind/db.10

情况如下：

![image](images/pic02.png?raw=true)

修改主机的dns服务器地址为自己的dns服务器地址：

    gedit  /etc/resolv.conf

![image](images/pic03.png?raw=true)

打开服务器：

    /etc/init.d/bind9 start

![image](images/pic04.png?raw=true)

执行指令：

    dig localhost

![image](images/pic05.png?raw=true)

执行指令：

    dig ns.example.com

![image](images/pic06.png?raw=true)

再执行指令，查找一个本地不存在的网址记录（可能需要等待一段时间）：

    dig baidu.com

![image](images/pic07.png?raw=true)

服务器成功地找到了baidu.com的ip地址，至此可说明一个可用的dns服务器已搭建完毕。



###二、在 DNS服务器上部署DNSSEC

####激活DNSSEC####

在BIND的配置文件中打开DNSSEC选项在/etc/bind/named.conf.options中加入以下部分

    options {
        directory "/var/cache/bind";
        dnssec-enable yes;
        dnssec-validation yes;
        dnssec-lookaside auto;
    }

####配置Trust anchor####

在配置文件中加入：

    trusted-keys {
        “test.net.”  256 3 5  “XJYm3DXd0wnBaq+vYaOsqKh17zrJx4p5HSkcaPqxAmeNQToJQfe8yZ9L 2iR/dhgU8LUi4bs6ICfbdG/eAxa+9g==”;
    };

####配置权威服务器####
先找到以下目录：

    cd /var/cache/bind
在里面创建文件db.test.net：

    $TTL    604800
    @       IN      SOA     ns.test.net. root.test. net. (
                                  1         ; Serial
                             604800         ; Refresh
                              86400         ; Retry
                            2419200         ; Expire
                             604800 )       ; Negative Cache TTL
    @      IN      NS      ns.test.net.
    ns     IN      A       125.125.125.125

####生成签名密钥对####
首先安装haveged，来加快秘钥生成速度：

    apt-get install haveged
然后为区（zone）文件生成区签名密钥ZSK和密钥签名密钥KSK：

    dnssec-keygen -a RSASHA1 -b 512 -n ZONE test.net
    dnssec-keygen -f KSK -a RSASHA1 -b 512 -n ZONE test.net

![image](images/pic15.png?raw=true)

然后生成了几个文件：

 ![image](images/pic16.png?raw=true)
然后把db.test.net改为：

    $TTL    604800
    $INCLUDE Ktest.net.+005+02373.key
    $INCLUDE Ktest.net.+005+17296.key
    @       IN      SOA     ns.test.net. root.test.net. (
                              1         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800  ）     ; Negative Cache TTL
    @       IN      NS      ns.test.net.
    ns      IN      A       125.125.125.125
执行签名操作，生成db.test.net.signed：

    dnssec-signzone  -g -o test.net. db.test.net

![image](images/pic17.png?raw=true)

最后向/etc/bind/named.conf.local加入

    zone "test.net" {
    type master;
    file "db.test.net.signed";
    };
检验，可见dns资源记录中DNSSEC的RRSIG字段已生成，公私钥匹配完成：

![image](images/pic18.png?raw=true)

####发布公钥####
要让其他人验证我的数字签名，其他人必须有一个可靠的途径获得我
的公开密钥。DNSSEC通过上一级域名服务器数字签名的方式签发我的
公钥。
如果上一级域名服务器还没有配置DNSSEC，则不得不另找其他方式了
，比如，把上述两个文件提交到一些公开的trust anchor数据库中发布
，或者直接交给愿意相信我的解析服务器的
管理员，配置到trust anchor文件中。






###三、 DNS劫持实验

**重要说明：DNSSEC的保障同时需要客户端的支持。如果客户端没有强制要求DNSSEC的话，那么对于即使部署了DNSSEC的域名，也不会强制请求DNSSEC有关的记录，导致DNSSEC的起不到保护客户端的作用。详见实验对比。**

**注2：DNSSEC起作用需要DNS服务器、域名提供者、客户端的三者同时有效才能发挥作用。部分DNS服务器并不提供DNSSEC服务，比如202.205.16.4(学校的DNS服务器)。详见[附加实验](#exp_extra)**

####实验环境
1.  使用软件：VirtualBox
2.  虚拟机环境：


    类型             | 操作系统              | IP
    ----             | ----                  | ----
    DNSSec服务器     | Ubuntu 14.04 LTS      | IP:10.0.2.15
    攻击服务器       | Kali 2.0              | IP:10.0.2.4
    受害者           | Ubuntu 14.04 LTS      | IP:10.0.2.5


3.   **上网方式：NAT网络。三个虚拟机处于同一个NAT网络中。**


####实验构想
使用Kali作为中间人，攻击受害者。将几个测试域名均劫持到*新闻学院的IP:202.205.16.2*上。

几个测试域名分别为：

    *   www.baidu.com
    *   dnssectest.sidnlabs.nl (注：该域名开启了DNSSEC保护）
    *   www.cuc.edu.cn (原IP: 202.205.16.1)

使用工具为ettercap 0.8.2

分别测试在DNS未劫持/劫持时，客户端开启/未开启DNSSEC强制验证时，DNS的解析结果，以及用浏览器访问该域名时的效果。

####实验流程

#####步骤1. 清空DNS缓存

```bash
    sudo service dns-clean start
```

#####步骤2. 验证当前的DNS解析记录。(未污染时)

```
$dig www.baidu.com +dnssec +multiline
```

```
; <<>> DiG 9.9.5-3ubuntu0.3-Ubuntu <<>> www.baidu.com +dnssec +multiline
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 38651
;; flags: qr rd ra; QUERY: 1, ANSWER: 3, AUTHORITY: 5, ADDITIONAL: 6

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags: do; udp: 4096
;; QUESTION SECTION:
;www.baidu.com.     IN A

;; ANSWER SECTION:
www.baidu.com.      280 IN CNAME www.a.shifen.com.
www.a.shifen.com.   300 IN A 220.181.112.244
www.a.shifen.com.   300 IN A 220.181.111.188

;; AUTHORITY SECTION:
a.shifen.com.       240 IN NS ns3.a.shifen.com.
a.shifen.com.       240 IN NS ns1.a.shifen.com.
a.shifen.com.       240 IN NS ns2.a.shifen.com.
a.shifen.com.       240 IN NS ns4.a.shifen.com.
a.shifen.com.       240 IN NS ns5.a.shifen.com.

;; ADDITIONAL SECTION:
ns1.a.shifen.com.   240 IN A 61.135.165.224
ns2.a.shifen.com.   240 IN A 180.149.133.241
ns3.a.shifen.com.   240 IN A 61.135.162.215
ns4.a.shifen.com.   240 IN A 115.239.210.176
ns5.a.shifen.com.   240 IN A 119.75.222.17

;; Query time: 222 msec
;; SERVER: 127.0.1.1#53(127.0.1.1)
;; WHEN: Sun Jan 03 01:50:35 CST 2016
;; MSG SIZE  rcvd: 271
```

```
$dig www.cuc.edu.cn +dnssec +multiline
```

```
; <<>> DiG 9.9.5-3ubuntu0.3-Ubuntu <<>> www.cuc.edu.cn +dnssec +multiline
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 6072
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 3, ADDITIONAL: 5

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags: do; udp: 4096
;; QUESTION SECTION:
;www.cuc.edu.cn.        IN A

;; ANSWER SECTION:
www.CUC.edu.cn.     3137 IN A 202.205.16.1

;; AUTHORITY SECTION:
CUC.edu.cn.     171934 IN NS BDNS.CUC.EDU.CN.
CUC.edu.cn.     171934 IN NS BDNS2.CUC.EDU.CN.
CUC.edu.cn.     171934 IN NS PDNS.CUC.EDU.CN.

;; ADDITIONAL SECTION:
BDNS.CUC.edu.cn.    171934 IN A 202.205.16.3
PDNS.CUC.edu.cn.    171934 IN A 202.205.16.5
PDNS.CUC.edu.cn.    85534 IN AAAA 2001:250:217:16::5
BDNS2.CUC.edu.cn.   171934 IN A 60.247.40.3

;; Query time: 0 msec
;; SERVER: 127.0.1.1#53(127.0.1.1)
;; WHEN: Sun Jan 03 01:50:44 CST 2016
;; MSG SIZE  rcvd: 227
```

```
$dig dnssectest.sidnlabs.nl +dnssec +multiline
```

```
; <<>> DiG 9.9.5-3ubuntu0.3-Ubuntu <<>> dnssectest.sidnlabs.nl +dnssec +multiline
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 48964
;; flags: qr rd ra ad; QUERY: 1, ANSWER: 4, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags: do; udp: 4096
;; QUESTION SECTION:
;dnssectest.sidnlabs.nl.    IN A

;; ANSWER SECTION:
dnssectest.sidnlabs.nl. 3112 IN CNAME check.sidnlabs.nl.
dnssectest.sidnlabs.nl. 3112 IN RRSIG CNAME 8 3 3600 (
                20160121173131 20151222164033 20853 sidnlabs.nl.
                ESV1d0Ol8LOKzRuRNwcFLe1BOyjGAwblyNbXgljzO3pt
                X8oyXdF5gEumig/TrPiX7+CNi3TU9tAImAplEeOlYVFv
                zxHsz2VHH19rrHVUAwHiTPtZe/iAyyYsd3/IvjudF/yj
                +ghvHOYos+vO9gSkQ+KDsNFYXsGL3aNA/KOxEp8= )
check.sidnlabs.nl.  2608 IN A 94.198.159.35
check.sidnlabs.nl.  2608 IN RRSIG A 8 3 3600 (
                20160121162239 20151222152659 20853 sidnlabs.nl.
                Pn1YKKc/kEJzsG/EwDWpsVC0gup8YF6Oguu+A9gmxra+
                o9rYr/00jzvmSfItjq+uFliqGNxwvCxxIB4d74YYrXJK
                YEP2ne0UGlHG0eV1BC/83R/m2wyGiYJadK1Ht4EJympN
                541xTiVcUiGqpMmveUnC4FI287ut8mVB9ogMfcw= )

;; Query time: 0 msec
;; SERVER: 127.0.1.1#53(127.0.1.1)
;; WHEN: Sun Jan 03 01:50:57 CST 2016
;; MSG SIZE  rcvd: 429

```

我们可以看到，在即使均加入+dnssec选项时，只有dnssectest.sidnlabs.nl这个域名返回了DNSSEC的RRSIG记录。

<a name='attack'></a>
#####步骤3.实施攻击
1. 准备工作。配置ettercap的DNS劫持选项。

    在Kali里打开/etc/ettercap/etter.dns 加入如下内容
        
        www.baidu.com A 202.205.16.2
        www.cuc.edu.cn A 202.205.16.2
        dnssectest.sidnlabs.nl A 202.205.16.2


2. 实施攻击

    在Kali中执行

        ettercap -i eth0 -T -q -P dns_spoof -M ARP:remote /// ///

    备注
    *   攻击同时利用了ARP欺骗攻击，使得受害者的流量可以从中间人走过，从而修改流量。
    *   也可以使用`ettercap -G`使用ettercap的GUI。请注意加载dns_spoof插件。


#####步骤4. 查看当前的DNS解析记录。(被劫持后，客户端没有采用DNSSEC强制政策)


**重要说明：DNSSEC的保障同时需要客户端的支持。如果客户端没有强制要求DNSSEC的话，那么对于即使部署了DNSSEC的服务器，也不会强制请求DNSSEC有关的记录，导致DNSSEC的起不到保护客户端的作用。**


在受害者上执行

```
$dig www.baidu.com +dnssec +multiline
```

```
; <<>> DiG 9.9.5-3ubuntu0.3-Ubuntu <<>> www.baidu.com +dnssec +multiline
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 31931
;; flags: qr aa ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;www.baidu.com.     IN A

;; ANSWER SECTION:
www.baidu.com.      3600 IN A 202.205.16.2

;; Query time: 1 msec
;; SERVER: 127.0.1.1#53(127.0.1.1)
;; WHEN: Sun Jan 03 02:33:08 CST 2016
;; MSG SIZE  rcvd: 47
```

```
$dig www.cuc.edu.cn +dnssec +multiline
```

```
; <<>> DiG 9.9.5-3ubuntu0.3-Ubuntu <<>> www.cuc.edu.cn +dnssec +multiline
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 61760
;; flags: qr aa ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;www.cuc.edu.cn.        IN A

;; ANSWER SECTION:
www.cuc.edu.cn.     3600 IN A 202.205.16.2

;; Query time: 3 msec
;; SERVER: 127.0.1.1#53(127.0.1.1)
;; WHEN: Sun Jan 03 02:33:10 CST 2016
;; MSG SIZE  rcvd: 48
```

```
$dig dnssectest.sidnlabs.nl +dnssec +multiline
```

```
; <<>> DiG 9.9.5-3ubuntu0.3-Ubuntu <<>> dnssectest.sidnlabs.nl +dnssec +multiline
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 11067
;; flags: qr aa ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;dnssectest.sidnlabs.nl.    IN A

;; ANSWER SECTION:
dnssectest.sidnlabs.nl. 3600 IN A 202.205.16.2

;; Query time: 0 msec
;; SERVER: 127.0.1.1#53(127.0.1.1)
;; WHEN: Sun Jan 03 02:33:12 CST 2016
;; MSG SIZE  rcvd: 56

```

![image](images/pic20.png?raw=true)

可以看到，即使dnssectest.sidnlabs.nl在服务器端部署了DNSSEC，但是客户端依旧会遭受DNS劫持的影响。

#####步骤5.在受害者上部署DNSSEC的强制验证，并重新攻击。

备注：推荐的是使用DNSSEC-Trigger保证强制验证DNSSEC。实际测试中发现
    *   DNSSEC-Trigger并没有deb包，需要编译安装。
    *   DNSSEC-Trigger的前置需求unbound已经自带[DNSSEC验证功能][DNSSEC_unbound]
所以这里直接安装unbound即可。

1.  先在Kali上按q (Ctrl+C不会RE-ARPing the victims)停止攻击

2.  在受害者上安装unbound.
    ```
        sudo apt-get install unbound
    ```

3.  配置unbound。其实已经在安装时配置完成。

    检查/etc/unbound/unbound.conf.d/root-auto-trust-anchor-file.conf是否存在。并且有没有包含在/etc/unbound/unbound.conf中即可。

    编译安装参考[Unbound: Howto enable DNSSEC][DNSSEC_unbound]

4.  重新劫持。[见上](#attack)

5.  重新执行DNS查询
首先执行 `sudo service unbound restart` 重启unbound. 保证清除了未被污染的缓存。

```
$dig www.baidu.com +dnssec +multiline
```

```
; <<>> DiG 9.9.5-3ubuntu0.3-Ubuntu <<>> www.baidu.com +dnssec +multiline
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 26776
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags: do; udp: 4096
;; QUESTION SECTION:
;www.baidu.com.     IN A

;; ANSWER SECTION:
www.baidu.com.      3600 IN A 202.205.16.2

;; Query time: 872 msec
;; SERVER: 127.0.0.1#53(127.0.0.1)
;; WHEN: Sun Jan 03 03:17:23 CST 2016
;; MSG SIZE  rcvd: 58
```

```
$dig www.cuc.edu.cn +dnssec +multiline
```

```
; <<>> DiG 9.9.5-3ubuntu0.3-Ubuntu <<>> www.cuc.edu.cn +dnssec +multiline
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 13058
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags: do; udp: 4096
;; QUESTION SECTION:
;www.cuc.edu.cn.        IN A

;; ANSWER SECTION:
www.cuc.edu.cn.     3600 IN A 202.205.16.2

;; Query time: 347 msec
;; SERVER: 127.0.0.1#53(127.0.0.1)
;; WHEN: Sun Jan 03 03:17:28 CST 2016
;; MSG SIZE  rcvd: 59
```

```
$dig dnssectest.sidnlabs.nl +dnssec +multiline
```

```
; <<>> DiG 9.9.5-3ubuntu0.3-Ubuntu <<>> dnssectest.sidnlabs.nl +dnssec +multiline
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: SERVFAIL, id: 36328
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags: do; udp: 4096
;; QUESTION SECTION:
;dnssectest.sidnlabs.nl.    IN A

;; Query time: 0 msec
;; SERVER: 127.0.0.1#53(127.0.0.1)
;; WHEN: Sun Jan 03 03:17:30 CST 2016
;; MSG SIZE  rcvd: 51

```

我们可以看到，开启了DNSSEC的dnssectest.sidnlabs.nl的解析记录为空。然而，其他2个域名仍然被劫持到新闻学院202.205.16.2。



~~顺便黑了一把新闻学院，banner竟然用Flash做~~

![image](images/pic21.png?raw=true)


<a name='exp_extra'></a>
#####附加实验：202.205.16.4是什么样的呢？
我们关闭DNS劫持。

在受害者上执行。

```
sudo service dns-clean start
dig @202.205.16.4 dnssectest.sidnlabs.nl +dnssec +multiline
```

```
; <<>> DiG 9.9.5-3ubuntu0.3-Ubuntu <<>> @202.205.16.4 dnssectest.sidnlabs.nl +dnssec +multiline
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 48608
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 8, ADDITIONAL: 9

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags: do; udp: 4096
;; QUESTION SECTION:
;dnssectest.sidnlabs.nl.    IN A

;; ANSWER SECTION:
dnssectest.sidnlabs.nl. 3600 IN CNAME check.sidnlabs.nl.
check.sidnlabs.nl.  3598 IN A 94.198.159.35

;; AUTHORITY SECTION:
nl.         131402 IN NS ns3.dns.nl.
nl.         131402 IN NS ns4.dns.nl.
nl.         131402 IN NS ns5.dns.nl.
nl.         131402 IN NS ns-nl.nic.fr.
nl.         131402 IN NS sns-pb.isc.org.
nl.         131402 IN NS nl1.dnsnode.net.
nl.         131402 IN NS ns1.dns.nl.
nl.         131402 IN NS ns2.dns.nl.

;; ADDITIONAL SECTION:
nl1.dnsnode.net.    131402 IN A 194.146.106.42
nl1.dnsnode.net.    131981 IN AAAA 2001:67c:1010:10::53
ns1.dns.nl.     5333 IN AAAA 2a00:d78:0:102:193:176:144:5
ns2.dns.nl.     86860 IN AAAA 2001:7b8:606::85
ns3.dns.nl.     143320 IN AAAA 2001:610:0:800d::10
ns4.dns.nl.     9665 IN AAAA 2a00:1188:5::212
ns5.dns.nl.     144928 IN AAAA 2001:678:2c:0:194:0:28:53
ns-nl.nic.fr.       93844 IN A 192.93.0.4

;; Query time: 130 msec
;; SERVER: 202.205.16.4#53(202.205.16.4)
;; WHEN: Sun Jan 03 04:19:40 CST 2016
;; MSG SIZE  rcvd: 464
```

并没有RRSIG记录。

在受害者上修改/etc/resolv.conf，DNS服务器锁定为202.205.16.4。再在Kali上执行劫持。

![image](images/pic22.png?raw=true)

当然是喜闻乐见被劫持了。


####实验结论
1.  DNSSEC不仅要在服务器上部署。如果不在服务器上开启强制DNSSEC验证形同虚设。
2.  在没有DNSSEC的情况下，DNS会被轻易劫持。
3.  如何防范DNS劫持？
    *   不在不安全的网络中上网。
    *   使用支持DNSSEC的服务器。尽量访问部署了DNSSEC的域名。
    *   开启本地的DNSSEC强行验证。
    *   留心DNS的变化。比如如果baidu.com的解析结果不是CNAME www.a.shifen.com而是A记录则一定有问题。
    *   如果作为站长，请积极部署DNSSEC。



####参考
[1]  [Unbound: Howto enable DNSSEC][DNSSEC_unbound]
[DNSSEC_unbound]:https://unbound.net/documentation/howto_anchor.html "Unbound: Howto enable DNSSEC"


###四、DNS投毒实验

缺少第三方服务器，并没有完成这个实验。这里只写出了实验原理和流程。


####原理：

向DNS缓存服务器发送不存在地址的DNS请求，然后伪造DNS主服务器向DNS缓存
服务器应答，从而把此ip地址映射到自己伪造的地址上。我们首先来分析DNS


####服务器对不存在网址的正常解析过程:

1. 客户端向DNS缓存服务器发送对www.xoxox.org（某不存在的网址）的DNS查询请求。
2. 当DNS缓存服务器上没有www.xoxox.org对应的IP地址，则DNS缓存服务器就会通过迭代的方法最后询问DNS主服务器上保存的www.xoxox.org对应的IP地址。
3. DNS主服务器响DNS缓存服务器的请求，返回www.xoxox.org对应的IP地址。
4.  DNS缓存服务器收到DNS主服务器的应答后，把应答消息转发给客户端。
5. 客户端通过该ip地址访问www.xoxox.org。

这就意味着，攻击方只要伪造响应报文给DNS缓存服务器，DNS缓存服务器上就记录了
错误的域名到IP地址的对应关系，然后DNS缓存服务器把这个错误的对应关系发给客
户端，就可以让他访问攻击方指定的ip地址。由此，可得攻击过程。

####攻击过程:

1. 客户端向DNS缓存服务器发送对www.xoxox.org（某不存在的网址）的DNS查询请求。
2. 当DNS缓存服务器上没有www.xoxox.org对应的IP地址，则DNS缓存服务器就会通过迭代的方法最后询问DNS主服务器上保存的www.xoxox.org对应的IP地址。
3. 在DNS主服务器还未返回给DNS缓存服务器时，攻击方发送响应报文，使之与已发送的dns查询报文的报头ID匹配（DNS报头的ID号是 16位2进制，命中率是1/65536），把错误的域名到IP对应关系告诉DNS缓存服务器，这就是给DNS缓存服务器的一次投毒。
4. DNS缓存服务器把攻击方的应答当成DNS主服务器的应答，并把应答消息转发给客户端。
5. 客户端通过该ip地址访问www.xoxox.org，却进入了攻击方指定的网址。

####防护:

1.  部署多台dns权威服务器，降低攻击效率。
2.  使用DNS ”源端口随机性”较好的软件或者版本，降低投毒命中率。
3.  使用dnssec协议，使攻击者无法伪造响应报文，而且杜绝了dns缓存投毒攻击。

####参考文献：
1. 《DNS安全（一）DNS缓存投毒与防护》http://zdzhu.blog.51cto.com/6180070/1575498
2. 《DNS缓存服务器投毒》网络安全攻防研究室(www.91ri.org) 信息安全小组https://www.91ri.org/2964.html

##名词解释##

###DNSSec###
域名系统安全扩展（Domain Name System Security Extensions），是为域名系统
（Domain Name System）鉴定数据来源和数据完整性、有效性的一种安全机制。主
要解决了DNS欺骗和缓存污染问题。

###DNS欺骗###
当我们用域名访问一个网站时，计算机一般会通过域名解析服务器（Resolver Sever）把域名转换成IP地址。解析服务器一般用过查询根域名服务器（root）、顶级域名服务器（TLD）、权威域名服务器（Authoritative Name Server）,通过递归查询的方式最终获得目标服务器的IP地址，然后交给用户的计算机。在这个过程中，攻击者可以假冒应答方（根、顶级域、权威域、或解析服务器中任意一个）给请求方发送一个伪造的响应，其中包含一个错误的IP地址。发送请求的用户计算机或者解析服务器接受了伪造的应答，导致用户无法访问正常网站，甚至可以把重定向到一个伪造的网站上去。由于正常的DNS解析使用UDP协议而不是TCP协议，伪造DNS的响应报文比较容易；如果攻击者可以监听上述过程中的任何一个通信链路，这种攻击就很容易实现。

###缓存污染###
在互联网上有可信赖的域名服务器，为了减缓阻塞，一般的域名都会暂存域名服务数据，当有机器请求解析，可马上提供。可是如果相关网域的局域域名服务器的缓存受到污染，就会给机器错误的IP地址。由于DNS缓存作用，错误的记录可能相当一段时间不消除，该域名解析服务器下的用户都会产生访问错误的问题。

###DNSSec工作原理###
依靠数字签名保证DNS应答报文的真实性和完整性。权威域名服务器生成自己的秘钥对，然后用的私有密钥对资源记录签名，解析服务器用权威服务器的公钥对收到的应答信息进行验证。若验证失败，表明为假，已在传输、缓存等过程中被篡改。

图例解释可以过程

![image](images/pic08.jpg?raw=true)
