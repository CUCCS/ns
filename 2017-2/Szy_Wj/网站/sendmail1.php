<?php

	/**
	 * �Ѽ���php7
	 * ע�����ʼ��඼�Ǿ����Ҳ��Գɹ��˵ģ������ҷ����ʼ���ʱ��������ʧ�ܵ����⣬������¼����Ų飺
	 * 1. �û����������Ƿ���ȷ��
	 * 2. ������������Ƿ�������smtp����
	 * 3. �Ƿ���php���������⵼�£�
	 * 4. ��26�е�$smtp->debug = false��Ϊtrue��������ʾ������Ϣ��Ȼ����Ը��Ʊ�����Ϣ��������һ�´����ԭ��
	 * 5. ������ǲ��ܽ�������Է��ʣ�http://www.daixiaorui.com/read/16.html#viewpl
	 *    ����������У���������Ҫ�ҵĴ𰸡�
	 *
	 *
	 * Last update time:2017/06
	 * UPDATE:
	 * 1���滻�˸߰汾��֧�ֵ�д������ereg��ereg_replace.
	 * 2���� var ��Ϊ public/private��.
	 * 3��ʹ�����php7.
	 *
	 */

	require_once "Smtp.class.php";
	function randomkeys($length)
	{
		$pattern = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLOMNOPQRSTUVWXYZ'; //�ַ���
			for($i=0;$i<$length;$i++)
			{
				$key .= $pattern{mt_rand(0,61)}; //����php�����
			}
		return $key;
	}
	$random=randomkeys(6);
	//******************** ������Ϣ ********************************
	$smtpserver = "smtp.126.com";//SMTP������
	$smtpserverport =25;//SMTP�������˿�
	$smtpusermail = "burnymcdull@126.com";//SMTP���������û�����
	$smtpemailto = $_POST['username'];//���͸�˭
	//$smtpemailto ="563038662@qq.com";
	$smtpuser = "burnymcdull@126.com";//SMTP���������û��ʺţ�ע����������ֻ��@ǰ����û���
	$smtppass = "szy19970107";//SMTP���������û�����
	$mailtitle = "���ϴ�����ϵͳ�����һ�";//�ʼ�����
	$mailcontent = "<h1>".$random."</h1>";//�ʼ�����
	$mailtype = "HTML";//�ʼ���ʽ��HTML/TXT��,TXTΪ�ı��ʼ�
	//************************ ������Ϣ ****************************
	include('connect.php');
	$sql="SELECT `E-mail` FROM `user` WHERE `E-mail`='$smtpemailto'";
  $result = mysqli_query($conn, $sql);
  $num=mysqli_num_rows($result);
  if($num){
    //$exist=1;
		$smtp = new Smtp($smtpserver,$smtpserverport,true,$smtpuser,$smtppass);//�������һ��true�Ǳ�ʾʹ�������֤,����ʹ�������֤.
		$smtp->debug = false;//�Ƿ���ʾ���͵ĵ�����Ϣ
		$state = $smtp->sendmail($smtpemailto, $smtpusermail, $mailtitle, $mailcontent, $mailtype);
		$sql = "UPDATE `user` SET `IdetifyCode` = '$random' WHERE `user`.`E-mail` = '$smtpemailto' ";
    mysqli_query($conn, $sql);
    echo"<script>alert('��ϲ���ʼ����ͳɹ�����������֤����֤��');self.location='FindPassword1.html';</script>";
  }
	else{
		echo"<script>alert('�Բ����ʼ�����ʧ�ܣ�����������д�Ƿ�����');self.location='login.html';</script>";
	}
/*
	echo "<div style='width:300px; margin:36px auto;'>";
	if($state==""){
		echo "�Բ����ʼ�����ʧ�ܣ�����������д�Ƿ�����";
		echo "<a href='FindPassword.html'>��˷���</a>";
		exit();
	}
	echo "��ϲ���ʼ����ͳɹ�����";
	echo "<a href='FindPassword1.html'>��˷���</a>";
	echo "</div>";
*/
?>
