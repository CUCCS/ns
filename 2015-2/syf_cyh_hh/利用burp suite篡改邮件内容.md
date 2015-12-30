</br>首先用被攻击账号登录mail.163.com，然后burp suite——intercept on
</br>写好的初始状态为：
</br>![](https://github.com/vsmile0601/Pic/blob/master/第二次初始邮件.png)
</br>点击发送后可以在HTTP history中看到拦截的历史：
</br>![](https://github.com/vsmile0601/Pic/blob/master/Proxy中的HTTP%20history.PNG)
</br>将所要选择的条目右键单击send to repeater，可以找到所写邮件的标题名称：
</br>![](https://github.com/vsmile0601/Pic/blob/master/第二次被攻击前的信件名称.PNG)
</br>将标题名称进行修改：然后点击上方的“GO”
</br>![](https://github.com/vsmile0601/Pic/blob/master/第二次修改信件名称.PNG)
</br>将intercept off后即可看到邮件发送成功，在收件人邮箱里可以看到被攻击的文件：
</br>![](https://github.com/vsmile0601/Pic/blob/master/第二次收到的邮件.png)
</br>但是不知道为什么收件人信箱每次实验可以收到两封邮件，一个是被攻击的，一个是没被攻击的：
</br>![](https://github.com/vsmile0601/Pic/blob/master/每次发两封？！.png)
</br>不知是否点击repeater中的GO时就已经发送了修改的邮件，然而off后邮件的客户端又发送了一下原本的邮件？？？？
</br>（Ps.我们一共连续实验了两次，上面展示的是第二次实验的内容）
