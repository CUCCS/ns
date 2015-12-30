</br>这次试验是通过ettercap进行DNS欺骗攻击！
</br>（1）查看DNS：locate etter.dns
</br>（2）修改etter.dns文件并保存，以确保它执行正确的DNS欺骗攻击
</br>![](https://github.com/hua12/PIC/blob/master/%E4%BF%AE%E6%94%B9dns%E6%96%87%E4%BB%B6.PNG)
</br>10.0.2.15是攻击者的IP地址。确保Web服务器运行在攻击者的机器，一定要启用IP转发
</br>![](https://github.com/hua12/PIC/blob/master/%E5%BC%80%E5%90%AFIP%E8%BD%AC%E5%8F%91.PNG)
</br>（3）清除DNS缓存
</br>![](https://github.com/hua12/PIC/blob/master/%E6%B8%85%E9%99%A4DNS%E7%BC%93%E5%AD%98.PNG)
</br>（4）通过ettercap启用DNS欺骗攻击
</br>![](https://github.com/hua12/PIC/blob/master/%E6%89%AB%E6%8F%8F.PNG)
</br>说明：-P  使用插件，这里我们使用的是dns_spoof；-T 使用基于文本界面；-q  启动安静模式（不回显的意思）；-M 启动ARP欺骗攻击
</br>（5）启用dns_spoof插件来执行DNS欺骗中间人攻击后,当受害者浏览freebuf网站的时候就会被重定向到10.0.2.15，在终端出现：
</br>dns_spoof:[freebuf.com]spoofed to [10.0.2.15]
</br>例如metasploit 渗透工具使用ettercap进行dns欺骗。选择想要的exploit，在payload中就选择 reverse_tcp：
</br>![](https://github.com/hua12/PIC/blob/master/MSF.PNG)
</br>![](https://github.com/hua12/PIC/blob/master/msf%E8%AE%BE%E7%BD%AE.PNG)
</br>一旦受害者打开该网站，就会被重定向到10.0.2.15中，然后会话开始！
