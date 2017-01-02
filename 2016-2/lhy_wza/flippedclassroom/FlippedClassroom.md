# 翻转课堂候选主题

* [ ] chap0x01 基于VirtualBox的网络攻防基础环境搭建实例讲解
    * 节点：靶机、网关、攻击者主机
    * 连通性
        * 靶机可以直接访问攻击者主机
        * 攻击者主机无法直接访问靶机
        * 网关可以直接访问攻击者主机和靶机
        * 靶机的所有对外上下行流量必须经过网关
        * 所有节点均可以访问互联网
    * 其他要求
        * 所有节点制作成基础镜像（多重加载的虚拟硬盘）
* chap0x02 CVSS与漏洞评分实例讲解（高中低危漏洞各举一例）
    * https://www.zhihu.com/question/26373469
* chap0x03 互联网与局域网身份隐藏与识别实例讲解
    * 代理
    * 匿名通信
    * XFF
    * CSRF
    * 盗用帐号
* chap0x04 基于VirtualBox的局域网中间人劫持攻击实验讲解
* [ ] chap0x05 自己动手编程实现并讲解TCP connect scan/TCP stealth scan/TCP XMAS scan/UDP scan
    * http://resources.infosecinstitute.com/port-scanning-using-scapy/ 
* chap0x06 DNS域传送漏洞及DNS信息收集实例讲解
    * https://digi.ninja/projects/zonetransferme.php
* [ ] chap0x07 从SQL注入到Shell
    * https://pentesterlab.com/exercises/from_sqli_to_shell
* chap0x08+chap0x09 实战Snort检测SQL注入和Shellshock漏洞攻击并联动iptables进行防御（阻断来源IP访问1分钟并记录日志）
* chap0x10 实战fail2ban防止Basic认证暴力破解和SSH口令爆破
* chap0x11 三种或以上不同SSH蜜罐应用实验对比分析报告
* [ ] chap0x12 实战Bro网络入侵取证
* chap0x13 电信诈骗案例与防骗总结

***说明***：

* 所有标记[ ]符号的主题，每个小组都需要完成并提交到[github](https://github.com/cuccs/ns)
* 没有标记[ ]符号的主题，在1周之内每个小组需要有专人通过电子邮件让我知晓你组github帐号和真人之间的对应关系和你组选题；
    * 当选题冲突时，遵循以下2个原则：
        * 先来先得。后来者是否可以继续做这个题目决定权在我；
        * 后来者要选择不同的主题切入方向或不同的实验对象。

