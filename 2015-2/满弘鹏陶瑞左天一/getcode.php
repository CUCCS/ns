
<?php
include_once("smtp.class.php");
$email = $_GET['email'];
$dbhost = 'localhost:3306';
$dbuser = 'root';
$dbpass = 'root';
$conn = @mysql_connect($dbhost, $dbuser, $dbpass);
$flag = 0;
if(! $conn )
{
  die('Could not connect: ' . mysql_error());
}
mysql_select_db("user", $conn);
$result = mysql_query("SELECT id FROM user_infor WHERE email = '$email'");
while($row = mysql_fetch_array($result))
  {
	  $userid=$row['id'];
	  
	$str = strval(rand(0,999999));
	$newStr= sprintf('%06s', $str);
	$e= time()+60*15;
	$tag1=mysql_query("UPDATE email_code SET exp_time = '0' WHERE userid = '$userid'");
	$tag2=mysql_query("INSERT INTO email_code (userid,code,exp_time) VALUES ('$userid','$newStr','$e')");
	if($tag1&&$tag2)
	{
		$smtpserver = "smtp.163.com";   
  $smtpserverport = 25; 
  $smtpusermail = "nstest@163.com";  
  $smtpuser = "nstest";   
  $smtppass = "code"; 
  $smtp = new Smtp($smtpserver, $smtpserverport, true, $smtpuser, $smtppass); 
  $emailtype = "HTML"; 
  $smtpemailto = $email;   
  $smtpemailfrom = $smtpusermail;   
  $emailsubject = "用户帐号激活";
  $emailbody = "您的验证码是".$newStr.",请于15分钟内进行认证。若非本人操作请忽略。【timedia】"; 
  $rs = $smtp->sendmail($smtpemailto, $smtpemailfrom, $emailsubject, $emailbody, $emailtype);   
  if($rs==1){         $msg = 1;     
  }
  else{
  //$msg = $rs;     
  $msg = 0;
  }
	}
	echo $msg;
	break;
  }

?>
