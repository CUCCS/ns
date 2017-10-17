# HTTPS传输过程详解 #

## SSL/TLS运行过程 ##
![](pic/sslTSL.png)

## 实验抓包 ##
- 访问baidu.com，抓取的数据包，首先客户端和服务器进行TCP的三次握手，接着客户端发送Client Hello与服务器协商，服务器确定加密的算法，然后传送加密的数据。实验数据显示，baidu.com使用的是TLSv1.2。而SSLv2 and SSLv3已经弃用。
- ![](pic/https.PNG)
- Client Hello数据包，包含cipher Suites和signature Alogrithms等内容，并且会生成随机数Random和Session ID
- ![](pic/clientHello.PNG)
- 浏览器支持的加密算法及服务器的信息，reserved data是missing状态
- ![](pic/cipherSuites.PNG)
- 浏览器支持的签名算法
- ![](pic/signatureAlogrithms.PNG)
- Server Hello数据包，包含传输过程使用的加密算法，生成随机数random，Session ID是客户端的Session ID
- ![](pic/serverHello.PNG)
- 服务器请求change cipher spec message
- ![](pic/changeCipherSpec.PNG)
- Encrypted handshake message
- ![](pic/handshakeMessage.PNG)
- 被加密传输的数据
- ![](pic/dataEnc.PNG)