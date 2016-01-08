</br>这一次做的是通过ARP欺骗的方式进行MITM的实验。此次使用的是sslsplit工具。
</br>基本步骤如下：
</br>1.在git上下载源码：
</br>git clone https://github.com/droe/sslsplit.git   /opt/sslsplit
</br>apt-get install libssl-dev libevent-dev
</br>安装成功：![](https://raw.githubusercontent.com/vsmile0601/2Pictures/master/完整版一.bmp) 
</br>2.利用小学期所讲授的知识，使用openssl生成一份数字证书：
</br>openssl genrsa -out ca.key 2048
</br>openssl req -new -x509 -days 1096 -key ca.key -out ca.crt
</br>![](https://raw.githubusercontent.com/vsmile0601/2Pictures/master/完整版二.bmp)
</br>![](https://raw.githubusercontent.com/vsmile0601/2Pictures/master/完整版三.bmp)
</br>3.在进行端口转发之前，打开ip_forward功能：
</br>首先输入：iptables -F 清除原有设置
</br>echo 1 > /proc/sys/net/ipv4/ip_forward
</br>使用iptables进行流量转发：
</br>![](https://raw.githubusercontent.com/vsmile0601/2Pictures/master/打开ip_forward转发并且用sslstrip监听10000端口.bmp)
</br>查看当前设置：
</br>![](https://raw.githubusercontent.com/vsmile0601/2Pictures/master/完整版四.bmp)
</br>![](https://raw.githubusercontent.com/vsmile0601/2Pictures/master/完整版五.bmp)
</br>4.ARP欺骗：
</br>![](https://raw.githubusercontent.com/vsmile0601/2Pictures/master/完整版六.bmp)
</br>其中192.168.1.103为物理机IP，192.168.1.1为物理机和虚拟机的网关。本实验的目的是攻击物理机。
</br>（PS:其中，为了让物理主机与虚拟机的IP在同一网段，我们进行了如下修改：)
</br>![](https://raw.githubusercontent.com/vsmile0601/2Pictures/master/解决方法（arp%20spoof）.bmp)
</br>![](https://raw.githubusercontent.com/vsmile0601/2Pictures/master/重启network.bmp)
</br>5.启动SSLSplit：
</br>![](https://raw.githubusercontent.com/vsmile0601/2Pictures/master/完整版2.bmp)
