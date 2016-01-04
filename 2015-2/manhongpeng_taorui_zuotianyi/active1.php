<?php
session_start();
$tag = 0;
$dbhost = 'localhost';
$dbuser = 'root';
$dbpass = 'root';
$conn = mysqli_connect($dbhost, $dbuser, $dbpass,"cucyueco_cucyue");
$verify = stripslashes(trim($_GET['verify']));
$nowtime = time(); 
$query = "select id,token_exptime from user_infor where status='0' and  token= ? ";
		if ($stmt = mysqli_prepare($conn, $query)) {
    mysqli_stmt_bind_param($stmt, 's', $verify);
    /* execute statement */
    mysqli_stmt_execute($stmt);

    /* bind result variables */
    mysqli_stmt_bind_result($stmt, $id3,$time3);
    $result=mysqli_query($conn,$query);

    /* fetch values */
    while (mysqli_stmt_fetch($stmt)) {
    	//echo $id3;
    	$tag = 1;
        $id=$id3;
        $time = $time3;
        break;
    }
    
    /* close statement */
    mysqli_stmt_close($stmt);
}
if($tag){
	if($nowtime>$time)
  { //24hour     
  	$msg = '您的激活有效期已过，请登录您的帐号重新发送激活邮件.';   
  }
  else{   
  	mysqli_query($conn,"update user_infor set status=1 where id=".$id);  
  	$msg = 'verify success!';   
  }
}
else{  
	$msg = 'error.';  
} 
echo $msg; 
?>



