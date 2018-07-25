# -*- coding: utf-8 -*-
import scrapy
from news.items import NewsItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spider import CrawlSpider,Rule

class News163Spider(CrawlSpider):
	name = 'news163'
	allowed_domains = ['news.163.com']
	start_urls = ['http://news.163.com/']
	rules = (
			Rule(LinkExtractor(allow=r"/18/07\d+/*"),
				callback="parse_news",follow=True),
		)

	def parse_news(self, response):
		item = NewsItem()
		item['news_thread'] = response.url.strip().split('/')[-1][:-5]
		self.get_title(response, item)
		self.get_time(response, item)
		self.get_source(response, item)
		self.get_url(response, item)
		self.get_source_url(response, item)
		self.get_text(response, item)
		return item

	def get_title(self,response,item):
		title = response.css('title::text').extract()
		print('*'*30)
		if title:
			print('title:{}'.format(title[0][:-5]))
			item['news_title'] = title[0][:-5]

	def get_time(self,response,item):
		time = response.css('.post_time_source::text').extract()
		if time:
			print('time:{}'.format(time[0][:-4].strip()))
			item['news_time'] = time[0][:-4]

	def get_source(self,response,item):
		source = response.css('#ne_article_source::text').extract()
		if source:
			print('source:{}'.format(source[0]))
			item['news_source'] = source[0]

	def get_source_url(self,response,item):
		source_url = response.css('#ne_article_source::attr(href)').extract()
		if source_url:
			print('source_url:{}'.format(source_url[0]))
			item['source_url'] = source_url[0]

	def get_text(self,response,item):
		text = response.css('#endText p::text').extract()
		if text:
			print('text:{}'.format(text))
			item['news_body'] = text

	def get_url(self,response,item):
		url = response.url
		if url:
			print('url:{}'.format(url))
			item['news_url'] = url


	# def parse(self, response):
	# 	pass
