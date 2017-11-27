<?php
if(!isset($_POST['submit'])){
      echo"<script>alert('非法访问！');self.location='login.html';</script>";
  }//判断是否有submit操作
  //$exist=0;
  $name=$_POST['username'];
  $code=$_POST['code'];
  session_start();
  include('connect.php');//链接数据库
  $sql="SELECT `UserName` FROM `user` WHERE (`UserName`='$name' or `E-mail`='$name') AND `IdetifyCode`='$code' ";
  $result = mysqli_query($conn, $sql);
  $num=mysqli_num_rows($result);
  if($num){
    //$exist=1;
    $_SESSION['name']=$name;
    echo"<script>alert('验证成功');self.location='resettingpsword1.php';</script>";
  }
  else{
	 echo"<script>alert('验证码不一致');self.location='Find.html';</script>";
   
  }
  mysqli_close($conn);//关闭数据库



?>
