
                                                   
 参考文献

	免密码登陆的公私钥生成参考文献：Tank的技术博客
	　　ssh-keygen -t rsa
	
	   默认在 ~/.ssh目录生成两个文件：
	    id_rsa      ：私钥
	    id_rsa.pub  ：公钥


	  
	为什么要远程免密码登录 使用 ssh 加地址访问的时候遇到了要求输入密码，输入开机密码不正确的情况，判断是ssh-server有预设密码，但是查不到，所以使用免密码登陆

           
                                   
 实验

          实验环境：kali linux rolling 两台 虚拟机vb 5.0.26版本
          环境预配置 ①在名叫root的虚拟机中安装ssh-client
                       在名叫server的虚拟机中安装ssh-server
                     ②两台虚拟机连接在同一个局域网内，相互可以ping通



          
 一、在client虚拟机中找到以下目录和文件根据文献代码生成密钥

	root@Server:/# cd ~/.ssh/
	root@Server:~/.ssh# ls
	authorized_keys  known_hosts
	
	这是ssh目录下的文件，根据目录下的密钥生成密钥
	root@Server:/etc/ssh# ls
	moduli       ssh_host_ecdsa_key      ssh_host_ed25519_key.pub
	ssh_config   ssh_host_ecdsa_key.pub  ssh_host_rsa_key
	sshd_config  ssh_host_ed25519_key    ssh_host_rsa_key.pub
	root@Server:/etc/ssh# cat authorized_keys
	



           
 二、生成导入进入server虚拟机（复制进server中）
	
	Shell代码 
		    
	cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys  


                  
 三：使用命令打开两台机器的ssh

	
	root@Server:~# sudo service ssh restart

                 
  四：使用ssh ip命令实现远程登录

           ssh远程登录后名称从kali变为server








                     
五、远程登录的验证



	可以由下图看到，确实可以从client虚拟机远程登录访问查询在server虚拟机桌面上的
	Wza文件夹，远程登录成功




下一次实验就是安装ssh蜜罐，诱导client访问蜜罐ssh，并用蜜罐应用查看client的操作记录