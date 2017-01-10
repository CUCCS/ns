# Metasploit学习    
  
##  metasploit的一些插件和辅助模块  
  
  
### **可利用插件**  
> load wmap装载wmap插件  
> wmap_targets 数据库中的对象  
> (-h帮助-r重载目标表-a对象-p打印目标-s id选择目标)  
> wmap_attack   爬行和测试  
> wmap_crawl    爬行网站  
> wmap_proxy    运行中间人代理  
> wmap_run      自动匹配漏洞  
> (-h帮助-t显示匹配的开发模块-e发动匹配的检查模块)  
> wmap_sql      查询数据库  
> wmap_website  列出网站结构  
> wmap_reports  报告  
> (-h帮助-p打印报告-s id file显示报告-x id file显示xml)  
> load nexpose装载nexpose，调用nexpose服务器工作  
> nexpose_activity    显示有nexpose的实例  
> nexpose_connect     连接NeXpose服务器(user:pass@host[:port])  
> nexpose_disconnect  断开NeXpose服务器  
> nexpose_discover    执行低调扫描  
> nexpose_dos         执行服务和设备的扫描(高调)  
> nexpose_exhaustive  扫描全部tcp断开  
> nexpose_scan        对导入的范围进行特定扫描  
> load nessus装载nessus  
> nessus_connect             连接nessus服务器  
> nessus_save                保存nessus登录信息会话  
> nessus_logout              退出nessus服务器    
> nessus_help                列出nessus命令    
> nessus_server_status       检查Nessus服务器的状态   
> nessus_admin               检测用户是否是管理员   
> nessus_server_feed         Nessus提供的类型   
> nessus_find_targets        在报告中找一个攻击目标(有漏洞)   
> nessus_server_prefs        显示服务器控制台                                 
> nessus_report_list         列出Nessus报告   
> nessus_report_get          导入另一个nessus服务器的报告   
> nessus_report_hosts        列出主机的报告   
> nessus_report_host_ports   列出主机开放的端口报告    
> nessus_report_host_detail  列出一个主机的详细的报告                                 
> nessus_scan_new            创建一个Nessus的扫描    
> nessus_scan_status         列出全部Nessus扫描状态  
> nessus_scan_pause          暂停一个Nessus扫描  
> nessus_scan_pause_all      暂停全部Nessus扫描  
> nessus_scan_stop           停止一个Nessus扫描  
> nessus_scan_stop_all       停止全部Nessus扫描  
> nessus_scan_resume         重新开始一个Nessus扫描  
> nessus_scan_resume_all     重新开始全部Nessus扫描                          
> nessus_plugin_list         列出全部插件  
> nessus_plugin_family       列出一个插件家族  
> nessus_plugin_details      列出一个特定插件                         
> nessus_user_list           显示Nessus用户  
> nessus_user_add            添加一个Nessus用户  
> nessus_user_del            删除一个Nessus用户  
> nessus_user_passwd         改变Nessus用户的密码                             
> nessus_policy_list         列出全部策略  
> nessus_policy_del          删除一个策略  
> 端口扫描auxiliary/scanner/portscan  
> scanner/portscan/ack        ACK防火墙扫描  
> scanner/portscan/ftpbounce  FTP跳端口扫描  
> scanner/portscan/syn        SYN端口扫描  
> scanner/portscan/tcp        TCP端口扫描  
> scanner/portscan/xmas       TCP"XMas"端口扫描  
> use sniffer使用sniffer抓包。  
> sniffer_dump保存抓的包。  
> sniffer_interfaces设置网卡  
> sniffer_start开始抓包  
> sniffer_stop停止抓包  
> sniffer_stats显示状态   
> persistence持久服务注入注册表。  
> use exploit/multi/handler  
> set PAYLOAD windows/meterpreter/reverse_tcp  
> metsvc后门  http://www.phreedom.org/software/metsvc/  
> use exploit/multi/handler  
> set PAYLOAD windows/metsvc_bind_tcp     
     
     
  
### **下面是一部分辅助模块**  
  
> dhcprpc扫描  
> 查询系统终结点映射器远程服务auxiliary/scanner/dcerpc/endpoint_mapper   
> 隐藏扫描收集rpc匿名访问auxiliary/scanner/dcerpc/hidden   
> 扫描rpc服务器信息auxiliary/scanner/dcerpc/management   
> 扫描范围确定DCERPC服务通过的TCP端口auxiliary/scanner/dcerpc/tcp_dcerpc_auditor  
> smb扫描  
> smb枚举auxiliary/scanner/smb/smb_enumusers  
> 返回DCERPC信息auxiliary/scanner/smb/pipe_dcerpc_auditor  
> 扫描SMB2协议auxiliary/scanner/smb/smb2  
> 扫描smb共享文件auxiliary/scanner/smb/smb_enumshares  
> 枚举系统上的用户auxiliary/scanner/smb/smb_enumusers  
> SMB登录auxiliary/scanner/smb/smb_login  
> SMB登录use windows/smb/psexec(通过md5值登录)  
> 扫描组的用户auxiliary/scanner/smb/smb_lookupsid  
> 扫描系统版本auxiliary/scanner/smb/smb_version  
> 空闲增量扫描auxiliary/scanner/ip/ipidseq  
> mssql扫描(端口tcp1433udp1434)  
> admin/mssql/mssql_enum     MSSQL枚举  
> admin/mssql/mssql_exec     MSSQL执行命令  
> admin/mssql/mssql_sql      MSSQL查询  
> scanner/mssql/mssql_login  MSSQL登陆工具  
> scanner/mssql/mssql_ping   测试MSSQL的存在和信息  
> smtp扫描  
> smtp枚举auxiliary/scanner/smtp/smtp_enum   
> 扫描smtp版本auxiliary/scanner/smtp/smtp_version  
> snmp扫描  
> 通过snmp扫描设备auxiliary/scanner/snmp/community  
> ssh扫描  
> ssh登录auxiliary/scanner/ssh/ssh_login  
> ssh公共密钥认证登录auxiliary/scanner/ssh/ssh_login_pubkey  
> 扫描ssh版本测试auxiliary/scanner/ssh/ssh_version  
> telnet扫描  
> telnet登录auxiliary/scanner/telnet/telnet_login   
> 扫描telnet版本auxiliary/scanner/telnet/telnet_version  
> tftp扫描  
> 扫描tftp的文件auxiliary/scanner/tftp/tftpbrute  
> ARP扫描auxiliary/scanner/discovery/arp_sweep  
> IPv6的邻居发现auxiliary/scanner/discovery/ipv6_neighbor  
> 扫描UDP服务的主机auxiliary/scanner/discovery/udp_probe  
> 检测常用的UDP服务auxiliary/scanner/discovery/udp_sweep  
> ftp版本扫描scanner/ftp/anonymous  
> sniffer密码auxiliary/sniffer/psnuffle  
> snmp扫描scanner/snmp/community  
> vnc扫描无认证扫描scanner/vnc/vnc_none_auth  
> 扫描X服务器scanner/x11/open_x11  
> php攻击exploit/unix/webapp/php_include  
> 指定攻击浏览器server/browser_autopwn    



 转载自：[www.metasploit.cn](www.metasploit.cn)



  

     
      
