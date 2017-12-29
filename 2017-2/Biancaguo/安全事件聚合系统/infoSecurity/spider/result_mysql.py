#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Author: will<willgeek@qq.com>
#         http://www.willgeek.com
# Created on 2015-11-02 11:00:48
#  
#使用方法： 
#    1, 把本文件放到pyspider/pyspider/libs/目录下命名为result_mysql.py; 
#    2, 建立相应的表和库; 
#    3, 在脚本文件里使用from pyspider.libs.result_mysql import insert_result引用本代码; 
#    4, 重写on_result方法调用insert_result. 
#    def on_result(self, result):
#        insert_result(self,dbhost,tablename,result)
 
import mysql.connector

 
def insert_result(self, database, tablename, result, config=None):
    #dbconfig 默认数据库配置自行修改
    if not config:
        config = {
            'host': '127.0.0.1',
            'user': 'root',
            'password': ''
            
        }
     
    config['database'] = database
    if not config['database']:
        config['database'] = 'test'
     
    print(result)
    #add by will
    if not result:
        return
     
    #addslashes#
    def escape(string):
        return '`%s`' % string
    def escapestr(string):
        return "'%s'" % string.replace("'", "")
 
    #creat sql#
    if result:
        _keys = ", ".join(escape(k) for k in result)
        _values = ", ".join(escapestr(result[k]) for k in result)
        sql_query = "REPLACE INTO %s (%s) VALUES (%s)" % (tablename, _keys, _values)
    #print sql_query
    else:
        print("no result")
 
    #update#
    global cnx
 
    try:
        if 'cnx' not in vars():
            cnx = mysql.connector.connect(**config)
        cur = cnx.cursor()
        cur.execute(sql_query)
        cnx.commit()
        cur.close()
    except mysql.connector.Error as err:
        print(err) 
