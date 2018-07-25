import scrapy


class QuotesSpdier(scrapy.Spider):
	"""docstring for QuotesSpdier"""
	name = 'quotes'

	def start_requests(self):
		urls = [
			# "http://quotes.toscrape.com/page/1/",
			# "http://quotes.toscrape.com/page/2/"
		]
		for i in range(1,3):
			urls.append("http://quotes.toscrape.com/page/{}/".format(i))

		
		for url in urls:
			yield scrapy.Request(url=url,callback=self.parse)

	def parse(self, response):
		page = response.url.split("/")[-2]	#分割 -2 表示列表倒数第二个
		file_name = "quotes-{}.txt".format(page)
		output=''
		for quote in response.css('.quote'):
			text = quote.css('span.text::text').extract_first() #提取span.text的内容
			author = quote.css('small.author::text').extract_first()
			tags = quote.css('a.tag::text').extract_first()
			output += text+'\r\n' +author +'\r\n'+tags+'\r\n'

		with open (file_name, 'wb') as f:
			# f.write(response.body)
			f.write(output.encode())
		self.log("Saved file {}".format(file_name))
