#coding=utf8

#_*_coding: utf-8 _*_

import os
os.environ.setdefault('SCRAPY_SETTING_MODULE','tutorial.settings')

import scrapy

from scrapy.crawler import CrawlerProcess

from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())

