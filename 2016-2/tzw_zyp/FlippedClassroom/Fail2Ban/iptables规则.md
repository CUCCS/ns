# iptables防火墙

* **所用到的iptables-command命令列表**
   * 命令 -A, --append
   范例 iptables -A INPUT ...  
   说明 新增规则到某个规则链中，该规则将会成为规则链中的最后一条规则。
   * 命令 -P, --policy
   范例 iptables -P INPUT DROP
   说明 定义过滤政策。 也就是未符合过滤条件之封包， 默认的处理方式。
   * 命令 -N, --new-chain
   范例 iptables -N allowed 
   说明 定义新的规则链。