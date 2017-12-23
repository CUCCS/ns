# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#from pymysql.cursors import DictCursor
import pymysql.cursors
import pymysql
#from twisted.enterprise import adbapi

class DBPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            user="root",
            passwd="root",
            port=3306,
            host="localhost",
            db="News",
            charset='utf8',
            use_unicode=False) #
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()
        i = self.cursor.execute('''select * from news_table''')
        print(i)
        print("数据库连接成功")

    def process_item(self, item, spider):
        try:
            # 查重处理
            list_len = len(item['News_title'])
            for i in range(0, list_len):
                self.cursor.execute(
                    '''select * from news_table where Link = %s''',
                    item['News_link'][i])
            # 是否有重复数据
            repetition = self.cursor.fetchone()

            # 重复
            if repetition:
                pass

            else:
                # 插入数据
                list_len = len(item['News_title'])
                for i in range(0,list_len):
                    self.cursor.execute(
                        '''INSERT INTO news_table(Title, Date, Link, Author ,Class) 
                        values(%s, %s, %s, %s, %s)''',
                        (item['News_title'][i],
                         item['News_date'][i],
                         item['News_link'][i],
                         item['News_author'][i],
                         item['News_class'][i]))
            # 提交sql语句
            self.connect.commit()
            self.cursor.close()
            self.connect.close()
        except Exception as error:
            print("出错")
            print(error)     #出现错误时打印错误日志
        return item

