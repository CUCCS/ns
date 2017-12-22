### bro 取证分析

- bro设置

  - 实验环境：

    ![1](image/1.png)

  - 设置bro
    - 提取文件负载
    - 提取FTP登录用户名和密码
    - 忽略校验和错误 

    ![2](image/2.png)

    ![3](image/3.png)

- 数据包分析

  - 数据包分析

    ![4](image/4.png)

  - 查看生成的文件

    ![5](image/5.png)

  - 查看提取的负载文件

    ![6](image/6.png)

  - 将负载文件上传到恶意文件检测平台（virustotal\实验所用机器的预警信息:) ）

    ![11](image/11.png)

    说明负载文件是恶意文件，查看恶意文件的来源

  - 根据文件标识找到会话，根据会话锁定IP

    - 根据files.log定位到会话标识（对应字段的含义可以通过bro官网的文档获得）

    ![7](image/7.png)

    - 根据conn.log文件中的会话表示定位到IP

    ![9](image/9.png)

    - 查看ftp.log

      ![10](image/10.png)

- 事件还原：

  ​	结合wireshark分析，可以知道这是一个先使用shellcode利用被攻击主机，然后通过shellcode执行指令从攻击者ftp上下载恶意软件的攻击过程。
