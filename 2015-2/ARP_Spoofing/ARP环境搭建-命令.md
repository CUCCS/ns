1.如果使用相同的镜像文件，则需修改uuid
    进入virtualbox的安装目录（以D：\Oracle\VirtualBox 为例）



    d:

    cd  .\Oracle\VirtualBox
    
    VBoxManage internalcommands sethduuid “F:\Linux_attacker\ Linux_attacker.vdi”

（””内为镜像所在的文件路径）

2.设置intnet的相关参数：

    VBoxManage dhcpserver modify --netname intnet --ip 192.168.64.9 --netmask 255.255.255.0 --lowerip 192.168.64.1 --upperip 192.168.64.10 –enable 
3.修改Linux_gateway的IP地址、子网掩码、网关
   
    netsh interface ip set address name="本地连接" source=static addr=192.168.64.1 mask=255.255.255.0 gateway=192.168.64.10 1

    netsh interface ip set dns "本地连接" source=static addr=8.8.8.8  
4.修改Linux_attacker的IP地址、子网掩码、网关

    vi /etc/network/interfaces
  将其中的eth0网卡设置为static模式  
  
    auto eth0
    iface eth0 inet static 
  写上IP地址及网关，子网掩码
  
    address 192.168.64.2 
    netmask 255.255.255.0 
    gateway 192.168.64.10
  重启网卡或者重启计算机
  
    /etc/init.d/networking restart
5.修改windows XP的IP地址、子网掩码、网关
  
    vi /etc/network/interfaces
  将其中的eth0网卡设置为static模式
 
    auto eth0
    iface eth0 inet static
  写上IP地址及网关，子网掩码

    address 192.168.64.10
    netmask 255.255.255.0
    gateway 192.168.64.255
  将其中的eth1网卡设置为dhcp模式
    
    auto eth1
    iface eth1 inet dhcp
  重启网卡或者重启计算机

    /etc/init.d/networking restart


