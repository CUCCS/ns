<?php
if(!isset($_POST['submit'])){
      echo"<script>alert('非法访问！');self.location='index.html';</script>";
  }//判断是否有submit操作
  //$exist=0;
  $name=$_POST['usernamesignup'];
  $email=$_POST['emailsignup'];
  $password=$_POST['passwordsignup'];
  $pwd_again=$_POST['passwordsignup_confirm'];

  if(!$password==$pwd_again){
     echo"<script>alert('密码不一致');self.location='login.html';</script>";
  }
  else{
    include('connect.php');//链接数据库
    include('edcrypt.php');
    $sql="SELECT `UserName`, `E-mail` FROM `user` WHERE `UserName`='$name'or `E-mail`='$email'";
    $result = mysqli_query($conn, $sql);
    $num=mysqli_num_rows($result);
    if($num){
      echo"<script>alert('用户名或邮箱已存在');self.location='login.html';</script>";
    }
    else{
      include('IpGet.php');
      $res=openssl_pkey_new(array('private_key_bits' => 512));
      openssl_pkey_export($res, $private_key);
      $public_key=openssl_pkey_get_details($res);
      $public_key=$public_key["key"];
      $salt_name=$name;
      $iterations=1000;
      $private=encrypt($private_key,$password);
      $hash_name = hash_pbkdf2("sha256", $password, $salt_name, $iterations, 20);
      $salt_email=$email;
      $hash_email=hash_pbkdf2("sha256", $password, $salt_email, $iterations, 20);
      $sql = "INSERT INTO `user`(`UserName`, `PassWordByUser`, `E-mail`,`PasswordByEmail`,`Type`,`PublicKey`,`PrivateKey`) VALUES ('$name','$hash_name','$email','$hash_email','0','$public_key','$private')";
      mysqli_query($conn, $sql);
      $ip=getIP();
      $sql_ip="INSERT INTO `IP_Table`(`UserName`, `IP`) VALUES ('$name','$ip')";
      mysqli_query($conn,$sql_ip);
      echo"<script>alert('注册成功！');self.location='index.html';</script>";
    }
    mysqli_close($conn);//关闭数据库
}
?>
