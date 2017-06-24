# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # 标签  小区  户型   面积    建造时间  价格   均价  详情链接  经纬度
    title = scrapy.Field()
    address = scrapy.Field()
    community = scrapy.Field()
    model = scrapy.Field()
    area = scrapy.Field()
    time = scrapy.Field()
    price = scrapy.Field()
    average_price = scrapy.Field()
    link = scrapy.Field()
    Latitude = scrapy.Field()
