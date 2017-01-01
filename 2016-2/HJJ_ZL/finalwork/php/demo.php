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
$c ->secretKey = "d5b8c91b28681688021b883db019fbef" ;
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
    );
    $charsLen = count($chars_array) - 1;

    $outputstr = "";
    for ($i=0; $i<4; $i++)
    {
        $outputstr .= $chars_array[mt_rand(0, $charsLen)];
    }
    return $outputstr;
}
