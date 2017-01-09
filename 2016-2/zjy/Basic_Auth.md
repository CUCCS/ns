# Basic 认证
## Basic认证概述
HTTP 有两种标准的认证方式，BASIC 和 DIGEST。正如"Basic Authentication"这个名字，它是 Authentication中最简单的方法。在HTTP协议进行通信的过程中，HTTP协议定义了基本认证过程以允许HTTP服务器对WEB浏览器进行用户身份认证的方法，当一个客户端向HTTP服务器进行数据请求时，如果客户端未被认证，则HTTP服务器将通过基本认证过程对客户端的用户名及密码进行验证，以决定用户是否合法。

## Basic认证基本实现方式
客户端在用户输入用户名及密码后，将用户名及密码以**BASE64**加密，加密后的密文将附加于请求信息中，如当用户名为Parry，密码为123456时，客户端将用户名和密码**用":"合并**，并将合并后的字符串用BASE64加密，并于每次请求数据时，将密文附加于**请求头（Request Header）**中。
HTTP服务器在每次收到请求包后，根据协议取得客户端附加的用户信息（BASE64加密的用户名和密码），解开请求包，对用户名及密码进行验证，如果用户名及密码正确，则根据客户端请求，返回客户端所需要的数据；否则，返回错误代码或重新要求客户端提供用户名及密码。
![Image text](https://github.com/Zhaojytt/ns/blob/master/2016-2/zjy/img_folder/basic_auth.jpg..png)

## Basic认证优缺点

- 优点是逻辑简单明了、设置简单。

- 缺点显而易见，即使是BASE64后也是可见的明文，很容易被破解、非法利用，安全性很差。另外，HTTP是无状态的，同一客户端每次都需要验证。

## Basic认证学习文档
[http://www.ibm.com/developerworks/cn/webservices/1106_webservicessecurity/index.html](url)

[http://blog.itpub.net/23071790/viewspace-709367](url)

[http://www.cnblogs.com/parry/archive/2012/11/09/ASPNET_MVC_Web_API_HTTP_Basic_Authorize.html](url)

> **之后我将模拟一下basic认证过程**
