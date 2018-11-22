import scrapy


class TruliaSpider(scrapy.Spider):
	name = "trulia"

	def start_requests(self):
		urls = [
			'https://www.trulia.com/CA/San_Francisco/11_p/'
		]
		TruliaSpider.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		print response.body