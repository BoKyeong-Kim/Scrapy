# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class NewsItem(scrapy.Item):
        company = scrapy.Field()
        date = scrapy.Field()
        titles= scrapy.Field()
        content = scrapy.Field()
        film_url = scrapy.Field()

