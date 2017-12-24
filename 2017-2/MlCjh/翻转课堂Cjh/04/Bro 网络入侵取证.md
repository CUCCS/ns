## 第四次实验报告· Bro 网络入侵取证

### 实验过程
##### 1. 安装bro
![image](https://raw.githubusercontent.com/CUCfromHY001/ns/HW4-Bro/2017-2/MlCjh/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82Cjh/04/%E5%AE%9E%E9%AA%8C%E6%88%AA%E5%9B%BE/1.PNG)

##### 2.查看实验环境
 
![image](https://raw.githubusercontent.com/CUCfromHY001/ns/HW4-Bro/2017-2/MlCjh/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82Cjh/04/%E5%AE%9E%E9%AA%8C%E6%88%AA%E5%9B%BE/2.PNG)

#### 3.编辑bro配置文件

**编辑 /etc/bro/site/ 目录下的 local.bro，在该文件末尾添加以下代码：**

```
@load frameworks/files/extract-all-files
@load mytuning.bro
```
![image](https://raw.githubusercontent.com/CUCfromHY001/ns/HW4-Bro/2017-2/MlCjh/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82Cjh/04/%E5%AE%9E%E9%AA%8C%E6%88%AA%E5%9B%BE/3.PNG)

**在/etc/bro/site/目录下创建新文件mytuning.bro，内容为**：

```
redef ignore_checksums = T;
```
![image](https://raw.githubusercontent.com/CUCfromHY001/ns/HW4-Bro/2017-2/MlCjh/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82Cjh/04/%E5%AE%9E%E9%AA%8C%E6%88%AA%E5%9B%BE/4.PNG)

#### 4.使用bro分析pcap文件
**使用下面的命令，利用bro自动化分析pcap:**

![image](https://raw.githubusercontent.com/CUCfromHY001/ns/HW4-Bro/2017-2/MlCjh/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82Cjh/04/%E5%AE%9E%E9%AA%8C%E6%88%AA%E5%9B%BE/5.PNG)

**新增2个日志文件，会报告在当前流量（数据包文件）中发现了本地网络IP和该IP关联的已知服务信息**

![image](https://raw.githubusercontent.com/CUCfromHY001/ns/HW4-Bro/2017-2/MlCjh/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82Cjh/04/%E5%AE%9E%E9%AA%8C%E6%88%AA%E5%9B%BE/6.PNG)

**在attack-trace.pcap文件的当前目录下会生成一些.log文件和一个extract_files目录，在该目录下我们会发现有一个文件:**
```
extract-1240198114.648099-FTP_DATA-FHUsSu3rWdP07eRE4l
```
![image](https://raw.githubusercontent.com/CUCfromHY001/ns/HW4-Bro/2017-2/MlCjh/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82Cjh/04/%E5%AE%9E%E9%AA%8C%E6%88%AA%E5%9B%BE/7.PNG)
 

**将该文件上传到virustotal我们会发现匹配了一个历史扫描报告，该报告表明这是一个已知的后门程序:**
![image](https://raw.githubusercontent.com/CUCfromHY001/ns/HW4-Bro/2017-2/MlCjh/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82Cjh/04/%E5%AE%9E%E9%AA%8C%E6%88%AA%E5%9B%BE/8.PNG)

**通过阅读/usr/share/bro/base/files/extract/main.bro的源代码 ， 可以了解到该文件名的最右一个-右侧对应的字符串FHUsSu3rWdP07eRE4l是 files.log 中的文件唯一标识**

![image](https://raw.githubusercontent.com/CUCfromHY001/ns/HW4-Bro/2017-2/MlCjh/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82Cjh/04/%E5%AE%9E%E9%AA%8C%E6%88%AA%E5%9B%BE/9.PNG)

**查看files.log，可以得到，该文件提取自FTP会话，并得到该流量的conn_uids为CbPIE03nLi8TywKtm3**


![image](https://raw.githubusercontent.com/CUCfromHY001/ns/HW4-Bro/2017-2/MlCjh/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82Cjh/04/%E5%AE%9E%E9%AA%8C%E6%88%AA%E5%9B%BE/10.PNG)

**查看conn.log，找到id为CbPIE03nLi8TywKtm3的五元组信息，得到该PE文件来自于IPv4地址为98.114.205.102的主机**

![image](https://raw.githubusercontent.com/CUCfromHY001/ns/HW4-Bro/2017-2/MlCjh/%E7%BF%BB%E8%BD%AC%E8%AF%BE%E5%A0%82Cjh/04/%E5%AE%9E%E9%AA%8C%E6%88%AA%E5%9B%BE/11.PNG)


### 实验完成。
