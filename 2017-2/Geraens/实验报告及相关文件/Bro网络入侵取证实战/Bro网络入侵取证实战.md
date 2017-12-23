Bro网络入侵取证实战
===============================

## 1.实验环境(已安装Bro)

![](https://raw.githubusercontent.com/Geraens/ns/2fc8b5c46e01758cdf57c1131a9b3a82cbd5a98e/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/Bro%E7%BD%91%E7%BB%9C%E5%85%A5%E4%BE%B5%E5%8F%96%E8%AF%81%E5%AE%9E%E6%88%98/bro%E5%AE%9E%E9%AA%8C%E6%88%AA%E5%9B%BE/%E7%B3%BB%E7%BB%9F%E4%BF%A1%E6%81%AF.png)


## 2.修改local.Bro

![](https://raw.githubusercontent.com/Geraens/ns/2fc8b5c46e01758cdf57c1131a9b3a82cbd5a98e/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/Bro%E7%BD%91%E7%BB%9C%E5%85%A5%E4%BE%B5%E5%8F%96%E8%AF%81%E5%AE%9E%E6%88%98/bro%E5%AE%9E%E9%AA%8C%E6%88%AA%E5%9B%BE/%E4%BF%AE%E6%94%B9local.bro.png)


## 3.在/etc/bro/site 下新建文件 mytuning.bro,编辑：

![](https://raw.githubusercontent.com/Geraens/ns/2fc8b5c46e01758cdf57c1131a9b3a82cbd5a98e/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/Bro%E7%BD%91%E7%BB%9C%E5%85%A5%E4%BE%B5%E5%8F%96%E8%AF%81%E5%AE%9E%E6%88%98/bro%E5%AE%9E%E9%AA%8C%E6%88%AA%E5%9B%BE/%E6%96%B0%E5%BB%BAmytuning.bro.png)

## 4.获取待分析的pcap包

![](https://raw.githubusercontent.com/Geraens/ns/2fc8b5c46e01758cdf57c1131a9b3a82cbd5a98e/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/Bro%E7%BD%91%E7%BB%9C%E5%85%A5%E4%BE%B5%E5%8F%96%E8%AF%81%E5%AE%9E%E6%88%98/bro%E5%AE%9E%E9%AA%8C%E6%88%AA%E5%9B%BE/%E8%8E%B7%E5%8F%96pcap%E5%8C%85.png)

## 5.使用bro自动分析pcap包：

![](https://raw.githubusercontent.com/Geraens/ns/2fc8b5c46e01758cdf57c1131a9b3a82cbd5a98e/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/Bro%E7%BD%91%E7%BB%9C%E5%85%A5%E4%BE%B5%E5%8F%96%E8%AF%81%E5%AE%9E%E6%88%98/bro%E5%AE%9E%E9%AA%8C%E6%88%AA%E5%9B%BE/%E5%88%86%E6%9E%90pcap.png)

## 6.在mytuning.bro添加 redef Site::local_nets ={192.150.11.0/24} 解决警告信息


## 7.再次分析pcap包

![](https://raw.githubusercontent.com/Geraens/ns/2fc8b5c46e01758cdf57c1131a9b3a82cbd5a98e/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/Bro%E7%BD%91%E7%BB%9C%E5%85%A5%E4%BE%B5%E5%8F%96%E8%AF%81%E5%AE%9E%E6%88%98/bro%E5%AE%9E%E9%AA%8C%E6%88%AA%E5%9B%BE/%E6%9F%A5%E7%9C%8B.png)

## 8.查看ftp.log,得到 uid为CIgPAn3cnI9anhUNi1

![](https://raw.githubusercontent.com/Geraens/ns/2fc8b5c46e01758cdf57c1131a9b3a82cbd5a98e/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/Bro%E7%BD%91%E7%BB%9C%E5%85%A5%E4%BE%B5%E5%8F%96%E8%AF%81%E5%AE%9E%E6%88%98/bro%E5%AE%9E%E9%AA%8C%E6%88%AA%E5%9B%BE/%E6%9F%A5%E7%9C%8Bftp.log.png)


## 9.查看conn.log ,可以找到 uid为CIgPAn3cnI9anhUNi1的IPv4地址为98.114.205.102

![](https://raw.githubusercontent.com/Geraens/ns/2fc8b5c46e01758cdf57c1131a9b3a82cbd5a98e/2017-2/Geraens/%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%E5%8F%8A%E7%9B%B8%E5%85%B3%E6%96%87%E4%BB%B6/Bro%E7%BD%91%E7%BB%9C%E5%85%A5%E4%BE%B5%E5%8F%96%E8%AF%81%E5%AE%9E%E6%88%98/bro%E5%AE%9E%E9%AA%8C%E6%88%AA%E5%9B%BE/%E6%9F%A5%E7%9C%8Bcomm.log.png)
