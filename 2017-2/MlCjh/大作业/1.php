<?php
//$action=$_GET['action'];    
//echo "document.write('".$action."');n";   

$link = mysqli_connect(
    'localhost',  /* The host to connect to 连接MySQL地址 */
    'root',     /* The user to connect as 连接MySQL用户名 */
    '12345678', /* The password to use 连接MySQL密码 */
    'news');    /* The default database to query 连接数据库名称*/
//连接数据库
if (!$link)
{
    printf("Can't connect to MySQL Server. Errorcode: %s ", mysqli_connect_error());
    exit;
}
$classname = $_GET['Class'];

$sql="SELECT * FROM `news_table` WHERE Class='$classname'";
$rst=$link->query($sql);

if ($rst) {
    // 输出数据
    while($row = $rst->fetch_assoc()) {
        printf($row["Title"]);
    }
} else {
    echo "0 结果";
}
?>