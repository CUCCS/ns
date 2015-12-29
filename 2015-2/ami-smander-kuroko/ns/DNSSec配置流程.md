#DNSSec配置流程#


##配置安全解析服务器##

###激活DNSSEC###

在BIND的配置文件中打开DNSSEC选项

    options {

    directory “/var/named”;

    dnssec-validation yes;

    ….

    };
这个位置一般为/etc/named.conf


###配置Trust anchor###


要给解析服务器配置可信锚（Trust Anchors）
也就是你所信任的权威域的DNSKEY。

（关于这个部分我自己的理解就是通过层级的信任部署获得根的秘钥，貌似
国内外好多网站可以授权这种信任，具体内容还有一部分没有理解）

文件格式如下：

    trusted-keys {

    “test.net.”  256 3 5  “AQPzzTWMz8qS…3mbz7Fh

    ……

    ….fHm9bHzMG1UBYtEIQ==”;

    “193.in-addr.arpa.” 257 3 5 “AwEAAc2Rn…HlCKscYl

    kf2kOcq9xCmZv….XXPN8E=”;

    };

之后，需要在该可信锚所属文件加入如下的语句

    include “/var/named/sec-trust-anchors.conf”;


###测试###

完成上述修改后重启named进程，到可信锚文件中包含的区或者他的下级域名


在解析服务器中用如下命令测试:

    #dig @127.0.0.1 +dnssec   test.net.  SOA

如果配置正确，应该返回test.net的SOA记录和相应的RRSIG记录，返回的
头部中应该包含AD标志位，表示DNSSEC相关的数字签名验证是正确的

如下:

    ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 1397


    ;; flags: qr rd ra ad; QUERY: 1, ANSWER: 2, AUTHORITY: 2, 
    ADDITIONAL: 3

若配置失败，则调查DNS日志寻找bug
使用前需要在/etc/named.conf配置日志，

配置：

    logging {

    channel dnssec_log {

    file “log/dnssec” size 20m;   // a DNSSEC log channel 20m;

    print-time yes;                   // timestamp the entries

    print-category yes;          // add category name to entries

    print-severity yes;          // add severity level to entries

    severity debug 3;         // print debug message <= 3 t

    };

    };
    category dnssec { dnssec_log; };


##配置权威服务器##

###生成签名密钥对###

首先为你的区（zone）文件生成密钥签名密钥KSK：

    # cd /var/named

    # dnssec-keygen -f KSK -a RSASHA1 -b 512 -n ZONE test.net.

    Ktest.edu.+005+15480

然后生成区签名密钥ZSK：

    # dnssec-keygen -a RSASHA1 -b 512 -n ZONE test.net.

    Ktest.edu.+005+03674

参数 -a 是签名算法，-b是密钥长度。上述命令共产生
两对DNSKEY密钥（共四个文件），分别以.key和.private结尾，
表明这个文件存储的是公开密钥或私有密钥。

###签名###

签名之前，你需要把上面的两个DNSKEY写入到区文件中

    #cat “$INCLUDE Ktest.net.+005+15480.key” >> db.test.net

    # cat “$INCLUDE Ktest.net.+005+03674.key” >> db.test.net

然后执行签名操作：

    # dnssec-signzone -o test.net. db.test.net

    db.test.net.signed

上面的-o选项指定代签名区的名字。生成的db.test.net.signed

然后修改/etc/named.conf如下：

    options  {

    directory “/var/named”;

    dnssec-enable yes;

    };

    zone “test.net” {

    type master;

    file “db.test.net.signed”;

    };

每次修改区中的数据时，都要重新签名：

    # dnssec-signzone -o test.net -f db.test.net.signed.new db.test.net.signed

    # mv db.test.net.signed db.test.net.signed.bak

    # mv db.test.net.signed.new db.test.net.signed

    # rndc reload test.net

###发布公钥###

要让其他人验证我的数字签名，其他人必须有一个可靠的途径获得我
的公开密钥。DNSSEC通过上一级域名服务器数字签名的方式签发我的
公钥。

用dnssec-signzone时，会自动生成keyset-文件和dsset-开头的两个
文件，分别存储着KSK的DNSKEY记录和DS记录。作为test.net区的管
理员，需要把这两个文件发送给.net的管理员，.net的管理员需要
把这两条记录增加到.net区中，并且用.net的密钥重新签名。

    test.net.              86400   IN NS   ns.test.net.

    86400   DS      15480 5 1 (

    F340F3A05DB4D081B6D3D749F300636DCE3D

    6C17 )

    86400   RRSIG   DS 5 2 86400 20060219234934 (

    20060120234934 23912   net.

    Nw4xLOhtFoP0cE6ECIC8GgpJKtGWstzk0uH6

    ……

    YWInWvWx12IiPKfkVU3F0EbosBA= )

如果上一级域名服务器还没有配置DNSSEC，则不得不另找其他方式了
，比如，把上述两个文件提交到一些公开的trust anchor数据库中发布
(如上面介绍过的secspider)，或者直接交给愿意相信我的解析服务器的
管理员，配置到trust anchor文件中。