<?php	 
	//session_start();
    //require_once "procedure.php";
    //$domain=$_SESSIONw['d'];
	$domain=$_GET['domain'];
	$x = shell_exec('python dns-resolve.py '.$domain);   
	echo $x;		
?>
