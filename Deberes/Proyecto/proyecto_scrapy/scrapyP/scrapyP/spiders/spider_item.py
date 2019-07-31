# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

import scrapy
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from scrapyP.items import ImpresoraItem

class ImpresorasSpider(CrawlSpider):
	name = 'impresoras'
	item_count = 0
	allowed_domain = ['www.mercadolibre.com.mx']
	start_urls = ['http://listado.mercadolibre.com.mx/impresoras#D[A:impresoras,L:1]']

	rules = {
		# Para cada item
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//li[@class="pagination__next"]/a'))),
		Rule(LinkExtractor(allow =(), restrict_xpaths = ('//h2[contains(@class,"item__title")]/a')),
							callback = 'parse_item', follow = False)
	}

	def parse_item(self, response):
		impresora_item = ImpresoraItem()
		#info de producto
		impresora_item['titulo'] = response.xpath('normalize-space(//h1[@class="item-title__primary "]/text())').extract_first()
		impresora_item['modelo'] = response.xpath('normalize-space(//*[@id="root-app"]/div[2]/div[1]/div[1]/section[3]/div/section/ul/li[3]/span)').extract()
		impresora_item['marca'] = response.xpath('normalize-space(//*[@id="root-app"]/div[2]/div[1]/div[1]/section[3]/div/section/ul/li[1]/span)').extract()
		impresora_item['precio'] = response.xpath('normalize-space(//span[@class="price-tag-fraction"]/text())').extract()
		impresora_item['condicion'] = response.xpath('normalize-space(//div[@class="item-conditions"]/text())').extract()
		impresora_item['opiniones'] = response.xpath('normalize-space(//span[@class="review-summary-average"]/text())').extract()
		#info de la tienda o vendedor
		impresora_item['tipo_vendedor'] = response.xpath('normalize-space(//p[contains(@class, "power-seller")]/text())').extract()
		impresora_item['ventas_vendedor'] = response.xpath('normalize-space(//dd[@class="reputation-relevant"]/strong/text())').extract()
		
		self.item_count += 1
		if self.item_count > 15:
			raise CloseSpider('item_exceeded')
		yield impresora_item
