<?php

if(!isset($_POST['submit'])){
    echo"<script>alert('非法访问！');self.location='login.html';</script>";
  }//判断是否有submit操作

  include('IpGet.php');
  $exist=0;
  $name=$_POST['username'];
  $email=$_POST['username'];
  session_start();
  $password=$_POST['password'];
  include('connect.php');//链接数据库

  $salt=$name;
  $iterations=1000;
  $hash = hash_pbkdf2("sha256", $password, $salt, $iterations, 20);
  $sql="SELECT `UserName`, `PassWordByUser`, `E-mail`,`PasswordByEmail` FROM `user` WHERE (`UserName`='$name'or `E-mail`='$email') and (`PassWordByUser`='$hash' or `PasswordByEmail`='$hash')";
  $sql1="SELECT `UserName` FROM `user` WHERE (`UserName`='$name'or `E-mail`='$email')";
  $result1 = mysqli_query($conn, $sql1);
  $row=$result1->fetch_object();
	$name=$row->UserName;
	//echo $name;
  $result = mysqli_query($conn, $sql);
  $num=mysqli_num_rows($result);
  echo $num;
  if($num){
    $exist=1;
    $_SESSION['name']=$name;
    $_SESSION['psw']=$password;
    echo"<script>alert('登录成功！');self.location='Main.php';</script>";
  }
  else{
  //$algo=sha256;
  echo"<script>alert('用户名或密码错误！');self.location='login.html';</script>";
  }
  mysql_close($conn);//关闭数据库

?>
