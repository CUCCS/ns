<html>
<head>
	<script src="http://libs.baidu.com/jquery/2.1.4/jquery.min.js"></script>
	<script>
	$(document).ready(function () {
		$("#button1").click(function () {
			$.get("getcode.php?email=" + $("#email").val(), function (data) {
				if (data == 0) {
					alert("该email未注册");
				} else {
					alert("获取验证码成功,请登录邮箱查看");
				}

			});
		});
	});
	</script>
</head>
<body>
	<?php
	include_once("smtp.class.php");
	if(getenv('HTTP_CLIENT_IP')) { 
		$onlineip = getenv('HTTP_CLIENT_IP'); 
	} 
	elseif(getenv('HTTP_X_FORWARDED_FOR')) { 
		$onlineip = getenv('HTTP_X_FORWARDED_FOR'); 
	} 
	elseif(getenv('REMOTE_ADDR')) { 
		$onlineip = getenv('REMOTE_ADDR'); 
	} 
	else { 
		$onlineip = $HTTP_SERVER_VARS['REMOTE_ADDR']; 
	} 
	$userip = $onlineip; 
	if(isset($_POST['add']))
	{
		$ttt = 0;
		$id = 0 ;
		$email = $_POST['email'];
		$code = $_POST['code'];
		$password = $_POST['password'];
		$dbhost = 'localhost';
		$dbuser = 'xxx';
		$dbpass = 'xxx';
		$conn = mysqli_connect($dbhost, $dbuser, $dbpass,"xxx");
		$flag = 0;
		$tag0 = 0;
		$tag2 = 0;
		if(! $conn )
		{
			die('Could not connect: ' . mysqli_error());
		}
		$query = "SELECT id FROM user_infor WHERE email = ? AND password = ?";
		if ($stmt = mysqli_prepare($conn, $query)) {
			mysqli_stmt_bind_param($stmt, 'ss', $email,$password);
			/* execute statement */
			mysqli_stmt_execute($stmt);
			/* bind result variables */
			mysqli_stmt_bind_result($stmt, $id3);
			$result=mysqli_query($conn,$query);
			/* fetch values */
			while (mysqli_stmt_fetch($stmt)) {
				//echo $id3;
				$id=$id3;
				break;
			}
			/* close statement */
			mysqli_stmt_close($stmt);
		}
		$tag2 = 1;
		$userid=$id;
		$now = time();
		$query = "SELECT count(*) FROM email_code WHERE userid = ? AND code = ? AND exp_time>?";
		if ($stmt = mysqli_prepare($conn, $query)) {
			mysqli_stmt_bind_param($stmt, 'sss',$userid,$code,$now);
			/* execute statement */
			mysqli_stmt_execute($stmt);
			/* bind result variables */
			mysqli_stmt_bind_result($stmt, $total);
			/* fetch values */
			while (mysqli_stmt_fetch($stmt)) {
				if($total==0)
					echo 'no';
				else
				{
					$ttt = 1;
				}
			break;
			}
			/* close statement */
			mysqli_stmt_close($stmt);
		}
		if($ttt == 1)
		{
			$res1 = mysqli_query($conn,"SELECT ip FROM email_ip WHERE userid = '$id' and isverified = 1");
			echo mysqli_error($conn);
			while($row2 = mysqli_fetch_array($res1))
			{
				if($userip=$row2['ip'])
				{
					$tag0 = 1;
					break;
				}
			}
			if($tag0 == 1)
			{
				$res1 = mysqli_query($conn,"UPDATE email_code SET exp_time = 0 WHERE userid ='$userid'");
				echo 'ok';
			}
			else
			{
				function randStr($len) {   
					$chars='ABDEFGHJKLMNPQRSTVWXYabdefghijkmnpqrstvwxy23456789'; // characters to build the password from   
					mt_srand((double)microtime()*1000000*getmypid()); // seed the random number generater (must be done)   
					$password='';   
					while(strlen($password)<$len)   
						$password.=substr($chars,(mt_rand()%strlen($chars)),1);   
					return $password;   
				}  
				$token = randStr(12);
				$res1 = mysqli_query($conn,"INSERT INTO email_ip (userid,ip,token,isverified) VALUES ('$userid','$userip','$token',0)");
				$smtpserver = "smtp.163.com";   
				$smtpserverport = 25; 
				$smtpusermail = "nsnsns@163.com";  
				$smtpuser = "nsnsns";   
				$smtppass = "xxxxx"; 
				$smtp = new Smtp($smtpserver, $smtpserverport, true, $smtpuser, $smtppass); 
				$emailtype = "HTML"; 
				$smtpemailto = $email;   
				$smtpemailfrom = $smtpusermail;   
				$emailsubject = "异地登陆验证";
				$p = base64_encode(file_get_contents('http://bshare.optimix.asia/barCode?site=weixin&url=http://www.13xinan.com/nstest/check.php%3Ftoken='.$token));
				$emailbody = "IP地址：".$userip."用您的账号进行登录，若是您本人操作，请访问(<a href='http://www.13xinan.com/nstest/check.php?token=".$token."'>http://www.13xinan.com/nstest/check.php?token=".$token."</a>) 或扫描二维码进行认证。若非您本人操作，则您的密码很可能已经泄露，请尽快修改密码！<img src='data:image/jpg;base64,".$p."'/>"; 
				$rs = $smtp->sendmail($smtpemailto, $smtpemailfrom, $emailsubject, $emailbody, $emailtype); 
				echo '异地登陆，请登录邮箱核验您的IP地址';
			}
		}
		if($tag2 == 0 )
		{
			echo "<script>alert('邮箱或密码错误或者您的验证码已过期，请重新获取');</script>";
		}
	}
?>
<form method="post">
	<input type="text" id='email' name='email' placeholder="邮箱"> <a style='border:1px solid black' id='button1'>获取验证码</a>
	<div id='code'></div>
	<input type="password" name='password' placeholder="密码"> 
	<input type="text" name='code' placeholder="验证码"> 
	<input type="submit" name="add"  value="提交">
</form>
</body>
</html>