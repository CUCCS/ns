#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import jieba
from selenium import webdriver

WEIBO_ACCOUNT = ''  #微博账号
WEIBO_PASSWORD = ''   #微博密码

def main():
    #用户的微博主页从第二页开始就是使用JavaScript脚本动态生成的，所以用浏览器加载网页得到完整网页内容
    browser = webdriver.Chrome()
    browser.get("https://passport.weibo.cn/signin/login?entry=mweibo&r=http%3A%2F%2Fweibo.cn&page=2&uid=3591355593&_T_WM=1ff404edd274066bcdfdcccd6cca2464")
    time.sleep(1)  #这里停一秒是因为由于网络原因，有时页面加载过慢，网页还没加载出来，而下面获取网页元素的命令已经执行了，防止出现这种错误

    #登录微博
    username=browser.find_element_by_xpath('//*[@id="loginName"]')
    password=browser.find_element_by_xpath('//*[@id="loginPassword"]')
    login=browser.find_element_by_xpath('//*[@id="loginAction"]')
    username.send_keys('')
    password.send_keys('')
    login.click()

    n= 48    #用户微博页面总数
    page = 1
    words=[]   #保存微博内容分词结果
    while page<=n:
    #获取lxml页面
       url = 'http://weibo.cn/u/%d?page=%d' % (3591355593, page)
       browser.get(url)

       #用户微博从第二页开始就需要登录了才能访问，所以获取第一次登录时的cookie
       browser.add_cookie({'name': 'userName', 'value': ''})
       browser.add_cookie({'name': 'password', 'value': ''})

       time.sleep(0.5)
       if page==1:
           x=browser.find_element_by_xpath('//*[@id="pagelist"]/form/div/input[1]')
           n2=x.get_attribute('value')    #获取用户微博页面总数
           #在这儿改变了n的值发现对循环的控制并不起作用


       #class属性为'ctt'的span标签包含了用户原创的微博内容
       a = browser.find_elements_by_xpath('//span[@class="ctt"]')
       for i in a:
          seg_list = jieba.cut(i.text, cut_all=False)  # 精确模式
          for j in seg_list:
              if len(j)>=2:
                  words.append(j)
       page=page+1

    #统计获取的内容的出现频次
    count = {}
    for i in words:
        if i in count:
            count[i] = count[i] + 1
        else:
            count[i] = 1
    #按照出现频次排序
    count = sorted(count.iteritems(), key=lambda asd: asd[1], reverse=True)

    #输出
    for key, value in count:
        p = key.encode('utf-8')
        print p, value

if __name__ == '__main__':
    main()