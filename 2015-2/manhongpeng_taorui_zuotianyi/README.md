##双因素认证系统注册登陆流程##
进入登陆页面otpverify.php后显示如下:




![](https://github.com/kadaokaduan/ns/blob/master/2015-2/manhongpeng_taorui_zuotianyi/1.png)


假设已有邮箱为‘6*669**44@qq.com’的用户，但该用户从未进行登录。
该用户欲登录首先要获取OTP一次一密验证码（此处使用邮箱而未使用手机短信形式）



点击获取验证码后，后台自动给该邮箱发送验证码，邮箱中显示如下




![](https://github.com/kadaokaduan/ns/blob/master/2015-2/manhongpeng_taorui_zuotianyi/2.png)


在15分钟之内将验证码填入otpverify.php并输入密码，点击登录则显示如下页面




![](https://github.com/kadaokaduan/ns/blob/master/2015-2/manhongpeng_taorui_zuotianyi/3.png)

现在再次登录邮箱收取邮件




![](https://github.com/kadaokaduan/ns/blob/master/2015-2/manhongpeng_taorui_zuotianyi/4.png)

由于本地访问网站，IP地址显示为::1，这个地址也是一个未知的，需要加入白名单。用户点击链接执行脚本后即可通过认证，用户下次登录即可通过验证。