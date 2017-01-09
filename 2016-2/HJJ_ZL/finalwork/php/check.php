<?php
/**
 * Created by PhpStorm.
 * User: dell1
 * Date: 2016/7/27
 * Time: 22:59
 */
$a="<br/>";
    $check=$_POST["check"];
    session_set_cookie_params(60);
    session_start();
    $user = $_SESSION['user'];
    $check_mobile=$_SESSION['rand'];
    $ps=$_SESSION['password'];
    $mobile=$_SESSION['mobile'];
    $check_allow='/^[a-zA-Z0-9]{4}$/u';

     if (!preg_match($check_allow, $check)) {
         exit('please input the valid verification code!<a href="javascript:history.back(-1);">back');
     }



     if ($check_mobile != $check) {
        exit('please input the right verification code!<a href="javascript:history.back(-1);">back');
    }

    else{
        //连接数据库
        $mysql=new mysqli('127.0.0.1','root','123','user');
        $mysql->query("set names gbk");
        if (mysqli_connect_errno($mysql))
        {   echo 'ERROR: could not connect the database';
            exit(1);
        }
        else {

//对用户口令哈希后连同手机号用户名一起存储
            $ps_hs = password_hash($ps, PASSWORD_DEFAULT);

            $sql = "insert into users(users,password,mobile)values(?,?,?)";

            $mysqli_stmt = $mysql->prepare($sql);

            $mysqli_stmt->bind_param("sss",$user,$ps_hs,$mobile);

            $b = $mysqli_stmt->execute();

            if(!$b){
                die("failed".$mysqli_stmt->error);
                exit();
            }else {
                echo "register successfully";
            }



        }
    }


    session_destroy();
echo $a;
echo('Ha ha! Welcome to be a member of my system though there is nothing!');
echo $a;
echo "<input type=\"button\" onclick=\"window.location.href='../html/index.html'\" value=\"return to the home page\">";






