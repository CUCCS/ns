
<?php

//方法二，去除所有html标签

strip_tags();

//方法三过滤可能产生代码

function php_sava($str)
{
    $farr = array(
        "/s+/",
        "/<(/?)(script|i?frame|style|html|body|title|link|meta|?|%)([^>]*?)>/isU",
        "/(<[^>]*)on[a-zA-Z]+s*=([^>]*>)/isU",

   );
   $tarr = array(
        " ",
        "＜＞",           //如果要直接清除不安全的标签，这里可以留空
        "",
   );

$str = preg_replace( $farr,$tarr,$str);
   return $str;
}

//php sql防注入代码

class sqlin
{

//dowith_sql($value)
function dowith_sql($str)
{
   $str = str_replace("and","",$str);
   $str = str_replace("execute","",$str);
   $str = str_replace("update","",$str);
   $str = str_replace("count","",$str);
   $str = str_replace("chr","",$str);
   $str = str_replace("mid","",$str);
   $str = str_replace("master","",$str);
   $str = str_replace("truncate","",$str);
   $str = str_replace("char","",$str);
   $str = str_replace("declare","",$str);
   $str = str_replace("select","",$str);
   $str = str_replace("create","",$str);
   $str = str_replace("delete","",$str);
   $str = str_replace("insert","",$str);
   $str = str_replace("'","",$str);
   $str = str_replace("\"","",$str);
   $str = str_replace(" ","",$str);
   $str = str_replace("or","",$str);
   $str = str_replace("=","",$str);
   $str = str_replace("%20","",$str);
   //echo $str;
   return $str;
}
//aticle()防SQL注入函数//php教程
function sqlin()
{
   foreach ($_GET as $key=>$value)
   {
       $_GET[$key]=$this->dowith_sql($value);
   }
   foreach ($_POST as $key=>$value)
   {
       $_POST[$key]=$this->dowith_sql($value);
   }
}
}

$dbsql=new sqlin();
?>
