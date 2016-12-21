# 基于开源系统、搭建类Zoomeye、shodan服务  
----  
### Zoomeye  
[Zoomeye](https://www.zoomeye.org)（钟馗之眼)是知道创宇推出的一款网络空间搜索引擎,可以搜索网络组建和网络设备,是国产的'shodan'。   
### IVRE  
[IVRE](https://ivre.rocks)(又名DRUNK)是一款基于python的网络侦查框架，包括两个基于p0f和Bro的被动侦查模块和一个基于Nmap&Zmap的主动侦查模块。采用Docker和Vagrant可以方便快速的搭建和管理维护。  
### Docker  
[Docker](http://www.docker.com):一个开源的应用容器引擎，让开发者可以打包他们的应用以及依赖包到一个可移植的容器中，然后发布到任何流行的 Linux 机器上，也可以实现虚拟化。容器是完全使用沙箱机制，相互之间不会有任何接口（类似 iPhone 的 app）。几乎没有性能开销,可以很容易地在机器和数据中心中运行。最重要的是,他们不依赖于任何语言、框架包括系统。   
### Vagrant 
TODO  
## 搭建过程

### 环境  
  virtualbox
  ubuntu-16.04-LTS-desktop-64bits  
1.安装docker  
更新列表
> sudo apt-get update 
 
使用curl命令进行安装  
> sudo curl -sSL https://get.docker.com/ | sh  

检查是否安装成功   
> sudo docker run hello-world  

如果出现"cannot connect to the docker daemon. is the docker daemon running on this host",大部分原因可能是因为权限问题注意sudo 
   
安装Vagrant  
> sudo apt-get install -y vagrant  

使用 vagrant -v 查看版本，版本要求大于1.4（好像是）以上才能使用,否则后续安装会提示会找不到docker。  
   
创建相关文件并安装ivre  
> mkdir -m 1777 var_{lib,log}_{mongodb,neo4j} ivre-share
> wget -q https://ivre.rocks/Vagrantfile
> sudo vagrant up --no-parallel (一定要有sudo!)  

会出现如下的输出:
> Bringing machine 'ivredb' up with 'docker' provider...
> Bringing machine 'ivreweb' up with 'docker' provider...
> Bringing machine 'ivreclient' up with  'docker'provider...
> [...]
  
 在浏览器中访问localhost可以查看IVRE的WebUI。  

TODO：其余功能的补充和使用
