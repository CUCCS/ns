#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-11-18 11:06:59
# Project: spider1

from pyspider.libs.base_handler import *
from pyspider.libs.result_mysql import insert_result
import time
import datetime

t= time.time()
mt=int(round(t*1000))

class Handler(BaseHandler):
    crawl_config = {
        "Host": "36kr.com",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Cookie": "aliyungf_tc=AQAAAG7BEQfJ3wwAAOuDDnN2gFWweK1O; device-uid=69bd83e0-cc05-11e7-85b6-e51cf4bf4c77; M-XSRF-TOKEN=ee9a7f2d04e0516faf460bf05de856132fe2fd3ea80c963b4b63d30f7b0c20ca; ktm_ab_test=t.6_v.deploy; kr_stat_uuid=5sGm225182845;  TY_SESSION_ID=5a644e89-2d44-48bb-adf1-63afb5c148ad; c_name=point; krnewsfrontss=daffa63b9e38dc8dca5286879a93e095",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0"
    }
   
    
    def on_start(self):
        topics=["漏洞","信息安全","黑客","网络安全"]
        for topic in topics:
            self.crawl('http://36kr.com/api/search/entity-search?page=1&per_page=40&keyword='+topic+'&entity_type=newsflash&_='+str(mt), callback=self.index_page,save={'topic':topic})
        

    def index_page(self, response):
        total_count=response.json["data"]["total_count"]
        page_size=response.json["data"]["page_size"]
        if total_count%page_size==0:
              page_num=total_count/page_size
        else:
            page_num=total_count/page_size+1
        print page_num
        for i in range(1,page_num+1):
            self.crawl('http://36kr.com/api/search/entity-search?page='+str(i)+'&per_page=40&keyword='+response.save['topic']+'&entity_type=newsflash&_='+str(mt), callback=self.detail_page,save={'topic':response.save['topic']})
        

    def detail_page(self, response):
        page_size=response.json["data"]["page_size"]
        for i in range(0,page_size):
             self.send_message(self.project_name, {
                "topic":response.save['topic'],
                "title": response.json["data"]["items"][i]["title"],
                "abstraction":response.json["data"]["items"][i]["description_text"],
                "news_url":response.json["data"]["items"][i]["news_url"],
                "publish_time":response.json["data"]["items"][i]["published_at"][0:10]
             }, url="%s#%s" % (response.url, i))
        
    

    def on_message(self, project, msg):
        if not msg or not msg['topic']:
            return
        print msg
        insert_result(self,"SpiderForIS","SpiderFor36ker",msg)
    
    '''
    def on_result(self, result):
        print result
        if not result or not result['topic']:
            return
        print result
        insert_result(self,"SpiderForIS","SpiderFor36ker",result)
'''
           
