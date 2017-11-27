#从SQL注入到Shell

----------

###实验准备：
1. 下载镜像安装虚拟机
![](https://github.com/ghan3/ns/blob/autumnSheepYJ/2017-2/GhYj/YjHW/SQL%E6%B3%A8%E5%85%A5/1.png?raw=true) 

2. 由于在虚拟机中浏览器反应过于迟缓，所以和Webgoat环境配置一样，可以配置虚拟机转发规则，并在宿主机浏览器设置代理服务器，以便在宿主机浏览器完成后续的实验
![](https://github.com/ghan3/ns/blob/autumnSheepYJ/2017-2/GhYj/YjHW/SQL%E6%B3%A8%E5%85%A5/2.png?raw=true) 
![](https://github.com/ghan3/ns/blob/autumnSheepYJ/2017-2/GhYj/YjHW/SQL%E6%B3%A8%E5%85%A5/3.png?raw=true) 


3. 测试宿主机是否能正确访问服务器
![](https://github.com/ghan3/ns/blob/autumnSheepYJ/2017-2/GhYj/YjHW/SQL%E6%B3%A8%E5%85%A5/4.png?raw=true) 


###实验过程：

1. 指纹提取：在响应头中收集到关于服务器的信息
![](https://github.com/ghan3/ns/blob/autumnSheepYJ/2017-2/GhYj/YjHW/SQL%E6%B3%A8%E5%85%A5/5.png?raw=true) 

2. SQL注入的检测和利用
  - 整数检测：id=1和id=2-1返回相同，说明直接做了2-1数据库按照id=1的操作。
![](https://github.com/ghan3/ns/blob/autumnSheepYJ/2017-2/GhYj/YjHW/SQL%E6%B3%A8%E5%85%A5/6.png?raw=true) 
![](https://github.com/ghan3/ns/blob/autumnSheepYJ/2017-2/GhYj/YjHW/SQL%E6%B3%A8%E5%85%A5/7.png?raw=true) 
    

  - 字符串检测：（1）用’测试 （2）--注释后续语句 （3）and '1'='1和and '1'='0（改变查询语句的语义）
![](https://github.com/ghan3/ns/blob/autumnSheepYJ/2017-2/GhYj/YjHW/SQL%E6%B3%A8%E5%85%A5/8.png?raw=true)
![](https://github.com/ghan3/ns/blob/autumnSheepYJ/2017-2/GhYj/YjHW/SQL%E6%B3%A8%E5%85%A5/9.png?raw=true)  


  - union关键字检测：（1）递增查询列数看数据库能查询多少列，列数为4时，返回正确 （2）order by,数据为5时，就返回错误信息
![](https://github.com/ghan3/ns/blob/autumnSheepYJ/2017-2/GhYj/YjHW/SQL%E6%B3%A8%E5%85%A5/10.png?raw=true) 
![](https://github.com/ghan3/ns/blob/autumnSheepYJ/2017-2/GhYj/YjHW/SQL%E6%B3%A8%E5%85%A5/11.png?raw=true) 
![](https://github.com/ghan3/ns/blob/autumnSheepYJ/2017-2/GhYj/YjHW/SQL%E6%B3%A8%E5%85%A5/12.png?raw=true) 
  
 
  - 利用SQL：（1）利用上述已经得到的信息，通过@@version，current_user()和database()获得数据库版本信息，用户信息和数据库的名字  （2）利用其他命令还可获取其他信息，可以发现users表中有login和password字段并查询，获得password哈希值，在线解密为P4ssw0rd
![](https://github.com/ghan3/ns/blob/autumnSheepYJ/2017-2/GhYj/YjHW/SQL%E6%B3%A8%E5%85%A5/13.png?raw=true) 
![](https://github.com/ghan3/ns/blob/autumnSheepYJ/2017-2/GhYj/YjHW/SQL%E6%B3%A8%E5%85%A5/14.png?raw=true) 
![](https://github.com/ghan3/ns/blob/autumnSheepYJ/2017-2/GhYj/YjHW/SQL%E6%B3%A8%E5%85%A5/15.png?raw=true) 
![](https://github.com/ghan3/ns/blob/autumnSheepYJ/2017-2/GhYj/YjHW/SQL%E6%B3%A8%E5%85%A5/16.png?raw=true) 
![](https://github.com/ghan3/ns/blob/autumnSheepYJ/2017-2/GhYj/YjHW/SQL%E6%B3%A8%E5%85%A5/17.png?raw=true) 
![](https://github.com/ghan3/ns/blob/autumnSheepYJ/2017-2/GhYj/YjHW/SQL%E6%B3%A8%E5%85%A5/18.png?raw=true) 
 

3. 访问用户页面和代码的执行
   - 登录账户
![](https://github.com/ghan3/ns/blob/autumnSheepYJ/2017-2/GhYj/YjHW/SQL%E6%B3%A8%E5%85%A5/19.png?raw=true)

   - 上传php文件，提示错误，可利用.php3和.php.test绕过php过滤
![](https://github.com/ghan3/ns/blob/autumnSheepYJ/2017-2/GhYj/YjHW/SQL%E6%B3%A8%E5%85%A5/20.png?raw=true)
![](https://github.com/ghan3/ns/blob/autumnSheepYJ/2017-2/GhYj/YjHW/SQL%E6%B3%A8%E5%85%A5/21.png?raw=true)
![](https://github.com/ghan3/ns/blob/autumnSheepYJ/2017-2/GhYj/YjHW/SQL%E6%B3%A8%E5%85%A5/22.png?raw=true)
![](https://github.com/ghan3/ns/blob/autumnSheepYJ/2017-2/GhYj/YjHW/SQL%E6%B3%A8%E5%85%A5/23.png?raw=true)
![](https://github.com/ghan3/ns/blob/autumnSheepYJ/2017-2/GhYj/YjHW/SQL%E6%B3%A8%E5%85%A5/24.png?raw=true)


   - 通过cmd，获取服务器大量信息，并执行代码：（1）ls得到当前目录或上级目录信息 （2）cat /etc/passwd得到系统用户列表 
![](https://github.com/ghan3/ns/blob/autumnSheepYJ/2017-2/GhYj/YjHW/SQL%E6%B3%A8%E5%85%A5/26.png?raw=true)
![](https://github.com/ghan3/ns/blob/autumnSheepYJ/2017-2/GhYj/YjHW/SQL%E6%B3%A8%E5%85%A5/25.png?raw=true)



###参考链接：
[https://pentesterlab.com/exercises/from_sqli_to_shell](https://pentesterlab.com/exercises/from_sqli_to_shell "From SQL Injection to Shell")