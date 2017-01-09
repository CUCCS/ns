<?php
/**
 * Created by PhpStorm.
 * User: dell1
 * Date: 2016/12/30
 * Time: 14:23
 */
function phonecheck($code,$mobile){
include ("../mobilesdk/TopSdk.php");
date_default_timezone_set('Asia/Shanghai');
$c = new TopClient;
$c ->appkey = "23584723";
$c ->secretKey = "**********" ;
$req = new AlibabaAliqinFcSmsNumSendRequest;
$req ->setExtend( "" );
$req ->setSmsType( "normal" );
$req ->setSmsFreeSignName( "信息安全2014" );
$req->setSmsParam('{"code":"'. $code .'"}');
$req ->setRecNum( "{$mobile}" );
$req ->setSmsTemplateCode( "SMS_37170038" );
$resp = $c ->execute( $req );
var_dump($resp);
}
function GetfourStr()
{
    $chars_array = array(
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
        "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
        "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G",
        "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
        "S", "T", "U", "V", "W", "X", "Y", "Z",

    );
    $charsLen = count($chars_array) - 1;

    $outputstr = "";
    for ($i=0; $i<4; $i++)
    {
        $outputstr .= $chars_array[mt_rand(0, $charsLen)];
    }
    return $outputstr;
}
