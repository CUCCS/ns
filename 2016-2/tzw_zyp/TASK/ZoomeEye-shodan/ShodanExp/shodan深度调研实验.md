## Shodan深度调研实验
### Shodan与Maltego工具结合进行攻击准备
* Maltego：
	* Maltego是一套网络情报与侦察应用工具，可以清楚呈现网络环境中的威胁关系图像的平台，它可以将网络架构中的单个实体的所有关系完整的展现出来，根据我们前面的介绍，可想而知，与shodan的结合更是锦上添花。
		* ![]("1.PNG")
* 实验步骤：
	* 1.在kali中打开Metasploit framework。(注意的是使用metasploit之前要先安装启动postgresql，确保端口处于listening状态，然后启动metasploit服务，再启动msfconsole才是如图所示，还可以使用db_status检验一下数据库的连通性)
		* ![]("2.PNG")
	* 2.在命令行中输入show auxiliary
		* ![]("3.PNG")
	* 3.使用 auxiliary/gather/Shodansearch 模块,可以用show options命令来查看模块需要的参数
		* ![]("4.PNG")
		* ![]("5.PNG")
	* 4.我们需要指定iis来搜索iis服务器，还需要登陆Shodan账户后得到的API key。现在我们可以用Run command 登录。
		* ![]("6.PNG")
		* 一般来说 auxiliary/gather/Shodan_search模块通过API向数据库查询前50个ip 地址。50个ip地址的限制可以通过购买无限制API key来扩大到查询10000个ip地址
