<?php

  //$password=123;
$algo=sha256;
$salt=cuc;
$interations=10;

$password = "password";
$iterations = 1;
echo "$password<br/>";
//$hash = hash_pbkdf2("sha256", $password, $salt, $iterations, 20);
echo $password;
// 使用 mcrypt_create_iv() 生成随机初始向量，
// 也可以使用 openssl_random_pseudo_bytes() 或其他适合的随机源。
//$salt = mcrypt_create_iv(16, MCRYPT_DEV_URANDOM);
$salt = paspdapsd;
$hash = hash_pbkdf2("sha256", $password, $salt, $iterations, 20);
echo $hash;
?>
