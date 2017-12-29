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
        'Host': 'netsecurity.51cto.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://www.cnbeta.com/topics.htm',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'itag':'v2333'
    }

    
    @every(minutes=24 * 60)
    def on_start(self):
            self.crawl('http://netsecurity.51cto.com/#listsmore',
                       fetch_type='js', js_script="""
                       function() {
                           for(var i=0;i<100;i++)
                           {
                               setTimeout("$('.listsmore a').click()", 1000);
                           }
                       }""", callback=self.index_page)
            
    
    def index_page(self, response):
        for each in response.doc('.home-left-list .rinfo > a').items():
                self.crawl(each.attr.href, callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        print response.doc('.wznr > h2').text()
        print response.doc('.wznr > p').text()
        print response.doc('.wznr em').text()
        self.send_message(self.project_name, {
            "news_url": response.url,
            "title": response.doc('.wznr > h2').text(),
            "abstraction": response.doc('.wznr > p').text(),
            "publish_time": response.doc('.wznr em').text(),
            "source":"netsecurity.51cto.com"
        }, url="%s" % (response.url))

    
   
    def on_message(self, project, msg):
        if not msg or not msg['title']:
            return
        insert_result(self,"SpiderForIS","SpiderFor51CTO",msg)         
            
            
            
            
            
            
            
            
            
            
            
            