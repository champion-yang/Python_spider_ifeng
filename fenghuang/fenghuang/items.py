# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class FenghuangItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field() #标题
    link = scrapy.Field()  # 链接
    biaoti = scrapy.Field()  #二级目录下的标题
    biaotilianjie = scrapy.Field() #二级目录下的标题链接
    time = scrapy.Field()
    neirong = scrapy.Field()












