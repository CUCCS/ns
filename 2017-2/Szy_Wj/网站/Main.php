<?php
//session_start();
if($_SESSION['name']){
  echo"<script>alert('请先登录！');self.location='login.html';;</script>";
}
?>
<!DOCTYPE html>
<!--[if lt IE 7 ]> <html lang="en" class="no-js ie6 lt8"> <![endif]-->
<!--[if IE 7 ]>    <html lang="en" class="no-js ie7 lt8"> <![endif]-->
<!--[if IE 8 ]>    <html lang="en" class="no-js ie8 lt8"> <![endif]-->
<!--[if IE 9 ]>    <html lang="en" class="no-js ie9"> <![endif]-->
<!--[if (gt IE 9)|!(IE)]><!--> <html lang="en" class="no-js"> <!--<![endif]-->
    <head>
        <meta charset="UTF-8" />
        <!-- <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">  -->
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="Login and Registration Form with HTML5 and CSS3" />
        <meta name="keywords" content="html5, css3, form, switch, animation, :target, pseudo-class" />
        <meta name="author" content="Codrops" />
        <link rel="shortcut icon" href="../favicon.ico">
        <link rel="stylesheet" type="text/css" href="css/demo.css" />
        <link rel="stylesheet" type="text/css" href="css/style3.css" />
		<link rel="stylesheet" type="text/css" href="css/animate-custom.css" />
    </head>
    <body>
        <div class="container">
            <!-- Codrops top bar -->
            <div class="codrops-top">

                <span class="right">
                    <a href="Main.php?action=logout">
                        <strong>Log Out</strong>
                    </a>
                </span>
                <div class="clr"></div>
            </div><!--/ Codrops top bar -->
            <header>
                <h1>云上传服务 </h1>
				<nav class="codrops-demos">
					<span>Hi <strong><?php echo $_SESSION['name'];?></strong> WelCome </span>
				</nav>
            </header>
            <section>
                <div id="container_demo" >

                    <div id="wrapper">
                        <div id="login" class="animate form">
						<form  action="Main2.php" autocomplete="on">
                                <p class="">
                                    <input type="submit" value="下载" />
								</p>
						</form>
                            <form  action="Main1.php" autocomplete="on">
                                <p class="">
                                    <input type="submit" value="上传" />
								</p>

                            </form>
                        </div>

                    </div>
                </div>

            </section>
        </div>
    </body>
</html>

<?php
if($_GET['action'] == "logout"){
  unset($_SESSION['name']);
  echo"<script>alert('注销登录成功！');self.location='login.html';</script>";
} ?>
