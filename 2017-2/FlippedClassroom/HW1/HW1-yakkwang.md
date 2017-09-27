**一、实验要求**

1.节点：靶机、网关、攻击者主机
2.连通性
- 靶机可以直接访问攻击者主机
- 攻击者主机无法直接访问靶机
- 网关可以直接访问攻击者主机和靶机
- 靶机的所有对外上下行流量必须经过网关
- 所有节点均可以访问互联网

**二、实验过程**

1.网关第一块网卡为NAT网络，eth0。第二块网卡为桥接网络，eth2。
![](http://upload-images.jianshu.io/upload_images/8107418-9c8755c143df67e8.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

靶机与攻击者主机均为一块网卡，为桥接网络。网关地址设置为上图网关主机的ip。
攻击者：
![](http://upload-images.jianshu.io/upload_images/8107418-21313f7ffa64d3d9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

靶机：
![](http://upload-images.jianshu.io/upload_images/8107418-438cffe4d3fb47aa.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

网关：192.168.1.17
靶机：192.168.1.18
攻击者：192.168.1.19  NAT为10.0.2.15

2.在靶机上设置防火墙，使攻击者无法访问靶机。
![](http://upload-images.jianshu.io/upload_images/8107418-a62dd5a167468114.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

靶机可以ping通攻击者。设置防火墙后，攻击者可以收到靶机的ping包，但无法发送回应包。
![](http://upload-images.jianshu.io/upload_images/8107418-271d97a08e4ec320.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

3.网关可以访问靶机和攻击者主机
![](http://upload-images.jianshu.io/upload_images/8107418-a4e05992afed7a5d.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![](http://upload-images.jianshu.io/upload_images/8107418-24d199d22afa3a65.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

4.靶机与攻击者主机均可访问互联网

靶机访问互联网
![](http://upload-images.jianshu.io/upload_images/8107418-e5946603a9b9ac2b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

攻击者主机访问互联网
![](http://upload-images.jianshu.io/upload_images/8107418-24a61cfe0299d8c2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

靶机流量经过网关
![](http://upload-images.jianshu.io/upload_images/8107418-039f9fb239d58330.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
