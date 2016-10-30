#SSH蜜罐实验准备

##设置远程登录

###实验环境



- 实验环境：kali linux rolling 两台 虚拟机vb 5.0.26版本

- 环境预配置 ：     
        ①在名叫root的虚拟机中安装ssh-client
         在名叫server的虚拟机中安装ssh-server
                     
      ②两台虚拟机连接在同一个局域网内，相互可以ping通，网络连接设置为NAT
###具体过程
- 在client虚拟机中找到以下目录和文件根据文献代码生成密钥
   

    `root@Server:/# cd ~/.ssh/`

     root@Server:~/.ssh# ls

    `authorized_keys  known_hosts``
- 生成导入进入server虚拟机（复制进server中）
Shell代码 

    ` cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys  `

- 打开两台机器的ssh

    `root@Server:~# sudo service ssh restart`
- 使用ssh ip命令实现远程登录

     ssh远程登录后名称从kali变为server
- 远程登录的验证
- 嗯，前期准备大概就是这些啦
