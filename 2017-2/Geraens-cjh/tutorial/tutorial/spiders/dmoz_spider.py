import scrapy
from ..items import NewsItem

class NewsSpider(scrapy.Spider):
    name = "News_spider"
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
            item = NewsItem()
            item['News_title'] =response.xpath('//dt/a[@title]/text()').extract()
            item['News_link'] = response.xpath('//dt/a/@href').extract()
            item['News_date'] = response.xpath('//dd/span[@class="time"]/text()').extract()
            item['News_author'] = response.xpath('//dd/span[@class="name"]/a[@rel="author"]/text()').extract()
            item['News_class'] = response.xpath('//div[@class="news_bot"]/span[@class="tags"]/a[@href][1]/text()').extract()
            yield item

