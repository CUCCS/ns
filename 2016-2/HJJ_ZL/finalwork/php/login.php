<?php
/**
 * Created by PhpStorm.
 * User: dell1
 * Date: 2016/7/27
 * Time: 0:22
 */
include ("demo.php");
if(isset($_POST["submit"]) && $_POST["submit"]=="登入")
{
    $user=$_POST["username"];
    $ps=$_POST["password"];
    $name_allow = '/^[a-zA-Z0-9\x{4e00}-\x{9fa5}]{3,20}$/u';
    //echo $user;
    echo "<br/>";
    if (!preg_match($name_allow, $user)) {

        exit('This is an invalid username!<a href="javascript:history.back(-1);">back');
    }
//连接数据库
    $mysql=new mysqli('127.0.0.1','root','123','user');
    if (mysqli_connect_errno($mysql))
    {   echo 'ERROR: could not connect the database';
        exit(1);
    }
    $mysql->query("set names gbk");


    $check_name="select users from users where users=?";
    $check_name_stmt = $mysql->prepare($check_name);
    $check_name_stmt->bind_param("s",$user);
    $c = $check_name_stmt->execute();

    if(!$c){
        die("failed".$check_stmt->error);
        exit();
    }
    if(!$check_name_stmt->fetch())
    {   $check_name_stmt->close();
        exit('Invalid username!Please register at first!<a href="javascript:history.back(-1);">back');
    }else{
        $check_name_stmt->close();
    }


//验证口令哈希值
    $ps_hs = password_hash($ps, PASSWORD_DEFAULT);
    $check_ps="select password from users where users=?";
    $check_ps_stmt = $mysql->prepare($check_ps);
    $check_ps_stmt->bind_param("s",$user);
    $check_ps_stmt->bind_result($password);
    $d = $check_ps_stmt->execute();
    echo $user;
    if(!$d){
        die("failed".$check_ps_stmt->error);
        exit();
    }

    if(!$check_ps_stmt->fetch())
    {
        $check_ps_stmt->close();
        exit('Error!<a href="javascript:history.back(-1);">back');
    }
    else{
        echo $password;
        $verify=$password;
        $check_ps_stmt->close();
    }



//获得该用户手机号
    $phone="select mobile from users where users=?";
    $phone_stmt = $mysql->prepare($phone);
    $phone_stmt->bind_param("s",$user);
    $phone_stmt->bind_result($mob);
    $e = $phone_stmt->execute();

    if(!$e){
        die("failed".$phone_stmt->error);
        exit();
    }
    else{
        while($phone_stmt->fetch()) {

            $mobile = $mob;
            $phone_stmt->close();
        }
    }

    if(password_verify($ps,$verify))
    {

        $rand = GetfourStr();
        mysqli_close($mysql);
        phonecheck($rand,$mobile);
        session_start();
        $_SESSION['user'] = $user;
        $_SESSION['mobile']=$mobile['mobile'];
        $_SESSION['rand'] = $rand;
        echo "<script>location.href='../html/login check.html';</script>";
    }
    else
    {
        exit('Password Error!<a href="javascript:history.back(-1);">back');
    }









}