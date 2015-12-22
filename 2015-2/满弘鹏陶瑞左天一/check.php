<?php
$token=$_GET['token'];
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

$result = mysql_query("SELECT id,count(*) AS total FROM email_ip WHERE token ='$token'");
echo mysql_error();
while($row = mysql_fetch_array($result))
  {
	  if($row['total']==0)
	  {
		  echo 'no';
		  break;
	  }
	  else{
		  	  $id=$row['id'];
				$result = mysql_query("UPDATE email_ip SET isverified = 1 WHERE id ='$id'");
				echo 'ok';
	break;
	  }

  }
?>
