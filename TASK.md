# 题目说明

* 无序列表的第一级为研究主题，二级、三级等内容为补充解释说明文字；
* 凡是标有[ ]符号的均为可选题目，没有必选题目的说法，大家可以自行设计其他网络安全相关的研究主题并和我探讨论证之后作为自己小组课程作业的主题任务；
* 某些研究主题可能涉及多个不同类型的研究对象，不同对象的研究方法或实验技术存在较大差别，所以一个研究主题会被按照研究对象的不同拆分为多个可选题目；
  * 例如：反射型/放大器型DoS/DDoS攻击的原理与实验，可以分别由3个小组的同学分别独立完成DNS、ICMP和NTP三选其一的拒绝服务攻击原理研究与攻防实验；
* 遵守国家、地方及相关行业和主管部门的法律和规定，不窃密、不篡改、不破坏；
* 是否问题，需要给出包括但不限于：详细论据、实验关键步骤和结果截图；
* 尊重他人的劳动成果和知识产权，给出必要的参考文献引用标注、第三方库引用声明等；

# 选题说明

* 可以分组完成，也可以独立一人完成；
* 每个小组至少选择一个题目，也可以选择多个题目；
* 每人均需要使用自己独立的github帐号提交自己完成的工作成果，我将通过检查你的github仓库提交历史评估你的任务贡献度；
  * 每个小组，可以由1个人fork本项目，然后
    * （推荐协作方式，较简单）其他人通过加入到该fork项目的协作者来共享一个仓库管理本小组的作业；
    * 或者，每个人都继续fork组长的这个分支项目，由组长来合并其他组员的分支提交；
* 每个小组需要有专人通过电子邮件让我知晓你组github帐号和真人之间的对应关系和你组选题；
* 当选题冲突时，遵循以下2个原则：
  * 先来先得。后来者是否可以继续做这个题目决定权在我；
  * 后来者要适当增加工作量。即，如果后来者坚持要继续做同一个选题，则需要适当增加题目深度或增加一个新的选题；

# 网络安全

## 安全方案设计

* [ ] 设计并实现一套双因素认证系统（默认已实现支持 用户名+密码 方式的身份认证）
  * 基于来源IP地址
  * 登录时发送二次确认电子邮件
    * 案例：linode的登录方式，需要把未知登录IP加入登录白名单
  * captcha机制
    * 基于浏览器JS执行
    * 基于图片验证码
  * OTP（智能手机APP方式）
  * 生物特征（可选）
    * 指纹、虹膜、声纹
* [ ] 设计并验证内网检测与防御ARP攻击系统
  * 基于可网管交换机
    * 支持端口流量镜像
  * 使用独立审计服务器，审计内网流量

## 逆向分析/点评

* [ ] 点评智能手机的指纹验证解锁
  * 对于原简单密码方式解锁的改进之处
  * 对于原简单密码方式解锁的存在的问题
  * 针对不同智能手机的指纹验证解锁机制的攻击方法、案例


* [ ] iptables规则题
  * 给定一个[iptables规则集合](http://sec.cuc.edu.cn/huangwei/textbook/ns/dist/chap0x08/exp.html)，让学生说明该规则可以实现网络访问控制规则应用效果
    * 给定一个数据包，让学生判断数据包最终是被：转发、丢弃、DENY、LOG、拒绝？

* [ ] 非图形验证码类CAPTCHA验证方式的原理和安全性分析？
  * geetest（极验）
  * 语音
  * 接收短信验证码
  * 编辑指定短信内容发送到指定号码
  * 电话回拨

* [ ] 网页屏幕键盘的原理和安全性分析？
  * 分析对象至少应包含以下2家：
    * 中传的一卡通在线充值转账系统
    * 建设银行个人网银登录
  * 对比直接使用物理键盘方式输入密码，屏幕键盘是否改进了安全性？请详细阐述理由。


## 研发与实验

* [ ] 设计并实现一套安全新闻、文章的聚合系统
  * 采用互联网爬虫技术
  * 具备数据挖掘能力，对相似主题文章进行分类
  * 对相同文章，展示原始出处文章，其他引用文章进行关联默认不展示
* 反射型/放大器型DoS/DDoS攻击的原理与实验
  * 常见的可用于反射型DoS/DDoS攻击的协议有哪些？
    * [ ] DNS
    * [ ] ICMP
    * [ ] NTP
  * 如何防御？
* [ ] 基于HTTP协议的DoS/DDoS攻击的原理与实验
  * 如何防御？
* [ ] 你家的智能设备有哪些？
  * 典型被分析对象如下：
    * 路由器
    * 智能电视
    * 电视盒子
    * IP摄像头
    * 红外传感报警器
  * 使用的通信协议？
  * 通信内容是否加密？
  * 是否可以抵御重放攻击？
  * 端口开放情况如何？  
* [ ] HTTPS协议中间人攻击的可能性探究与实验
  * DNS查询泄漏（经由DNS解析服务器）与MITM
  * ARP欺骗与MITM
  * 伪造证书
  * 合法证书签名
  * [WPAD中间人劫持](http://www.netresec.com/?page=Blog&month=2012-07&post=WPAD-Man-in-the-Middle)
* [ ] DNSSec协议详解，搭建支持DNSSec协议的DNS服务器，并详细说明协议的安全机理
* [ ] 搭建一个支持域名递归解析的DNS服务器，从全球13个根域名解析服务器同步所有TLD域名记录
* [ ] 反垃圾邮件检测服务搭建
  * 伪造发信人地址的可行性实践
  * 绕过垃圾邮件检测实践
  * 改进反垃圾邮件检测策略，检测出上一步的绕过手段
  * 改进垃圾邮件构造方法，绕过上一步的检测手段
* [ ] 开放网络服务信息收集实验
  * alexa全球排名top 10000的站点选择其一
  * 禁止使用任何方式直接扫描目标站点
  * 禁止对目标站点进行任何形式的渗透测试或攻击行为
  * 信息收集手段包括但不限于：搜索引擎搜索、whois查询、域名枚举、使用合法客户端连接目标端口等
  * 信息收集内容包括但不限于：子域名及其对应服务说明、IP地址段、电子邮件、组织结构信息、联系方式信息、公开的漏洞信息等
* [ ] 基于开源系统，搭建类ZoomeEye、shodan服务
* 为知名扫描器开发一款原创漏洞扫描或利用插件
  * [ ] bugscan
  * [ ] metasploit 
  * [ ] nmap
  * [ ] burpsuite
* [ ] 使用数据可视化技术在世界地图上呈现一次域名解析的完整递归过程
  * 通过网页技术实现，可以直接在网页上输入域名后完成整个可视化交互过程
  * 每一次查询获得的DNS响应结果对应的IP地址通过IP归属地查询后在地图上高亮出来
  * 用连线方式绘制表示请求的发送和接收过程涉及到的2个实际IP之间的通信过程

## 调研报告
* [ ] GMail将邮件中的所有图片、附件存储在自己的服务器上，有何安全意义？
* [ ] 公有云服务平台安全的过去、现在和将来
  * 列举并介绍全球（特别是中国）每年有影响力的安全事件
* [ ] IANA与互联网？
  * 域名管理机制
  * IP地址管理机制
  * 协议管理机制
  * 中文域名如何注册和解析？
* [ ] https站点如何启用CDN服务？
  * 是否一定要上传源站点的SSL证书私钥到CDN服务提供商？
    * 如果不是，请详细阐述解决方案及其原理。
      * ref: http://www.ruanyifeng.com/blog/2014/09/illustration-ssl.html
* [ ] ZoomeEye、shodan类互联网安全垂直搜索引擎使用深度研究

## 文献阅读与翻译

### 网络扫描

* [ZMap: Fast Internet-wide Scanning and Its Security Applications](papers/ZMap- Fast Internet-wide Scanning and Its Security Applications.pdf)
* [Network Forensics: Detection and Analysis of Stealth Port Scanning Attack](papers/Network Forensics- Detection and Analysis of Stealth Port Scanning Attack.pdf)

### DoS/DDoS

* [A SURVEY OF TRENDS IN MASSIVE DDOS ATTACKS AND CLOUD-BASED MITIGATIONS](papers/A SURVEY OF TRENDS IN MASSIVE DDOS ATTACKS AND CLOUD-BASED MITIGATIONS.pdf)
* [The Rise and Decline of NTP DDoS](papers/The Rise and Decline of NTP DDoS.pdf)

### Web安全

* [ADAPTIVE USER INTERFACE RANDOMIZATION AS AN ANTI-CLICKJACKING STRATEGY](papers/ADAPTIVE USER INTERFACE RANDOMIZATION AS AN ANTI-CLICKJACKING STRATEGY.pdf)
* [Cross-Site Request Forgeries: Exploitation and Prevention](papers/Cross-Site Request Forgeries- Exploitation and Prevention.pdf)
* [The Tangled Web of Password Reuse](papers/The Tangled Web of Password Reuse.pdf)
* [CSRF: Attack and Defense](papers/wp-csrf-attack-defense.pdf)

### DNS

* [Security Issues with DNS](papers/Security Issues with DNS.pdf)

### 匿名通信

* [Tor vs NSA](papers/Tor vs NSA.pdf)

### 数据分析/入侵取证/入侵检测

* [Beehive: Large-Scale Log Analysis for Detecting Suspicious Activity in Enterprise Networks](papers/Beehive - Large-Scale Log Analysis for Detecting Suspicious Activity in Enterprise Networks.pdf)

