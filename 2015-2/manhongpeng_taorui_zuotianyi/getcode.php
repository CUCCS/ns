<?php
include_once("smtp.class.php");
$tag = 0;;
$email = $_GET['email'];
$dbhost = 'localhost';
$dbuser = 'xxx';
$dbpass = 'xxx';
$conn = mysqli_connect($dbhost, $dbuser, $dbpass,"xxx");
if(! $conn )
{
  die('Could not connect: ' . mysqli_error());
}
$query = "SELECT id FROM user_infor WHERE email = ?";
if ($stmt = mysqli_prepare($conn, $query)) {
	mysqli_stmt_bind_param($stmt, 's', $email);
	/* execute statement */
	mysqli_stmt_execute($stmt);
	/* bind result variables */
	mysqli_stmt_bind_result($stmt, $id3);
	$result=mysqli_query($conn,$query);
	/* fetch values */
	while (mysqli_stmt_fetch($stmt)) {
		//echo $id3;
		$tag = 1;
		$id=$id3;
		break;
	}
	/* close statement */
	mysqli_stmt_close($stmt);
}
if($tag)
{
	$userid=$id;
	$str = strval(rand(0,999999));
	$newStr= sprintf('%06s', $str);
	$e= time()+60*15;
	$tag1=mysqli_query($conn,"UPDATE email_code SET exp_time = '0' WHERE userid = '$userid'");
	$tag2=mysqli_query($conn,"INSERT INTO email_code (userid,code,exp_time) VALUES ('$userid','$newStr','$e')");
	if($tag1&&$tag2)
	{
		$smtpserver = "smtp.163.com";   
		$smtpserverport = 25; 
		$smtpusermail = "nsnsns@163.com";  
		$smtpuser = "nsnsns";   
		$smtppass = "xxx"; 
		$smtp = new Smtp($smtpserver, $smtpserverport, true, $smtpuser, $smtppass); 
		$emailtype = "HTML"; 
		$smtpemailto = $email;   
		$smtpemailfrom = $smtpusermail;   
		$emailsubject = "用户帐号激活";
		$emailbody = "您的验证码是".$newStr.",请于15分钟内进行认证。若非本人操作请忽略。【timedia】"; 
		$rs = $smtp->sendmail($smtpemailto, $smtpemailfrom, $emailsubject, $emailbody, $emailtype);   
		if($rs==1){         
			$msg = 1;     
		}
		else{
			$msg = 0;
		}
	}
	echo $msg;
}
?>
