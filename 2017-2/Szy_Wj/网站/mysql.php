<?php
    //主机名
    $db_host = 'localhost';
    //用户名
    $db_user = 'root';
    //密码
    $db_password = 'wasdWJ0315';
    //数据库名
    $db_name = 'User';
    //端口
    $db_port = '3306';
    //连接数据库
    $conn = mysqli_connect($db_host,$db_user,$db_password,$db_name) or die('连接数据库失败！');

    //选择数据库
    mysqli_select_db($conn, $db_name) or die('选择数据库失败！');
    $result = mysqli_query($conn, "SELECT * FROM user");

    //处理返回的数据集
    $data = [];
    while($row = mysqli_fetch_assoc($result)) {//mysqli_fetch_array
        $data[] = $row;
    }

    //在页面上打印
    var_dump($data);
    $sql = "INSERT INTO `user`(`UserName`, `PassWord`, `E-mail`) VALUES ($name,$password,$email)";
    //mysqli_query($conn,"INSERT INTO user(UserName, PassWord, E-mail) VALUES ('1','2','3')");
    mysqli_query($conn,"INSERT INTO `user`(`UserName`, `PassWord`, `E-mail`) VALUES ('$name','$password','$email')");
    if (!mysqli_query($conn,$sql))

   {

   die('Error: ' . mysqli_error());

    }



  //关闭连接

    //查询数据库
?>
