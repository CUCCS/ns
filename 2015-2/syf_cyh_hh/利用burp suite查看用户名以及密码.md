</br>所遇到的问题反馈：
</br>之前做实验的时候总是会遇到网络不通的问题。最终选用了桥接的网络模式。
</br>物理主机的IP信息
</br>![](https://github.com/vsmile0601/Pictures/blob/master/主机IP信息.PNG)
</br>虚拟机的IP信息
</br>![](https://github.com/vsmile0601/Pictures/blob/master/虚拟机IP信息.PNG)
</br>选用了桥接模式：
</br>![](https://github.com/vsmile0601/Pictures/blob/master/网络模式为桥接.PNG)
</br>浏览器代理设置：
</br>![](https://github.com/vsmile0601/Pictures/blob/master/浏览器代理设置.PNG)
</br>burpsuite代理设置：
</br>![](https://github.com/vsmile0601/Pictures/blob/master/burp suite代理设置.PNG)
</br>进入到邮箱的登录界面后，开启burp suite的Intercept功能，即Intercept on，输入用户名和密码，点击“登录”
</br>![](https://github.com/vsmile0601/Pictures/blob/master/登陆页面.png)
</br>如图，可以清楚的看到截获的用户名及密码（为确保隐私，以打上马赛克）
</br>![](https://github.com/vsmile0601/Pictures/blob/master/截获密码.png)
</br>测试发送邮件截获邮件内容：
</br>![](https://github.com/vsmile0601/Pictures/blob/master/发送邮件.png)
</br>从所标识的地方就可以用肉眼看出所发信件的内容：
</br>![](https://github.com/vsmile0601/Pictures/blob/master/信件内容.png)

