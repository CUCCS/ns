# 第三次实验报告

## SQL注入

### 准备工作
下载镜像，配置网络，但遇到了问题导致无法配置NAT网络，后查找资料并没有得到解决 尝试使用了网络地址转换 但无法改变ip地址 通过学习他人的经验 了解到可以通过宿主机直接访问来避免这个问题

![image](https://github.com/BurnyMcDull/image/raw/master/hw3/1.png)

![image](https://github.com/BurnyMcDull/image/raw/master/hw3/2.png)

通过改变端口转发规则以及改变宿主机的代理规则

![image](https://github.com/BurnyMcDull/image/raw/master/hw3/3.png)

![image](https://github.com/BurnyMcDull/image/raw/master/hw3/4.png)

实现在宿主机直接进行访问
![image](https://github.com/BurnyMcDull/image/raw/master/hw3/5.png)

分析发送的请求 获得服务器的信息
![image](https://github.com/BurnyMcDull/image/raw/master/hw3/6.png)

### 检查sql漏洞

整数检测

![image](https://github.com/BurnyMcDull/image/raw/master/hw3/7.png)

![image](https://github.com/BurnyMcDull/image/raw/master/hw3/8.png)

存在sql的漏洞

通过尝试得知select语句含有四列

![image](https://github.com/BurnyMcDull/image/raw/master/hw3/9.png)

通过注入获得信息

![image](https://github.com/BurnyMcDull/image/raw/master/hw3/10.png)

![image](https://github.com/BurnyMcDull/image/raw/master/hw3/11.png)

http://127.0.0.1:8080/cat.php?id=3 union select 1,table_name,3,4 from information_schema.tables

![image](https://github.com/BurnyMcDull/image/raw/master/hw3/12.png)

在通过查询找到users表里有账号与密码

http://127.0.0.1:8080/cat.php?id=3 union select 1,concat(login,':’27,password),3,4 from users

![image](https://github.com/BurnyMcDull/image/raw/master/hw3/13.png)

获得管理员的密码

在线解密得到P4ssw0rd

![image](https://github.com/BurnyMcDull/image/raw/master/hw3/14.png)

![image](https://github.com/BurnyMcDull/image/raw/master/hw3/15.png)

上传php文件

![image](https://github.com/BurnyMcDull/image/raw/master/hw3/16.png)

分析页面

![image](https://github.com/BurnyMcDull/image/raw/master/hw3/17.png)

访问地址获得返回值

运行成功

![image](https://github.com/BurnyMcDull/image/raw/master/hw3/18.png)



