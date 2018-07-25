# -*- coding: utf-8 -*-
import scrapy


class ShixisengSpider(scrapy.Spider):
    name = 'shixiseng'
    allowed_domains = ['shixiseng.com']
    start_urls = ['http://shixiseng.com/']

    def parse(self, response):
        pass
