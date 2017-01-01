<?php
/**
 * Created by PhpStorm.
 * User: dell1
 * Date: 2016/7/27
 * Time: 22:59
 */
$a="<br/>";
    $check=$_POST["check"];
    session_start();
    $user = $_SESSION['user'];
    $check_mobile=$_SESSION['rand'];
    $ps=$_SESSION['password'];
    $mobile=$_SESSION['mobile'];

    if ($check_mobile != $check) {
        exit('please input the right verification code!<a href="javascript:history.back(-1);">back');
    }

    else{
        //连接数据库
        $mysql=new mysqli('127.0.0.1','root','123','user');
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

//对用户口令哈希后连同手机号用户名一起存储
            $ps_hs = password_hash($ps, PASSWORD_DEFAULT);
            $mysql_insert = "insert into users(users,password,mobile)values('$user','$ps_hs','$mobile')";
            if (!mysqli_query($mysql, $mysql_insert))
            {
                die('ERROR:' . mysqli_error($mysql));
            } else
            {
                echo "THE USER $user REGISTER SUCCESSFULLY!'";
                echo $a;
            }

        }
    }
    session_destroy();
echo $a;
echo('Ha ha! Welcome to be a member of my system though there is nothing!');
echo $a;
echo "<input type=\"button\" onclick=\"window.location.href='../html/index.html'\" value=\"return to the home page\">";






