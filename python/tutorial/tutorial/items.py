# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	titile = scrapy.Field()
	link = scrapy.Field()
        height = scrapy.Field()
        width = scrapy.Field()
        image = scrapy.Field()
        pic_ext = scrapy.Field()

