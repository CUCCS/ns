# Captcha
Completely Automated Public Test to tell Computers and Humans Apart

* 专业点儿的翻译是：全自动区分计算机和人类的图灵测试。
  * 其实图灵测试是由人来操控，而captcha是由计算机，所以是一种逆向测试
* 朴实点解释就是人机验证，验证码校验

CAPTCHA的目的很明确，就是区分计算机和人类的一种程序算法，并且这种程序必须能生成并评价人类能很容易通过但计算机却通不过的测试。

### 基本特征
* 完全自动化 
	* 几乎不需要人来干预和维护，降低成本，更为可靠
* 算法公开
	* 算法的公开并不会影响到它的安全，想要破解必须依靠AI（人工智能）或reverse engineering（逆向工程）

### 实现方式
* 基于文本
	* 短信
	* 图片中扭曲的杂糅的文本等等	
* 基于语音
	* 语音验证码
* JCaptcha
	* 提供了javascript的支持
	* smart captcha 
* MCaptcha
	* 一些简单的数学问题

不同方式的Captcha有不同的优缺点，有的照顾到特殊人群，有的相对安全，有的效率较高，安全性也各有不同，之后会对此进行深入探究。

### 攻击思路
* 用廉价的劳动力去识别captcha
* 利用执行中可以完全绕过captcha的bug
* 通过机器学习打造自动求解器

### 改进方式
总的思路是图片比文本更能抵抗基于机器学习的攻击,同时减少耗时，效率也更高

* geetest...
	* 图片填充比文本更复杂
* ASIRRA...
	* 图片混淆比文本更复杂

### 生活中我遇到过的captcha
* 微信非本机登陆时选择自己的好友头像，支付宝，手淘等等都有
* 微信非本机登陆时让好友发送验证码给自己，qq安全验证时也有
* 美团外卖等等的短信验证码，语音验证码
* 中传教务在线的数字文本验证码
* 拼图验证码
* 12306验证码等等


> 以上是自己学习的总结，如有错误，欢迎及时批评指正

[https://en.wikipedia.org/wiki/CAPTCHA#Origin_and_inventorship](url)

[https://luosimao.com/service/captcha](url)

[http://www.zzhaoz.com/edu/jingyan/10538.html](url)

[http://research.microsoft.com/en-us/um/redmond/projects/asirra/](url)

[http://www.geetest.com/](url)
