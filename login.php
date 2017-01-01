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
    //echo $user;
    echo "<br/>";

//连接数据库
    $mysql=new mysqli('127.0.0.1','root','123','user');
    if (mysqli_connect_errno($mysql))
    {   echo 'ERROR: could not connect the database';
        exit(1);
    }
    //mysqli_query("set names 'utf8'");
    /*else
    {
        echo 30;
    }*/
 //匹配用户名
    $check=mysqli_query($mysql,"select users from users where users='$user'");
    $result=mysqli_fetch_array($check);

    if (!$result)
    {
        exit('Invalid username!Please register at first!<a href="javascript:history.back(-1);">back');
    }
//验证口令哈希值
    $ps_hs = password_hash($ps, PASSWORD_DEFAULT);
    $ps_hs_db=mysqli_query($mysql,"select password from users where users='$user'");
    $verify=mysqli_fetch_array($ps_hs_db);
    //echo $verify[0];
    //echo $ps_hs;
//获得该用户手机号
    $mob=mysqli_query($mysql,"select mobile from users where users='$user'");
    $mobile=mysqli_fetch_array($mob);
    //echo $mobile['mobile'];
    if(password_verify($ps,$verify[0]))
    {
        $rand = GetfourStr();
        mysqli_close($mysql);
        phonecheck($rand,$mobile['mobile']);
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