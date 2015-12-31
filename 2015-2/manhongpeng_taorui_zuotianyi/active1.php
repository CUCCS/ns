<?php
session_start();
$dbhost = 'localhost:3306';
$dbuser = 'root';
$dbpass = 'root';
$conn = @mysql_connect($dbhost, $dbuser, $dbpass);
  $verify = stripslashes(trim($_GET['verify']));
  $nowtime = time(); 
  mysql_select_db("cucyueco_cucyue", $conn);
  $query = mysql_query("select id,token_exptime from user_infor where status='0' and  token='$verify'");
  $row = mysql_fetch_array($query); 
  if($row){  
  if($nowtime>$row['token_exptime'])
  { //24hour     
    $msg = '您的激活有效期已过，请登录您的帐号重新发送激活邮件.';   
	}
	else{   
	mysql_query("update user_infor set status=1 where id=".$row['id']);  
	   
    $msg = 'verify success!';   
	}
	}
	else{  
	$msg = 'error.';  
	} 
	echo $msg; 
?>



