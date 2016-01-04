<?php
$token=$_GET['token'];
$dbhost = 'localhost';
$dbuser = 'xxx';
$dbpass = 'xxx';
$conn = mysqli_connect($dbhost, $dbuser, $dbpass,"xxx");
$flag = 0;
if(! $conn )
{
  die('Could not connect: ' . mysqli_error());
}
$query = "SELECT id,count(*) FROM email_ip WHERE token = ?";
if ($stmt = mysqli_prepare($conn, $query)) {
	mysqli_stmt_bind_param($stmt, 's', $token);
	/* execute statement */
	mysqli_stmt_execute($stmt);
	/* bind result variables */
	mysqli_stmt_bind_result($stmt, $id3,$total3);
	$result=mysqli_query($conn,$query);
	/* fetch values */
	while (mysqli_stmt_fetch($stmt)) {
		//echo $id3;
		$id=$id3;
		$total = $total3;
		break;
	}
	/* close statement */
	mysqli_stmt_close($stmt);
	}
if($total==0)
{
	echo 'no';
}
else{
	$result = mysqli_query($conn,"UPDATE email_ip SET isverified = 1 WHERE id ='$id'");
	echo '您的IP已加入白名单，请重试登录！';
}
?>
