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
    ; BIND data file for local loopback interface
    ;
    $TTL    604800
    @       IN      SOA     ns.example.com. root.example.com. (
                                1         ; Serial
                                604800         ; Refresh
                                86400         ; Retry
                                2419200         ; Expire
                                604800 )       ; Negative Cache TTL
    ;
    @       IN      NS      ns.example.com.
    ns      IN      A       192.168.1.10

    ;also list other computers
    box     IN      A       192.168.1.21
以及db.192文件，文件内容：

    ;
    ; BIND reverse data file for local loopback interface
    ;
    $TTL    604800
    @       IN      SOA     ns.example.com. root.example.com. (
                                2         ; Serial
                                604800         ; Refresh
                                86400         ; Retry
                                2419200         ; Expire
                                604800 )       ; Negative Cache TTL
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

    zone "1.168.192.in-addr.arpa" {
             type master;
             notify no;
             file "/etc/bind/db.192";
        };

修改named.conf.options文件内容，将：

    //forwarders {
    //       0.0.0.0;
    //    };
替换为：

     forwarders {
             1.2.3.4;
             5.6.7.8;
          };
检验配置情况，命令：

    named-checkconf
    named-checkzone example.com /etc/bind/db.example.com
    named-checkzone 1.168.192.in-addr.arpa. /etc/bind/db.192

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

###二、 DNS劫持实验

在该实验中我们拙劣的采用了作为管理者强行修改了DNS资源记录的方式，来展示被劫
持之后，劫持者可以达到何种的恶意目的。并不是作为第三方去真正劫持了一个用户

####实验流程

首先伪造一份用于dns劫持的dns资源记录。

    gedit  /etc/bind/db.google.com

将www.google.com劫持到baidu.com的ip地址(220.181.57.217)

写入文件：

    $TTL    604800
    $ORIGIN google.com.
    @       IN      SOA     ns1.google.com. ns2.google.com.(
                                  1         ; Serial
                             604800         ; Refresh
                              86400         ; Retry
                            2419200         ; Expire
                             604800 )       ; Negative Cache TTL
    @      IN  NS     ns1.google.com. ; in the domain
    ns1    IN  A      220.181.57.217    ;web server definition
    ns2    IN  A      123.1.151.4       ;web server definition
    www    IN  CNAME  ns1.google.com.  ;web server definition
    ftp    IN  CNAME  ns2.google.com.  ;ftp server definitionbox

之后，打开dns服务器，进行验证：

    /etc/init.d/bind9 start
    nslookup www.google.com

![image](images/pic10.png?raw=true)

确认www.google.com已被劫持。

打开wireshark，同时ping目标网址，进行抓包验证：

![image](images/pic11.png?raw=true)
![image](images/pic12.png?raw=true)


结果成功将本应发送给www.google.com的包发给了baidu.com，dns劫持成功。
此时访问www.google.com,则会提示连接已被重置。

![image](images/pic13.png?raw=true)

###三、DNS投毒实验

缺少第三方服务器，并没用完成这个实验。这里只写出了实验原理和流程。


####原理：

向DNS缓存服务器发送不存在地址的DNS请求，然后伪造DNS主服务器向DNS缓存
服务器应答，从而把此ip地址映射到自己伪造的地址上。我们首先来分析DNS


####服务器对不存在网址的正常解析过程:

1. 客户端向DNS缓存服务器发送对www.xoxox.org（某不存在的网址）的DNS查询请求。
2. 当DNS缓存服务器上没有www.xoxox.org对应的IP地址，则DNS缓存服务器就会通过迭
   代的方法最后询问DNS主服务器上保存的www.xoxox.org对应的IP地址。
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
2.    使用DNS ”源端口随机性”较好的软件或者版本，降低投毒命中率。
3.	使用dnssec协议，使攻击者无法伪造响应报文，而且杜绝了dns缓存投毒攻击。

####参考文献：
1. 《DNS安全（一）DNS缓存投毒与防护》http://zdzhu.blog.51cto.com/6180070/1575498
2. 《DNS缓存服务器投毒》网络安全攻防研究室(www.91ri.org) 信息安全小组https://www.91ri.org/2964.html

###四、在 DNS服务器上完成 DNSSec

####激活DNSSEC####

在BIND的配置文件中打开DNSSEC选项在/etc/bind/named.conf.options中加入以下部分

    options {
        directory "/var/cache/bind";
	    dnssec-enable yes;
	    dnssec-validation yes;
	    dnssec-lookaside auto;
    }

####配置Trust anchor####

在文件中加入：

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
    ns      IN      A       125.125.125.125

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



##安全分析##

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
