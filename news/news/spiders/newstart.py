# -*- coding: utf-8 -*-
import scrapy
import codecs
import re
import urllib.parse
import parsel
import scrapy.contracts
from scrapy import Request
from scrapy.selector import Selector
from scrapy.http.request import Request
import time

from news.items import NewsItem

class NewstartSpider(scrapy.Spider):
    name = 'newstart'
    allowed_domains = ['news.einfomax.co.kr']
    start_urls = []

    for i in range(1, 506):
        start_urls.append('http://news.einfomax.co.kr/news/articleList.html?page={}&total=15159&box_idxno=&sc_area=A&view_type=sm&sc_section_code=&sc_level=&sc_article_type=&sc_sdate=2019-01-01&sc_edate=2019-11-14&sc_order_by=E&sc_word=%EA%B8%88%EB%A6%AC&sc_andor=OR&sc_word2='.format(i))
    
    def parse_start_url(self, response):
        return self.parse(response)

    def parse(self, response):
        urls = response.xpath('''//div[@class="list-block"]/div[@class="list-titles"]/a[contains(@href,list-titles)]/@href''').extract()

        for url in urls:
            url = 'http://news.einfomax.co.kr' + url
            
            yield scrapy.Request(url, callback=self.parse_details)

    def parse_details(self, response):
        item = NewsItem()
        item['company'] = ['연합인포맥스']
        item['date'] = response.xpath('// *[ @ id = "user-container"] / div[3] / header / section / div / ul / li[2] / text()').extract()
        item['titles'] = response.xpath('//div[@class="article-head-title"]/text()').extract()
        item['content'] = response.xpath('//div[@id="article-view-content-div"]/text()').extract()
        item['film_url'] = response.url
        return item
