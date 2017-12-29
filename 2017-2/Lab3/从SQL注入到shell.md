# 从SQL注入到shell

## 实验环境 
### 下载IOS镜像并装入虚拟机，查看服务器IP：
![image](https://raw.githubusercontent.com/wq0712/ns/master/2017-2/Lab3/sql-IP.png)

### 攻击者主机IP：
![image](https://raw.githubusercontent.com/wq0712/ns/master/2017-2/Lab3/%E6%94%BB%E5%87%BB%E8%80%85%E4%B8%BB%E6%9C%BAIP.PNG)

### 攻击者主机浏览器设置代理：
![image](https://github.com/wq0712/ns/blob/master/2017-2/Lab3/%E8%AE%BE%E7%BD%AE%E4%BB%A3%E7%90%86.PNG?raw=true)


## 实验步骤
### 指纹
#### 使用burpsuite查看通信数据：http响应报头，可收集服务器的相关信息，如PHP版本。
![image](https://github.com/wq0712/ns/blob/master/2017-2/Lab3/%E6%8C%87%E7%BA%B9.png?raw=true)

### 检测并利用SQL注入
#### 基于整数的检测
##### 通过 http://10.0.2.15/cat.php?id=1 与  http://10.0.2.15/cat.php?id=2-1 返回的页面相同，说明数据库直接进行了减法，而没有对这种输入过滤， 因此存在SQL注入的可能性。
![image](https://github.com/wq0712/ns/blob/master/2017-2/Lab3/1.png?raw=true)
![image](https://github.com/wq0712/ns/blob/master/2017-2/Lab3/2-1.png?raw=true)

##### 使用union查询获取列数为4。
![image](https://github.com/wq0712/ns/blob/master/2017-2/Lab3/select1234.PNG?raw=true)

##### 通过@@version获得数据库版本信息。
![image](https://github.com/wq0712/ns/blob/master/2017-2/Lab3/version.PNG?raw=true)

##### 通过current_user()获得当前用户信息。
![image](https://github.com/wq0712/ns/blob/master/2017-2/Lab3/User.PNG?raw=true)

##### 通过database()获得数据库名。
![image](https://github.com/wq0712/ns/blob/master/2017-2/Lab3/database.PNG?raw=true)

##### 获取表名和列名对应关系。
![image](https://github.com/wq0712/ns/blob/master/2017-2/Lab3/tableColumn.PNG?raw=true)

##### 获取user表中的login和password字段。
![image](https://github.com/wq0712/ns/blob/master/2017-2/Lab3/password.PNG?raw=true)

##### 将得到的密码解密后登陆。
![image](https://github.com/wq0712/ns/blob/master/2017-2/Lab3/login.PNG?raw=true)

##### 上传文件。
![image](https://github.com/wq0712/ns/blob/master/2017-2/Lab3/%E4%B8%8A%E4%BC%A0%E6%96%87%E4%BB%B6.PNG?raw=true)
![image](https://github.com/wq0712/ns/blob/master/2017-2/Lab3/%E4%B8%8A%E4%BC%A0%E6%96%87%E4%BB%B62.PNG?raw=true)
