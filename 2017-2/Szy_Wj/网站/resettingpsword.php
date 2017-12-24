<?php
if(!isset($_POST['submit'])){
      echo"<script>alert('非法访问！');self.location='login.html';</script>";
  }//判断是否有submit操作

  //$exist=0;
  //$name=$_POST['usernamesignup'];
  //$email=$_POST['emailsignup'];
  //$name="login";
  //$email="logi@qq.com";
  //$password="login";
  session_start();
  $password=$_POST['passwordsignup'];
  $pwd_again=$_POST['passwordsignup_confirm'];
  $hi= $_SESSION['name'];
  echo $hi;
  if(!$password==$pwd_again){
     echo"<script>alert('密码不一致');self.location='login.html';</script>";
  }
  else{
  include('connect.php');//链接数据库
  $sql="SELECT `UserName`, `E-mail` FROM `user` WHERE `UserName`='$hi'or `E-mail`='$hi'";
  $result = mysqli_query($conn, $sql);
  $num=mysqli_num_rows($result);
	$sql1="SELECT `UserName` FROM `user` WHERE (`UserName`='$hi'or `E-mail`='$hi')";
  $result1 = mysqli_query($conn, $sql1);
$row=$result1->fetch_object();
	$name=$row->UserName;
echo $name;
$sql2="SELECT `E-mail` FROM `user` WHERE (`UserName`='$hi'or `E-mail`='$hi')";
  $result2 = mysqli_query($conn, $sql1);
$row=$result2->fetch_object();
	$email=$row->E-mail;
  if($num){
    //$exist=1;
    //$algo=sha256;
    $salt_name=$name;
    $iterations=1000;
    $hash_name = hash_pbkdf2("sha256", $password, $salt_name, $iterations, 20);
    $salt_email=$email;
    $hash_email=hash_pbkdf2("sha256", $password, $salt_email, $iterations, 20);
    $sql = "UPDATE `user` SET `PasswordByUser` = '$hash_name',`PasswordByEmail` = '$hash_email' WHERE `UserName`='$name'";
    mysqli_query($conn, $sql);
    echo"<script>alert('注册成功！');self.location='login.html';</script>";
  }
}
  mysqli_close($conn);//关闭数据库


?>
