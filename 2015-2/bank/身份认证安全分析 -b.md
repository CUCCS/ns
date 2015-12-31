# 身份认证安全分析 #

----------
###身份认证安全分析将从以下几个方面展开：
1. 密码算法：即使用了什么算法如何将明文密码转换为密文；
2. 密码及认证传输：密码和相应认证在网络中如何传输；
3. 密码存储：密码在后台数据库中的存储方式等；
4. 对相关风险的猜想；

- 1.获取用户密码
-
&nbsp;&nbsp;&nbsp;&nbsp;在客户端安全分析中我们可以看到，在前端对密码的处理十分少，对于后端的处理我们暂时也无法得知，但是我们可以讨论下从前端获取到的密码是什么样子的，它传输给后端时有什么处理，找出相关代码如下：

    ***获取密码
    function setCalcButtonBg()
    {
    for(var i=0;i<Calc.elements.length;i++)
    {
    if(Calc.elements[i].type=="button"&&Calc.elements[i].bgtype!="1")
    {
    if(Calc.elements[i].bgtype=="2"){
    Calc.elements[i].className="btn_num";
    }else{
    Calc.elements[i].className="btn_letter";
    }
    var str1=Calc.elements[i].value;
    str1=str1.trim();
    if(str1.length==1)
    {
    }
    var thisButtonValue=Calc.elements[i].value;
    thisButtonValue=thisButtonValue.trim();
    if(thisButtonValue.length==1)
    {
    Calc.elements[i].onmouseup =
    function ()
    {
    var thisButtonValue=this.value;
    thisButtonValue=thisButtonValue.trim();
    thisButtonValue=jiamiMimaKey(thisButtonValue);//调用加密
    addValue(thisButtonValue);
    }
    }
    }
    }
    }
    ***实施加密
    function  jiamiMimaKey(newValue) {
    	if (typeof(b) == "undefined" || typeof(ifUseYinshe) == "undefined" || ifUseYinshe == 0) {return newValue;}
    	var everyone = '';
    	var afterPass = '';
    	for (var i=0;i<newValue.length;i++ ) {
    			everyone = newValue.charAt(i);
    			for (var j =0;j<((b.length)/2);j++) {
    					if (everyone == b[2*j]) {
    							afterPass = afterPass + b[2*j+1];
    							break;
    					}
    			}
    		}
    		newValue= afterPass;
    		if (typeof(jiami) != "undefined"){
    				jiami = 1;
    		}		
    		return afterPass;
    }

对从键盘上获得的值存储到Calc.elements[i].value，并用Calc.elements[i].elements标记了是数字还是字母，而整个类的定义都在后端。

- 2.密码及认证传输
-
&nbsp;&nbsp;&nbsp;&nbsp;传输过程中，该行使用传输协议https，Https是基于安全目的的Http通道。Https在数据通信之前需要客户端、服务器进行握手（身份认证），建立连接后，传输数据经过加密，通信端口443。其安全基础由SSL层来保证，双向认证 SSL 协议的具体通讯过程中要求服务器和用户双方必须都有证书。SSL协议是通过非对称密钥机制保证双方身份认证，并完成建立连接，在实际数据通信时通过对称密钥机制保障数据安全性。 

> 附：</br>
1. https发展历史：https://en.wikipedia.org/wiki/Transport_Layer_Security</br>
2. https工作原理：https://cattail.me/tech/2015/11/30/how-https-works.html

**在了解了该行前后台数据交互的原理后，结合https协议，使用代理服务器，burpsuit进行抓包实验，对抓到的数据包进行分析如下:**

1. 在从建行主页点击个人网上银行登录按钮时，截获到顺序执行的链接如下图一，截获到的第一个的第一个数据包如下图二，我们可以看到它发送的第一个请求是获取个人登录的界面，此时是成功执行，返回值为200，在此html下依次调用了接下来的链接：

图一：
![](http://www.mftp.info/20151001/1451527200x-568361186.png)

图二：
request：
![](http://www.mftp.info/20151001/1451525875x-568361186.png)
response：
![](http://www.mftp.info/20151001/1451527368x-568361186.png)

2. 接下来调用的链接我们可以从图一中得知，在使用代理的情况下（并未对数据包有任何修改），这几个链接的返回值都为304，即报错，但是在不使用代理的情况下就完全可以连通，相关提示如下图：

![](http://www.mftp.info/20151001/1451535839x-568361186.png)

![](http://www.mftp.info/20151001/1451535874x-568361186.png)

***在网络监测这部分，安全性比较高，对有网络代理都进行了屏蔽，而且在正常联通后，会立马启用https协议代替http协议，保证整个交互过程中加密。后续探讨和代码研究想要找出如何实现了这部分的网络验证，以及https协议利用过程中是否有漏洞。***

- 3.密码存储
-
&nbsp;&nbsp;&nbsp;&nbsp;对于密码在后天的存储情况，因https传输协议的限制，就目前还没有获得相应的进展。

-4.相关猜想
-
&nbsp;&nbsp;&nbsp;&nbsp;我们都知道，整个网页的实现过程中，前后端不断对进行交互，且对时间，次数等有严密的限制，并且整个过程有https协议帮忙加密，找出交互时传递的主要参数也有一定困难，但是，我们是否依旧可以实施中间人攻击呢？

假设：
1，我们分析出了前后端交互时传递的全部参数，截获用户在正常登录情况下发送的包，提取出用户的相关信息，对于时间等参数，进行替换，在相应理论的支持下，实现hash强碰撞攻击。

> 相应参考文献如下：
> 
> 1. Hash函数HAS160和MD5潜在威胁的分析http://wenku.baidu.com/view/f0bf451414791711cc7917b5.html?from=related
> 2. https://en.wikipedia.org/wiki/Hash_table
> 3. 哈希表碰撞攻击的基本原理：http://www.oschina.net/question/54100_49403

2，构造钓鱼网站：攻击者重画一个和建行一模一样的钓鱼网站，但是在用户密码输入时，加入一部分代码，将用户名及密码，先传递到自己的接收器，再正常给用户实施登录到正常页面。
