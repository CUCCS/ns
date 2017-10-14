# 网络安全实验报告 #
## 基于VirtualBox的攻防环境搭建 ##
![](https://raw.githubusercontent.com/Geraens/ns/42cca8babe13db13ed0912a39bf0248acdb6452c/2017-2/Geraens/%E5%9B%BE%E7%89%87/image1.png)
### 网关机的环境 ###
![](https://raw.githubusercontent.com/Geraens/ns/42cca8babe13db13ed0912a39bf0248acdb6452c/2017-2/Geraens/%E5%9B%BE%E7%89%87/image2.png)


### 靶机的环境 ###
![](https://raw.githubusercontent.com/Geraens/ns/42cca8babe13db13ed0912a39bf0248acdb6452c/2017-2/Geraens/%E5%9B%BE%E7%89%87/image3.png)

### 攻击机的环境 ###
![](https://raw.githubusercontent.com/Geraens/ns/42cca8babe13db13ed0912a39bf0248acdb6452c/2017-2/Geraens/%E5%9B%BE%E7%89%87/image4.png)

### 靶机可以直接访问攻击者主机 ###
![](https://raw.githubusercontent.com/Geraens/ns/42cca8babe13db13ed0912a39bf0248acdb6452c/2017-2/Geraens/%E5%9B%BE%E7%89%87/image5.png)

### 攻击者主机无法直接访问靶机 ###
![](https://raw.githubusercontent.com/Geraens/ns/b62556faa0b4756977f9132c526707fd151ddeca/2017-2/Geraens/%E5%9B%BE%E7%89%87/image13.png)
### 网关可以直接访问攻击者主机和靶机 ###
#### 网关机ping通攻击机 ####
![](https://raw.githubusercontent.com/Geraens/ns/42cca8babe13db13ed0912a39bf0248acdb6452c/2017-2/Geraens/%E5%9B%BE%E7%89%87/image7.png)
#### 网关机ping通靶机 ####
![](https://raw.githubusercontent.com/Geraens/ns/42cca8babe13db13ed0912a39bf0248acdb6452c/2017-2/Geraens/%E5%9B%BE%E7%89%87/image6.png)
### 靶机的所有对外上下行流量必须经过网关 ###
#### 图为网关机抓取靶机的上网的包 ####
![](https://raw.githubusercontent.com/Geraens/ns/master/2017-2/Geraens/%E5%9B%BE%E7%89%87/image8.png)
 
### 所有节点均可以访问互联网 ###
#### 图为三个节点机器访问百度，即可以访问互联网 ####
![](https://raw.githubusercontent.com/Geraens/ns/master/2017-2/Geraens/%E5%9B%BE%E7%89%87/image10.png)
![](https://raw.githubusercontent.com/Geraens/ns/master/2017-2/Geraens/%E5%9B%BE%E7%89%87/image11.png)
![](https://raw.githubusercontent.com/Geraens/ns/master/2017-2/Geraens/%E5%9B%BE%E7%89%87/image12.png)



