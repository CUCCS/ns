# 逆向分析/点评 #
----------
10/22/2015 12:39:52 PM
### 屏幕键盘的原理和安全性分析 ###

分析对象至少应包含以下2家：

1 中传的一卡通在线充值转账系统 

###2、 建设银行个人网银登录

对比直接使用物理键盘方式输入密码，屏幕键盘是否改进了安全性？请详细阐述理由。

## 目录 ##

**2 建设银行个人网银登录**

-   基本情况
-   登录界面
-   软键盘安全性

**2、  探查分析**

- chorme浏览器Network工具

**3、 初步实验**

- 穷举密码、分析规律

**4、 提出猜想**

- 软键盘存在的漏洞
- 密码的获取方法

**5、深度实验**

- 工具及实验环境
- 实验过程及结果
- 漏洞利用、编写代码

**6、安全建议**  

- 深层分析  
- 提出建议

## 正文 ##

###2、 建设银行个人网银登录###

####基本情况：####

中国建设银行个人网上银行可用任何网络登录。使用https全站加密。
 [https://ibsbjstar.ccb.com.cn/app/V5/CN/STY1/login.jsp?UDC_CUSTOMER_ID=&UDC_CUSTOMER_NAME=&UDC_COOKIE=55db7a7686c3567fovXFSTsXQwrDHKJbu3Gi1447316596250oAeRkYNfiXp211LrdCCg6adec1ee677022fc1c1a341abebc2f14&UDC_SESSION_ID=ZT1EMzx79kGMLjQac5484c63d48-20151112162319](https://ibsbjstar.ccb.com.cn/app/V5/CN/STY1/login.jsp?UDC_CUSTOMER_ID=&UDC_CUSTOMER_NAME=&UDC_COOKIE=55db7a7686c3567fovXFSTsXQwrDHKJbu3Gi1447316596250oAeRkYNfiXp211LrdCCg6adec1ee677022fc1c1a341abebc2f14&UDC_SESSION_ID=ZT1EMzx79kGMLjQac5484c63d48-20151112162319)

####登录界面：####

![建设银行个人网银登录界面](http://i.imgur.com/UnS3sFD.png)

####软键盘安全性：####

打开软键盘后的界面：

![建设银行个人网银软键盘](http://i.imgur.com/0xTi8dm.png)

连续刷新十次，得到不同的软键盘：

1. 1074569823
2. 3694157802
3. 7248156093
4. 1936508274
5. 1834207695
6. 8624537109
7. 7134502698
8. 4520937816
9. 4230587196
10. 1052476893

11/12/2015 10:08:30 PM 

可以看到，每次软键盘数字的排列都是随机打乱的。

    由chorme开发者工具得到的代码：

    <tr>
	<td class="tar">登录密码：</td>
	<td>

	 <input style="vertical-align:middle;width:154px;" name="LOGPASS" id="LOGPASS" type="password" autocomplete="off" size="20" minlength="6" maxlength="12" title="登录密码" onchange="$('Calc').password.value=this.value;
	 keyJiami(this);" onfocus="if($('softkeyboard').style.display == 'none'){ if(isShowKeyboard()){this.value = ''; 
	 password1=this; showkeyboard(); this.readOnly=1; $('Calc').password.value='';} if(useSoftBoard){this.value = '';
	 useSoftBoard = false;}}" readonly=""> 
	
     <!--软键盘 开始-->
                     
     <div id="span0" class="rujian1" title="软键盘指软件模拟键盘，您可以通过鼠标点击输入字符，防止木马记录键盘输入的密码。" onclick="if (true) { $('LOGPASS').value = ''; password1 = $('LOGPASS'); showkeyboard(); $('LOGPASS').readOnly = 1; $('Calc').password.value = ''; };">
     <img src="/V5/images5/softkeyboard.gif" width="56" height="18" border="0" alt="" id="img_id">
     </div>
                            
     <script>

       try {	 
            var isCurrIE6=(navigator.userAgent.toLowerCase().indexOf("msie 6.0") != -1);
            var isCurrIE7=(navigator.userAgent.toLowerCase().indexOf("msie 7.0") != -1);
            //IE6特殊处理
            if(isCurrIE6)	{
                                document.getElementById("span0").className = "ruanjian"; 
                                var obj=document.getElementById("icon_event");
                            	obj.attachEvent("onmouseover",function(){ document.getElementById("icon_pop").style.display = "block"; document.getElementById("img_id").style.display = "none";});
                            	obj.attachEvent("onmouseout",function(){ document.getElementById("icon_pop").style.display = "none";  document.getElementById("img_id").style.display = ""; });
                              }
                              if(isCurrIE7){
                            	document.getElementById("span0").style.left = "217px"; 
                            	document.getElementById("span0").style.top = "131px"; 
                            	var obj=document.getElementById("icon_event");
                            	obj.attachEvent("onmouseover",function(){ document.getElementById("img_id").style.display = "none";});
                            	obj.attachEvent("onmouseout",function(){  document.getElementById("img_id").style.display = ""; });
                              }
          } catch (e) {}
       </script>   

       <!--软键盘 结束-->	 
       </td>
	   <td width="30px"></td>
	   <td class="form_area_table_r" style="padding-left:0px;"><a tabindex="-1" href="#" onclick="refreshLoginPwd();">忘记密码？</a></td>
	   </tr>

       <div align="center" id="softkeyboard" name="softkeyboard" style="position: absolute; left: 14px; top: 141px; width: 400px; z-index: 65535; display: block;"><table id="CalcTable" width="" border="0" align="center" cellpadding="0" cellspacing="0" bgcolor="" style="border: 1px solid rgb(181, 173, 241);"><form id="Calc" name="Calc" action="" method="post" autocomplete="off"></form><tbody><tr><td class="table_title" title="尊敬的客户：为了保证网上交易安全,建议使用密码输入器输入密码!" align="right" valign="middle" bgcolor="" style="cursor: default; background-color: rgb(181, 173, 241);"><input type="hidden" value="R4_D=7y" name="password"><input type="hidden" value="ok" name="action2">&nbsp;<font style="font-weight:bold; font-size:15px; color:#075BC3">中国建设银行&nbsp;&nbsp;密码输入器</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input id="useKey" class="btn_letter" style="width:110px;height:25px;BORDER:1px solid blue; font-size:14px" type="button" value="使用键盘输入" bgtype="1" onclick="password1.readOnly=0;password1.focus();closekeyboard();password1.value='';setShowKeyBoard(false);" onkeyup="if(event.keyCode==13){password1.readOnly=0;password1.focus();closekeyboard();password1.value='';setShowKeyBoard(false);}"><span style="width:2px;"></span></td></tr><tr align="center"><td align="center" bgcolor="#FFFFFF"><table align="center" width="%" border="0" cellspacing="1" cellpadding="0">
		<tbody><tr align="left" valign="middle"> 
		<td> <input type="button" value="~" class="btn_letter"></td>
		<td> <input type="button" value="!" class="btn_letter"></td>
		<td> <input type="button" value="@" class="btn_letter"></td>
		<td> <input type="button" value="#" class="btn_letter"></td>
		<td> <input type="button" value="$" class="btn_letter"></td>
		<td><input type="button" value="%" class="btn_letter"></td>
		<td><input type="button" value="^" class="btn_letter"></td>
		<td> <input type="button" value="&amp;" class="btn_letter"></td>
		<td><input type="button" value="*" class="btn_letter"></td>
		<td><input type="button" value="(" class="btn_letter"></td>
		<td><input type="button" value=")" class="btn_letter"></td>
		<td><input type="button" value="_" class="btn_letter"></td>
		<td> <input type="button" value="+" class="btn_letter"></td>
		<td><input type="button" value="|" class="btn_letter"></td>
		<td colspan="1" rowspan="2"> <input name="button10" type="button" value=" 退格 " onmouseup="setpassvalue();" '="" style="width:100px;height:42px;BORDER-RIGHT:1px none;FONT-SIZE: 18px" class="btn_letter"> 
		</td>
		</tr>
		<tr align="left" valign="middle"> 
		<td><input width="38" height="38" type="button" value="`" class="btn_letter"></td>
		<td><input type="button" bgtype="2" name="button_number1" value="3" class="btn_letter"></td>
		<td> <input type="button" bgtype="2" name="button_number2" value="2" class="btn_letter"></td>
		<td> <input type="button" bgtype="2" name="button_number3" value="0" class="btn_letter"></td>
		<td> <input type="button" bgtype="2" name="button_number4" value="4" class="btn_letter"></td>
		<td> <input type="button" bgtype="2" name="button_number5" value="1" class="btn_letter"></td>
		<td> <input type="button" bgtype="2" name="button_number6" value="6" class="btn_letter"></td>
		<td> <input type="button" bgtype="2" name="button_number7" value="7" class="btn_letter"></td>
		<td> <input type="button" bgtype="2" name="button_number8" value="5" class="btn_letter"></td>
		<td> <input type="button" bgtype="2" name="button_number9" value="8" class="btn_letter"></td>
		<td> <input bgtype="2" name="button_number0" type="button" value="9" class="btn_letter"></td>
		<td> <input type="button" value="-" class="btn_letter"></td>
		<td> <input type="button" value="=" class="btn_letter"></td>
		<td> <input type="button" value="\" class="btn_letter"></td>
		<td> </td>
		</tr>
		<tr align="left" valign="middle"> 
		<td> <input type="button" value="q" class="btn_letter"></td>
		<td> <input type="button" value="w" class="btn_letter"></td>
		<td> <input type="button" value="e" class="btn_letter"></td>
		<td> <input type="button" value="r" class="btn_letter"></td>
		<td> <input type="button" value="t" class="btn_letter"></td>
		<td> <input type="button" value="y" class="btn_letter"></td>
		<td> <input type="button" value="u" class="btn_letter"></td>
		<td> <input type="button" value="i" class="btn_letter"></td>
		<td> <input type="button" value="o" class="btn_letter"></td>
		<td> <input name="button8" type="button" value="p" class="btn_letter"></td>
		<td> <input name="button9" type="button" value="{" class="btn_letter"></td>
		<td> <input type="button" value="}" class="btn_letter"></td>
		<td> <input type="button" value="[" class="btn_letter"></td>
		<td> <input type="button" value="]" class="btn_letter"></td>
		<td><input name="button9" type="button" onclick="capsLockText();setCapsLock();" ondblclick="capsLockText();setCapsLock();" value="切换大/小写" style="width:100px;height:21px;BORDER-RIGHT:1px none;font-size:15px" class="btn_letter"></td>
		</tr>
		<tr align="left" valign="middle"> 
		<td> <input type="button" value="a" class="btn_letter"></td>
		<td> <input type="button" value="s" class="btn_letter"></td>
		<td> <input type="button" value="d" class="btn_letter"></td>
		<td> <input type="button" value="f" class="btn_letter"></td>
		<td> <input type="button" value="g" class="btn_letter"></td>
		<td> <input type="button" value="h" class="btn_letter"></td>
		<td> <input type="button" value="j" class="btn_letter"></td>
		<td> <input name="button3" type="button" value="k" class="btn_letter"></td>
		<td> <input name="button4" type="button" value="l" class="btn_letter"></td>
		<td> <input name="button5" type="button" value=":" class="btn_letter"></td>
		<td> <input name="button7" type="button" value="&quot;" class="btn_letter"></td>
		<td> <input type="button" value=";" class="btn_letter"></td>
		<td> <input type="button" value="'" class="btn_letter"></td>
		<td rowspan="2" colspan="2"> <input name="button12" type="button" bgtype="1" onclick="OverInput();" value="   确定   " style="BORDER:3px solid blue;width:126px;height:42px;FONT-SIZE: 18px;" class="btn_letter"></td>
		</tr>
		<tr align="left" valign="middle"> 
		<td><input name="button2" type="button" value="z" class="btn_letter"></td>
		<td> <input type="button" value="x" class="btn_letter"></td>
		<td> <input type="button" value="c" class="btn_letter"></td>
		<td> <input type="button" value="v" class="btn_letter"></td>
		<td> <input type="button" value="b" class="btn_letter"></td>
		<td> <input type="button" value="n" class="btn_letter"></td>
		<td> <input type="button" value="m" class="btn_letter"></td>
		<td> <input type="button" value="<" class="btn_letter"></td>
		<td> <input type="button" value=">" class="btn_letter"></td>
		<td> <input type="button" value="?" class="btn_letter"></td>
		<td> <input type="button" value="," class="btn_letter"></td>
		 <td> <input type="button" value="." class="btn_letter"></td>
		 <td> <input type="button" value="/" class="btn_letter"></td>
		</tr>
		</tbody></table></td></tr></tbody></table></div>


从这段代码中，可以发现：

- 键盘由HTML代码构成，而不是使用点击坐标返回值的方法。
- 代码
`<input type="button" bgtype="2" name="button_number5" value="1" class="btn_letter">`中可以看见每个软键盘对应的按键给的value值。此value值随着页面的手动右键刷新不断更改成为下一组随机数。

###2、  探查分析###

#### chorme浏览器：####

可探查到：

![data](http://i.imgur.com/EIiDArS.png)

此LOGPASS与输入的并不一致。

使用network工具：

**General:**  
Remote Address:106.37.193.66:443  
Request URL:https://ibsbjstar.ccb.com.cn/app/V5/CN/STY1/login.jsp  
Request Method:POST  
Status Code:200 OK

>200请求成功 303重定向 400请求错误 401未授权 
>403禁止访问 404文件未找到 500服务器错误  
>
> 此处无法直接使用远程IP地址转到目的网页。


> 第二次抓包（12/12/2015 9:13:33 PM ）：  
> Remote Address:219.142.89.66:443。  
> Request URL:https://ibsbjstar.ccb.com.cn/app/B2CMainPlatV5?CCB_IBSVersion=V5&SERVLET_NAME=B2CMainPlatV5
>第三次抓包：
>Remote Address:124.127.108.2:443。
>远程端口就是和你连机的电脑或服务器的端口。校园网每一次登录时远程地址都相同。可以看出，建设银行具有多台服务器。


> 对类似的网站都做了类似处理，不能直接登入看到有关的任何信息。
> 网页上只会显示未收到数据或无法显示该网页。

**Response Headers: **  
Connection:Keep-Alive  
Content-Type:text/html; charset=ISO_8859_1  
Date:Wed, 02 Dec 2015 01:23:51 GMT  
Keep-Alive:timeout=5, max=100  
Server:Apache

> 第二次抓包此处新增：  
> Set-Cookie:FAVOR=|||||||||1|||||||||||; expires=Thursday, 09-Jun-2016 10:16:49 UTC
> 
Set-Cookie:UDC_ON=0  
Set-Cookie:_BOA_mf_txcode_=100101  
Set-Cookie:CCBIBS1=QK1gg9j1G4il2suhIMLmycAt9K6l6ceZ4KulMcLdEK0mscpqOiByRsSyvSR0cMKd9N8mRc19ISvlKsit7NWlycb90OplwcRlCYrIxRC8Op  
Transfer-Encoding:chunked  
X-Powered-By:Servlet/2.5 JSP/2.1

**view source:**  
HTTP/1.1 200 OK  
Date: Wed, 02 Dec 2015 01:23:51 GMT  
Server: Apache  
X-Powered-By: Servlet/2.5 JSP/2.1  
Keep-Alive: timeout=5, max=100  
Connection: Keep-Alive  
Transfer-Encoding: chunked  
Content-Type: text/html; charset=ISO_8859_1


**Request Headers:**  
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8  
Accept-Encoding:gzip, deflate  
Accept-Language:zh-CN,zh;q=0.8  
Cache-Control:max-age=0  
Connection:keep-alive  
Content-Length:14  
Content-Type:application/x-www-form-urlencoded  
Cookie:CCBIBS1=GI%2CAP3DFz5zfHmebbGvgdW6nrEffXWYTkEAfTWuXbEMg8WJk49vme2csdt5t82aXTH6gkWi32DRfHmI3NG4gUmTb8F6fW26TbSuiczzrMZ; FAVOR=|||||||||1|||||||||||; UDC_ON=0; _BOA_mf_txcode_=100101; null=354615818.2336.0000; JSESSIONID=GJspWpHVYnvt2N8X9cMw8F0LZhX4wy2nNBLlGvBFQ18HpZQfBsTn!330156228  
Host:ibsbjstar.ccb.com.cn  
Origin:https://ibsbjstar.ccb.com.cn  
Referer:https://ibsbjstar.ccb.com.cn/app/B2CMainPlatV5?CCB_IBSVersion=V5&SERVLET_NAME=B2CMainPlatV5  
Upgrade-Insecure-Requests:1  
User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36

**view source:**  
POST /app/V5/CN/STY1/login.jsp HTTP/1.1  
Host: ibsbjstar.ccb.com.cn  
Connection: keep-alive  
Content-Length: 14  
Cache-Control: max-age=0  
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8  
Origin: https://ibsbjstar.ccb.com.cn  
Upgrade-Insecure-Requests: 1  
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36  
Content-Type: application/x-www-form-urlencoded  
Referer: https://ibsbjstar.ccb.com.cn/app/B2CMainPlatV5?  
CCB_IBSVersion=V5&SERVLET_NAME=B2CMainPlatV5  
Accept-Encoding: gzip, deflate  
Accept-Language: zh-CN,zh;q=0.8  
Cookie: CCBIBS1=GI%2CAP3DFz5zfHmebbGvgdW6nrEffXWYTkEAfTWuXbEMg8WJk49vme2csdt5t82aXTH6gkWi32DRfHmI3NG4gUmTb8F6fW26TbSuiczzrMZ; FAVOR=|||||||||1|||||||||||;   
UDC_ON=0;  
_BOA_mf_txcode_=100101;    
null=354615818.2336.0000;   
JSESSIONID=GJspWpHVYnvt2N8X9cMw8F0LZhX4wy2nNBLlGvBFQ18HpZQfBsTn!330156228

> 第二次抓包此处新增：  
> Query String Parameters  
> CCB_IBSVersion:V5  
> SERVLET_NAME:B2CMainPlatV5


**Form Data:**
UKEYSERIALNUM:

> 第二次抓包新增：    
> TXCODE:100101
>   
> 此处的TXCODE为交易码，是由中国建设银行统一分配的。出自于 中国建设银行接口使用详细说明 - 苏飞 - 博客园
http://www.cnblogs.com/sufei/archive/2010/07/22/1783168.html
> 
> CCB_PWD_MAP_GIGEST:S000028433488713|LOGPASS  
> errURL:/app/V5/CN/STY1/login.jsp?UKEYSERIALNUM=  
> CCB_IBSVersion:  
> PT_STYLE:  
> PT_LANGUAGE:  
> resType:  
> PRIVATEINFO:  
> DESKTOP:0  
> EXIT_PAGE:login.jsp   
> UKEYSERIALNUM:  
> WANGZHANGLOGIN:  
> CCB_PWD_ENCKEY:  
> NAVIGATORNAME:1  
> FORMEPAY:   
> USERID:a  
> LOGPASS:777777  
> PT_CONFIRM_PWD:4epf4  

> 这里的PT_CONFIRM_PWD的值是刚才输入的附加码，即验证码。
> 
> CHOOSE_VERSION:1

**view source:**  
UKEYSERIALNUM: 
 
> 第二次抓包新增：  
> TXCODE=100101&CCB_PWD_MAP_GIGEST=S000028433488713%7CLOGPASS&errURL=%2Fapp%2FV5%2FCN%2FSTY1%2Flogin.jsp%3FUKEYSERIALNUM%3D&CCB_IBSVersion=&PT_STYLE=&PT_LANGUAGE=&resType=&PRIVATEINFO=&DESKTOP=0&EXIT_PAGE=login.jsp&UKEYSERIALNUM=&WANGZHANGLOGIN=&CCB_PWD_ENCKEY=&NAVIGATORNAME=1&FORMEPAY=&USERID=a&LOGPASS=777777&PT_CONFIRM_PWD=4epf4&CHOOSE_VERSION=1

![限制输错密码三次](http://image17-c.poco.cn/mypoco/myphoto/20151212/20/17863501720151212200731026_640.jpg?455x129_130)
与校园网不同，建设银行对输错密码进行了限制，这也说明难以用网页穷举攻击来获得用户密码。

![附加码](http://i.imgur.com/BPz5dJ5.png)

![附加码抓包1](http://image17-c.poco.cn/mypoco/myphoto/20151212/20/17863501720151212200843017_640.jpg?390x56_130)

![附加码抓包2](http://i.imgur.com/vc9V13y.png)

建设银行登录界面的附加码判别是前端判别。可以看出在network包中就可以获得附加码的明文，这也让输入附加码的这个操作变的不是很有意义。

###3、  初步实验###

#### 穷举分析：####

![测试数据](http://image17-c.poco.cn/mypoco/myphoto/20151212/21/17863501720151212210005027_640.jpg?697x145_130)

经过一系列数据的测试，可以初步推测POST包中密码的加密是与CCB_PWD_MAP_GIGEST有关的。而CCB_PWD_MAP_GIGEST的值也许会随着时间等因素而改变（测试期间分别5分钟，10分钟左右改变过值）。这样也增加了密码的安全性，难以像校园网一样破解。

*小笔记*
3 掌握好做网站的度和用户体验好难，因为你要在考虑网站安全性的同时，考虑到用户体验。而操作过于复杂往往不是用户想要的。

