<?php

	/**
	 * 已兼容php7
	 * 注：本邮件类都是经过我测试成功了的，如果大家发送邮件的时候遇到了失败的问题，请从以下几点排查：
	 * 1. 用户名和密码是否正确；
	 * 2. 检查邮箱设置是否启用了smtp服务；
	 * 3. 是否是php环境的问题导致；
	 * 4. 将26行的$smtp->debug = false改为true，可以显示错误信息，然后可以复制报错信息到网上搜一下错误的原因；
	 * 5. 如果还是不能解决，可以访问：http://www.daixiaorui.com/read/16.html#viewpl
	 *    下面的评论中，可能有你要找的答案。
	 *
	 *
	 * Last update time:2017/06
	 * UPDATE:
	 * 1、替换了高版本不支持的写法，如ereg、ereg_replace.
	 * 2、将 var 改为 public/private等.
	 * 3、使其兼容php7.
	 *
	 */

	require_once "Smtp.class.php";
	function randomkeys($length)
	{
		$pattern = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLOMNOPQRSTUVWXYZ'; //字符池
			for($i=0;$i<$length;$i++)
			{
				$key .= $pattern{mt_rand(0,61)}; //生成php随机数
			}
		return $key;
	}
	$random=randomkeys(6);
	//******************** 配置信息 ********************************
	$smtpserver = "smtp.126.com";//SMTP服务器
	$smtpserverport =25;//SMTP服务器端口
	$smtpusermail = "burnymcdull@126.com";//SMTP服务器的用户邮箱
	$smtpemailto = $_POST['username'];//发送给谁
	//$smtpemailto ="563038662@qq.com";
	$smtpuser = "burnymcdull@126.com";//SMTP服务器的用户帐号，注：部分邮箱只需@前面的用户名
	$smtppass = "szy19970107";//SMTP服务器的用户密码
	$mailtitle = "云上传服务系统密码找回";//邮件主题
	$mailcontent = "<h1>".$random."</h1>";//邮件内容
	$mailtype = "HTML";//邮件格式（HTML/TXT）,TXT为文本邮件
	//************************ 配置信息 ****************************
	include('connect.php');
	$sql="SELECT `E-mail` FROM `user` WHERE `E-mail`='$smtpemailto'";
  $result = mysqli_query($conn, $sql);
  $num=mysqli_num_rows($result);
  if($num){
    //$exist=1;
		$smtp = new Smtp($smtpserver,$smtpserverport,true,$smtpuser,$smtppass);//这里面的一个true是表示使用身份验证,否则不使用身份验证.
		$smtp->debug = false;//是否显示发送的调试信息
		$state = $smtp->sendmail($smtpemailto, $smtpusermail, $mailtitle, $mailcontent, $mailtype);
		$sql = "UPDATE `user` SET `IdetifyCode` = '$random' WHERE `user`.`E-mail` = '$smtpemailto' ";
    mysqli_query($conn, $sql);
    echo"<script>alert('恭喜！邮件发送成功！请输入验证码验证！');self.location='FindPassword1.html';</script>";
  }
	else{
		echo"<script>alert('对不起，邮件发送失败！请检查邮箱填写是否有误。');self.location='FindPassword.html';</script>";
	}
/*
	echo "<div style='width:300px; margin:36px auto;'>";
	if($state==""){
		echo "对不起，邮件发送失败！请检查邮箱填写是否有误。";
		echo "<a href='FindPassword.html'>点此返回</a>";
		exit();
	}
	echo "恭喜！邮件发送成功！！";
	echo "<a href='FindPassword1.html'>点此返回</a>";
	echo "</div>";
*/
?>
