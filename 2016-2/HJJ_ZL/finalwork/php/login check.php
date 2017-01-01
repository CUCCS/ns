<?php
/**
 * Created by PhpStorm.
 * User: dell1
 * Date: 2017/1/1
 * Time: 23:22
 */
$a="<br/>";
$check=$_POST["check"];
session_start();
$user = $_SESSION['user'];
$check_mobile=$_SESSION['rand'];
$mobile=$_SESSION['mobile'];

if ($check_mobile != $check) {
    exit('please input the right verification code!<a href="javascript:history.back(-1);">back');
}
else
    {

        echo ('WELCOME TO BACK ! ');
        echo $user;
        echo $a;
        echo('Ha ha!This is my lovely system though there is nothing!');
        echo $a;
        session_destroy();
        echo "<input type=\"button\" onclick=\"window.location.href='system.php'\" value=\"go into the system\">";

    }