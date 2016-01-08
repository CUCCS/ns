DNS欺骗  

首先找到etter.dns文件，然后在最后添加欺骗内容，使访问baidu.com转到自己IP
![image](https://github.com/henopu89iu/henopu89iu/raw/master/1tobaidu.jpeg)  
使用ettercap中的DNS插件进行dns欺骗。然后使用特定的接口执行欺骗。找到整个子网存活的主机，确定目标用户，这里直接让所有存活的主机成为目标用户，同时自己也成为了目标用户。图中命令有问题，正确的截图丢失，应该是ettercap -T -q -i eth0 -P dns_spoof -M arp ////
![image](https://github.com/henopu89iu/henopu89iu/raw/master/1pettercap.jpeg) 
![image](https://github.com/henopu89iu/henopu89iu/raw/master/1pettercaped.jpeg)  
访问baidu的时候也就可以重定向到自己的IP了。  
![image](https://github.com/henopu89iu/henopu89iu/raw/master/1baidu.jpeg)  
![image](https://github.com/henopu89iu/henopu89iu/raw/master/1dns_spoof.jpeg)  
还可以使用渗透工具metasploit用ettercap进行dns欺骗。    
同样需要配置etter.dns，确定重定向的IP。  
![image](https://github.com/henopu89iu/henopu89iu/raw/master/1msfconsole.jpeg)   
![image](https://github.com/henopu89iu/henopu89iu/raw/master/1usemsf.jpeg)     
