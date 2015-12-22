
<html>
<head>
<script type="text/javascript" src="http://code.jquery.com/jquery-latest.js"></script>
<script>
$(document).ready(function(){
  $("#button1").click(function(){
    $.get("getcode.php?email="+$("#email").val(), function(data){
		  if(data==0)
		{
			alert("该email未注册");
		} 
		else
		{
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
} elseif(getenv('HTTP_X_FORWARDED_FOR')) { 
$onlineip = getenv('HTTP_X_FORWARDED_FOR'); 
} elseif(getenv('REMOTE_ADDR')) { 
$onlineip = getenv('REMOTE_ADDR'); 
} else { 
$onlineip = $HTTP_SERVER_VARS['REMOTE_ADDR']; 
} 
$userip = $onlineip; 

if(isset($_POST['add']))
{
	$email = $_POST['email'];
	$code = $_POST['code'];
	$password = $_POST['password'];
$dbhost = 'localhost:3306';
$dbuser = 'root';
$dbpass = 'root';
$conn = @mysql_connect($dbhost, $dbuser, $dbpass);
$flag = 0;
$tag0 = 0;
$tag2 = 0;
if(! $conn )
{
  die('Could not connect: ' . mysql_error());
}
mysql_select_db("user", $conn);
$result = mysql_query("SELECT id FROM user_infor WHERE email = '$email' AND password = '$password'");
while($row = mysql_fetch_array($result))
  {
	  $tag2 = 1;
	  $userid=$row['id'];
	
	$now = time();
	$res = mysql_query("SELECT count(*) AS total FROM email_code WHERE userid = '$userid' AND code = '$code'AND exp_time>'$now'");
	while($row1 = mysql_fetch_array($res))
	{
		if($row1['total']==0)
			echo 'no';
		else
		{
			
			$res1 = mysql_query("SELECT ip FROM email_ip WHERE userid = '$userid' and isverified = 1");
			while($row2 = mysql_fetch_array($res1))
			{
				if($userip=$row2['ip'])
				{
					$tag0 = 1;
					break;
				}
			}
			if($tag0 == 1)
			{
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
	$res1 = mysql_query("INSERT INTO email_ip (userid,ip,token,isverified) VALUES ('$userid','$userip','$token',0)");
  $smtpserver = "smtp.163.com";   
  $smtpserverport = 25; 
  $smtpusermail = "nstest@163.com";  
  $smtpuser = "nstest";   
  $smtppass = "code"; 
  $smtp = new Smtp($smtpserver, $smtpserverport, true, $smtpuser, $smtppass); 
  $emailtype = "HTML"; 
  $smtpemailto = $email;   
  $smtpemailfrom = $smtpusermail;   
  $emailsubject = "异地登陆验证";
  $emailbody = "IP地址：".$userip."用您的账号进行登录，若是您本人操作，请访问(http://localhost/cucyue/check.php?token=".$token.") 进行认证。若非您本人操作，则您的密码很可能已经泄露，请尽快修改密码！"; 
  $rs = $smtp->sendmail($smtpemailto, $smtpemailfrom, $emailsubject, $emailbody, $emailtype); 
				echo '异地登陆，请登录邮箱核验您的IP地址';
			}
		}
	}
	
	break;
  }
  if($tag2 == 0 )
  {
	  echo "<script>alert('邮箱或密码错误');</script>";
  }
}
?>

<form method="post">
<input type="text" id='email' name='email' placeholder="邮箱"> <a style='border:1px solid black' id='button1'>获取验证码</a>
<div id='code'></div>
<input type="text" name='password' placeholder="密码"> 
<input type="text" name='code' placeholder="验证码"> 
<input type="submit" name="add"  value="提交">
</form>

</body>
</html>