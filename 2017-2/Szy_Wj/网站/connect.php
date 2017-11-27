<?php
//主机名
$db_host = 'localhost';
//用户名
$db_user = 'root';
//密码
$db_password = 'root';
//数据库名
$db_name = 'test';
//端口
$db_port = '3306';
//连接数据库
$conn = mysqli_connect($db_host,$db_user,$db_password,$db_name) or die('连接数据库失败！');
  if(!$conn){
    die("can't connect".mysqli_connect_error());//如果链接失败输出错误
  }

  //mysql_select_db('test',$con);//选择数据库（我的是test）
?>
