# **基于开源系统、搭建类Zoomeye、shodan服务**  
  
## **一、名词解释**
#### Zoomeye  
[Zoomeye](https://www.zoomeye.org)（钟馗之眼)是知道创宇推出的一款网络空间搜索引擎,可以搜索网络组建和网络设备,是国产的'shodan'。     
这种以各大组件指纹作为识别基础的数据平台，更多的是为了使得安全研究人员更好地评估漏洞的影响范围与其中隐含的数据模式。  
Zoomeye的后端架构图：  
![](image/17.jpg)  
对于一次漏洞的评估，启动调度框架分配域名或者IP列表给扫描节点，节点完成任务后执行回调  

#### IVRE  
[IVRE](https://ivre.rocks)(又名DRUNK)是一款基于python的网络侦查框架，包括两个基于p0f和Bro的被动侦查模块和一个基于Nmap&Zmap的主动侦查模块。采用Docker和Vagrant可以方便快速的搭建和管理维护。  
#### Docker  
[Docker](http://www.docker.com):一个开源的应用容器引擎，让开发者可以打包他们的应用以及依赖包到一个可移植的容器中，然后发布到任何流行的 Linux 机器上，也可以实现虚拟化。容器是完全使用沙箱机制，相互之间不会有任何接口（类似 iPhone 的 app）。几乎没有性能开销,可以很容易地在机器和数据中心中运行。最重要的是,他们不依赖于任何语言、框架包括系统。   
#### Vagrant 
Vagrant是一个基于Ruby的工具，用于创建和部署虚拟化开发环境。它 使用Oracle的开源VirtualBox虚拟化系统，使用 Chef创建自动化虚拟环境。  
**功能：**  
1. 统一开发环境。一次配置打包，统一分发给团队成员，统一团队开发环境，解决诸如“编码问题”，“缺少模块”，“配置文件不同”带来的问题；  
2. 避免重复搭建开发环境。新员工加入，不用浪费时间搭建开发环境，快速加入开发，减少时间成本的浪费；  
3. 多个相互隔离开发环境。可以在不用box里跑不同的语言，或者编译安装同一语言不同版本，搭建多个相互隔离的开发环境，卸载清除时也很快捷轻松。   

## **二、搭建过程**

### 运行环境  
virtualbox   ubuntu-16.04-LTS-desktop-64bits     
Docker  
IVRE 
### 安装docker  
更新列表
> sudo apt-get update 
 
使用curl命令进行安装  
> sudo curl -sSL https://get.docker.com/ | sh  

检查是否安装成功   
> sudo docker run hello-world  

如果出现"cannot connect to the docker daemon. is the docker daemon running on this host",大部分原因可能是因为权限问题注意sudo   
安装成功：  
![](image/6.jpg)  

### 安装Vagrant  
> sudo apt-get install -y vagrant  

使用 vagrant -v 查看版本，版本要求大于1.4（好像是）以上才能使用,否则后续安装会提示会找不到docker。  
     
### 安装IVRE
创建相关文件并安装ivre  
> mkdir -m 1777 var_{lib,log}_{mongodb,neo4j} ivre-share  
> wget -q https://ivre.rocks/Vagrantfile   
> sudo vagrant up --no-parallel  
  
![](image/8.jpg) 
> docker attach ivreclient   
  
![](image/7.jpg)  
  
此时IVRE已经安装成功  
通过Docker装好的IVRE是没有数据的  
在浏览器中访问localhost可以查看IVRE的WebUI。        
![](image/9.jpg)  
  
### IVRE运行和停止  
查看docker有那些容器  
> sudo docker ps –a  
  
开启IVRE分三步  
1. 要开启database serve  
> sudo docker start ivredb  

2. 开启web  
> sudo docker start ivreweb  

3. 开启客户端  
> sudo docker start ivreclient  

### IVRE扫描并导入数据     

通过attach命令进入ivreclient  
> sudo docker attach ivreclient  
> root@881486651a32:/$ ivre  ipdata --download

对互联网上10个随机主机进行标准扫描，开启13个nmap进程   
> root@881486651a32:/$ ivre runscans --routable --limit 10 --output=XMLFork    
 
![](image/19.jpg)   

![](image/20.jpg)    

![](image/21.jpg) 
 

#### runscans命令的用法:  
**select output method for scan results :**  
 --output {XML,XMLFull,XMLFork,Test,Count,List,ListAll,ListAllRand,ListCIDRs,CommandLine}
**number of addresses to output :**  
 --limit LIMIT, -l LIMIT                    
**select a country :**	  
--country CODE, -c CODE  
**select a region :**	   
--region COUNTRY_CODE REGION_CODE  

扫描结果入库  
> root@881486651a32:/$ ivre nmap2db -c ROUTABLE-CAMPAIGN-001 -s MySource -r scans/ROUTABLE/up  

在浏览器中查看扫描结果：  
![](image/13.jpg)   
打开其中一项扫描结果：  
 ![](image/16.jpg)   
上述结果（Host scripts,Traceroute等信息）在扫描时的终端界面上都出现过    



### 搜索项细节分析  
主要包括以下数据元：  
（1）域名 or  IP  or title  
（2）组件信息（Win32）OpenSSL  
（3）国家、城市信息  
（4）信息更新时间  
（5）Http Response header    
**以下面的扫描结果为例，其中包含的信息有：**  

 ![](image/14.jpg)    
SSH 为建立在应用层基础上的安全协议  
  
 ![](image/22.jpg)   
 ![](image/23.jpg)   
 ![](image/24.jpg)   
 ![](image/25.jpg)   
 ![](image/26.jpg)   
 ![](image/27.jpg)   
 **traceroute(路由跟踪):**  
 由遍布全球的几万局域网和数百万台计算机组成，并通过用于异构网络的TCP/IP协议进行网间通信。互联网中，信息的传送是通过网中许多段的传输介质和设备（路由器，交换机，服务器，网关等等）从一端到达另一端。每一个连接在Internet上的设备，如主机、路由器、接入服务器等一般情况下都会有一个独立的IP地址。通过Traceroute我们可以知道信息从你的计算机到互联网另一端的主机是走的什么路径。  

 **OS Detection:**  
 Nmap最着名的功能之一是使用TCP / IP堆栈指纹识别的远程操作系统检测。    
 ![](image/28.jpg)     

 **Common Platform Enumeration (CPE)** is a standardized method of describing and identifying classes of applications, operating systems, and hardware devices present among an enterprise's computing assets. CPE是一个描述和刻画应用程序、操作系统和硬件设备等企业计算资产主要组成分类类别的标准化方法。

 ![](image/29.jpg)   

### IVRE数据统计功能    
通过左侧的过滤器功能，可以在数据库中按条件筛选信息  

![](image/18.jpg)    

左侧栏有数据统计选项：  
![](image/30.jpg)   
对现有的数据进行统计：  
![](image/31.jpg)     
The Address space button displays a graphical representation of the filtered addresses. The abscissa axis represents the two high bytes (or the three when the results belong to the same /16 network), and the ordinate axis represents the two low bytes (or the low byte).  
显示已过滤IP地址的图形表示。横坐标轴表示两个高位字节，纵坐标轴表示两个低位字节  
![](image/32.jpg)  
统计端口状态，横坐标表示IP地址的前两位，纵坐标表示tcp的端口号，黄色表示扫描到的被过滤掉的端口，绿色的表示开放状态的端口  
![](image/33.jpg)    
The Map button displays the locations of the results on a world map.   
“地图”按钮在世界地图上显示扫描结果的位置  
![](image/34.jpg)     
The Timeline and Timeline 24h buttons display time-lines where the abscissa axis represents the time and the ordinate axis represents the IP addresses.  
时间轴和24h时间轴中横坐标轴表示时间，纵坐标轴表示IP地址前两位  
![](image/35.jpg)   

    
##  三、参考资料  
 * [IVRE官方网站](https://ivre.rocks/)  
 * [IVRE官方文档](https://github.com/cea-sec/ivre/tree/master/doc)  
 * [通过Docker搭建开源版IVRE](http://www.freebuf.com/sectool/92179.html)  
 * [开源版ZoomEye：基于Python的网络侦查框架 – IVRE](http://www.freebuf.com/sectool/74083.html)
 * [如何自己构建一个小型的Zoomeye----从技术细节探讨到实现](http://blog.csdn.net/u011721501/article/details/41967847)




## 四、实验过程中出现的问题
1. ** 使用apt-get进行软件的install或update时，有时会出现以下提示信息：**    
E: Could not get lock /var/lib/dpkg/lock - open (11 Resource temporarily unavailable)  
E: Unable to lock the administration directory (/var/lib/dpkg/), is another process using it?  
![](image/1.jpg)  
原因是有可能有其他的apt-get进程在活动。  
**解决办法:**  
把apt-get进程找出来，杀死  
    ps aux | grep apt-get  
    sudo kill -9 <PID>  
如果再次执行apt-get，还是有这样情况出现，删除/var/lib/dpkg/lock文件，即可。  
	sudo rm /var/cache/apt/archives/lock  
	sudo rm /var/lib/dpkg/lock   

2.  **docker安装后出现Cannot connect to the Docker daemon.**  
![](image/2.jpg)   
查看了docker的状态，发现是运行的  
![](image/3.jpg)    
发现是没有添加sudo的原因  
![](image/4.jpg)  
    
3. **查看docker有那些容器时，无法连接docker daemon**     
![](image/10.jpg)    
**解决办法:**  
首先要查看docker daemon是否在运行    
ps aux | grep docker      
  ![](image/11.jpg)  
这样看来，docker deamon正在运行，但是报此错误实属不应该。那么将其停止，再启动  
 service docker stop  
 service docker start   
  还是失败了，考虑权限问题，切换到root
 sudo docker ps -a  
  ![](image/12.jpg)  
发现是权限问题

4.  **通过attach命令进入ivreclient时直接在root@eb73787b6d32:/# 后面输入指令会提示无法识别指令**   
  ![](image/15.jpg)   
**解决办法:**    
在每条命令语句前添加ivre即可  

