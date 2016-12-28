# 今天来谈谈Google的reCaptcha

## 最初的 recaptcha

* 最初的reCAPTCHA是由CMU设计的一个让电脑去向人类求助的强大系统。**它利用CAPTCHA的原理（CAPTCHA在之前的文档中已经介绍过），借助于人类大脑对难以识别的字符的辨别能力，进行对古旧书籍中难以被OCR识别的字符进行辨别的技术。**reCAPTCHA 最有名的例子是协助纽约时报数码化其历年来全部的纸本文章，总共 150 年的报纸，不少文章已经因为年代久远油墨褪色，不易辨识。

* 具体做法是：
	
	将OCR软件无法识别的文字扫描图传给世界各大网站，用以替换原来的验证码图片；那些网站的用户在正确识别出这些文字之后，其答案便会被传回CMU。 显示屏上会有两组文字或数字，一组是电脑辨识的出来，另一组是电脑辨识不出来，需要人类协助辨识。如下图所示：
 
	![Image text](https://github.com/Zhaojytt/ns/blob/master/2016-2/zjy/img_folder/1.jpg)

* 存在的问题
	
	* **安全性**一直都在受到挑战，就连 Google 自己都破解了 CAPTCHA 验证系统 ，G研究团队发现能够教会计算机读懂CAPTCHA系统的晦涩文字，并且准确率竟然高达99.8%，这也就意味着CAPTCHA的漏洞会被黑客轻易破解。
	* 降低用户验证效率，工作不流畅，体验不友好。
	* “点击劫持”
	
## No CAPTCHA reCAPTCHA
### reCaptcha的升级版

No CAPTCHA可以让“人类用户”更加容易的证明自己是个人，而让“机器用户”经过更多的审查判断其身份。该系统只提供了一个复选框，用户勾选“我不是机器人”之后，系统算法便利用“风险分析引擎”，根据用户在该网站的一系列行为，判断用户是否为人类，并过滤掉任何容易识别为人类的用户。对于用户来说，流程做了改进，操作更方便，验证更准确。官方宣称安全性相较之前有了很大的提升（但是否如此下文会讲一讲）
	
### 具体实现

* 和要求用户输入文字不同，该系统只提供一个复选框，写着“我不是机器人”，如果你勾选，Google 就会用“风险分析引擎”来确定你是不是人类。	

![Image text](https://github.com/Zhaojytt/ns/blob/master/2016-2/zjy/img_folder/2.gif)

* 如果 noCAPTCHA 认为是人类，那么无需更多的验证了；如果没有通过，会被要求进一步验证，不过也无需眯着眼难受地看小图，然后手动输入。只需从几张图片中，点选正确的选项。

![Image text](https://github.com/Zhaojytt/ns/blob/master/2016-2/zjy/img_folder/3.png)
* 所谓的“风险分析引擎”，可以跟踪用户点击验证框之前、当时和之后的行为，来判断是否是人为操作。可能是出于安全性的考虑，官方并未给出“风险分析引擎”的具体实现。
* 此外，Google也明白用户对验证码的苦恼，新的No Captcha系统的算法仅仅只需要用户验证一次，在下一次访问网站时，便无需任何验证，因为系统会自动检验用户cookies。除非你是定时清理cookies狂魔，那么你每一次访问都必须通过这种无聊的“我不是机器人”验证。

### 安全性分析

其对cookies高度依赖，有不小的安全隐患。

* 对于机器用户来说，一旦第一次通过验证，它们会通过OCR识别，特意留下相关的访问cookies的证据，把自己伪装的更像是人类用户。这些“故意制造”的cookies便会成为今机器用户今后正常访问的通行证，机器人也不需要任何的验证码了。
* 当No Captcha系统无法识别到用户的历史浏览行为，例如用户无痕浏览，Google就会搬出传统的Captcha验证码检测，但是这些已经被机器用户攻破了。
* No Captcha系统在防止“点击劫持”等黑客手法时也有一定的安全隐患。这一手法通过网站跳转，让用户帮助黑客识别出验证码。


目前看来，No Captcha系统足够成熟可靠仍是要等待不短的时间。



## Invisible reCAPTCHA
 Google即将正式推出！据说是一种无需用户互动，利用演算法便可分辨人类和程序的验证操作。目前还没有发布。期待中(●'◡'●)

![Image text](https://github.com/Zhaojytt/ns/blob/master/2016-2/zjy/img_folder/4.png)
### 畅想与思考
>验证码是一个充满矛盾的产物，一方面，人类希望计算机能够通过算法帮助我们解决问题，一定程度上代替人类，另一方面，人类在极力避免计算机利用算法做坏事。随着技术的发展，计算机将变得越来越“通情达理”，越来越接近人类。**如果有一天，计算机能够通过验证码验证，又该如何区分人类和计算机呢？**

###学习来源
> 因为不能翻墙，连接不到谷歌的官网，所以没有官方的文档，这非常遗憾。是时候要翻墙去了O(∩_∩)O

[http://www.leiphone.com/news/201412/Hnux7n19OcNWwUFt.html](url)

[http://www.kejilie.com/sohu/article/aIJbae.html](url)

[https://www.wired.com/2014/12/google-one-click-recaptcha/](url)

[http://www.kejilie.com/leiphone/article/C74B3B67BCEC187408BB06BDCF8241B3.html](url)

[http://technews.cn/2014/12/04/prove-your-human-the-new-recaptcha-just-check-your-human-by-check/](url)

[http://www.kejilie.com/ifanr/article/F96F0E89778795EB4C0C0FA7A087C904.html](url)

[http://jandan.net/2013/02/17/recaptcha.html](url)

[https://www.landiannews.com/archives/28238.html](url)
