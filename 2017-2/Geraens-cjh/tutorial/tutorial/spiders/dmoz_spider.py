import scrapy
from ..items import NewsItem


class VulsSpider(scrapy.Spider):

    name = "Vuls_spider"
    allowed_domains = ["freebuf.com"]
    start_urls = [
        'http://www.freebuf.com/vuls'
        #'http://www.freebuf.com/sectool'
        #'http://www.freebuf.com/articles/web'
        #'http://www.freebuf.com/articles/system'
        #"http://www.freebuf.com/articles/network"
        #"http://www.freebuf.com/articles/wireless"
        #"http://www.freebuf.com/articles/terminal"
        #"http://www.freebuf.com/articles/database"
        #"http://www.freebuf.com/articles/security-management"
        #"http://www.freebuf.com/articles/es"
        #"http://www.freebuf.com/ics-articles"
        #"http://www.freebuf.com/news"

    ]

    def parse(self,response):
        print("启动Vuls_spider")
        item = NewsItem()
        item['News_title'] = response.xpath('//dt/a[@title]/text()').extract()
        item['News_link'] = response.xpath('//dt/a/@href').extract()
        item['News_date'] = response.xpath('//dd/span[@class="time"]/text()').extract()
        item['News_author'] = response.xpath('//dd/span[@class="name"]/a[@rel="author"]/text()').extract()
        item['News_class'] = response.xpath('//div[@class="news_bot"]/span[@class="tags"]/a[@href][1]/text()').extract()
        yield item

class SectoolSpider(scrapy.Spider):

    name = "Sectool_spider"
    allowed_domains = ["freebuf.com"]
    start_urls = [
        #'http://www.freebuf.com/vuls'
        'http://www.freebuf.com/sectool'
        #'http://www.freebuf.com/articles/web'
        #'http://www.freebuf.com/articles/system'
        #"http://www.freebuf.com/articles/network"
        #"http://www.freebuf.com/articles/wireless"
        #"http://www.freebuf.com/articles/terminal"
        #"http://www.freebuf.com/articles/database"
        #"http://www.freebuf.com/articles/security-management"
        #"http://www.freebuf.com/articles/es"
        #"http://www.freebuf.com/ics-articles"
        #"http://www.freebuf.com/news"

    ]

    def parse(self,response):
        print("启动Sectool_spider")
        item = NewsItem()
        item['News_title'] = response.xpath('//dt/a[@title]/text()').extract()
        item['News_link'] = response.xpath('//dt/a/@href').extract()
        item['News_date'] = response.xpath('//dd/span[@class="time"]/text()').extract()
        item['News_author'] = response.xpath('//dd/span[@class="name"]/a[@rel="author"]/text()').extract()
        item['News_class'] = response.xpath('//div[@class="news_bot"]/span[@class="tags"]/a[@href][1]/text()').extract()
        yield item


class Webpider(scrapy.Spider):

    name = "Web_spider"
    allowed_domains = ["freebuf.com"]
    start_urls = [
        #'http://www.freebuf.com/vuls'
        #'http://www.freebuf.com/sectool'
        'http://www.freebuf.com/articles/web'
        #'http://www.freebuf.com/articles/system'
        #"http://www.freebuf.com/articles/network"
        #"http://www.freebuf.com/articles/wireless"
        #"http://www.freebuf.com/articles/terminal"
        #"http://www.freebuf.com/articles/database"
        #"http://www.freebuf.com/articles/security-management"
        #"http://www.freebuf.com/articles/es"
        #"http://www.freebuf.com/ics-articles"
        #"http://www.freebuf.com/news"

    ]

    def parse(self,response):
        print("启动Web_spider")
        item = NewsItem()
        item['News_title'] = response.xpath('//dt/a[@title]/text()').extract()
        item['News_link'] = response.xpath('//dt/a/@href').extract()
        item['News_date'] = response.xpath('//dd/span[@class="time"]/text()').extract()
        item['News_author'] = response.xpath('//dd/span[@class="name"]/a[@rel="author"]/text()').extract()
        item['News_class'] = response.xpath('//div[@class="news_bot"]/span[@class="tags"]/a[@href][1]/text()').extract()
        yield item


class Systempider(scrapy.Spider):

    name = "System_spider"
    allowed_domains = ["freebuf.com"]
    start_urls = [
        #'http://www.freebuf.com/vuls'
        #'http://www.freebuf.com/sectool'
        #'http://www.freebuf.com/articles/web'
        'http://www.freebuf.com/articles/system'
        #"http://www.freebuf.com/articles/network"
        #"http://www.freebuf.com/articles/wireless"
        #"http://www.freebuf.com/articles/terminal"
        #"http://www.freebuf.com/articles/database"
        #"http://www.freebuf.com/articles/security-management"
        #"http://www.freebuf.com/articles/es"
        #"http://www.freebuf.com/ics-articles"
        #"http://www.freebuf.com/news"

    ]

    def parse(self,response):
        print("启动System_spider")
        item = NewsItem()
        item['News_title'] = response.xpath('//dt/a[@title]/text()').extract()
        item['News_link'] = response.xpath('//dt/a/@href').extract()
        item['News_date'] = response.xpath('//dd/span[@class="time"]/text()').extract()
        item['News_author'] = response.xpath('//dd/span[@class="name"]/a[@rel="author"]/text()').extract()
        item['News_class'] = response.xpath('//div[@class="news_bot"]/span[@class="tags"]/a[@href][1]/text()').extract()
        yield item

class Networkpider(scrapy.Spider):

    name = "Network_spider"
    allowed_domains = ["freebuf.com"]
    start_urls = [
        #'http://www.freebuf.com/vuls'
        #'http://www.freebuf.com/sectool'
        #'http://www.freebuf.com/articles/web'
        #'http://www.freebuf.com/articles/system'
        "http://www.freebuf.com/articles/network"
        #"http://www.freebuf.com/articles/wireless"
        #"http://www.freebuf.com/articles/terminal"
        #"http://www.freebuf.com/articles/database"
        #"http://www.freebuf.com/articles/security-management"
        #"http://www.freebuf.com/articles/es"
        #"http://www.freebuf.com/ics-articles"
        #"http://www.freebuf.com/news"

    ]

    def parse(self,response):
        print("启动Network_spider")
        item = NewsItem()
        item['News_title'] = response.xpath('//dt/a[@title]/text()').extract()
        item['News_link'] = response.xpath('//dt/a/@href').extract()
        item['News_date'] = response.xpath('//dd/span[@class="time"]/text()').extract()
        item['News_author'] = response.xpath('//dd/span[@class="name"]/a[@rel="author"]/text()').extract()
        item['News_class'] = response.xpath('//div[@class="news_bot"]/span[@class="tags"]/a[@href][1]/text()').extract()
        yield item


class Wirelesspider(scrapy.Spider):
    name = "Wireless_spider"
    allowed_domains = ["freebuf.com"]
    start_urls = [
        #'http://www.freebuf.com/vuls'
        #'http://www.freebuf.com/sectool'
        #'http://www.freebuf.com/articles/web'
        #'http://www.freebuf.com/articles/system'
        #"http://www.freebuf.com/articles/network"
        "http://www.freebuf.com/articles/wireless"
        #"http://www.freebuf.com/articles/terminal"
        #"http://www.freebuf.com/articles/database"
        #"http://www.freebuf.com/articles/security-management"
        #"http://www.freebuf.com/articles/es"
        #"http://www.freebuf.com/ics-articles"
        #"http://www.freebuf.com/news"

    ]

    def parse(self,response):
        print("启动Wireless_spider")
        item = NewsItem()
        item['News_title'] = response.xpath('//dt/a[@title]/text()').extract()
        item['News_link'] = response.xpath('//dt/a/@href').extract()
        item['News_date'] = response.xpath('//dd/span[@class="time"]/text()').extract()
        item['News_author'] = response.xpath('//dd/span[@class="name"]/a[@rel="author"]/text()').extract()
        item['News_class'] = response.xpath('//div[@class="news_bot"]/span[@class="tags"]/a[@href][1]/text()').extract()
        yield item


class Terminalpider(scrapy.Spider):

    name = "Terminal_spider"
    allowed_domains = ["freebuf.com"]
    start_urls = [
        #'http://www.freebuf.com/vuls'
        #'http://www.freebuf.com/sectool'
        #'http://www.freebuf.com/articles/web'
        #'http://www.freebuf.com/articles/system'
        #"http://www.freebuf.com/articles/network"
        #"http://www.freebuf.com/articles/wireless"
        "http://www.freebuf.com/articles/terminal"
        #"http://www.freebuf.com/articles/database"
        #"http://www.freebuf.com/articles/security-management"
        #"http://www.freebuf.com/articles/es"
        #"http://www.freebuf.com/ics-articles"
        #"http://www.freebuf.com/news"

    ]

    def parse(self,response):
        print("启动Terminal_spider")
        item = NewsItem()
        item['News_title'] = response.xpath('//dt/a[@title]/text()').extract()
        item['News_link'] = response.xpath('//dt/a/@href').extract()
        item['News_date'] = response.xpath('//dd/span[@class="time"]/text()').extract()
        item['News_author'] = response.xpath('//dd/span[@class="name"]/a[@rel="author"]/text()').extract()
        item['News_class'] = response.xpath('//div[@class="news_bot"]/span[@class="tags"]/a[@href][1]/text()').extract()
        yield item


class Databasepider(scrapy.Spider):

    name = "Database_spider"
    allowed_domains = ["freebuf.com"]
    start_urls = [
        #'http://www.freebuf.com/vuls'
        #'http://www.freebuf.com/sectool'
        #'http://www.freebuf.com/articles/web'
        #'http://www.freebuf.com/articles/system'
        #"http://www.freebuf.com/articles/network"
        #"http://www.freebuf.com/articles/wireless"
        #"http://www.freebuf.com/articles/terminal"
        "http://www.freebuf.com/articles/database"
        #"http://www.freebuf.com/articles/security-management"
        #"http://www.freebuf.com/articles/es"
        #"http://www.freebuf.com/ics-articles"
        #"http://www.freebuf.com/news"

    ]

    def parse(self,response):
        print("启动Database_spider")
        item = NewsItem()
        item['News_title'] = response.xpath('//dt/a[@title]/text()').extract()
        item['News_link'] = response.xpath('//dt/a/@href').extract()
        item['News_date'] = response.xpath('//dd/span[@class="time"]/text()').extract()
        item['News_author'] = response.xpath('//dd/span[@class="name"]/a[@rel="author"]/text()').extract()
        item['News_class'] = response.xpath('//div[@class="news_bot"]/span[@class="tags"]/a[@href][1]/text()').extract()
        yield item


class SerMpider(scrapy.Spider):

    name = "SerM_spider"
    allowed_domains = ["freebuf.com"]
    start_urls = [
        #'http://www.freebuf.com/vuls'
        #'http://www.freebuf.com/sectool'
        #'http://www.freebuf.com/articles/web'
        #'http://www.freebuf.com/articles/system'
        #"http://www.freebuf.com/articles/network"
        #"http://www.freebuf.com/articles/wireless"
        #"http://www.freebuf.com/articles/terminal"
        #"http://www.freebuf.com/articles/database"
        "http://www.freebuf.com/articles/security-management"
        #"http://www.freebuf.com/articles/es"
        #"http://www.freebuf.com/ics-articles"
        #"http://www.freebuf.com/news"

    ]

    def parse(self,response):
        print("启动SerM_spider")
        item = NewsItem()
        item['News_title'] = response.xpath('//dt/a[@title]/text()').extract()
        item['News_link'] = response.xpath('//dt/a/@href').extract()
        item['News_date'] = response.xpath('//dd/span[@class="time"]/text()').extract()
        item['News_author'] = response.xpath('//dd/span[@class="name"]/a[@rel="author"]/text()').extract()
        item['News_class'] = response.xpath('//div[@class="news_bot"]/span[@class="tags"]/a[@href][1]/text()').extract()
        yield item



class Espider(scrapy.Spider):

    name = "Es_spider"
    allowed_domains = ["freebuf.com"]
    start_urls = [
        #'http://www.freebuf.com/vuls'
        #'http://www.freebuf.com/sectool'
        #'http://www.freebuf.com/articles/web'
        #'http://www.freebuf.com/articles/system'
        #"http://www.freebuf.com/articles/network"
        #"http://www.freebuf.com/articles/wireless"
        #"http://www.freebuf.com/articles/terminal"
        #"http://www.freebuf.com/articles/database"
        #"http://www.freebuf.com/articles/security-management"
        "http://www.freebuf.com/articles/es"
        #"http://www.freebuf.com/ics-articles"
        #"http://www.freebuf.com/news"

    ]

    def parse(self,response):
        print("启动Es_spider")
        item = NewsItem()
        item['News_title'] = response.xpath('//dt/a[@title]/text()').extract()
        item['News_link'] = response.xpath('//dt/a/@href').extract()
        item['News_date'] = response.xpath('//dd/span[@class="time"]/text()').extract()
        item['News_author'] = response.xpath('//dd/span[@class="name"]/a[@rel="author"]/text()').extract()
        item['News_class'] = response.xpath('//div[@class="news_bot"]/span[@class="tags"]/a[@href][1]/text()').extract()
        yield item




class Icspider(scrapy.Spider):

    name = "Ics_spider"
    allowed_domains = ["freebuf.com"]
    start_urls = [
        #'http://www.freebuf.com/vuls'
        #'http://www.freebuf.com/sectool'
        #'http://www.freebuf.com/articles/web'
        #'http://www.freebuf.com/articles/system'
        #"http://www.freebuf.com/articles/network"
        #"http://www.freebuf.com/articles/wireless"
        #"http://www.freebuf.com/articles/terminal"
        #"http://www.freebuf.com/articles/database"
        #"http://www.freebuf.com/articles/security-management"
        #"http://www.freebuf.com/articles/es"
        "http://www.freebuf.com/ics-articles"
        #"http://www.freebuf.com/news"

    ]

    def parse(self,response):
        print("启动Ics_spider")
        item = NewsItem()
        item['News_title'] = response.xpath('//dt/a[@title]/text()').extract()
        item['News_link'] = response.xpath('//dt/a/@href').extract()
        item['News_date'] = response.xpath('//dd/span[@class="time"]/text()').extract()
        item['News_author'] = response.xpath('//dd/span[@class="name"]/a[@rel="author"]/text()').extract()
        item['News_class'] = response.xpath('//div[@class="news_bot"]/span[@class="tags"]/a[@href][1]/text()').extract()
        yield item





class Newspider(scrapy.Spider):

    name = "News_spider"
    allowed_domains = ["freebuf.com"]
    start_urls = [
        #'http://www.freebuf.com/vuls'
        #'http://www.freebuf.com/sectool'
        #'http://www.freebuf.com/articles/web'
        #'http://www.freebuf.com/articles/system'
        #"http://www.freebuf.com/articles/network"
        #"http://www.freebuf.com/articles/wireless"
        #"http://www.freebuf.com/articles/terminal"
        #"http://www.freebuf.com/articles/database"
        #"http://www.freebuf.com/articles/security-management"
        #"http://www.freebuf.com/articles/es"
        #"http://www.freebuf.com/ics-articles"
        "http://www.freebuf.com/news"

    ]

    def parse(self,response):
        print("启动News_spider")
        item = NewsItem()
        item['News_title'] = response.xpath('//dt/a[@title]/text()').extract()
        item['News_link'] = response.xpath('//dt/a/@href').extract()
        item['News_date'] = response.xpath('//dd/span[@class="time"]/text()').extract()
        item['News_author'] = response.xpath('//dd/span[@class="name"]/a[@rel="author"]/text()').extract()
        item['News_class'] = response.xpath('//div[@class="news_bot"]/span[@class="tags"]/a[@href][1]/text()').extract()
        yield item