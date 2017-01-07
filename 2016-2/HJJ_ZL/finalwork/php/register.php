<?php
/**
 * Created by PhpStorm.
 * User: dell1
 * Date: 2016/7/26
 * Time: 9:05
 */
include ("demo.php");
$a="<br/>";

 if(isset($_POST["submit"]) && $_POST["submit"]=="注册") {
     $user = $_POST["username"];
     $ps = $_POST["password"];
     $va = $_POST["validate"];
     $mobile = $_POST["mobile"];
     $name_allow = '/^[a-zA-Z0-9\x{4e00}-\x{9fa5}]{3,20}$/u';
     $ps_allow = '/^(?!([\d_])+$)(?!([a-zA-Z_]{3,20}+)$)\w+$/';
     $mobile_allow = '/^0?(13|14|15|17|18)[0-9]{9}$/';
     //echo 1;
//禁止输入空值
     if ($user == "" || $ps == "" || $va == "" || $mobile == "") {
         exit('Do not input the invalid value!<a href="javascript:history.back(-1);">back');

     }


     //用户名规范限制
     if (!preg_match($name_allow, $user)) {

         exit('This is an invalid username!<a href="javascript:history.back(-1);">back');
     }
//手机号规范限制
    if (!preg_match($mobile_allow, $mobile)) {

         exit('This is an invalid phone number!<a href="javascript:history.back(-1);">back');
     }
//密码长度限制
     if (strlen($ps) > 10) {
         exit('your password is out of limit!<a href="javascript:history.back(-1);">back');
     }

     //禁止输入弱口令
     if (!preg_match($ps_allow, $ps)) {

         exit('This password is too simple!<a href="javascript:history.back(-1);">back');
     }

     //验证密码
     if ($ps != $va) {
         exit('please input the same password!<a href="javascript:history.back(-1);">back');
     }

     //检查是否存在相同用户名
     $mysql=new mysqli('127.0.0.1','root','123','user');
     if (mysqli_connect_errno($mysql))
     {   echo 'ERROR: could not connect the database';
         exit(1);
     }
     $mysql->query("set names gbk");
//检查是否存在相同用户名
     $check="select users from users where users=?";
     $check_stmt = $mysql->prepare($check);
     $check_stmt->bind_param("s",$user);
     $c = $check_stmt->execute();

     if(!$c){
         die("failed".$check_stmt->error);
         exit();
     }
     if($check_stmt->fetch())
     {   $check_stmt->close();
         exit('The username exits!<a href="javascript:history.back(-1);">back');
     }


     $rand = GetfourStr();
     session_start();
     $_SESSION['user'] = $user;
     $_SESSION['password'] = $ps;
     $_SESSION['mobile'] = $mobile;
     $_SESSION['rand'] = $rand;

     phonecheck($rand,$mobile);
     echo "<script>location.href='../html/mobile check.html';</script>";
 }

//连接数据库

   /*  $mysql=new mysqli('127.0.0.1','root','123','user');
     if (mysqli_connect_errno($mysql))
     {   echo 'ERROR: could not connect the database';
         exit(1);
     }
     mysqli_query("set names 'utf8'");
//检查是否存在相同用户名
     $check=mysqli_query($mysql,"select users from users where users='$user'");
     $result=mysqli_num_rows($check);
     if($result)
     {
         exit('the username exists!<a href="javascript:history.back(-1);">back');
     }
     else
     {

//对用户口令哈希后存储
         $ps_hs = password_hash($ps, PASSWORD_DEFAULT);
         $mysql_insert = "insert into users(users,password)values('$user','$ps_hs')";
         if (!mysqli_query($mysql, $mysql_insert))
         {
             die('ERROR:' . mysqli_error($mysql));
         } else
             {
             echo "用户名为 $user 注册成功";
         }
     }

 }*/
