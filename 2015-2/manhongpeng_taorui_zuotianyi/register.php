<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8" />
	<title>CUC约</title>
	<link rel="stylesheet" type="text/css" href="css/style.css" />
	<link rel="stylesheet" type="text/css" href="css/cs-select.css" />
	<link rel="stylesheet" type="text/css" href="css/cs-skin-rotate.css" />
	<script src="js/modernizr.custom.63321.js"></script>
	<style>	
		body {
			background: #7f9b4e url(images/bg2.jpg) no-repeat center top;
			-webkit-background-size: cover;
			-moz-background-size: cover;
			background-size: cover;
			}
		.container > header h1,
	</style>
</head>
<body>
	<?php
		error_reporting(E_ALL ^ E_DEPRECATED);
		include_once("smtp.class.php");
		if(isset($_POST['add']))
		{
			@session_start();
			$dbhost = 'localhost';
			$dbuser = 'root';
			$dbpass = 'root';
			$conn = mysqli_connect($dbhost, $dbuser, $dbpass,"cucyueco_cucyue");
			$flag = 0;
			if(! $conn )
			{
				die('Could not connect: ' . mysqli_error());
			}
			if(! get_magic_quotes_gpc() )
			{
			//$id = addslashes ($_POST['id']);
				$username = addslashes ($_POST['username']);
			}
			else
			{
			//$id = $_POST['id'];
				$username = $_POST['username'];
			}
			$chknumber = $_POST['chknumber'];
			$password = trim($_POST['password']);
			$email = trim($_POST['email']);
			$regtime = time(); 
			$token = md5($username.$password.$regtime); //创建用于激活识别码
			$token_exptime = time()+60*60*24;//过期时间为24小时后 
			//$ritnumber = $_SESSION['randcode'];
			if($_SESSION['randcode'] == $chknumber)
			{
				$query = "SELECT id FROM user_infor WHERE email = ?";
				if ($stmt = mysqli_prepare($conn, $query)) {
					mysqli_stmt_bind_param($stmt, 's', $email);
					/* execute statement */
					mysqli_stmt_execute($stmt);
					/* bind
					result variables */
					mysqli_stmt_bind_result($stmt, $id1);
					$result=mysqli_query($conn,$query);
					/* fetch values */
					while (mysqli_stmt_fetch($stmt)) {
			        echo "<script> alert('该邮箱已被注册，请重新输入！');parent.location.href='./register.php'; </script>"; 
					$flag = 1;
					break;
					}
					/* close statement */
					mysqli_stmt_close($stmt);
				}
				if($flag == 0){
					$date = date('Y-m-d');
					$sql = "INSERT INTO user_infor ".
					"(username,password,email,token,token_exptime,regtime) ".
					"VALUES ".
					"(?,?,?,?,?,?)";
					if ($stmt = mysqli_prepare($conn, $sql)) {
						mysqli_stmt_bind_param($stmt, 'ssssss', $username,$password,$email,$token,$token_exptime,$regtime);
						/* execute statement */
						mysqli_stmt_execute($stmt);
						$result=mysqli_query($conn,$sql);
						echo $result;
						/* close statement */
						mysqli_stmt_close($stmt);
					}
					//"('$username','$password','$email','$token','$token_exptime','$regtime')";
					//mysqli_query($conn,$sql);
					$smtpserver = "smtp.163.com";   
					$smtpserverport = 25; 
					$smtpusermail = "test@163.com";  
					$smtpuser = "testuser";   
					$smtppass = "testpass"; 
					$smtp = new Smtp($smtpserver, $smtpserverport, true, $smtpuser, $smtppass); 
					$emailtype = "HTML"; 
					$smtpemailto = $email;   
					$smtpemailfrom = $smtpusermail;   
					$emailsubject = "用户帐号激活";
					$emailbody = "亲爱的".$username."：<br/>感谢您在我站注册了新帐号。<br/>请点击链接激活您的帐号。<br/>   
						<a href='http://www.13xinan.com/nstest/active1.php?verify=".$token."' target= '_blank'>http://www.13xinan.com/nstest/active1.php?verify=".$token."</a><br/>  
						如果以上链接无法点击，请将它复制到你的浏览器地址栏中进入访问，该链接24小时内有效。"; 
					$rs = $smtp->sendmail($smtpemailto, $smtpemailfrom, $emailsubject, $emailbody, $emailtype);   
					if($rs==1){         
						$msg = '恭喜您，注册成功！<br/>请登录到您的邮箱及时激活您的帐号！';     
					}
					else{     
						$msg = '邮箱输入有误或网络错误！';     
					} 
					echo $msg; 
				}
			}
			if($_SESSION['randcode'] != $chknumber){
				echo "<script> alert('验证码错误，请重新输入！');parent.location.href='./register.php'; </script>"; 
				session_unset();
			}
		}
	?>
	<div class="container">
	<div class="codrops-top">
	<a href="http://www.cucyue.com/#">
		<strong>&laquo;BACK</strong>
	</a>
	</div>
	<header>
		<h1>CUC <strong>yue</strong></h1>
		<div class="support-note">
			<span class="note-ie">Sorry, only modern browsers.</span>
		</div>
	</header>
	<section class="main">
		<form class="form-4" method="post">
			<h1>Sign&nbsp;in</h1>
			<p>
				<label for="text">Email</label>
				<input type="text" name='email' placeholder="邮箱" required> 
			</p>
			<p>
				<label for="login">Username</label>
				<input type="text" name="username" placeholder="用户名" required>
			</p>
			<p>
				<label for="password">Password</label>
				<input type="password" name='password' placeholder="密码" required> 
			</p>
		<script src="js/classie.js"></script>
		<script src="js/selectFx.js"></script>
		<script>
		(function () {
			[].slice.call(document.querySelectorAll('select.cs-select')).forEach(function (el) {
				new SelectFx(el);
			});
		})();
		</script>
		<p>&nbsp;</p>
		<p>&nbsp;</p>
		p>&nbsp;</p>   
		<SCRIPT LANGUAGE="JavaScript">
		function reloadcode() {
			var d = new Date();
			document.getElementById('safecode').src = "code.php?t=" + d.toTimeString()
		}
		</SCRIPT>
		<!--<input name="chknumber" type="text" maxlength="4" class="chknumber_input" value="验证码"/>-->
		<input type="text" name='chknumber' placeholder="验证码" maxlength="4"required> 
		<img src='code.php' id="safecode" onclick="reloadcode()" title="看不清楚?点击切换!">
		</img>
		<br><br>
		<p>
			<input type="submit" name="add"  value="创建">
		</p>       
		</form>​
	</section>
	</div>
</body>
</html>

