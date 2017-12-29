1#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-12-04 11:18:57
# Project: spiderForcnbeta

from pyspider.libs.base_handler import *
from pyspider.libs.result_mysql import insert_result
import time
import datetime

t= time.time()
mt=int(round(t*1000))


from selenium import webdriver



class Handler(BaseHandler):
    crawl_config = {
        'Host': 'www.cnbeta.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://www.cnbeta.com/topics.htm',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0'
    }

    
    @every(minutes=24 * 60)
    def on_start(self):
        driver = webdriver.PhantomJS()
        driver.set_page_load_timeout(10)
        try:
            driver.get('http://www.cnbeta.com/topics/157.htm')
        except:
            print "error!"
        for i in range(5):
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(1)
        urls=driver.find_elements_by_css_selector("dt > a")      
        for url in urls:
            self.crawl(url.get_attribute("href"), callback=self.detail_page)
            
        

    @config(priority=2)
    def detail_page(self, response):
        self.send_message(self.project_name, {
            "news_url": response.url,
            "title": response.doc('.title > h1').text(),
            "abstraction": response.doc('.article-summary > p').text(),
            "publish_time": response.doc('.meta > span').text()[0:17],
            "source":"www.cnbeta.com"
        }, url="%s" % (response.url))

    
   
    def on_message(self, project, msg):
        if not msg or not msg['title']:
            return
        insert_result(self,"SpiderForIS","SpiderForCnbeta",msg)         
            
            
            
            
            
            
            
            
            
            
            
            