1.如果使用相同的镜像文件，则需修改uuid
  
   进入virtualbox的安装目录（以D：\Oracle\VirtualBox 为例）
    
    d:

    cd  .\Oracle\VirtualBox
    
    VBoxManage internalcommands sethduuid “F:\Linux_attacker\ Linux_attacker.vdi”

（””内为镜像所在的文件路径）

2.设置Nat网络的相关参数：
    VBoxManage natnetwork add --netname NatNetwork1 --network "10.0.3.0/24" --enable

3.修改XP_ SP3_host1的IP地址、子网掩码、网关
   
    netsh interface ip set address name="本地连接" source=static addr=10.0.3.3 mask=255.255.255.0 gateway=10.0.3.1 1

    netsh interface ip set dns "本地连接" source=static addr=8.8.8.8  
4.修改XP_ SP3_host1的IP地址、子网掩码、网关
   
    netsh interface ip set address name="本地连接" source=static addr=10.0.3.4 mask=255.255.255.0 gateway=10.0.3.1 1

    netsh interface ip set dns "本地连接" source=static addr=8.8.8.8  
5.修改Linux_attacker的IP地址、子网掩码、网关

    vi /etc/network/interfaces
  将其中的eth0网卡设置为static模式  
  
    auto eth0
    iface eth0 inet static 
  写上IP地址及网关，子网掩码
  
    address 10.0.3.5 
    netmask 255.255.255.0 
    gateway 10.0.3.1
  重启网卡或者重启计算机
  
    /etc/init.d/networking restart
